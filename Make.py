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
preprocessing_tokens = [
    [ "$COMFY_UI_BUTTON_ROUNDING$", str(4) ],
    [ "$COMFY_UI_FRAME_ROUNDING$" , str(4) ],
]

dir_structure = [
    "gui",
    "gui/button",
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
    "mod_assets/font/Nunito-SemiBold.ttf",
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

################################################################################
# Script itself
################################################################################
import os
import shutil

def PreprocessSVG(input_name, output_name):
    text = ""

    with open(input_name, "r") as file:
        text = file.read()

    for token, string in preprocessing_tokens:
        text = text.replace(token, string)

    with open(output_name, "w") as file:
        file.write(text)

def Build(build_dir):
    if os.path.exists(build_dir):
        print("Cleaning up previous build...")
        shutil.rmtree(build_dir)

    print("Creating directory %s..." % build_dir)
    os.mkdir(build_dir)

    for dir_name in dir_structure:
        if not os.path.exists("%s/%s" % (build_dir, dir_name)):
            print("Creating directory %s/%s..." % (build_dir, dir_name))
            os.mkdir("%s/%s" % (build_dir, dir_name))

    for file_name in common_files:
        print("Copying file %s..." % file_name)
        shutil.copyfile("Source/%s" % file_name, "%s/%s" % (build_dir, file_name))

    for image_name in vector_images:
        print("Converting file %s.svg..." % image_name)
        PreprocessSVG("Source/%s.svg" % image_name, "Temporary.svg")
        os.system("inkscape "
                    "--export-dpi=\"96\" "
                    "--export-type=\"png\" "
                    "--export-file=\"%s/%s.png\" "
                    "Temporary.svg" % (build_dir, image_name))

    print("Cleaning up...")
    os.remove("Temporary.svg")

    print("Finished!")

Build("Build")
