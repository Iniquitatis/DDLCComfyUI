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

theme_dir        = "Themes"
source_dir       = "Source"
asset_source_dir = "Source/Assets"
build_dir        = "Build"

common_files = [
    "comfy_ui.rpy",
]

theme_files = [
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
    "gui/button/slot_idle_background.svg",
    "gui/button/slot_hover_background.svg",
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
    "mod_assets/buttons/generic/idle_bg.svg",
    "mod_assets/buttons/generic/idle_bg_d.svg",
    "mod_assets/buttons/generic/hover_bg.svg",
    "mod_assets/buttons/generic/hover_bg_d.svg",
    "mod_assets/buttons/generic/insensitive_bg.svg",
    "mod_assets/buttons/generic/insensitive_bg_d.svg",
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
    "mod_assets/calendar/calendar_today_bg.svg",
    "mod_assets/calendar/calendar_today_bg-n.svg",
    "mod_assets/calendar/calendar_today_hover_bg.svg",
    "mod_assets/calendar/calendar_today_hover_bg-n.svg",
    "mod_assets/calendar/calendar_today_disabled_bg.svg",
    "mod_assets/calendar/calendar_today_disabled_bg-n.svg",
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
    "info.json",
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
    "comfy_ui/scrollbar/horizontal_bar_lt.svg",
    "comfy_ui/scrollbar/horizontal_bar_dk.svg",
    "comfy_ui/scrollbar/horizontal_idle_thumb_lt.svg",
    "comfy_ui/scrollbar/horizontal_idle_thumb_dk.svg",
    "comfy_ui/scrollbar/horizontal_hover_thumb_lt.svg",
    "comfy_ui/scrollbar/horizontal_hover_thumb_dk.svg",
    "comfy_ui/scrollbar/vertical_bar_lt.svg",
    "comfy_ui/scrollbar/vertical_bar_dk.svg",
    "comfy_ui/scrollbar/vertical_idle_thumb_lt.svg",
    "comfy_ui/scrollbar/vertical_idle_thumb_dk.svg",
    "comfy_ui/scrollbar/vertical_hover_thumb_lt.svg",
    "comfy_ui/scrollbar/vertical_hover_thumb_dk.svg",
    "comfy_ui/slider/horizontal_idle_thumb_lt.svg",
    "comfy_ui/slider/horizontal_idle_thumb_dk.svg",
    "comfy_ui/slider/horizontal_hover_thumb_lt.svg",
    "comfy_ui/slider/horizontal_hover_thumb_dk.svg",
    "comfy_ui/slider/vertical_idle_thumb_lt.svg",
    "comfy_ui/slider/vertical_idle_thumb_dk.svg",
    "comfy_ui/slider/vertical_hover_thumb_lt.svg",
    "comfy_ui/slider/vertical_hover_thumb_dk.svg",
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

def GetImageList(macro_args, method_args):
    result = ""
    for file_path in theme_files:
        (file_name, file_ext) = os.path.splitext(file_path)
        if file_ext == ".svg":
            result += "\"%s.png\",\n" % file_name
    return result

def GetThemeParameter(macro_args, method_args):
    return str(method_args)

def GetUIScale(macro_args, method_args):
    return str(method_args)

def GetUIScaleInv(macro_args, method_args):
    return str(1.0 / method_args)

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
        # No arguments have been passed to the macro
        return []

    args_string = match.group(1)

    query = r""
    for i in range(0, 4):
        query += r"\s*([\w\-.]+)\s*"
        result = re.findall(query, args_string)
        if len(result) > 0:
            return result
        query += r","

def PreprocessTextFile(in_path, out_path, theme, scale):
    macros = [
        # Name                       | Method           | Arguments
        [ "CUI_THEME_NAME"           , GetThemeParameter, (theme["name"] if scale == 1 else "%s (HiDPI)" % theme["name"]) ],
        [ "CUI_BTN_ROUNDING"         , GetThemeParameter, (theme["button_rounding"])                                      ],
        [ "CUI_FRM_ROUNDING"         , GetThemeParameter, (theme["frame_rounding"])                                       ],
        [ "CUI_DLG_ROUNDING"         , GetThemeParameter, (theme["dialogue_rounding"])                                    ],
        [ "CUI_MNU_PTSHAPE"          , GetThemeParameter, (theme["menu_pattern_shape"])                                   ],
        [ "CUI_DLG_PTSHAPE"          , GetThemeParameter, (theme["dialogue_pattern_shape"])                               ],
        [ "CUI_MAIN_FONT_REGULAR"    , GetThemeParameter, (theme["main_font"]["regular"])                                 ],
        [ "CUI_MAIN_FONT_ITALIC"     , GetThemeParameter, (theme["main_font"]["italic"])                                  ],
        [ "CUI_MAIN_FONT_BOLD"       , GetThemeParameter, (theme["main_font"]["bold"])                                    ],
        [ "CUI_MAIN_FONT_BOLD_ITALIC", GetThemeParameter, (theme["main_font"]["bold_italic"])                             ],
        [ "CUI_MENU_FONT"            , GetThemeParameter, (theme["menu_font"])                                            ],
        [ "CUI_OPTION_FONT"          , GetThemeParameter, (theme["option_font"])                                          ],
        [ "CUI_MAIN_FONT_KERNING"    , GetThemeParameter, (theme["main_font_kerning"])                                    ],
        [ "CUI_DLG_VERT_OFFSET"      , GetThemeParameter, (theme["dialogue_vertical_offset"])                             ],
        [ "CUI_DLG_LINE_SPACING"     , GetThemeParameter, (theme["dialogue_line_spacing"])                                ],
        [ "CUI_PRM_COLOR"            , ModulateColors   , (theme["primary_hue"], theme["primary_saturation"])             ],
        [ "CUI_SCD_COLOR"            , ModulateColors   , (theme["secondary_hue"], theme["secondary_saturation"])         ],
        [ "CUI_SCALE"                , GetUIScale       , (scale)                                                         ],
        [ "CUI_SCALE_INV"            , GetUIScaleInv    , (scale)                                                         ],
        [ "CUI_IMAGE_LIST"           , GetImageList     , ()                                                              ],
    ]

    text = ""

    with open(in_path, "r") as file:
        text = file.read()

    for macro_name, method, method_args in macros:
        query = macro_name + r"\(([\w\s\-.,]*)\)"
        text = re.sub(query, lambda match: method(ParseMacroArguments(match), method_args), text)

    with open(out_path, "w") as file:
        file.write(text)

# Image rendering
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

def Glitch(image_path, scale):
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
            x  *= scale
            y  *= scale
            w  *= scale
            h  *= scale
            dx *= scale
            dy *= scale
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

def Build():
    # Clear previous build
    if os.path.exists(build_dir):
        Log("Cleaning up previous build...")
        shutil.rmtree(build_dir)

    # Create build directory
    Log("Creating build directory...")
    os.mkdir(build_dir)

    # Copy common files
    for file_path in common_files:
        Log("Copying file %s..." % file_path)
        src_path = os.path.join(source_dir, file_path)
        dst_path = os.path.join(build_dir, file_path)
        shutil.copyfile(src_path, dst_path)

    # Make themes
    themes = PreloadThemes()

    for theme in themes:
        for scale in range(1, 3):
            target_id = theme["id"] if scale == 1 else "%s_hidpi" % theme["id"]
            target_dir = os.path.join(build_dir, "comfy_meta", target_id)

            # Replicate directory structure
            for file_path in theme_files:
                dir_path = os.path.dirname(file_path)
                dir_full_path = os.path.join(target_dir, dir_path)

                if not os.path.exists(dir_full_path):
                    Log("Creating directory %s..." % dir_full_path)
                    os.makedirs(dir_full_path)

            # Process source files
            for file_path in theme_files:
                (file_name, file_ext) = os.path.splitext(file_path)

                if file_ext == ".svg":
                    Log("Rendering image %s..." % file_path)
                    png_path = "%s.png" % file_name
                    tmp_path = os.path.join(build_dir, "Temporary.svg")
                    src_path = os.path.join(asset_source_dir, file_path)
                    dst_path = os.path.join(target_dir, png_path)
                    PreprocessTextFile(src_path, tmp_path, theme, scale)
                    RenderImage(tmp_path, dst_path, scale, png_path in glitched_boxes)
                    os.remove(tmp_path)
                elif file_ext == ".rpy":
                    Log("Processing script %s..." % file_path)
                    src_path = os.path.join(asset_source_dir, file_path)
                    dst_path = os.path.join(target_dir, file_path)
                    PreprocessTextFile(src_path, dst_path, theme, scale)
                elif file_ext == ".json":
                    Log("Processing JSON %s..." % file_path)
                    src_path = os.path.join(asset_source_dir, file_path)
                    dst_path = os.path.join(target_dir, file_path)
                    PreprocessTextFile(src_path, dst_path, theme, scale)
                else:
                    Log("Copying file %s..." % file_path)
                    src_path = os.path.join(asset_source_dir, file_path)
                    dst_path = os.path.join(target_dir, file_path)
                    shutil.copyfile(src_path, dst_path)

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
