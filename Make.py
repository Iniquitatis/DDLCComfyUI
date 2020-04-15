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
dpi_scale = 1

theme_dir  = "Themes"
source_dir = "Source"
build_dir  = "Build"

dir_structure = [
    "gui",
    "gui/button",
    "gui/overlay",
    "mod_assets",
    "mod_assets/buttons",
    "mod_assets/buttons/squares",
    "mod_assets/calendar",
    "mod_assets/console",
    "mod_assets/font",
    "mod_assets/frames",
    "mod_assets/games",
    "mod_assets/games/hangman",
]

common_files = [
    "mod_assets/font/Nunito-Bold.ttf",
    "mod_assets/font/Nunito-SemiBold.ttf",
    "mod_assets/font/Nunito-SemiBoldItalic.ttf",
    "mod_assets/font/OFL.txt",
]

scripts = [
    "zzz_comfy_ui.rpy",
]

vector_images = [
    "gui/ctc",
    "gui/frame",
    "gui/frame_d",
    "gui/menu_bg",
    "gui/menu_bg_d",
    "gui/namebox",
    "gui/namebox_d",
    "gui/textbox",
    "gui/textbox_d",
    "gui/textbox_monika",
    "gui/textbox_monika_d",
    "gui/button/choice_dark_hover_background",
    "gui/button/choice_dark_idle_background",
    "gui/button/choice_hover_background",
    "gui/button/choice_idle_background",
    "gui/button/scrollable_menu_dark_disable_background",
    "gui/button/scrollable_menu_dark_hover_background",
    "gui/button/scrollable_menu_dark_idle_background",
    "gui/button/scrollable_menu_disable_background",
    "gui/button/scrollable_menu_hover_background",
    "gui/button/scrollable_menu_idle_background",
    "gui/button/twopane_scrollable_menu_dark_hover_background",
    "gui/button/twopane_scrollable_menu_dark_idle_background",
    "gui/button/twopane_scrollable_menu_hover_background",
    "gui/button/twopane_scrollable_menu_idle_background",
    "gui/overlay/confirm",
    "gui/overlay/confirm_d",
    "gui/overlay/game_menu",
    "gui/overlay/game_menu_d",
    "gui/overlay/main_menu",
    "gui/overlay/main_menu_d",
    "mod_assets/hkb_disabled_background",
    "mod_assets/hkb_disabled_background_d",
    "mod_assets/hkb_hover_background",
    "mod_assets/hkb_hover_background_d",
    "mod_assets/hkb_idle_background",
    "mod_assets/hkb_idle_background_d",
    "mod_assets/island_hover_background",
    "mod_assets/island_hover_background_d",
    "mod_assets/island_idle_background",
    "mod_assets/island_idle_background_d",
    "mod_assets/music_menu",
    "mod_assets/music_menu_d",
    "mod_assets/buttons/squares/square_disabled",
    "mod_assets/buttons/squares/square_disabled_d",
    "mod_assets/buttons/squares/square_hover",
    "mod_assets/buttons/squares/square_hover_d",
    "mod_assets/buttons/squares/square_idle",
    "mod_assets/buttons/squares/square_idle_d",
    "mod_assets/calendar/calendar_bg",
    "mod_assets/calendar/calendar_bg-n",
    "mod_assets/calendar/calendar_close",
    "mod_assets/calendar/calendar_close-n",
    "mod_assets/calendar/calendar_close_hover",
    "mod_assets/calendar/calendar_close_hover-n",
    "mod_assets/calendar/calendar_day_bg",
    "mod_assets/calendar/calendar_day_bg-n",
    "mod_assets/calendar/calendar_day_disabled_bg",
    "mod_assets/calendar/calendar_day_disabled_bg-n",
    "mod_assets/calendar/calendar_day_hover_bg",
    "mod_assets/calendar/calendar_day_hover_bg-n",
    "mod_assets/calendar/calendar_day_name_bg",
    "mod_assets/calendar/calendar_day_name_bg-n",
    "mod_assets/calendar/calendar_left_arrow",
    "mod_assets/calendar/calendar_left_arrow-n",
    "mod_assets/calendar/calendar_left_arrow_hover",
    "mod_assets/calendar/calendar_left_arrow_hover-n",
    "mod_assets/calendar/calendar_right_arrow",
    "mod_assets/calendar/calendar_right_arrow-n",
    "mod_assets/calendar/calendar_right_arrow_hover",
    "mod_assets/calendar/calendar_right_arrow_hover-n",
    "mod_assets/console/cn_frame",
    "mod_assets/frames/black70_pinkborder100",
    "mod_assets/frames/black70_pinkborder100_d",
    "mod_assets/frames/black70_pinkborder100_2px",
    "mod_assets/frames/black70_pinkborder100_2px_d",
    "mod_assets/frames/black70_pinkborder100_5px",
    "mod_assets/frames/black70_pinkborder100_5px_d",
    "mod_assets/frames/modebar",
    "mod_assets/frames/modebar_d",
    "mod_assets/frames/selector_overlay",
    "mod_assets/frames/selector_overlay_d",
    "mod_assets/frames/selector_overlay_disabled",
    "mod_assets/frames/selector_overlay_disabled_d",
    "mod_assets/frames/selector_top_frame",
    "mod_assets/frames/selector_top_frame_d",
    "mod_assets/frames/selector_top_frame_disabled",
    "mod_assets/frames/selector_top_frame_disabled_d",
    "mod_assets/frames/selector_top_frame_selected",
    "mod_assets/frames/selector_top_frame_selected_d",
    "mod_assets/frames/trans_pink2pxborder100",
    "mod_assets/frames/trans_pink2pxborder100_d",
    "mod_assets/games/hangman/hm_0",
    "mod_assets/games/hangman/hm_1",
    "mod_assets/games/hangman/hm_2",
    "mod_assets/games/hangman/hm_3",
    "mod_assets/games/hangman/hm_4",
    "mod_assets/games/hangman/hm_5",
    "mod_assets/games/hangman/hm_6",
    "mod_assets/games/hangman/hm_frame",
    "mod_assets/games/hangman/hm_frame_d",
    "mod_assets/games/hangman/hm_sm_0",
    "mod_assets/games/hangman/hm_sm_1",
    "mod_assets/games/hangman/hm_sm_2",
    "mod_assets/games/hangman/hm_sm_3",
    "mod_assets/games/hangman/hm_sm_4",
    "mod_assets/games/hangman/hm_sm_5",
    "mod_assets/games/hangman/hm_sm_6",
]

glitched_boxes = [
    "gui/textbox_monika",
    "gui/textbox_monika_d",
]

glitch_regions = [
    #   X    Y    W    H   DX   DY
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

################################################################################
# Script itself
################################################################################
import json
import os
import re
import shutil

from PIL import Image
from hsluv import *

themes = []

# Text file preprocessing
def FormatRGBHexString(r, g, b):
    return "#%02x%02x%02x" % (int(r), int(g), int(b))

def FormatRGBAHexString(r, g, b, a):
    return "#%02x%02x%02x%02x" % (int(r), int(g), int(b), int(a))

def ModulateRGBColor(r, g, b, h, s):
    r = float(r) / 255.0
    g = float(g) / 255.0
    b = float(b) / 255.0

    ch, cs, cl = rgb_to_hsluv([r, g, b])
    r, g, b = hsluv_to_rgb([h, cs * s, cl])

    return (int(r * 255.0),
            int(g * 255.0),
            int(b * 255.0))

def ModulateRGBAColor(r, g, b, a, h, s):
    r = float(r) / 255.0
    g = float(b) / 255.0
    b = float(b) / 255.0
    a = float(a) / 255.0

    ch, cs, cl = rgb_to_hsluv([r, g, b])
    r, g, b = hsluv_to_rgb([h, cs * s, cl])

    return (int(r * 255.0),
            int(g * 255.0),
            int(b * 255.0),
            int(a * 255.0))

def GetThemeParameter(macro_args, method_args):
    return str(method_args)

def ModulateColors(macro_args, method_args):
    h, s = method_args

    if len(macro_args) == 3:
        r, g, b = macro_args
        if h == None or s == None:
            return FormatRGBHexString(r, g, b)
        r, g, b = ModulateRGBColor(int(r), int(g), int(b), float(h), float(s))
        return FormatRGBHexString(r, g, b)
    elif len(macro_args) == 4:
        r, g, b, a = macro_args
        if h == None or s == None:
            return FormatRGBAHexString(r, g, b, a)
        r, g, b, a = ModulateRGBAColor(int(r), int(g), int(b), int(a), float(h), float(s))
        return FormatRGBAHexString(r, g, b, a)

    return "#baadf00d"

def ParseMacroArguments(match):
    if match.lastindex == None or match.lastindex == 0:
        # No arguments has been passed to the macro
        return []

    args_string = match.group(1)

    query = r""
    for i in range(0, 4):
        query += r"\s*([A-Za-z0-9_\-.]+)\s*"
        result = re.findall(query, args_string)
        if len(result) > 0:
            return result
        query += r","

def PreprocessTextFile(in_path, out_path, theme):
    text = ""

    with open(in_path, "r") as file:
        text = file.read()

    macros = [
        [ "CUI_BTN_ROUNDING"    , GetThemeParameter, (theme["button_rounding"])                              ],
        [ "CUI_FRM_ROUNDING"    , GetThemeParameter, (theme["frame_rounding"])                               ],
        [ "CUI_DLG_ROUNDING"    , GetThemeParameter, (theme["dialog_rounding"])                              ],
        [ "CUI_MAIN_FONT"       , GetThemeParameter, (theme["main_font"]["normal"])                          ],
        [ "CUI_MAIN_FONT_BOLD"  , GetThemeParameter, (theme["main_font"]["bold"])                            ],
        [ "CUI_MAIN_FONT_ITALIC", GetThemeParameter, (theme["main_font"]["italic"])                          ],
        [ "CUI_MENU_FONT"       , GetThemeParameter, (theme["menu_font"])                                    ],
        [ "CUI_OPTION_FONT"     , GetThemeParameter, (theme["option_font"])                                  ],
        [ "CUI_PRM_COLOR"       , ModulateColors   , (theme["primary_hue"], theme["primary_saturation"])     ],
        [ "CUI_SCD_COLOR"       , ModulateColors   , (theme["secondary_hue"], theme["secondary_saturation"]) ],
    ]

    for macro_name, method, method_args in macros:
        query = macro_name + r"\(([A-Za-z0-9_\-,. ]*)\)"
        text = re.sub(query, lambda match: method(ParseMacroArguments(match), method_args), text)

    with open(out_path, "w") as file:
        file.write(text)

# Image glitching
def ShiftRegion(pixel_data, x, y, w, h, dx, dy):
    region_data = []
    for ix in range(0, w):
        region_data.append([])
        for iy in range(0, h):
            region_data[-1].append((0, 0, 0, 0))

    for ix in range(0, w):
        for iy in range(0, h):
            region_data[ix][iy] = pixel_data[x + ix, y + iy]
            pixel_data[x + ix, y + iy] = (0, 0, 0, 0)

    for ix in range(0, w):
        for iy in range(0, h):
            # FIXME: actually, the pixels should be mixed differently, but let's just overwrite them for now
            pixel_data[x + dx + ix, y + dy + iy] = region_data[ix][iy]

def Glitch(image_path):
    with Image.open(image_path) as image:
        pixel_data = image.load()
        for x, y, w, h, dx, dy in glitch_regions:
            x  *= dpi_scale
            y  *= dpi_scale
            w  *= dpi_scale
            h  *= dpi_scale
            dx *= dpi_scale
            dy *= dpi_scale
            ShiftRegion(pixel_data, x, y, w, h, dx, dy)
        image.save(image_path)

# Theme loading
def PreloadThemes():
    for base_path, dirs, files in os.walk(theme_dir):
        for file_path in files:
            with open(os.path.join(base_path, file_path), "r") as json_file:
                json_data = json.load(json_file)
                themes.append(json_data)

# Build chain
def Log(message):
    print("BUILD: %s" % message)

def Build():
    if os.path.exists(build_dir):
        Log("Cleaning up previous build...")
        shutil.rmtree(build_dir)

    Log("Creating directory %s..." % build_dir)
    os.mkdir(build_dir)

    for theme in themes:
        theme_dir = "%s/%s" % (build_dir, theme["asset_directory"])
        Log("Creating directory %s..." % (theme_dir))
        os.mkdir(theme_dir)

        for dir_path in dir_structure:
            dir_full_path = ("%s/%s") % (theme_dir, dir_path)
            Log("Creating directory %s..." % (dir_full_path))
            os.mkdir(dir_full_path)

        for file_path in common_files:
            Log("Copying file %s..." % file_path)
            shutil.copyfile("%s/%s" % (source_dir, file_path), "%s/%s" % (theme_dir, file_path))

        for script_path in scripts:
            Log("Processing file %s..." % script_path)
            PreprocessTextFile("%s/%s" % (source_dir, script_path), "%s/%s" % (theme_dir, script_path), theme)

        for image_path in vector_images:
            Log("Rendering file %s.svg..." % image_path)
            PreprocessTextFile("%s/%s.svg" % (source_dir, image_path), "Temporary.svg", theme)
            os.system("inkscape "
                        "--batch-process "
                        "--export-dpi=\"%i\" "
                        "--export-filename=\"%s/%s.png\" "
                        "--export-overwrite "
                        "--export-type=\"png\" "
                        "Temporary.svg" % (96 * dpi_scale, theme_dir, image_path))
            os.remove("Temporary.svg")

        for image_path in glitched_boxes:
            Log("Glitching image %s.png..." % image_path)
            Glitch("%s/%s.png" % (theme_dir, image_path))

    Log("Finished!")

PreloadThemes()
Build()
