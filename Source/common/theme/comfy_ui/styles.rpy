################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################

################################################################################
# Option buttons
################################################################################

# Check button
init 999 style check_button_text:
    idle_color        comfy_ui.option_button_text.idle_color
    hover_color       comfy_ui.option_button_text.hover_color
    selected_color    comfy_ui.option_button_text.selected_color
    insensitive_color comfy_ui.option_button_text.insensitive_color
    outlines          []

# Radio button
init 999 style radio_button_text:
    idle_color        comfy_ui.option_button_text.idle_color
    hover_color       comfy_ui.option_button_text.hover_color
    selected_color    comfy_ui.option_button_text.selected_color
    insensitive_color comfy_ui.option_button_text.insensitive_color
    outlines          []



################################################################################
# Game menu
################################################################################

# Title
init 999 style game_menu_label_text:
    color    comfy_ui.menu_title.color
    outlines comfy_ui.menu_title.outlines

# Preference label
init 999 style pref_label_text:
    color    comfy_ui.menu_label.color
    outlines comfy_ui.menu_label.outlines

# Version text
init 999 style main_menu_version:
    color    comfy_ui.menu_text.color
    outlines comfy_ui.menu_text.outlines

# Menu button
init 999 style navigation_button_text:
    color                comfy_ui.menu_button_text.color
    outlines             comfy_ui.menu_button_text.idle_outlines
    hover_outlines       comfy_ui.menu_button_text.hover_outlines
    insensitive_outlines comfy_ui.menu_button_text.insensitive_outlines

# File menu
init 999 style page_label_text:
    color    comfy_ui.menu_text.color
    outlines comfy_ui.menu_text.outlines

init 999 style slot_time_text:
    idle_color        comfy_ui.button_text.idle_color
    hover_color       comfy_ui.button_text.hover_color
    selected_color    comfy_ui.button_text.selected_color
    insensitive_color comfy_ui.button_text.insensitive_color
    outlines          comfy_ui.button_text.outlines

init 999 style slot_name_text:
    idle_color        comfy_ui.button_text.idle_color
    hover_color       comfy_ui.button_text.hover_color
    selected_color    comfy_ui.button_text.selected_color
    insensitive_color comfy_ui.button_text.insensitive_color
    outlines          comfy_ui.button_text.outlines

init 999 style page_button_text:
    idle_color        comfy_ui.button_text.idle_color
    hover_color       comfy_ui.button_text.hover_color
    selected_color    comfy_ui.button_text.selected_color
    insensitive_color comfy_ui.button_text.insensitive_color
    outlines          comfy_ui.button_text.outlines



################################################################################
# Dialogue
################################################################################

# Name
init 999 style say_label:
    color    comfy_ui.menu_label.color
    outlines comfy_ui.menu_label.outlines

# Text
init 999 style normal:
    color    comfy_ui.dialogue_text.color
    outlines comfy_ui.dialogue_text.outlines

# Quick button
init 999 style quick_button_text:
    idle_color        comfy_ui.quick_button_text.idle_color
    hover_color       comfy_ui.quick_button_text.hover_color
    selected_color    comfy_ui.quick_button_text.selected_color
    insensitive_color comfy_ui.quick_button_text.insensitive_color
    outlines          comfy_ui.quick_button_text.outlines



################################################################################
# History
################################################################################

# Name
init 999 style history_name_text:
    color    comfy_ui.history_name.color
    outlines comfy_ui.history_name.outlines

# Text
init 999 style history_text:
    color    comfy_ui.history_text.color
    outlines comfy_ui.history_text.outlines



################################################################################
# Frames
################################################################################

# Frame
define gui.frame_borders = Borders(5, 5, 5, 5, -1, -1, -1, -1)

# Confirm frame
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)

init 999 style confirm_prompt_text:
    color    comfy_ui.confirm_prompt_text.color
    outlines comfy_ui.confirm_prompt_text.outlines



################################################################################
# Choice menu
################################################################################
init 999 style choice_button:
    background Frame("gui/button/choice_[prefix_]background.png", Borders(5, 5, 5, 5))

init 999 style choice_button_text:
    xpadding          25
    idle_color        comfy_ui.button_text.idle_color
    hover_color       comfy_ui.button_text.hover_color
    selected_color    comfy_ui.button_text.selected_color
    insensitive_color comfy_ui.button_text.insensitive_color
    outlines          comfy_ui.button_text.outlines



################################################################################
# Poem game
################################################################################
style poemgame_text:
    color          comfy_ui.poem_game_text.color
    outlines       comfy_ui.poem_game_text.outlines
    hover_outlines comfy_ui.poem_game_text.hover_outlines



################################################################################
# Input caret
################################################################################
init 999 image input_caret:
    Solid(comfy_ui.input_caret_color)
    size (2, 25)
    subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat
