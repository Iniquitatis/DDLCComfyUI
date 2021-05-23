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
define comfy_ui.menu_title.color     = "CUI_SCD_COLOR(255, 255, 255)"
define comfy_ui.menu_title.outlines  = [(6, "CUI_SCD_COLOR(187, 85, 153)", 0, 0), (3, "CUI_SCD_COLOR(187, 85, 153)", 2, 2)]

define comfy_ui.menu_label.font_size = 24
define comfy_ui.menu_label.color     = "CUI_SCD_COLOR(255, 255, 255)"
define comfy_ui.menu_label.outlines  = [(3, "CUI_SCD_COLOR(187, 85, 153)", 0, 0), (1, "CUI_SCD_COLOR(187, 85, 153)", 1, 1)]

define comfy_ui.menu_text.font_size = 16
define comfy_ui.menu_text.color     = "CUI_SCD_COLOR(56, 56, 56)"
define comfy_ui.menu_text.outlines  = []

define comfy_ui.menu_button_text.font_size            = 24
define comfy_ui.menu_button_text.color                = "CUI_SCD_COLOR(255, 255, 255)"
define comfy_ui.menu_button_text.idle_outlines        = [(4, "CUI_SCD_COLOR(187, 85, 153)", 0, 0), (2, "CUI_SCD_COLOR(187, 85, 153)", 2, 2)]
define comfy_ui.menu_button_text.hover_outlines       = [(4, "CUI_SCD_COLOR(255, 170, 204)", 0, 0), (2, "CUI_SCD_COLOR(255, 170, 204)", 2, 2)]
define comfy_ui.menu_button_text.insensitive_outlines = [(4, "CUI_SCD_COLOR(255, 204, 238)", 0, 0), (2, "CUI_SCD_COLOR(255, 204, 238)", 2, 2)]

define comfy_ui.confirm_prompt_text.color    = "CUI_PRM_COLOR(56, 56, 56)"
define comfy_ui.confirm_prompt_text.outlines = []

define comfy_ui.dialogue_text.vertical_offset = CUI_DLG_VERT_OFFSET()
define comfy_ui.dialogue_text.line_spacing    = CUI_DLG_LINE_SPACING()
define comfy_ui.dialogue_text.color           = "CUI_PRM_COLOR(248, 248, 248)"
define comfy_ui.dialogue_text.outlines        = [(2, "CUI_PRM_COLOR(40, 40, 40)", 0, 0)]

define comfy_ui.history_name.color    = "CUI_PRM_COLOR(248, 248, 248)"
define comfy_ui.history_name.outlines = [(2, "CUI_PRM_COLOR(40, 40, 40)", 0, 0)]

define comfy_ui.history_text.color    = "CUI_PRM_COLOR(255, 255, 255)"
define comfy_ui.history_text.outlines = [(2, "CUI_PRM_COLOR(40, 40, 40)", 0, 0)]

define comfy_ui.quick_button_text.font_size         = 14
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

define comfy_ui.option_button_text.font              = "CUI_OPTION_FONT()"
define comfy_ui.option_button_text.font_kerning      = 0.0
define comfy_ui.option_button_text.font_size         = 24
define comfy_ui.option_button_text.idle_color        = "CUI_SCD_COLOR(170, 170, 170)"
define comfy_ui.option_button_text.hover_color       = "CUI_SCD_COLOR(204, 102, 153)"
define comfy_ui.option_button_text.selected_color    = "CUI_SCD_COLOR(187, 85, 136)"
define comfy_ui.option_button_text.insensitive_color = "CUI_SCD_COLOR(170, 170, 170, 127)"

define comfy_ui.choice_button_spacing = 12



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
# Generic styles
################################################################################

# Button
init 999 style generic_button:
    padding        (5, 5, 5, 5)
    hover_sound    gui.hover_sound
    activate_sound gui.activate_sound
    background     Frame("comfy_ui/button/[prefix_]bg.png", Borders(5, 5, 5, 5))

init 999 style generic_button_text:
    font              comfy_ui.common.font
    kerning           comfy_ui.common.font_kerning
    size              comfy_ui.common.font_size
    align             (0.5, 0.5)
    idle_color        comfy_ui.button_text.idle_color
    hover_color       comfy_ui.button_text.hover_color
    selected_color    comfy_ui.button_text.selected_color
    insensitive_color comfy_ui.button_text.insensitive_color
    outlines          comfy_ui.button_text.outlines

# Option button
init 999 style generic_option_button:
    foreground "gui/button/check_[prefix_]foreground.png"
    padding    (28, 4, 4, 4)

init 999 style generic_option_button_text:
    font              comfy_ui.option_button_text.font
    kerning           comfy_ui.option_button_text.font_kerning
    size              comfy_ui.option_button_text.font_size
    idle_color        comfy_ui.option_button_text.idle_color
    hover_color       comfy_ui.option_button_text.hover_color
    selected_color    comfy_ui.option_button_text.selected_color
    insensitive_color comfy_ui.option_button_text.insensitive_color
    outlines          []

# Scrollbars
init 999 style generic_horizontal_scrollbar:
    ysize        18
    unscrollable "hide"
    bar_vertical False
    bar_invert   True
    base_bar     Frame("comfy_ui/scrollbar/horizontal_bar.png")
    thumb        Frame("comfy_ui/scrollbar/horizontal_[prefix_]thumb.png", Borders(6, 6, 6, 6))

init 999 style generic_vertical_scrollbar:
    xsize        18
    unscrollable "hide"
    bar_vertical True
    bar_invert   True
    base_bar     Frame("comfy_ui/scrollbar/vertical_bar.png")
    thumb        Frame("comfy_ui/scrollbar/vertical_[prefix_]thumb.png", Borders(6, 6, 6, 6))



################################################################################
# Option buttons
################################################################################

# Check button
init 999 style check_button is generic_option_button:
    clear

init 999 style check_button_text is generic_option_button_text:
    clear

# Radio button
init 999 style radio_button is generic_option_button:
    clear

init 999 style radio_button_text is generic_option_button_text:
    clear



################################################################################
# Game menu
################################################################################

# Title
init 999 style game_menu_label_text:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_title.font_size
    color    comfy_ui.menu_title.color
    outlines comfy_ui.menu_title.outlines

# Preference label
init 999 style pref_label_text:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_label.font_size
    color    comfy_ui.menu_label.color
    outlines comfy_ui.menu_label.outlines

# Version text
init 999 style main_menu_version:
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    size     comfy_ui.menu_text.font_size
    color    comfy_ui.menu_text.color
    outlines comfy_ui.menu_text.outlines

# Menu button
init 999 style navigation_button_text:
    font                 comfy_ui.menu_font
    kerning              comfy_ui.menu_font_kerning
    size                 comfy_ui.menu_button_text.font_size
    color                comfy_ui.menu_button_text.color
    outlines             comfy_ui.menu_button_text.idle_outlines
    hover_outlines       comfy_ui.menu_button_text.hover_outlines
    insensitive_outlines comfy_ui.menu_button_text.insensitive_outlines

# File menu
init 999 style page_label_text:
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    color    comfy_ui.menu_text.color
    outlines comfy_ui.menu_text.outlines

init 999 style slot_time_text is generic_button_text:
    size 16

init 999 style slot_name_text is generic_button_text:
    size 16

init 999 style page_button_text is generic_button_text



################################################################################
# Dialogue
################################################################################

# Name
init 999 style say_label:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_label.font_size
    color    comfy_ui.menu_label.color
    outlines comfy_ui.menu_label.outlines

# Text
init 999 style normal:
    font         comfy_ui.common.font
    kerning      comfy_ui.common.font_kerning
    yoffset      comfy_ui.dialogue_text.vertical_offset
    line_spacing comfy_ui.dialogue_text.line_spacing
    color        comfy_ui.dialogue_text.color
    outlines     comfy_ui.dialogue_text.outlines

# Quick button
init 999 style quick_button_text:
    font              comfy_ui.common.font
    kerning           comfy_ui.common.font_kerning
    size              comfy_ui.quick_button_text.font_size
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
    xpos     0
    ypos     5
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    size     comfy_ui.common.font_size
    bold     True
    color    comfy_ui.history_name.color
    outlines comfy_ui.history_name.outlines

# Text
init 999 style history_text:
    xpos     165
    ypos     5
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    size     comfy_ui.common.font_size
    bold     False
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
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    size     comfy_ui.common.font_size
    color    comfy_ui.confirm_prompt_text.color
    outlines comfy_ui.confirm_prompt_text.outlines



################################################################################
# Choice menu
################################################################################
init 999 style choice_vbox:
    spacing comfy_ui.choice_button_spacing

init 999 style choice_button is generic_button:
    clear
    xysize  (420, None)
    padding (25, 5, 25, 5)

init 999 style choice_button_text is generic_button_text:
    clear
