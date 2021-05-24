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
define comfy_ui.menu_title.color    = "CUI_SCD_COLOR(255, 255, 255)"
define comfy_ui.menu_title.outlines = [(6, "CUI_SCD_COLOR(187, 85, 153)", 0, 0), (3, "CUI_SCD_COLOR(187, 85, 153)", 2, 2)]

define comfy_ui.menu_label.color    = "CUI_SCD_COLOR(255, 255, 255)"
define comfy_ui.menu_label.outlines = [(3, "CUI_SCD_COLOR(187, 85, 153)", 0, 0), (1, "CUI_SCD_COLOR(187, 85, 153)", 1, 1)]

define comfy_ui.menu_text.color    = "CUI_SCD_COLOR(56, 56, 56)"
define comfy_ui.menu_text.outlines = []

define comfy_ui.menu_button_text.color                = "CUI_SCD_COLOR(255, 255, 255)"
define comfy_ui.menu_button_text.idle_outlines        = [(4, "CUI_SCD_COLOR(187, 85, 153)", 0, 0), (2, "CUI_SCD_COLOR(187, 85, 153)", 2, 2)]
define comfy_ui.menu_button_text.hover_outlines       = [(4, "CUI_SCD_COLOR(255, 170, 204)", 0, 0), (2, "CUI_SCD_COLOR(255, 170, 204)", 2, 2)]
define comfy_ui.menu_button_text.insensitive_outlines = [(4, "CUI_SCD_COLOR(255, 204, 238)", 0, 0), (2, "CUI_SCD_COLOR(255, 204, 238)", 2, 2)]

define comfy_ui.confirm_prompt_text.color    = "CUI_PRM_COLOR(56, 56, 56)"
define comfy_ui.confirm_prompt_text.outlines = []

define comfy_ui.dialogue_text.color    = "CUI_PRM_COLOR(248, 248, 248)"
define comfy_ui.dialogue_text.outlines = [(2, "CUI_PRM_COLOR(40, 40, 40)", 0, 0)]

define comfy_ui.history_name.color    = "CUI_PRM_COLOR(248, 248, 248)"
define comfy_ui.history_name.outlines = [(2, "CUI_PRM_COLOR(40, 40, 40)", 0, 0)]

define comfy_ui.history_text.color    = "CUI_PRM_COLOR(255, 255, 255)"
define comfy_ui.history_text.outlines = [(2, "CUI_PRM_COLOR(40, 40, 40)", 0, 0)]

define comfy_ui.quick_button_text.idle_color        = "CUI_SCD_COLOR(85, 34, 34)"
define comfy_ui.quick_button_text.hover_color       = "CUI_SCD_COLOR(255, 204, 204)"
define comfy_ui.quick_button_text.selected_color    = "CUI_SCD_COLOR(255, 255, 255)"
define comfy_ui.quick_button_text.insensitive_color = "CUI_SCD_COLOR(170, 102, 102)"
define comfy_ui.quick_button_text.outlines          = []

define comfy_ui.button_text.idle_color        = "CUI_PRM_COLOR(56, 56, 56)"
define comfy_ui.button_text.hover_color       = "CUI_PRM_COLOR(255, 170, 153)"
define comfy_ui.button_text.selected_color    = "CUI_PRM_COLOR(187, 85, 136)"
define comfy_ui.button_text.insensitive_color = "CUI_PRM_COLOR(170, 170, 170, 127)"
define comfy_ui.button_text.outlines          = []

define comfy_ui.option_button_text.idle_color        = "CUI_SCD_COLOR(170, 170, 170)"
define comfy_ui.option_button_text.hover_color       = "CUI_SCD_COLOR(204, 102, 153)"
define comfy_ui.option_button_text.selected_color    = "CUI_SCD_COLOR(187, 85, 136)"
define comfy_ui.option_button_text.insensitive_color = "CUI_SCD_COLOR(170, 170, 170, 127)"

define comfy_ui.poem_game_text.color          = "CUI_PRM_COLOR(56, 56, 56)"
define comfy_ui.poem_game_text.outlines       = []
define comfy_ui.poem_game_text.hover_outlines = [(3, "CUI_PRM_COLOR(255, 238, 255)", 0, 0), (2, "CUI_PRM_COLOR(255, 204, 255)", 0, 0), (1, "CUI_PRM_COLOR(255, 170, 255)", 0, 0)]



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
    color        comfy_ui.dialogue_text.color
    outlines     comfy_ui.dialogue_text.outlines

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
# Choice button
################################################################################
init 999 style choice_button:
    background Frame("gui/button/choice_[prefix_]background.png", Borders(5, 5, 5, 5))

init 999 style choice_button_text:
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
image input_caret:
    Solid("CUI_SCD_COLOR(187, 85, 153)")
    size (2, 25)
    subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat
