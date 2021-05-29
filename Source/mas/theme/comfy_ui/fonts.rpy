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
