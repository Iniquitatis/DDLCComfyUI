################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################

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
init 999 style check_button_text:
    font    comfy_ui.option_button_text.font
    kerning comfy_ui.option_button_text.font_kerning
    size    comfy_ui.option_button_text.font_size

init 999 style check_button_text_dark:
    font    comfy_ui.option_button_text.font
    kerning comfy_ui.option_button_text.font_kerning
    size    comfy_ui.option_button_text.font_size

# Radio button
init 999 style radio_button_text:
    font    comfy_ui.option_button_text.font
    kerning comfy_ui.option_button_text.font_kerning
    size    comfy_ui.option_button_text.font_size

init 999 style radio_button_text_dark:
    font    comfy_ui.option_button_text.font
    kerning comfy_ui.option_button_text.font_kerning
    size    comfy_ui.option_button_text.font_size

# Fancy check button
init 999 style generic_fancy_check_button_text:
    yoffset comfy_ui.button_text.vertical_offset
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size

init 999 style generic_fancy_check_button_text_dark:
    yoffset comfy_ui.button_text.vertical_offset
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size



################################################################################
# Game menu
################################################################################

# Title
init 999 style game_menu_label_text:
    font    comfy_ui.menu_font
    kerning comfy_ui.menu_font_kerning
    size    comfy_ui.menu_title.font_size

init 999 style game_menu_label_text_dark:
    font    comfy_ui.menu_font
    kerning comfy_ui.menu_font_kerning
    size    comfy_ui.menu_title.font_size

# Preference label
init 999 style pref_label_text:
    font    comfy_ui.menu_font
    kerning comfy_ui.menu_font_kerning
    size    comfy_ui.menu_label.font_size

init 999 style pref_label_text_dark:
    font    comfy_ui.menu_font
    kerning comfy_ui.menu_font_kerning
    size    comfy_ui.menu_label.font_size

# Version text
# NOTE: this style is also used for the tooltips at the bottom of the menu screen
init 999 style main_menu_version:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.menu_text.font_size

init 999 style main_menu_version_dark:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.menu_text.font_size

# Menu button
init 999 style navigation_button_text:
    font    comfy_ui.menu_font
    kerning comfy_ui.menu_font_kerning
    size    comfy_ui.menu_button_text.font_size

init 999 style navigation_button_text_dark:
    font    comfy_ui.menu_font
    kerning comfy_ui.menu_font_kerning
    size    comfy_ui.menu_button_text.font_size

# File menu
init 999 style page_label_text:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning

init 999 style page_label_text_dark:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning

init 999 style slot_time_text:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning

init 999 style slot_time_text_dark:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning

init 999 style slot_name_text:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning

init 999 style slot_name_text_dark:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning

init 999 style page_button_text:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size

init 999 style page_button_text_dark:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size



################################################################################
# Music menu
################################################################################

# Music menu button
init 999 style music_menu_button_text:
    font    comfy_ui.music_menu_button_text.font
    kerning comfy_ui.music_menu_button_text.font_kerning
    size    comfy_ui.music_menu_button_text.font_size

init 999 style music_menu_button_text_dark:
    font    comfy_ui.music_menu_button_text.font
    kerning comfy_ui.music_menu_button_text.font_kerning
    size    comfy_ui.music_menu_button_text.font_size



################################################################################
# Dialogue
################################################################################

# Name
init 999 style say_label:
    font    comfy_ui.menu_font
    kerning comfy_ui.menu_font_kerning
    size    comfy_ui.menu_label.font_size

init 999 style say_label_dark:
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

init 999 style quick_button_text_dark:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.quick_button_text.font_size



################################################################################
# History
################################################################################

# Name
init 999 style history_name_text:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size

# Text
init 999 style history_text:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size



################################################################################
# Frames
################################################################################
init 999 style confirm_prompt_text:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size

init 999 style confirm_prompt_text_dark:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size



################################################################################
# Choice menu
################################################################################
init 999 style choice_button:
    top_padding    (5 + int(math.floor(float(comfy_ui.button.height_adjustment) / 2.0)))
    bottom_padding (5 + int(math.ceil (float(comfy_ui.button.height_adjustment) / 2.0)))

init 999 style choice_button_dark:
    top_padding    (5 + int(math.floor(float(comfy_ui.button.height_adjustment) / 2.0)))
    bottom_padding (5 + int(math.ceil (float(comfy_ui.button.height_adjustment) / 2.0)))

init 999 style choice_button_text:
    yoffset comfy_ui.button_text.vertical_offset
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size

init 999 style choice_button_text_dark:
    yoffset comfy_ui.button_text.vertical_offset
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size



################################################################################
# Scrollable menu
################################################################################
init 999 style scrollable_menu_button:
    top_padding    (5 + int(math.floor(float(comfy_ui.button.height_adjustment) / 2.0)))
    bottom_padding (5 + int(math.ceil (float(comfy_ui.button.height_adjustment) / 2.0)))

init 999 style scrollable_menu_button_dark:
    top_padding    (5 + int(math.floor(float(comfy_ui.button.height_adjustment) / 2.0)))
    bottom_padding (5 + int(math.ceil (float(comfy_ui.button.height_adjustment) / 2.0)))

init 999 style scrollable_menu_button_text:
    yoffset comfy_ui.button_text.vertical_offset
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size

init 999 style scrollable_menu_button_text_dark:
    yoffset comfy_ui.button_text.vertical_offset
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size



################################################################################
# Two-pane scrollable menu
################################################################################
init 999 style twopane_scrollable_menu_button:
    top_padding    (5 + int(math.floor(float(comfy_ui.button.height_adjustment) / 2.0)))
    bottom_padding (5 + int(math.ceil (float(comfy_ui.button.height_adjustment) / 2.0)))

init 999 style twopane_scrollable_menu_button_dark:
    top_padding    (5 + int(math.floor(float(comfy_ui.button.height_adjustment) / 2.0)))
    bottom_padding (5 + int(math.ceil (float(comfy_ui.button.height_adjustment) / 2.0)))

init 999 style twopane_scrollable_menu_button_text:
    yoffset comfy_ui.button_text.vertical_offset
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size

init 999 style twopane_scrollable_menu_button_text_dark:
    yoffset comfy_ui.button_text.vertical_offset
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size



################################################################################
# Talk choice menu
################################################################################
init 999 style talk_choice_button:
    top_padding    (5 + int(math.floor(float(comfy_ui.button.height_adjustment) / 2.0)))
    bottom_padding (5 + int(math.ceil (float(comfy_ui.button.height_adjustment) / 2.0)))

init 999 style talk_choice_button_dark:
    top_padding    (5 + int(math.floor(float(comfy_ui.button.height_adjustment) / 2.0)))
    bottom_padding (5 + int(math.ceil (float(comfy_ui.button.height_adjustment) / 2.0)))

init 999 style talk_choice_button_text:
    yoffset comfy_ui.button_text.vertical_offset
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size

init 999 style talk_choice_button_text_dark:
    yoffset comfy_ui.button_text.vertical_offset
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size



################################################################################
# Hotkey button menu
################################################################################
init 999 style hkb_button:
    top_padding    (5 + int(math.floor(float(comfy_ui.button.height_adjustment) / 2.0)))
    bottom_padding (5 + int(math.ceil (float(comfy_ui.button.height_adjustment) / 2.0)))

init 999 style hkb_button_dark:
    top_padding    (5 + int(math.floor(float(comfy_ui.button.height_adjustment) / 2.0)))
    bottom_padding (5 + int(math.ceil (float(comfy_ui.button.height_adjustment) / 2.0)))

init 999 style hkb_button_text:
    yoffset comfy_ui.button_text.vertical_offset
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size

init 999 style hkb_button_text_dark:
    yoffset comfy_ui.button_text.vertical_offset
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size



################################################################################
# Island buttons
################################################################################
init 999 style island_button:
    top_padding    (5 + int(math.floor(float(comfy_ui.button.height_adjustment) / 2.0)))
    bottom_padding (5 + int(math.ceil (float(comfy_ui.button.height_adjustment) / 2.0)))

init 999 style island_button_dark:
    top_padding    (5 + int(math.floor(float(comfy_ui.button.height_adjustment) / 2.0)))
    bottom_padding (5 + int(math.ceil (float(comfy_ui.button.height_adjustment) / 2.0)))

init 999 style island_button_text:
    yoffset comfy_ui.button_text.vertical_offset
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size

init 999 style island_button_text_dark:
    yoffset comfy_ui.button_text.vertical_offset
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size



################################################################################
# Extras menu
################################################################################
init 999 style mas_adjustable_button:
    top_padding    (5 + int(math.floor(float(comfy_ui.button.height_adjustment) / 2.0)))
    bottom_padding (5 + int(math.ceil (float(comfy_ui.button.height_adjustment) / 2.0)))

init 999 style mas_adjustable_button_dark:
    top_padding    (5 + int(math.floor(float(comfy_ui.button.height_adjustment) / 2.0)))
    bottom_padding (5 + int(math.ceil (float(comfy_ui.button.height_adjustment) / 2.0)))

init 999 style mas_adjustable_button_text:
    yoffset comfy_ui.button_text.vertical_offset
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size

init 999 style mas_adjustable_button_text_dark:
    yoffset comfy_ui.button_text.vertical_offset
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size
