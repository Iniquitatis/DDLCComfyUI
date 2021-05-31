################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################

################################################################################
# Configuration variables
################################################################################
release_mode = False

theme_dir  = "Themes"
source_dir = "Source"
build_dir  = "Build"

mod_dirs = [
    "common",

    # NOTE: uncomment for MAS support
    #"mas",
]

glitched_boxes = [
    "textbox_monika.png",
    "textbox_monika_d.png",
]

################################################################################
# Script itself
################################################################################
import json
import os
import re
import shutil
from subprocess import Popen, PIPE, STDOUT

from PIL import Image
from hsluv import *

# Text file preprocessing
def clamp(value, lower, upper):
    return min(max(value, lower), upper)

def format_rgb_hex_string(r, g, b):
    return f"#{int(r):02x}{int(g):02x}{int(b):02x}"

def format_rgba_hex_string(r, g, b, a):
    return f"#{int(r):02x}{int(g):02x}{int(b):02x}{int(a):02x}"

def modulate_rgb_color(r, g, b, h, s, l):
    r = float(r) / 255.0
    g = float(g) / 255.0
    b = float(b) / 255.0

    ch, cs, cl = rgb_to_hsluv([r, g, b])
    r, g, b = hsluv_to_rgb([clamp(h, 0.0, 360.0),
                            clamp(cs * s, 0.0, 100.0),
                            clamp(cl + l * 100.0, 0.0, 100.0)])

    return (int(r * 255.0),
            int(g * 255.0),
            int(b * 255.0))

def modulate_rgba_color(r, g, b, a, h, s, l):
    r = float(r) / 255.0
    g = float(b) / 255.0
    b = float(b) / 255.0
    a = float(a) / 255.0

    ch, cs, cl = rgb_to_hsluv([r, g, b])
    r, g, b = hsluv_to_rgb([clamp(h, 0.0, 360.0),
                            clamp(cs * s, 0.0, 100.0),
                            clamp(cl + l * 100.0, 0.0, 100.0)])

    return (int(r * 255.0),
            int(g * 255.0),
            int(b * 255.0),
            int(a * 255.0))

def modulate_colors(macro_args, method_args):
    h, s, l = method_args

    if len(macro_args) == 3:
        r, g, b = macro_args

        if h != None and s != None and l != None:
            r, g, b = modulate_rgb_color(int(r), int(g), int(b), float(h), float(s), float(l))

        return format_rgb_hex_string(r, g, b)

    elif len(macro_args) == 4:
        r, g, b, a = macro_args

        if h != None and s != None and l != None:
            r, g, b, a = modulate_rgba_color(int(r), int(g), int(b), int(a), float(h), float(s), float(l))

        return format_rgba_hex_string(r, g, b, a)

    return "#baadf00d"

def stringize(macro_args, method_args):
    return str(method_args)

def parse_macro_args(match):
    if match.lastindex == None or match.lastindex == 0:
        # No arguments have been passed to the macro
        return []

    args_string = match.group(1)

    query = r""

    for i in range(4):
        query += r"\s*([\w\-.]+)\s*"
        result = re.findall(query, args_string)

        if len(result) > 0:
            return result

        query += r","

def preprocess_text_file(in_path, out_path, theme, scale):
    prm_color = theme["primary_color"]
    scd_color = theme["secondary_color"]

    macros = [
        # Name                       | Method         | Arguments
        [ "CUI_THEME_ID"             , stringize      , (("%s" if scale == 1 else "%s_hidpi") % theme["id"])     ],
        [ "CUI_THEME_NAME"           , stringize      , (("%s" if scale == 1 else "%s (HiDPI)") % theme["name"]) ],
        [ "CUI_BTN_ROUNDING"         , stringize      , (theme["button_rounding"])                               ],
        [ "CUI_FRM_ROUNDING"         , stringize      , (theme["frame_rounding"])                                ],
        [ "CUI_DLG_ROUNDING"         , stringize      , (theme["dialogue_rounding"])                             ],
        [ "CUI_MNU_PTSHAPE"          , stringize      , (theme["menu_pattern_shape"])                            ],
        [ "CUI_DLG_PTSHAPE"          , stringize      , (theme["dialogue_pattern_shape"])                        ],
        [ "CUI_MAIN_FONT_REGULAR"    , stringize      , (theme["main_font"]["regular"])                          ],
        [ "CUI_MAIN_FONT_ITALIC"     , stringize      , (theme["main_font"]["italic"])                           ],
        [ "CUI_MAIN_FONT_BOLD"       , stringize      , (theme["main_font"]["bold"])                             ],
        [ "CUI_MAIN_FONT_BOLD_ITALIC", stringize      , (theme["main_font"]["bold_italic"])                      ],
        [ "CUI_MENU_FONT"            , stringize      , (theme["menu_font"])                                     ],
        [ "CUI_OPTION_FONT"          , stringize      , (theme["option_font"])                                   ],
        [ "CUI_MAIN_FONT_KERNING"    , stringize      , (theme["main_font_kerning"])                             ],
        [ "CUI_DLG_VERT_OFFSET"      , stringize      , (theme["dialogue_vertical_offset"])                      ],
        [ "CUI_DLG_LINE_SPACING"     , stringize      , (theme["dialogue_line_spacing"])                         ],
        [ "CUI_BTN_HEIGHT_ADJUSTMENT", stringize      , (theme["button_height_adjustment"])                      ],
        [ "CUI_PRM_COLOR"            , modulate_colors, (prm_color["h"], prm_color["s"], prm_color["l"])         ],
        [ "CUI_SCD_COLOR"            , modulate_colors, (scd_color["h"], scd_color["s"], scd_color["l"])         ],
        [ "CUI_SCALE"                , stringize      , (scale)                                                  ],
        [ "CUI_SCALE_INV"            , stringize      , (1.0 / scale)                                            ],
    ]

    with open(in_path, "r") as in_file, open(out_path, "w") as out_file:
        text = in_file.read()

        for macro_name, method, method_args in macros:
            query = macro_name + r"\(([\w\s\-.,]*)\)"
            text = re.sub(query, lambda match: method(parse_macro_args(match), method_args), text)

        out_file.write(text)

# Image rendering
def clear_alpha(p):
    return (p[0], p[1], p[2], 0)

def mix_pixel_glitched(l, r):
    a = min(max(int(l[3] * 0.25) + r[3],
                int(r[3] * 0.25) + l[3]), 255)
    return (r[0], r[1], r[2], a)

def shift_region(pixel_data, x, y, w, h, dx, dy):
    region_data = [[pixel_data[x + i, y + j] for j in range(h)] for i in range(w)]

    for i in range(w):
        for j in range(h):
            cx, cy = x + i, y + j
            pixel_data[cx, cy] = clear_alpha(pixel_data[cx, cy])

    for i in range(w):
        for j in range(h):
            cx, cy = x + dx + i, y + dy + j
            pixel_data[cx, cy] = mix_pixel_glitched(pixel_data[cx, cy], region_data[i][j])

def glitch(image_path, scale):
    regions = [
        # X  | Y  | W  | H  | DX | DY
        [  42,   5, 144,  15, -25,   0 ],
        [  42,  36,  41,  10,  25,   0 ],
        [  42,  62,  91,   5, -25,   0 ],
        [  42,  92,  87,   7, -25,   0 ],
        [  42, 108,  30,   4,  25,   0 ],
        [ 123, 115, 183,  20,  25,   0 ],
        [ 183,  77, 129,  22, -26,   0 ],
        [ 215,  86,  50,   1,   1,   0 ],
        [ 225,  40,  99,  20, -25,   0 ],
        [ 273,  15, 136,  11,  25,   0 ],
        [ 309,  86,  58,   1, -25,   0 ],
        [ 336,  87, 147,  28, -26,   0 ],
        [ 372,  54, 213,   4,  25,   0 ],
        [ 408,  20,  80,   3, -26,   0 ],
        [ 444,  72, 159,   6, -25,   0 ],
        [ 448, 127,  83,   9, -25,   0 ],
        [ 516,  35, 116,   6, -26,   0 ],
        [ 564,  93, 128,   3, -26,   0 ],
        [ 625,  36, 108,   8, -25,   0 ],
        [ 670, 101, 156,  12, -25,   0 ],
        [ 675,  67, 135,   9, -26,   0 ],
        [ 802,  45,  56,   2,  25,   0 ],
        [ 810,  64,  48,  15,  25,   0 ],
        [ 817,  19,  41,   2, -25,   0 ],
        [ 827,  43,  31,   6, -25,   0 ],
        [ 834, 122,  24,   7,  25,   0 ],
        [ 575, 103,  95,   1,  25,   0 ],
    ]

    with Image.open(image_path) as image:
        pixel_data = image.load()

        for region in regions:
            x, y, w, h, dx, dy = [i * scale for i in region]
            shift_region(pixel_data, x, y, w, h, dx, dy)

        image.save(image_path)

def install_fonts(fonts):
    proc = Popen("inkscape --actions=\"user-data-directory;\"", stdout = PIPE)
    stdout, _ = proc.communicate()
    proc.wait()

    inkscape_dir = stdout.decode().strip()
    inkscape_fonts_dir = os.path.join(inkscape_dir, "fonts")

    for font_path in fonts:
        shutil.copy2(font_path, inkscape_fonts_dir)

def batch_render(image_batch):
    proc = Popen("inkscape --shell", stdin = PIPE, stdout = PIPE, stderr = STDOUT, shell = True)

    cmd = ""

    for in_path, out_path, scale, glitched in image_batch:
        cmd += f"file-open:{in_path};"
        cmd += f"export-dpi:{96 * scale};"
        cmd += f"export-filename:{out_path};"
        cmd += f"export-overwrite;"
        cmd += f"export-type:png;"
        cmd += f"export-do;"
        cmd += "\n"

    proc.communicate(input = cmd.encode(), timeout = 600)
    proc.wait()

    for in_path, out_path, scale, glitched in image_batch:
        if glitched:
            glitch(out_path, scale)

        os.remove(in_path)

# Preview generation
def generate_preview(image_path, dst_path):
    with Image.open(image_path) as image:
        image.crop((0, 0, 128, 128)).save(dst_path)

# Theme loading
def preload_themes():
    result = []

    for base_path, dirs, files in os.walk(theme_dir):
        for file_path in files:
            with open(os.path.join(base_path, file_path), "r") as theme_file:
                theme = json.load(theme_file)
                result.append(theme)

    return result

# Build chain
def log(message):
    print(f"BUILD: {message}")

def replicate_dir_structure(file_path, dst_path):
    dir_path = os.path.dirname(file_path)
    dir_full_path = os.path.join(dst_path, dir_path)

    if not os.path.exists(dir_full_path):
        log(f"Creating directory {dir_full_path}...")
        os.makedirs(dir_full_path)

def list_files_recursive(dir):
    result = []

    for base_path, dirs, files in os.walk(dir):
        for file_path in files:
            full_path = os.path.join(base_path, file_path)
            result.append(full_path)

    return result

def build():
    # Clear previous build
    if os.path.exists(build_dir):
        log("Cleaning up previous build...")
        shutil.rmtree(build_dir)

    # Create build directory
    log("Creating build directory...")
    os.mkdir(build_dir)

    # Copy main files
    fonts = []

    for mod_dir in mod_dirs:
        main_src_dir = os.path.join(source_dir, mod_dir, "main")
        main_files = list_files_recursive(main_src_dir)

        for file_path in main_files:
            rel_path = os.path.relpath(file_path, main_src_dir)
            _, file_ext = os.path.splitext(rel_path)

            replicate_dir_structure(rel_path, build_dir)

            if file_ext in [".otf", ".ttf"]:
                log(f"Copying font {file_path}...")
                dst_path = os.path.join(build_dir, rel_path)
                shutil.copyfile(file_path, dst_path)
                fonts.append(dst_path)

            else:
                log(f"Copying file {file_path}...")
                dst_path = os.path.join(build_dir, rel_path)
                shutil.copyfile(file_path, dst_path)

    # Install fonts for SVG rendering
    log("Installing fonts...")
    install_fonts(fonts)

    # Make themes
    themes = preload_themes()

    for theme in themes:
        for scale in range(1, 3):
            image_batch = []

            for mod_dir in mod_dirs:
                theme_src_dir = os.path.join(source_dir, mod_dir, "theme")
                theme_files = list_files_recursive(theme_src_dir)

                target_id = ("%s" if scale == 1 else "%s_hidpi") % theme["id"]
                target_dir = os.path.join(build_dir, "comfy_meta", target_id)

                # Process source files
                for file_path in theme_files:
                    rel_path = os.path.relpath(file_path, theme_src_dir)
                    file_name, file_ext = os.path.splitext(rel_path)

                    replicate_dir_structure(rel_path, target_dir)

                    if file_ext == ".svg":
                        log(f"Processing image {file_path}...")
                        png_path = f"{file_name}.png"
                        tmp_path = os.path.join(target_dir, rel_path)
                        dst_path = os.path.join(target_dir, png_path)
                        preprocess_text_file(file_path, tmp_path, theme, scale)
                        image_batch.append((tmp_path, dst_path, scale, os.path.basename(png_path) in glitched_boxes))

                    elif file_ext == ".rpy":
                        log(f"Processing script {file_path}...")
                        dst_path = os.path.join(target_dir, rel_path)
                        preprocess_text_file(file_path, dst_path, theme, scale)

                    elif file_ext == ".json":
                        log(f"Processing JSON {file_path}...")
                        dst_path = os.path.join(target_dir, rel_path)
                        preprocess_text_file(file_path, dst_path, theme, scale)

                    else:
                        log(f"Copying file {file_path}...")
                        dst_path = os.path.join(target_dir, rel_path)
                        shutil.copyfile(file_path, dst_path)

            log("Rendering images...")
            batch_render(image_batch)

            log("Generating theme preview...")
            textbox_path = os.path.join(target_dir, "comfy_ui", "replacers", "gui", "textbox.png")
            preview_path = os.path.join(target_dir, "preview.png")
            generate_preview(textbox_path, preview_path)

            # Pack assets
            log(f"Creating archive for {target_id}...")
            shutil.make_archive(target_dir, "zip", target_dir)
            os.rename(f"{target_dir}.zip", f"{target_dir}.arc")
            shutil.rmtree(target_dir)

    # Create release archive if needed
    if release_mode:
        log("Creating release archive...")
        shutil.make_archive("Release", "zip", build_dir)
        shutil.rmtree(build_dir)

    log("Finished!")

preload_themes()
build()
