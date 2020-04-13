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

color_schemes = [
    { "name": "default", "hue": None, "saturation_mul": 1.0 },
    { "name": "gray"   , "hue": 0   , "saturation_mul": 0.0 },
    { "name": "red"    , "hue": 0   , "saturation_mul": 1.0 },
    { "name": "peach"  , "hue": 30  , "saturation_mul": 0.6 },
    { "name": "yellow" , "hue": 55  , "saturation_mul": 1.0 },
    { "name": "green"  , "hue": 120 , "saturation_mul": 0.7 },
    { "name": "cyan"   , "hue": 188 , "saturation_mul": 0.8 },
    { "name": "blue"   , "hue": 240 , "saturation_mul": 1.0 },
    { "name": "purple" , "hue": 300 , "saturation_mul": 1.0 },
]

preprocessing_tokens = [
    [ "$COMFY_UI_BUTTON_ROUNDING$", 4 ],
    [ "$COMFY_UI_FRAME_ROUNDING$" , 4 ],
]

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
    "zzz_comfy_ui.rpy",
    "mod_assets/font/Nunito-Bold.ttf",
    "mod_assets/font/Nunito-SemiBold.ttf",
    "mod_assets/font/Nunito-SemiBoldItalic.ttf",
    "mod_assets/font/OFL.txt",
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
import os
import re
import shutil

from PIL import Image
from hsluv import *

def ModulateColorByRegexMatch(match, scheme):
    r = float(match.group(1)) / 255.0
    g = float(match.group(2)) / 255.0
    b = float(match.group(3)) / 255.0
    h, s, l = rgb_to_hsluv([r, g, b])
    r, g, b = hsluv_to_rgb([scheme["hue"], s * scheme["saturation_mul"], l])
    return "rgb(%i, %i, %i)" % (int(r * 255.0),
                                int(g * 255.0),
                                int(b * 255.0))

def PreprocessSVG(input_path, output_path, scheme):
    text = ""

    with open(input_path, "r") as file:
        text = file.read()

    for token, value in preprocessing_tokens:
        text = text.replace(token, str(value))

    if scheme["hue"] != None:
        text = re.sub("rgb\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)",
                      lambda match : ModulateColorByRegexMatch(match, scheme), text)

    with open(output_path, "w") as file:
        file.write(text)

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

def Build(build_dir):
    if os.path.exists(build_dir):
        print("Cleaning up previous build...")
        shutil.rmtree(build_dir)

    print("Creating directory %s..." % build_dir)
    os.mkdir(build_dir)

    for scheme in color_schemes:
        scheme_dir = "%s/%s" % (build_dir, scheme["name"])
        if not os.path.exists(scheme_dir):
            print("Creating directory %s..." % (scheme_dir))
            os.mkdir(scheme_dir)

        for dir_path in dir_structure:
            dir_full_path = ("%s/%s") % (scheme_dir, dir_path)
            if not os.path.exists(dir_full_path):
                print("Creating directory %s..." % (dir_full_path))
                os.mkdir(dir_full_path)

        for file_path in common_files:
            print("Copying file %s..." % file_path)
            shutil.copyfile("Source/%s" % file_path, "%s/%s" % (scheme_dir, file_path))

        for image_path in vector_images:
            print("Converting file %s.svg..." % image_path)
            PreprocessSVG("Source/%s.svg" % image_path, "Temporary.svg", scheme)
            os.system("inkscape "
                        "--export-dpi=\"%i\" "
                        "--export-type=\"png\" "
                        "--export-file=\"%s/%s.png\" "
                        "Temporary.svg" % (96 * dpi_scale, scheme_dir, image_path))
            os.remove("Temporary.svg")

        for image_path in glitched_boxes:
            print("Glitching image %s.png..." % image_path)
            Glitch("%s/%s.png" % (scheme_dir, image_path))

    print("Finished!")

Build("Build")
