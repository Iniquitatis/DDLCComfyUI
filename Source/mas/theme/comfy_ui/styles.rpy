################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################

################################################################################
# Definitions
################################################################################
define mas_ui.light_button_text_idle_color        = comfy_ui.button_text.light.idle_color
define mas_ui.light_button_text_hover_color       = comfy_ui.button_text.light.hover_color
define mas_ui.light_button_text_insensitive_color = comfy_ui.button_text.light.insensitive_color
define mas_ui.dark_button_text_idle_color         = comfy_ui.button_text.dark.idle_color
define mas_ui.dark_button_text_hover_color        = comfy_ui.button_text.dark.hover_color
define mas_ui.dark_button_text_insensitive_color  = comfy_ui.button_text.dark.insensitive_color



################################################################################
# Option buttons
################################################################################

# Check button
init 999 style check_button_text:
    idle_color        comfy_ui.option_button_text.light.idle_color
    hover_color       comfy_ui.option_button_text.light.hover_color
    selected_color    comfy_ui.option_button_text.light.selected_color
    insensitive_color comfy_ui.option_button_text.light.insensitive_color
    outlines          []

init 999 style check_button_text_dark:
    idle_color        comfy_ui.option_button_text.dark.idle_color
    hover_color       comfy_ui.option_button_text.dark.hover_color
    selected_color    comfy_ui.option_button_text.dark.selected_color
    insensitive_color comfy_ui.option_button_text.dark.insensitive_color
    outlines          []

# Radio button
init 999 style radio_button_text:
    idle_color        comfy_ui.option_button_text.light.idle_color
    hover_color       comfy_ui.option_button_text.light.hover_color
    selected_color    comfy_ui.option_button_text.light.selected_color
    insensitive_color comfy_ui.option_button_text.light.insensitive_color
    outlines          []

init 999 style radio_button_text_dark:
    idle_color        comfy_ui.option_button_text.dark.idle_color
    hover_color       comfy_ui.option_button_text.dark.hover_color
    selected_color    comfy_ui.option_button_text.dark.selected_color
    insensitive_color comfy_ui.option_button_text.dark.insensitive_color
    outlines          []

# Fancy check button
init 999 style generic_fancy_check_button:
    idle_background     Solid(comfy_ui.fancy_check_button.light.idle_background_color)
    hover_background    Solid(comfy_ui.fancy_check_button.light.hover_background_color)
    selected_background Solid(comfy_ui.fancy_check_button.light.selected_background_color)

init 999 style generic_fancy_check_button_dark:
    idle_background     Solid(comfy_ui.fancy_check_button.dark.idle_background_color)
    hover_background    Solid(comfy_ui.fancy_check_button.dark.hover_background_color)
    selected_background Solid(comfy_ui.fancy_check_button.dark.selected_background_color)

init 999 style generic_fancy_check_button_text:
    font           comfy_ui.fancy_check_button_text.font
    kerning        comfy_ui.fancy_check_button_text.font_kerning
    size           comfy_ui.fancy_check_button_text.font_size
    color          comfy_ui.fancy_check_button_text.light.idle_color
    hover_color    comfy_ui.fancy_check_button_text.light.hover_color
    selected_color comfy_ui.fancy_check_button_text.light.selected_color

init 999 style generic_fancy_check_button_text_dark:
    font           comfy_ui.fancy_check_button_text.font
    kerning        comfy_ui.fancy_check_button_text.font_kerning
    size           comfy_ui.fancy_check_button_text.font_size
    color          comfy_ui.fancy_check_button_text.dark.idle_color
    hover_color    comfy_ui.fancy_check_button_text.dark.hover_color
    selected_color comfy_ui.fancy_check_button_text.dark.selected_color



################################################################################
# Bars
################################################################################

# Classroom vertical scrollbar
init 999 style classroom_vscrollbar:
    base_bar Frame("comfy_ui/scrollbar/vertical_bar_lt.png")
    thumb    Frame("comfy_ui/scrollbar/vertical_[prefix_]thumb_lt.png", Borders(6, 6, 6, 6))

init 999 style classroom_vscrollbar_dark:
    base_bar Frame("comfy_ui/scrollbar/vertical_bar_dk.png")
    thumb    Frame("comfy_ui/scrollbar/vertical_[prefix_]thumb_dk.png", Borders(6, 6, 6, 6))

# Selector vertical scrollbar
# NOTE: complete definitions are needed because dark style is not defined in MAS yet
init 999 style mas_selector_sidebar_vbar:
    xsize        18
    base_bar     Frame("comfy_ui/scrollbar/vertical_bar_lt.png")
    thumb        Frame("comfy_ui/scrollbar/vertical_[prefix_]thumb_lt.png", Borders(6, 6, 6, 6))
    bar_vertical True
    bar_invert   True

init 999 style mas_selector_sidebar_vbar_dark:
    xsize        18
    base_bar     Frame("comfy_ui/scrollbar/vertical_bar_dk.png")
    thumb        Frame("comfy_ui/scrollbar/vertical_[prefix_]thumb_dk.png", Borders(6, 6, 6, 6))
    bar_vertical True
    bar_invert   True



################################################################################
# Game menu
################################################################################

# Title
init 999 style game_menu_label_text:
    color    comfy_ui.menu_title.light.color
    outlines comfy_ui.menu_title.light.outlines

init 999 style game_menu_label_text_dark:
    color    comfy_ui.menu_title.dark.color
    outlines comfy_ui.menu_title.dark.outlines

# Preference label
init 999 style pref_label_text:
    color    comfy_ui.menu_label.light.color
    outlines comfy_ui.menu_label.light.outlines

init 999 style pref_label_text_dark:
    color    comfy_ui.menu_label.dark.color
    outlines comfy_ui.menu_label.dark.outlines

# Version text
# NOTE: this style is also used for the tooltips at the bottom of the menu screen
init 999 style main_menu_version:
    color    comfy_ui.menu_text.light.color
    outlines comfy_ui.menu_text.light.outlines

init 999 style main_menu_version_dark:
    color    comfy_ui.menu_text.dark.color
    outlines comfy_ui.menu_text.dark.outlines

# Menu button
init 999 style navigation_button_text:
    color                comfy_ui.menu_button_text.light.color
    outlines             comfy_ui.menu_button_text.light.idle_outlines
    hover_outlines       comfy_ui.menu_button_text.light.hover_outlines
    insensitive_outlines comfy_ui.menu_button_text.light.insensitive_outlines

init 999 style navigation_button_text_dark:
    color                comfy_ui.menu_button_text.dark.color
    outlines             comfy_ui.menu_button_text.dark.idle_outlines
    hover_outlines       comfy_ui.menu_button_text.dark.hover_outlines
    insensitive_outlines comfy_ui.menu_button_text.dark.insensitive_outlines

# File menu
init 999 style page_label_text:
    color    comfy_ui.menu_text.light.color
    outlines comfy_ui.menu_text.light.outlines

init 999 style page_label_text_dark:
    color    comfy_ui.menu_text.dark.color
    outlines comfy_ui.menu_text.dark.outlines

init 999 style slot_button:
    background "gui/button/slot_[prefix_]background.png"

init 999 style slot_button_dark:
    background "gui/button/slot_[prefix_]background_d.png"

init 999 style slot_time_text:
    idle_color        comfy_ui.button_text.light.idle_color
    hover_color       comfy_ui.button_text.light.hover_color
    selected_color    comfy_ui.button_text.light.selected_color
    insensitive_color comfy_ui.button_text.light.insensitive_color
    outlines          comfy_ui.button_text.light.outlines

init 999 style slot_time_text_dark:
    idle_color        comfy_ui.button_text.dark.idle_color
    hover_color       comfy_ui.button_text.dark.hover_color
    selected_color    comfy_ui.button_text.dark.selected_color
    insensitive_color comfy_ui.button_text.dark.insensitive_color
    outlines          comfy_ui.button_text.dark.outlines

init 999 style slot_name_text:
    idle_color        comfy_ui.button_text.light.idle_color
    hover_color       comfy_ui.button_text.light.hover_color
    selected_color    comfy_ui.button_text.light.selected_color
    insensitive_color comfy_ui.button_text.light.insensitive_color
    outlines          comfy_ui.button_text.light.outlines

init 999 style slot_name_text_dark:
    idle_color        comfy_ui.button_text.dark.idle_color
    hover_color       comfy_ui.button_text.dark.hover_color
    selected_color    comfy_ui.button_text.dark.selected_color
    insensitive_color comfy_ui.button_text.dark.insensitive_color
    outlines          comfy_ui.button_text.dark.outlines

init 999 style page_button_text:
    idle_color        comfy_ui.button_text.light.idle_color
    hover_color       comfy_ui.button_text.light.hover_color
    selected_color    comfy_ui.button_text.light.selected_color
    insensitive_color comfy_ui.button_text.light.insensitive_color
    outlines          comfy_ui.button_text.light.outlines

init 999 style page_button_text_dark:
    idle_color        comfy_ui.button_text.dark.idle_color
    hover_color       comfy_ui.button_text.dark.hover_color
    selected_color    comfy_ui.button_text.dark.selected_color
    insensitive_color comfy_ui.button_text.dark.insensitive_color
    outlines          comfy_ui.button_text.dark.outlines



################################################################################
# Music menu
################################################################################

# Music menu button
init 999 style music_menu_button_text:
    color                comfy_ui.music_menu_button_text.light.color
    outlines             comfy_ui.music_menu_button_text.light.idle_outlines
    hover_outlines       comfy_ui.music_menu_button_text.light.hover_outlines
    insensitive_outlines comfy_ui.music_menu_button_text.light.insensitive_outlines

init 999 style music_menu_button_text_dark:
    color                comfy_ui.music_menu_button_text.dark.color
    outlines             comfy_ui.music_menu_button_text.dark.idle_outlines
    hover_outlines       comfy_ui.music_menu_button_text.dark.hover_outlines
    insensitive_outlines comfy_ui.music_menu_button_text.dark.insensitive_outlines



################################################################################
# Dialogue
################################################################################

# Name
init 999 style say_label:
    color    comfy_ui.menu_label.light.color
    outlines comfy_ui.menu_label.light.outlines

init 999 style say_label_dark:
    color    comfy_ui.menu_label.dark.color
    outlines comfy_ui.menu_label.dark.outlines

# Text
init 999 style normal:
    color    comfy_ui.dialogue_text.color
    outlines comfy_ui.dialogue_text.outlines

# Quick button
init 999 style quick_button_text:
    idle_color        comfy_ui.quick_button_text.light.idle_color
    hover_color       comfy_ui.quick_button_text.light.hover_color
    selected_color    comfy_ui.quick_button_text.light.selected_color
    insensitive_color comfy_ui.quick_button_text.light.insensitive_color
    outlines          comfy_ui.quick_button_text.light.outlines

init 999 style quick_button_text_dark:
    idle_color        comfy_ui.quick_button_text.dark.idle_color
    hover_color       comfy_ui.quick_button_text.dark.hover_color
    selected_color    comfy_ui.quick_button_text.dark.selected_color
    insensitive_color comfy_ui.quick_button_text.dark.insensitive_color
    outlines          comfy_ui.quick_button_text.dark.outlines



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
    color    comfy_ui.confirm_prompt_text.light.color
    outlines comfy_ui.confirm_prompt_text.light.outlines

init 999 style confirm_prompt_text_dark:
    color    comfy_ui.confirm_prompt_text.dark.color
    outlines comfy_ui.confirm_prompt_text.dark.outlines



################################################################################
# Choice menu
################################################################################
init 999 style choice_button:
    background Frame("comfy_ui/button/[prefix_]bg_lt.png", Borders(5, 5, 5, 5))

init 999 style choice_button_dark:
    background Frame("comfy_ui/button/[prefix_]bg_dk.png", Borders(5, 5, 5, 5))

init 999 style choice_button_text:
    idle_color        comfy_ui.button_text.light.idle_color
    hover_color       comfy_ui.button_text.light.hover_color
    selected_color    comfy_ui.button_text.light.selected_color
    insensitive_color comfy_ui.button_text.light.insensitive_color
    outlines          comfy_ui.button_text.light.outlines

init 999 style choice_button_text_dark:
    idle_color        comfy_ui.button_text.dark.idle_color
    hover_color       comfy_ui.button_text.dark.hover_color
    selected_color    comfy_ui.button_text.dark.selected_color
    insensitive_color comfy_ui.button_text.dark.insensitive_color
    outlines          comfy_ui.button_text.dark.outlines



################################################################################
# Scrollable menu
################################################################################
init 999 style scrollable_menu_button:
    background Frame("comfy_ui/button/[prefix_]bg_lt.png", Borders(5, 5, 5, 5))

init 999 style scrollable_menu_button_dark:
    background Frame("comfy_ui/button/[prefix_]bg_dk.png", Borders(5, 5, 5, 5))

init 999 style scrollable_menu_button_text:
    idle_color        comfy_ui.button_text.light.idle_color
    hover_color       comfy_ui.button_text.light.hover_color
    selected_color    comfy_ui.button_text.light.selected_color
    insensitive_color comfy_ui.button_text.light.insensitive_color
    outlines          comfy_ui.button_text.light.outlines

init 999 style scrollable_menu_button_text_dark:
    idle_color        comfy_ui.button_text.dark.idle_color
    hover_color       comfy_ui.button_text.dark.hover_color
    selected_color    comfy_ui.button_text.dark.selected_color
    insensitive_color comfy_ui.button_text.dark.insensitive_color
    outlines          comfy_ui.button_text.dark.outlines



################################################################################
# Two-pane scrollable menu
################################################################################
init 999 style twopane_scrollable_menu_button:
    background Frame("comfy_ui/button/[prefix_]bg_lt.png", Borders(5, 5, 5, 5))

init 999 style twopane_scrollable_menu_button_dark:
    background Frame("comfy_ui/button/[prefix_]bg_dk.png", Borders(5, 5, 5, 5))

init 999 style twopane_scrollable_menu_button_text:
    idle_color        comfy_ui.button_text.light.idle_color
    hover_color       comfy_ui.button_text.light.hover_color
    selected_color    comfy_ui.button_text.light.selected_color
    insensitive_color comfy_ui.button_text.light.insensitive_color
    outlines          comfy_ui.button_text.light.outlines

init 999 style twopane_scrollable_menu_button_text_dark:
    idle_color        comfy_ui.button_text.dark.idle_color
    hover_color       comfy_ui.button_text.dark.hover_color
    selected_color    comfy_ui.button_text.dark.selected_color
    insensitive_color comfy_ui.button_text.dark.insensitive_color
    outlines          comfy_ui.button_text.dark.outlines



################################################################################
# Talk choice menu
################################################################################
init 999 style talk_choice_button:
    background Frame("comfy_ui/button/[prefix_]bg_lt.png", Borders(5, 5, 5, 5))

init 999 style talk_choice_button_dark:
    background Frame("comfy_ui/button/[prefix_]bg_dk.png", Borders(5, 5, 5, 5))

init 999 style talk_choice_button_text:
    idle_color        comfy_ui.button_text.light.idle_color
    hover_color       comfy_ui.button_text.light.hover_color
    selected_color    comfy_ui.button_text.light.selected_color
    insensitive_color comfy_ui.button_text.light.insensitive_color
    outlines          comfy_ui.button_text.light.outlines

init 999 style talk_choice_button_text_dark:
    idle_color        comfy_ui.button_text.dark.idle_color
    hover_color       comfy_ui.button_text.dark.hover_color
    selected_color    comfy_ui.button_text.dark.selected_color
    insensitive_color comfy_ui.button_text.dark.insensitive_color
    outlines          comfy_ui.button_text.dark.outlines



################################################################################
# Hotkey button menu
################################################################################
init 999 style hkb_button:
    background Frame("comfy_ui/button/[prefix_]bg_lt.png", Borders(5, 5, 5, 5))

init 999 style hkb_button_dark:
    background Frame("comfy_ui/button/[prefix_]bg_dk.png", Borders(5, 5, 5, 5))

init 999 style hkb_button_text:
    align             (0.5, 0.5)
    text_align        0.5
    idle_color        comfy_ui.button_text.light.idle_color
    hover_color       comfy_ui.button_text.light.hover_color
    selected_color    comfy_ui.button_text.light.selected_color
    insensitive_color comfy_ui.button_text.light.insensitive_color
    outlines          comfy_ui.button_text.light.outlines

init 999 style hkb_button_text_dark:
    align             (0.5, 0.5)
    text_align        0.5
    idle_color        comfy_ui.button_text.dark.idle_color
    hover_color       comfy_ui.button_text.dark.hover_color
    selected_color    comfy_ui.button_text.dark.selected_color
    insensitive_color comfy_ui.button_text.dark.insensitive_color
    outlines          comfy_ui.button_text.dark.outlines



################################################################################
# Island buttons
################################################################################
init 999 style island_button:
    background Frame("comfy_ui/button/[prefix_]bg_lt.png", Borders(5, 5, 5, 5))

init 999 style island_button_dark:
    background Frame("comfy_ui/button/[prefix_]bg_dk.png", Borders(5, 5, 5, 5))

init 999 style island_button_text:
    align             (0.5, 0.5)
    text_align        0.5
    idle_color        comfy_ui.button_text.light.idle_color
    hover_color       comfy_ui.button_text.light.hover_color
    selected_color    comfy_ui.button_text.light.selected_color
    insensitive_color comfy_ui.button_text.light.insensitive_color
    outlines          comfy_ui.button_text.light.outlines

init 999 style island_button_text_dark:
    align             (0.5, 0.5)
    text_align        0.5
    idle_color        comfy_ui.button_text.dark.idle_color
    hover_color       comfy_ui.button_text.dark.hover_color
    selected_color    comfy_ui.button_text.dark.selected_color
    insensitive_color comfy_ui.button_text.dark.insensitive_color
    outlines          comfy_ui.button_text.dark.outlines



################################################################################
# Extras menu
################################################################################
init 999 style mas_extra_menu_frame:
    background Frame("mod_assets/frames/trans_pink2pxborder100.png", Borders(5, 5, 5, 5, pad_top = 2, pad_bottom = 4))

init 999 style mas_extra_menu_frame_dark:
    background Frame("mod_assets/frames/trans_pink2pxborder100_d.png", Borders(5, 5, 5, 5, pad_top = 2, pad_bottom = 4))

init 999 style mas_extra_menu_label_text:
    color "#f8f8f8"

init 999 style mas_extra_menu_label_text_dark:
    color comfy_ui.button_text.dark.idle_color

# NOTE: complete definitions are needed because dark style is not defined in MAS yet
init 999 style mas_adjust_vbar:
    xsize        18
    base_bar     Frame("comfy_ui/scrollbar/vertical_bar_lt.png", Borders(4, 4, 4, 4))
    thumb        "comfy_ui/slider/vertical_[prefix_]thumb_lt.png"
    bar_vertical True

init 999 style mas_adjust_vbar_dark:
    xsize        18
    base_bar     Frame("comfy_ui/scrollbar/vertical_bar_dk.png", Borders(4, 4, 4, 4))
    thumb        "comfy_ui/slider/vertical_[prefix_]thumb_dk.png"
    bar_vertical True

init 999 style mas_adjustable_button:
    background Frame("comfy_ui/button/[prefix_]bg_lt.png", Borders(5, 5, 5, 5))

init 999 style mas_adjustable_button_dark:
    background Frame("comfy_ui/button/[prefix_]bg_dk.png", Borders(5, 5, 5, 5))

init 999 style mas_adjustable_button_text:
    align             (0.5, 0.5)
    text_align        0.5
    idle_color        comfy_ui.button_text.light.idle_color
    hover_color       comfy_ui.button_text.light.hover_color
    selected_color    comfy_ui.button_text.light.selected_color
    insensitive_color comfy_ui.button_text.light.insensitive_color
    outlines          comfy_ui.button_text.light.outlines

init 999 style mas_adjustable_button_text_dark:
    align             (0.5, 0.5)
    text_align        0.5
    idle_color        comfy_ui.button_text.dark.idle_color
    hover_color       comfy_ui.button_text.dark.hover_color
    selected_color    comfy_ui.button_text.dark.selected_color
    insensitive_color comfy_ui.button_text.dark.insensitive_color
    outlines          comfy_ui.button_text.dark.outlines



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
