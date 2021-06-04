################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################
import itertools
import json
import re
import shutil
from argparse import ArgumentParser
from pathlib import Path
from subprocess import Popen, PIPE, STDOUT

import freetype
from PIL import Image
from hsluv import *

theme_dir  = Path("Themes")
source_dir = Path("Source")
build_dir  = Path("Build")
ddlc_dir   = Path("ddlc")

rpa_name = "comfy_ui.rpa"

rpatool_path = Path("rpatool.py")

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

    ch, cs, cl = rgb_to_hsluv((r, g, b))
    r, g, b = hsluv_to_rgb((clamp(h, 0.0, 360.0),
                            clamp(cs * s, 0.0, 100.0),
                            clamp(cl + l * 100.0, 0.0, 100.0)))

    return (int(round(r * 255.0)),
            int(round(g * 255.0)),
            int(round(b * 255.0)))

def modulate_rgba_color(r, g, b, a, h, s, l):
    r = float(r) / 255.0
    g = float(b) / 255.0
    b = float(b) / 255.0
    a = float(a) / 255.0

    ch, cs, cl = rgb_to_hsluv((r, g, b))
    r, g, b = hsluv_to_rgb((clamp(h, 0.0, 360.0),
                            clamp(cs * s, 0.0, 100.0),
                            clamp(cl + l * 100.0, 0.0, 100.0)))

    return (int(round(r * 255.0)),
            int(round(g * 255.0)),
            int(round(b * 255.0)),
            int(round(a * 255.0)))

def modulate_colors(h, s, l):
    is_modulated = (h != None and s != None and l != None)

    def macro(args, _):
        if len(args) == 3:
            r, g, b = args

            if is_modulated:
                r, g, b = modulate_rgb_color(int(r), int(g), int(b), float(h), float(s), float(l))

            return format_rgb_hex_string(r, g, b)

        elif len(args) == 4:
            r, g, b, a = args

            if is_modulated:
                r, g, b, a = modulate_rgba_color(int(r), int(g), int(b), int(a), float(h), float(s), float(l))

            return format_rgba_hex_string(r, g, b, a)

        return "#baadf00d"

    return macro

def include_text():
    def macro(args, file_meta):
        file_path, line, column = file_meta
        inc_path = file_path.parent / args[0]

        result = ""

        with open(inc_path, "r") as inc_file:
            indentation = " " * column

            for i, inc_line in enumerate(inc_file):
                if i == 0 or inc_line == "\n":
                    result += inc_line
                else:
                    result += indentation + inc_line

        return result

    return macro

def stringize(value):
    string = str(value)

    def macro(args, _):
        return string

    return macro

def get_font_name(path):
    font = freetype.Face(str(build_dir / path))
    font_name = font.family_name.decode()

    def macro(args, _):
        return font_name

    return macro

def parse_macro_args(match):
    if match.lastindex == None or match.lastindex == 0:
        # No arguments have been passed to the macro
        return []

    args_string = match.group(1)

    query = r""

    for i in range(4):
        query += r"\s*([\w\-./]+)\s*"
        result = re.findall(query, args_string)

        if len(result) > 0:
            return result

        query += r","

def preprocess_text_file(in_path, out_path, theme, scale):
    prm_color = theme["primary_color"]
    scd_color = theme["secondary_color"]

    macros = {
        "CUI_INCLUDE":               include_text(),
        "CUI_THEME_ID":              stringize(("%s" if scale == 1 else "%s_hidpi") % theme["id"]),
        "CUI_THEME_NAME":            stringize(("%s" if scale == 1 else "%s (HiDPI)") % theme["name"]),
        "CUI_BTN_ROUNDING":          stringize(theme["button_rounding"]),
        "CUI_FRM_ROUNDING":          stringize(theme["frame_rounding"]),
        "CUI_DLG_ROUNDING":          stringize(theme["dialogue_rounding"]),
        "CUI_MNU_PTSHAPE":           stringize(theme["menu_pattern_shape"]),
        "CUI_DLG_PTSHAPE":           stringize(theme["dialogue_pattern_shape"]),
        "CUI_MAIN_FONT_NAME":        get_font_name(theme["main_font"]["regular"]),
        "CUI_MAIN_FONT_REGULAR":     stringize(theme["main_font"]["regular"]),
        "CUI_MAIN_FONT_ITALIC":      stringize(theme["main_font"]["italic"]),
        "CUI_MAIN_FONT_BOLD":        stringize(theme["main_font"]["bold"]),
        "CUI_MAIN_FONT_BOLD_ITALIC": stringize(theme["main_font"]["bold_italic"]),
        "CUI_MENU_FONT":             stringize(theme["menu_font"]),
        "CUI_OPTION_FONT":           stringize(theme["option_font"]),
        "CUI_MAIN_FONT_KERNING":     stringize(theme["main_font_kerning"]),
        "CUI_DLG_VERT_OFFSET":       stringize(theme["dialogue_vertical_offset"]),
        "CUI_DLG_LINE_SPACING":      stringize(theme["dialogue_line_spacing"]),
        "CUI_BTN_HEIGHT_ADJUSTMENT": stringize(theme["button_height_adjustment"]),
        "CUI_PRM_COLOR":             modulate_colors(prm_color["h"], prm_color["s"], prm_color["l"]),
        "CUI_SCD_COLOR":             modulate_colors(scd_color["h"], scd_color["s"], scd_color["l"]),
        "CUI_SCALE":                 stringize(scale),
        "CUI_SCALE_INV":             stringize(1.0 / scale),
    }

    with open(in_path, "r") as in_file, open(out_path, "w") as out_file:
        for i, line in enumerate(in_file):
            for macro_name, macro in macros.items():
                query = macro_name + r"\(([\w\s\-.,/]*)\)"
                line = re.sub(query, lambda match: macro(parse_macro_args(match), (in_path, i, match.start())), line)

            out_file.write(line)

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
        #  X|   Y|   W|   H|  DX|  DY
        ( 42,   5, 144,  15, -25,   0),
        ( 42,  36,  41,  10,  25,   0),
        ( 42,  62,  91,   5, -25,   0),
        ( 42,  92,  87,   7, -25,   0),
        ( 42, 108,  30,   4,  25,   0),
        (123, 115, 183,  20,  25,   0),
        (183,  77, 129,  22, -26,   0),
        (215,  86,  50,   1,   1,   0),
        (225,  40,  99,  20, -25,   0),
        (273,  15, 136,  11,  25,   0),
        (309,  86,  58,   1, -25,   0),
        (336,  87, 147,  28, -26,   0),
        (372,  54, 213,   4,  25,   0),
        (408,  20,  80,   3, -26,   0),
        (444,  72, 159,   6, -25,   0),
        (448, 127,  83,   9, -25,   0),
        (516,  35, 116,   6, -26,   0),
        (564,  93, 128,   3, -26,   0),
        (625,  36, 108,   8, -25,   0),
        (670, 101, 156,  12, -25,   0),
        (675,  67, 135,   9, -26,   0),
        (802,  45,  56,   2,  25,   0),
        (810,  64,  48,  15,  25,   0),
        (817,  19,  41,   2, -25,   0),
        (827,  43,  31,   6, -25,   0),
        (834, 122,  24,   7,  25,   0),
        (575, 103,  95,   1,  25,   0),
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

    inkscape_dir = Path(stdout.decode().strip())
    inkscape_fonts_dir = inkscape_dir / "fonts"

    for font_path in fonts:
        shutil.copy2(font_path, inkscape_fonts_dir)

def batch_render(images, scale):
    proc = Popen("inkscape --shell", stdin = PIPE, stdout = PIPE, stderr = STDOUT, shell = True)

    cmd = ""

    for svg_path in images:
        png_path = svg_path.with_suffix(".png")

        cmd += f"file-open:{svg_path};"
        cmd += f"export-dpi:{96 * scale};"
        cmd += f"export-filename:{png_path};"
        cmd += f"export-overwrite;"
        cmd += f"export-type:png;"
        cmd += f"export-do;"
        cmd += "\n"

    proc.communicate(input = cmd.encode(), timeout = 600)
    proc.wait()

    glitched_boxes = ["textbox_monika.png", "textbox_monika_d.png"]

    for svg_path in images:
        png_path = svg_path.with_suffix(".png")

        if png_path.name in glitched_boxes:
            glitch(png_path, scale)

        svg_path.unlink()

# Build chain
def log(message):
    print(f"BUILD: {message}")

def copy_dir_contents(src_dir, dst_dir, theme = None, scale = None):
    fonts, images = [], []

    for file_path in src_dir.rglob("*.*"):
        src_path = file_path.relative_to(src_dir)
        dst_path = dst_dir / src_path

        file_ext = src_path.suffix

        dst_path.parent.mkdir(parents = True, exist_ok = True)

        if file_ext == ".svg" and theme and scale:
            log(f"Processing image {file_path}...")
            preprocess_text_file(file_path, dst_path, theme, scale)
            images.append(dst_path)

        elif file_ext == ".rpy" and theme and scale:
            log(f"Processing script {file_path}...")
            preprocess_text_file(file_path, dst_path, theme, scale)

        elif file_ext == ".json" and theme and scale:
            log(f"Processing JSON {file_path}...")
            preprocess_text_file(file_path, dst_path, theme, scale)

        elif file_ext in [".otf", ".ttf"]:
            log(f"Copying font {file_path}...")
            shutil.copyfile(file_path, dst_path)
            fonts.append(dst_path)

        else:
            log(f"Copying file {file_path}...")
            shutil.copyfile(file_path, dst_path)

    if len(fonts) > 0:
        log("Installing fonts...")
        install_fonts(fonts)

    if len(images) > 0:
        log("Rendering images...")
        batch_render(images, scale)

def make_archive(dir, archive_path, remove_dir = False):
    shutil.make_archive(archive_path.with_suffix(""), "zip", dir)
    archive_path.with_suffix(".zip").rename(archive_path)

    if remove_dir:
        shutil.rmtree(dir)

def make_rpa(build_dir, ddlc_dir):
    import os
    import time

    files = [path.relative_to(build_dir) for path in build_dir.rglob("*.*")]

    base_dir = Path.cwd()
    ddlc_game_dir = ddlc_dir / "game"

    for path in files:
        src = build_dir / path
        dst = ddlc_game_dir / path
        dst.parent.mkdir(parents = True, exist_ok = True)
        shutil.copyfile(src, dst)

    # HACK: arguments will prevent the game from starting, but it will still compile the scripts
    os.system(str(ddlc_dir / "DDLC") + " --blah")
    time.sleep(10)

    for path in files:
        if path.suffix == ".rpy":
            rpyc_src = (ddlc_game_dir / path).with_suffix(".rpyc")
            rpyc_dst = (build_dir / path).with_suffix(".rpyc")
            shutil.copyfile(rpyc_src, rpyc_dst)
            rpyc_src.unlink()

        (ddlc_game_dir / path).unlink()

    rpatool_rel_path = os.path.relpath(rpatool_path, build_dir)

    os.chdir(build_dir)

    os.system(f"python {rpatool_rel_path} -v -c {rpa_name} " + " ".join(os.listdir(".")))
    os.system(f"python {rpatool_rel_path} -l {rpa_name}")

    os.chdir(base_dir)

def build(mod_dirs, release_mode):
    # Clear previous build
    if build_dir.exists():
        log("Cleaning up previous build...")
        shutil.rmtree(build_dir)

    # Create build directory
    log("Creating build directory...")
    build_dir.mkdir()

    # Copy main files
    for mod_dir in mod_dirs:
        main_src_dir = source_dir / mod_dir / "main"
        copy_dir_contents(main_src_dir, build_dir)

    # Make themes
    for theme_path, scale in itertools.product(theme_dir.iterdir(), range(1, 3)):
        theme = json.load(theme_path.open("r"))

        target_id = ("%s" if scale == 1 else "%s_hidpi") % theme["id"]
        target_dir = build_dir / "comfy_meta" / target_id

        for mod_dir in mod_dirs:
            theme_src_dir = source_dir / mod_dir / "theme"
            copy_dir_contents(theme_src_dir, target_dir, theme, scale)

    make_rpa(build_dir, ddlc_dir)

    # Create release archive if needed
    if release_mode:
        log("Creating release archive...")
        make_archive(build_dir, "Release.zip", True)

    log("Finished!")

if __name__ == "__main__":
    ap = ArgumentParser()
    ap.add_argument("-t", "--target",
                    type = str,
                    choices = ["ddlc", "mas"],
                    default = "ddlc",
                    help = "set target")
    ap.add_argument("-r", "--release",
                    action = "store_true",
                    help = "enable release mode")

    args = ap.parse_args()

    mod_dirs = [Path("common")]

    if args.target and args.target == "mas":
        mod_dirs.append(Path("mas"))

    build(mod_dirs, args.release)
