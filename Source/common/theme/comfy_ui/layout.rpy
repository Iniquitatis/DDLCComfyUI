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
define comfy_ui.common.font_regular     = "CUI_MAIN_FONT_REGULAR()"
define comfy_ui.common.font_italic      = "CUI_MAIN_FONT_ITALIC()"
define comfy_ui.common.font_bold        = "CUI_MAIN_FONT_BOLD()"
define comfy_ui.common.font_bold_italic = "CUI_MAIN_FONT_BOLD_ITALIC()"
define comfy_ui.common.font             = FontGroup().add(
    comfy_ui.common.font_regular, 0x0020, 0x00ff).add( # Main
    "gui/font/Aller_Rg.ttf"     , 0x0000, 0xffff)      # Fallback
define comfy_ui.common.font_kerning     = CUI_MAIN_FONT_KERNING()
define comfy_ui.common.font_size        = 24

define comfy_ui.menu_font         = "CUI_MENU_FONT()"
define comfy_ui.menu_font_kerning = 0.0

define comfy_ui.menu_title.font_size = 38

define comfy_ui.menu_label.font_size = 24

define comfy_ui.menu_text.font_size = 16

define comfy_ui.menu_button_text.font_size = 24

define comfy_ui.dialogue_text.vertical_offset = CUI_DLG_VERT_OFFSET()
define comfy_ui.dialogue_text.line_spacing    = CUI_DLG_LINE_SPACING()

define comfy_ui.quick_button_text.font_size = 14

define comfy_ui.option_button_text.font         = "CUI_OPTION_FONT()"
define comfy_ui.option_button_text.font_kerning = 0.0
define comfy_ui.option_button_text.font_size    = 24

define comfy_ui.choice_button_spacing = 22



################################################################################
# Init
################################################################################
init python:
    config.font_replacement_map[comfy_ui.common.font_regular, False, True] = (comfy_ui.common.font_italic, False, False)
    config.font_replacement_map[comfy_ui.common.font_regular, True, False] = (comfy_ui.common.font_bold, False, False)
    config.font_replacement_map[comfy_ui.common.font_regular, True, True] = (comfy_ui.common.font_bold_italic, False, False)



################################################################################
# Definitions
################################################################################
define gui.default_font = comfy_ui.common.font



################################################################################
# Option buttons
################################################################################

# Check button
init 999 style check_button:
    clear
    foreground "gui/button/check_[prefix_]foreground.png"
    padding    (28, 4, 4, 4)

init 999 style check_button_text:
    clear
    font    comfy_ui.option_button_text.font
    kerning comfy_ui.option_button_text.font_kerning
    size    comfy_ui.option_button_text.font_size

# Radio button
init 999 style radio_button:
    clear
    foreground "gui/button/check_[prefix_]foreground.png"
    padding    (28, 4, 4, 4)

init 999 style radio_button_text:
    clear
    font    comfy_ui.option_button_text.font
    kerning comfy_ui.option_button_text.font_kerning
    size    comfy_ui.option_button_text.font_size



################################################################################
# Game menu
################################################################################

# Title
init 999 style game_menu_label_text:
    font    comfy_ui.menu_font
    kerning comfy_ui.menu_font_kerning
    size    comfy_ui.menu_title.font_size

# Preference label
init 999 style pref_label_text:
    font    comfy_ui.menu_font
    kerning comfy_ui.menu_font_kerning
    size    comfy_ui.menu_label.font_size

# Version text
init 999 style main_menu_version:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.menu_text.font_size

# Menu button
init 999 style navigation_button_text:
    font    comfy_ui.menu_font
    kerning comfy_ui.menu_font_kerning
    size    comfy_ui.menu_button_text.font_size

# File menu
init 999 style page_label_text:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning

init 999 style slot_time_text:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    16
    align   (0.5, 0.5)

init 999 style slot_name_text:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    16
    align   (0.5, 0.5)

init 999 style page_button_text:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size
    align   (0.5, 0.5)



################################################################################
# Dialogue
################################################################################

# Name
init 999 style say_label:
    font    comfy_ui.menu_font
    kerning comfy_ui.menu_font_kerning
    size    comfy_ui.menu_label.font_size

# Text
init 999 style normal:
    font         comfy_ui.common.font
    kerning      comfy_ui.common.font_kerning
    yoffset      comfy_ui.dialogue_text.vertical_offset
    line_spacing comfy_ui.dialogue_text.line_spacing

# Quick button
init 999 style quick_button_text:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.quick_button_text.font_size



################################################################################
# History
################################################################################

# Name
init 999 style history_name_text:
    xpos    0
    ypos    5
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size
    bold    True

# Text
init 999 style history_text:
    xpos    165
    ypos    5
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size
    bold    False



################################################################################
# Frames
################################################################################
init 999 style confirm_prompt_text:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size



################################################################################
# Choice menu/button
################################################################################
init 999 style choice_vbox:
    spacing comfy_ui.choice_button_spacing

init 999 style choice_button:
    clear
    xysize  (420, None)
    padding (25, 5, 25, 5)

init 999 style choice_button_text:
    clear
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size
    align   (0.5, 0.5)
