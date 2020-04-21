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
dpi_scale = 1

theme_dir  = "Themes"
source_dir = "Source"
build_dir  = "Build"

files = [
    # Default
    "gui/ctc.svg",
    "gui/frame.svg",
    "gui/frame_d.svg",
    "gui/menu_bg.svg",
    "gui/menu_bg_d.svg",
    "gui/namebox.svg",
    "gui/namebox_d.svg",
    "gui/textbox.svg",
    "gui/textbox_d.svg",
    "gui/textbox_monika.svg",
    "gui/textbox_monika_d.svg",
    "gui/button/choice_idle_background.svg",
    "gui/button/choice_hover_background.svg",
    "gui/button/choice_dark_idle_background.svg",
    "gui/button/choice_dark_hover_background.svg",
    "gui/button/scrollable_menu_idle_background.svg",
    "gui/button/scrollable_menu_hover_background.svg",
    "gui/button/scrollable_menu_disable_background.svg",
    "gui/button/scrollable_menu_dark_idle_background.svg",
    "gui/button/scrollable_menu_dark_hover_background.svg",
    "gui/button/scrollable_menu_dark_disable_background.svg",
    "gui/button/twopane_scrollable_menu_idle_background.svg",
    "gui/button/twopane_scrollable_menu_hover_background.svg",
    "gui/button/twopane_scrollable_menu_dark_idle_background.svg",
    "gui/button/twopane_scrollable_menu_dark_hover_background.svg",
    "gui/overlay/confirm.svg",
    "gui/overlay/confirm_d.svg",
    "gui/overlay/game_menu.svg",
    "gui/overlay/game_menu_d.svg",
    "gui/overlay/main_menu.svg",
    "gui/overlay/main_menu_d.svg",
    "mod_assets/hkb_idle_background.svg",
    "mod_assets/hkb_idle_background_d.svg",
    "mod_assets/hkb_hover_background.svg",
    "mod_assets/hkb_hover_background_d.svg",
    "mod_assets/hkb_disabled_background.svg",
    "mod_assets/hkb_disabled_background_d.svg",
    "mod_assets/island_idle_background.svg",
    "mod_assets/island_idle_background_d.svg",
    "mod_assets/island_hover_background.svg",
    "mod_assets/island_hover_background_d.svg",
    "mod_assets/music_menu.svg",
    "mod_assets/music_menu_d.svg",
    "mod_assets/buttons/squares/square_idle.svg",
    "mod_assets/buttons/squares/square_idle_d.svg",
    "mod_assets/buttons/squares/square_hover.svg",
    "mod_assets/buttons/squares/square_hover_d.svg",
    "mod_assets/buttons/squares/square_disabled.svg",
    "mod_assets/buttons/squares/square_disabled_d.svg",
    "mod_assets/calendar/calendar_bg.svg",
    "mod_assets/calendar/calendar_bg-n.svg",
    "mod_assets/calendar/calendar_close.svg",
    "mod_assets/calendar/calendar_close-n.svg",
    "mod_assets/calendar/calendar_close_hover.svg",
    "mod_assets/calendar/calendar_close_hover-n.svg",
    "mod_assets/calendar/calendar_day_bg.svg",
    "mod_assets/calendar/calendar_day_bg-n.svg",
    "mod_assets/calendar/calendar_day_hover_bg.svg",
    "mod_assets/calendar/calendar_day_hover_bg-n.svg",
    "mod_assets/calendar/calendar_day_disabled_bg.svg",
    "mod_assets/calendar/calendar_day_disabled_bg-n.svg",
    "mod_assets/calendar/calendar_day_name_bg.svg",
    "mod_assets/calendar/calendar_day_name_bg-n.svg",
    "mod_assets/calendar/calendar_left_arrow.svg",
    "mod_assets/calendar/calendar_left_arrow-n.svg",
    "mod_assets/calendar/calendar_left_arrow_hover.svg",
    "mod_assets/calendar/calendar_left_arrow_hover-n.svg",
    "mod_assets/calendar/calendar_right_arrow.svg",
    "mod_assets/calendar/calendar_right_arrow-n.svg",
    "mod_assets/calendar/calendar_right_arrow_hover.svg",
    "mod_assets/calendar/calendar_right_arrow_hover-n.svg",
    "mod_assets/console/cn_frame.svg",
    "mod_assets/frames/black70_pinkborder100.svg",
    "mod_assets/frames/black70_pinkborder100_d.svg",
    "mod_assets/frames/black70_pinkborder100_2px.svg",
    "mod_assets/frames/black70_pinkborder100_2px_d.svg",
    "mod_assets/frames/black70_pinkborder100_5px.svg",
    "mod_assets/frames/black70_pinkborder100_5px_d.svg",
    "mod_assets/frames/modebar.svg",
    "mod_assets/frames/modebar_d.svg",
    "mod_assets/frames/selector_overlay.svg",
    "mod_assets/frames/selector_overlay_d.svg",
    "mod_assets/frames/selector_overlay_disabled.svg",
    "mod_assets/frames/selector_overlay_disabled_d.svg",
    "mod_assets/frames/selector_top_frame.svg",
    "mod_assets/frames/selector_top_frame_d.svg",
    "mod_assets/frames/selector_top_frame_selected.svg",
    "mod_assets/frames/selector_top_frame_selected_d.svg",
    "mod_assets/frames/selector_top_frame_disabled.svg",
    "mod_assets/frames/selector_top_frame_disabled_d.svg",
    "mod_assets/frames/trans_pink2pxborder100.svg",
    "mod_assets/frames/trans_pink2pxborder100_d.svg",
    "mod_assets/games/hangman/hm_0.svg",
    "mod_assets/games/hangman/hm_1.svg",
    "mod_assets/games/hangman/hm_2.svg",
    "mod_assets/games/hangman/hm_3.svg",
    "mod_assets/games/hangman/hm_4.svg",
    "mod_assets/games/hangman/hm_5.svg",
    "mod_assets/games/hangman/hm_6.svg",
    "mod_assets/games/hangman/hm_frame.svg",
    "mod_assets/games/hangman/hm_frame_d.svg",
    "mod_assets/games/hangman/hm_sm_0.svg",
    "mod_assets/games/hangman/hm_sm_1.svg",
    "mod_assets/games/hangman/hm_sm_2.svg",
    "mod_assets/games/hangman/hm_sm_3.svg",
    "mod_assets/games/hangman/hm_sm_4.svg",
    "mod_assets/games/hangman/hm_sm_5.svg",
    "mod_assets/games/hangman/hm_sm_6.svg",

    # Custom
    "zzz_comfy_ui.rpy",
    "comfy_ui/button/idle_bg_lt.svg",
    "comfy_ui/button/idle_bg_dk.svg",
    "comfy_ui/button/hover_bg_lt.svg",
    "comfy_ui/button/hover_bg_dk.svg",
    "comfy_ui/button/insensitive_bg_lt.svg",
    "comfy_ui/button/insensitive_bg_dk.svg",
    "comfy_ui/fonts/Asap-Medium.ttf",
    "comfy_ui/fonts/Asap-MediumItalic.ttf",
    "comfy_ui/fonts/Asap-Bold.ttf",
    "comfy_ui/fonts/Asap-BoldItalic.ttf",
    "comfy_ui/fonts/Nunito-Bold.ttf",
    "comfy_ui/fonts/Nunito-BoldItalic.ttf",
    "comfy_ui/fonts/Nunito-SemiBold.ttf",
    "comfy_ui/fonts/Nunito-SemiBoldItalic.ttf",
    "comfy_ui/fonts/OFL.txt",
]

glitched_boxes = [
    "gui/textbox_monika.png",
    "gui/textbox_monika_d.png",
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
    macros = [
        # Name                       | Method           | Arguments
        [ "CUI_BTN_ROUNDING"         , GetThemeParameter, (theme["button_rounding"])                              ],
        [ "CUI_FRM_ROUNDING"         , GetThemeParameter, (theme["frame_rounding"])                               ],
        [ "CUI_DLG_ROUNDING"         , GetThemeParameter, (theme["dialogue_rounding"])                            ],
        [ "CUI_MAIN_FONT_REGULAR"    , GetThemeParameter, (theme["main_font"]["regular"])                         ],
        [ "CUI_MAIN_FONT_ITALIC"     , GetThemeParameter, (theme["main_font"]["italic"])                          ],
        [ "CUI_MAIN_FONT_BOLD"       , GetThemeParameter, (theme["main_font"]["bold"])                            ],
        [ "CUI_MAIN_FONT_BOLD_ITALIC", GetThemeParameter, (theme["main_font"]["bold_italic"])                     ],
        [ "CUI_MENU_FONT"            , GetThemeParameter, (theme["menu_font"])                                    ],
        [ "CUI_OPTION_FONT"          , GetThemeParameter, (theme["option_font"])                                  ],
        [ "CUI_MAIN_FONT_KERNING"    , GetThemeParameter, (theme["main_font_kerning"])                            ],
        [ "CUI_DLG_VERT_OFFSET"      , GetThemeParameter, (theme["dialogue_vertical_offset"])                     ],
        [ "CUI_DLG_LINE_SPACING"     , GetThemeParameter, (theme["dialogue_line_spacing"])                        ],
        [ "CUI_PRM_COLOR"            , ModulateColors   , (theme["primary_hue"], theme["primary_saturation"])     ],
        [ "CUI_SCD_COLOR"            , ModulateColors   , (theme["secondary_hue"], theme["secondary_saturation"]) ],
    ]

    text = ""

    with open(in_path, "r") as file:
        text = file.read()

    for macro_name, method, method_args in macros:
        query = macro_name + r"\(([A-Za-z0-9_\-,. ]*)\)"
        text = re.sub(query, lambda match: method(ParseMacroArguments(match), method_args), text)

    with open(out_path, "w") as file:
        file.write(text)

# Image rendering
def RenderImage(in_path, out_path):
    if release_mode:
        os.system("inkscape "
                 "--batch-process "
                 "--export-dpi=\"%i\" "
                 "--export-filename=\"%s\" "
                 "--export-overwrite "
                 "--export-type=\"png\" "
                 "\"%s\"" % (96 * dpi_scale, out_path, in_path))
    else:
        os.system("magick "
                  "-background \"none\" "
                  "-density \"%i\" "
                  "\"%s\" "
                  "\"%s\"" % (96 * dpi_scale, in_path, out_path))

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
    glitch_regions = [
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
    result = []

    for base_path, dirs, files in os.walk(theme_dir):
        for file_path in files:
            with open(os.path.join(base_path, file_path), "r") as json_file:
                json_data = json.load(json_file)
                result.append(json_data)

    return result

# Build chain
def Log(message):
    print("BUILD: %s" % message)

def Build():
    if os.path.exists(build_dir):
        Log("Cleaning up previous build...")
        shutil.rmtree(build_dir)

    themes = PreloadThemes()

    for theme in themes:
        asset_dir = "%s/%s" % (build_dir, theme["asset_directory"])

        # Replicate directory structure
        for file_path in files:
            dir_path = os.path.dirname(file_path)
            dir_full_path = "%s/%s" % (asset_dir, dir_path)

            if not os.path.exists(dir_full_path):
                Log("Creating directory %s..." % (dir_full_path))
                os.makedirs(dir_full_path)

        for file_path in files:
            (file_name, file_ext) = os.path.splitext(file_path)

            if file_ext == ".svg":
                Log("Rendering image %s..." % file_path)
                temp_file_path = os.path.join(build_dir, "Temporary.svg")
                PreprocessTextFile("%s/%s" % (source_dir, file_path), temp_file_path, theme)
                RenderImage(temp_file_path, "%s/%s.png" % (asset_dir, file_name))
                os.remove(temp_file_path)
            elif file_ext == ".rpy":
                Log("Processing script %s..." % file_path)
                PreprocessTextFile("%s/%s" % (source_dir, file_path), "%s/%s" % (asset_dir, file_path), theme)
            else:
                Log("Copying file %s..." % file_path)
                shutil.copyfile("%s/%s" % (source_dir, file_path), "%s/%s" % (asset_dir, file_path))

        for image_path in glitched_boxes:
            Log("Glitching image %s..." % image_path)
            Glitch("%s/%s" % (asset_dir, image_path))

    if release_mode:
        Log("Creating release archive...")
        shutil.make_archive("Release", "zip", build_dir)
        shutil.rmtree(build_dir)

    Log("Finished!")

PreloadThemes()
Build()
