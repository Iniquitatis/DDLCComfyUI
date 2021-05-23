################################################################################
#
# Copyright (c) 2020 Dominus Iniquitatis <zerosaiko@gmail.com>
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
    "mas",
]

glitched_boxes = [
    "comfy_ui/replacers/gui/textbox_monika.png",
    "comfy_ui/replacers/gui/textbox_monika_d.png",
]

################################################################################
# Script itself
################################################################################
import json
import os
import re
import shutil

from PIL import Image
from hsluv import *

# Text file preprocessing
def Clamp(value, lower, upper):
    return min(max(value, lower), upper)

def FormatRGBHexString(r, g, b):
    return "#%02x%02x%02x" % (int(r), int(g), int(b))

def FormatRGBAHexString(r, g, b, a):
    return "#%02x%02x%02x%02x" % (int(r), int(g), int(b), int(a))

def ModulateRGBColor(r, g, b, h, s, l):
    r = float(r) / 255.0
    g = float(g) / 255.0
    b = float(b) / 255.0

    ch, cs, cl = rgb_to_hsluv([r, g, b])
    r, g, b = hsluv_to_rgb([Clamp(h, 0.0, 360.0),
                            Clamp(cs * s, 0.0, 100.0),
                            Clamp(cl + l * 100.0, 0.0, 100.0)])

    return (int(r * 255.0),
            int(g * 255.0),
            int(b * 255.0))

def ModulateRGBAColor(r, g, b, a, h, s, l):
    r = float(r) / 255.0
    g = float(b) / 255.0
    b = float(b) / 255.0
    a = float(a) / 255.0

    ch, cs, cl = rgb_to_hsluv([r, g, b])
    r, g, b = hsluv_to_rgb([Clamp(h, 0.0, 360.0),
                            Clamp(cs * s, 0.0, 100.0),
                            Clamp(cl + l * 100.0, 0.0, 100.0)])

    return (int(r * 255.0),
            int(g * 255.0),
            int(b * 255.0),
            int(a * 255.0))

def ModulateColors(macro_args, method_args):
    h, s, l = method_args

    if len(macro_args) == 3:
        r, g, b = macro_args
        if h != None and s != None and l != None:
            r, g, b = ModulateRGBColor(int(r), int(g), int(b), float(h), float(s), float(l))
        return FormatRGBHexString(r, g, b)
    elif len(macro_args) == 4:
        r, g, b, a = macro_args
        if h != None and s != None and l != None:
            r, g, b, a = ModulateRGBAColor(int(r), int(g), int(b), int(a), float(h), float(s), float(l))
        return FormatRGBAHexString(r, g, b, a)

    return "#baadf00d"

def Stringize(macro_args, method_args):
    return str(method_args)

def ParseMacroArguments(match):
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

def PreprocessTextFile(in_path, out_path, theme, scale):
    prm_color = theme["primary_color"]
    scd_color = theme["secondary_color"]

    macros = [
        # Name                       | Method        | Arguments
        [ "CUI_THEME_NAME"           , Stringize     , (("%s" if scale == 1 else "%s (HiDPI)") % theme["name"]) ],
        [ "CUI_BTN_ROUNDING"         , Stringize     , (theme["button_rounding"])                               ],
        [ "CUI_FRM_ROUNDING"         , Stringize     , (theme["frame_rounding"])                                ],
        [ "CUI_DLG_ROUNDING"         , Stringize     , (theme["dialogue_rounding"])                             ],
        [ "CUI_MNU_PTSHAPE"          , Stringize     , (theme["menu_pattern_shape"])                            ],
        [ "CUI_DLG_PTSHAPE"          , Stringize     , (theme["dialogue_pattern_shape"])                        ],
        [ "CUI_MAIN_FONT_REGULAR"    , Stringize     , (theme["main_font"]["regular"])                          ],
        [ "CUI_MAIN_FONT_ITALIC"     , Stringize     , (theme["main_font"]["italic"])                           ],
        [ "CUI_MAIN_FONT_BOLD"       , Stringize     , (theme["main_font"]["bold"])                             ],
        [ "CUI_MAIN_FONT_BOLD_ITALIC", Stringize     , (theme["main_font"]["bold_italic"])                      ],
        [ "CUI_MENU_FONT"            , Stringize     , (theme["menu_font"])                                     ],
        [ "CUI_OPTION_FONT"          , Stringize     , (theme["option_font"])                                   ],
        [ "CUI_MAIN_FONT_KERNING"    , Stringize     , (theme["main_font_kerning"])                             ],
        [ "CUI_DLG_VERT_OFFSET"      , Stringize     , (theme["dialogue_vertical_offset"])                      ],
        [ "CUI_DLG_LINE_SPACING"     , Stringize     , (theme["dialogue_line_spacing"])                         ],
        [ "CUI_PRM_COLOR"            , ModulateColors, (prm_color["h"], prm_color["s"], prm_color["l"])         ],
        [ "CUI_SCD_COLOR"            , ModulateColors, (scd_color["h"], scd_color["s"], scd_color["l"])         ],
        [ "CUI_SCALE"                , Stringize     , (scale)                                                  ],
        [ "CUI_SCALE_INV"            , Stringize     , (1.0 / scale)                                            ],
    ]

    with open(in_path, "r") as in_file, open(out_path, "w") as out_file:
        text = in_file.read()

        for macro_name, method, method_args in macros:
            query = macro_name + r"\(([\w\s\-.,]*)\)"
            text = re.sub(query, lambda match: method(ParseMacroArguments(match), method_args), text)

        out_file.write(text)

# Image rendering
def ShiftRegion(pixel_data, x, y, w, h, dx, dy):
    region_data = [[pixel_data[x + i, y + j] for j in range(h)] for i in range(w)]

    for i in range(w):
        for j in range(h):
            pixel_data[x + i, y + j] = (0, 0, 0, 0)

    for i in range(w):
        for j in range(h):
            # FIXME: actually, the pixels should be mixed differently, but let's just overwrite them for now
            pixel_data[x + dx + i, y + dy + j] = region_data[i][j]

def Glitch(image_path, scale):
    regions = [
        # X  | Y  | W  | H  | DX | DY
        [  42,   5, 144,  15, -25,   0 ],
        [  42,  36,  41,  10,  25,   0 ],
        [  42,  62,  91,   5, -25,   0 ],
        [  42,  92,  87,   7, -25,   0 ],
        [  42, 108,  30,   4,  25,   0 ],
        [ 123, 115, 183,  20,  25,   0 ],
        [ 183,  77, 129,  22, -26,   0 ],
        [ 225,  40,  99,  20, -25,   0 ],
        [ 273,  15, 136,  11,  25,   0 ],
        [ 309,  86,  58,   1, -25,   0 ],
        [ 336,  87, 147,  28, -26,   0 ],
        [ 372,  54, 213,   4,  25,   0 ],
        [ 408,  20,  80,   3, -26,   0 ],
        [ 444,  72, 159,   6, -25,   0 ],
        [ 448, 127,  83,   9, -25,   0 ],
        [ 516,  35, 116,   6, -33,   0 ],
        [ 564,  93, 128,   3, -26,   0 ],
        [ 575, 103,  95,   1,  25,   0 ],
        [ 625,  36, 108,   8, -25,   0 ],
        [ 670, 101, 156,  12, -25,   0 ],
        [ 675,  67, 135,   9, -26,   0 ],
        [ 802,  45,  56,   2,  25,   0 ],
        [ 810,  64,  48,  15,  25,   0 ],
        [ 817,  19,  41,   2, -25,   0 ],
        [ 827,  43,  31,   6, -25,   0 ],
        [ 834, 122,  24,   7,  25,   0 ],
    ]

    with Image.open(image_path) as image:
        pixel_data = image.load()
        for region in regions:
            [x, y, w, h, dx, dy] = [i * scale for i in region]
            ShiftRegion(pixel_data, x, y, w, h, dx, dy)
        image.save(image_path)

def RenderImage(in_path, out_path, scale, glitched):
    if release_mode:
        os.system("inkscape "
                 "--batch-process "
                 "--export-dpi=\"%i\" "
                 "--export-filename=\"%s\" "
                 "--export-overwrite "
                 "--export-type=\"png\" "
                 "\"%s\"" % (96 * scale, out_path, in_path))
    else:
        os.system("magick "
                  "-background \"none\" "
                  "-density \"%i\" "
                  "\"%s\" "
                  "\"%s\"" % (96 * scale, in_path, out_path))

    if glitched:
        Glitch(out_path, scale)

# Theme loading
def PreloadThemes():
    result = []

    for base_path, dirs, files in os.walk(theme_dir):
        for file_path in files:
            with open(os.path.join(base_path, file_path), "r") as theme_file:
                theme = json.load(theme_file)
                result.append(theme)

    return result

# Build chain
def Log(message):
    print("BUILD: %s" % message)

def ReplicateDirStructure(file_path, dst_path):
    dir_path = os.path.dirname(file_path)
    dir_full_path = os.path.join(dst_path, dir_path)

    if not os.path.exists(dir_full_path):
        Log("Creating directory %s..." % dir_full_path)
        os.makedirs(dir_full_path)

def ListFilesRecursive(dir):
    result = []

    for base_path, dirs, files in os.walk(dir):
        for file_path in files:
            full_path = os.path.join(base_path, file_path)
            result.append(full_path)

    return result

def Build():
    # Clear previous build
    if os.path.exists(build_dir):
        Log("Cleaning up previous build...")
        shutil.rmtree(build_dir)

    # Create build directory
    Log("Creating build directory...")
    os.mkdir(build_dir)

    # Replicate directory structure
    for mod_dir in mod_dirs:
        main_src_dir = os.path.join(source_dir, mod_dir, "main")
        main_files = ListFilesRecursive(main_src_dir)

        # Copy common files
        for file_path in main_files:
            Log("Copying file %s..." % file_path)
            rel_path = os.path.relpath(file_path, main_src_dir)
            dst_path = os.path.join(build_dir, rel_path)
            ReplicateDirStructure(rel_path, build_dir)
            shutil.copyfile(file_path, dst_path)

    # Make themes
    themes = PreloadThemes()

    for theme in themes:
        for scale in range(1, 3):
            for mod_dir in mod_dirs:
                theme_src_dir = os.path.join(source_dir, mod_dir, "theme")
                theme_files = ListFilesRecursive(theme_src_dir)

                target_id = ("%s" if scale == 1 else "%s_hidpi") % theme["id"]
                target_dir = os.path.join(build_dir, "comfy_meta", target_id)

                # Process source files
                for file_path in theme_files:
                    rel_path = os.path.relpath(file_path, theme_src_dir)
                    (file_name, file_ext) = os.path.splitext(rel_path)

                    ReplicateDirStructure(rel_path, target_dir)

                    if file_ext == ".svg":
                        Log("Rendering image %s..." % file_path)
                        png_path = "%s.png" % file_name
                        tmp_path = os.path.join(build_dir, "Temporary.svg")
                        dst_path = os.path.join(target_dir, png_path)
                        PreprocessTextFile(file_path, tmp_path, theme, scale)
                        RenderImage(tmp_path, dst_path, scale, png_path in glitched_boxes)
                        os.remove(tmp_path)
                    elif file_ext == ".rpy":
                        Log("Processing script %s..." % file_path)
                        dst_path = os.path.join(target_dir, rel_path)
                        PreprocessTextFile(file_path, dst_path, theme, scale)
                    elif file_ext == ".json":
                        Log("Processing JSON %s..." % file_path)
                        dst_path = os.path.join(target_dir, rel_path)
                        PreprocessTextFile(file_path, dst_path, theme, scale)
                    else:
                        Log("Copying file %s..." % file_path)
                        dst_path = os.path.join(target_dir, rel_path)
                        shutil.copyfile(file_path, dst_path)

            # Pack assets
            Log("Creating archive for %s..." % target_id)
            shutil.make_archive(target_dir, "zip", target_dir)
            os.rename("%s.zip" % target_dir, "%s.arc" % target_dir)
            shutil.rmtree(target_dir)

    # Create release archive if needed
    if release_mode:
        Log("Creating release archive...")
        shutil.make_archive("Release", "zip", build_dir)
        shutil.rmtree(build_dir)

    Log("Finished!")

PreloadThemes()
Build()
