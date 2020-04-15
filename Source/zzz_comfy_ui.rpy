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
define mas_comfy_ui.common.font         = "CUI_MAIN_FONT()"
define mas_comfy_ui.common.font_bold    = "CUI_MAIN_FONT_BOLD()"
define mas_comfy_ui.common.font_italic  = "CUI_MAIN_FONT_ITALIC()"
define mas_comfy_ui.common.font_kerning = 0.0
define mas_comfy_ui.common.font_size    = 24

define mas_comfy_ui.menu_font         = "CUI_MENU_FONT()"
define mas_comfy_ui.menu_font_kerning = 0.0

define mas_comfy_ui.menu_title.font_size      = 38
define mas_comfy_ui.menu_title.light.color    = "CUI_SCD_COLOR(255, 255, 255)"
define mas_comfy_ui.menu_title.light.outlines = [(6, "CUI_SCD_COLOR(187, 85, 153)", 0, 0), (3, "CUI_SCD_COLOR(187, 85, 153)", 2, 2)]
define mas_comfy_ui.menu_title.dark.color     = "CUI_SCD_COLOR(255, 217, 232)"
define mas_comfy_ui.menu_title.dark.outlines  = [(6, "CUI_SCD_COLOR(222, 54, 126)", 0, 0), (3, "CUI_SCD_COLOR(222, 54, 126)", 2, 2)]

define mas_comfy_ui.menu_button_text.font_size                  = 24
define mas_comfy_ui.menu_button_text.light.color                = "CUI_SCD_COLOR(255, 255, 255)"
define mas_comfy_ui.menu_button_text.light.idle_outlines        = [(4, "CUI_SCD_COLOR(187, 85, 153)", 0, 0), (2, "CUI_SCD_COLOR(187, 85, 153)", 2, 2)]
define mas_comfy_ui.menu_button_text.light.hover_outlines       = [(4, "CUI_SCD_COLOR(255, 170, 204)", 0, 0), (2, "CUI_SCD_COLOR(255, 170, 204)", 2, 2)]
define mas_comfy_ui.menu_button_text.light.insensitive_outlines = [(4, "CUI_SCD_COLOR(255, 204, 238)", 0, 0), (2, "CUI_SCD_COLOR(255, 204, 238)", 2, 2)]
define mas_comfy_ui.menu_button_text.dark.color                 = "CUI_SCD_COLOR(255, 217, 232)"
define mas_comfy_ui.menu_button_text.dark.idle_outlines         = [(4, "CUI_SCD_COLOR(222, 54, 126)", 0, 0), (2, "CUI_SCD_COLOR(222, 54, 126)", 2, 2)]
define mas_comfy_ui.menu_button_text.dark.hover_outlines        = [(4, "CUI_SCD_COLOR(255, 128, 183)", 0, 0), (2, "CUI_SCD_COLOR(255, 128, 183)", 2, 2)]
define mas_comfy_ui.menu_button_text.dark.insensitive_outlines  = [(4, "CUI_SCD_COLOR(255, 178, 212)", 0, 0), (2, "CUI_SCD_COLOR(255, 178, 212)", 2, 2)]

define mas_comfy_ui.option_button_text.font                    = "CUI_OPTION_FONT()"
define mas_comfy_ui.option_button_text.font_kerning            = 0.0
define mas_comfy_ui.option_button_text.font_size               = 24
define mas_comfy_ui.option_button_text.light.idle_color        = "CUI_SCD_COLOR(170, 170, 170)"
define mas_comfy_ui.option_button_text.light.hover_color       = "CUI_SCD_COLOR(204, 102, 153)"
define mas_comfy_ui.option_button_text.light.selected_color    = "CUI_SCD_COLOR(187, 85, 136)"
define mas_comfy_ui.option_button_text.light.insensitive_color = "CUI_SCD_COLOR(170, 170, 170, 127)"
define mas_comfy_ui.option_button_text.dark.idle_color         = "CUI_SCD_COLOR(170, 170, 170)"
define mas_comfy_ui.option_button_text.dark.hover_color        = "CUI_SCD_COLOR(255, 128, 183)"
define mas_comfy_ui.option_button_text.dark.selected_color     = "CUI_SCD_COLOR(222, 54, 126)"
define mas_comfy_ui.option_button_text.dark.insensitive_color  = "CUI_SCD_COLOR(170, 170, 170, 127)"

define mas_comfy_ui.menu_label.font_size      = 24
define mas_comfy_ui.menu_label.light.color    = "CUI_SCD_COLOR(255, 255, 255)"
define mas_comfy_ui.menu_label.light.outlines = [(3, "CUI_SCD_COLOR(187, 85, 153)", 0, 0), (1, "CUI_SCD_COLOR(187, 85, 153)", 1, 1)]
define mas_comfy_ui.menu_label.dark.color     = "CUI_SCD_COLOR(255, 217, 232)"
define mas_comfy_ui.menu_label.dark.outlines  = [(3, "CUI_SCD_COLOR(222, 54, 126)", 0, 0), (1, "CUI_SCD_COLOR(222, 54, 126)", 1, 1)]

define mas_comfy_ui.version_label.font_size      = 16
define mas_comfy_ui.version_label.light.color    = "CUI_SCD_COLOR(64, 64, 64)"
define mas_comfy_ui.version_label.light.outlines = []
define mas_comfy_ui.version_label.dark.color     = "CUI_SCD_COLOR(253, 91, 162)"
define mas_comfy_ui.version_label.dark.outlines  = []

define mas_comfy_ui.music_menu_button_text.font                       = "mod_assets/font/mplus-2p-regular.ttf"
define mas_comfy_ui.music_menu_button_text.font_kerning               = 0.0
define mas_comfy_ui.music_menu_button_text.font_size                  = 24
define mas_comfy_ui.music_menu_button_text.light.color                = "CUI_SCD_COLOR(255, 255, 255)"
define mas_comfy_ui.music_menu_button_text.light.idle_outlines        = [(3, "CUI_SCD_COLOR(187, 85, 153)", 0, 0), (1, "CUI_SCD_COLOR(187, 85, 153)", 1, 1)]
define mas_comfy_ui.music_menu_button_text.light.hover_outlines       = [(3, "CUI_SCD_COLOR(255, 170, 204)", 0, 0), (1, "CUI_SCD_COLOR(255, 170, 204)", 1, 1)]
define mas_comfy_ui.music_menu_button_text.light.insensitive_outlines = [(3, "CUI_SCD_COLOR(255, 204, 238)", 0, 0), (1, "CUI_SCD_COLOR(255, 204, 238)", 1, 1)]
define mas_comfy_ui.music_menu_button_text.dark.color                 = "CUI_SCD_COLOR(255, 217, 232)"
define mas_comfy_ui.music_menu_button_text.dark.idle_outlines         = [(3, "CUI_SCD_COLOR(222, 54, 126)", 0, 0), (1, "CUI_SCD_COLOR(222, 54, 126)", 1, 1)]
define mas_comfy_ui.music_menu_button_text.dark.hover_outlines        = [(3, "CUI_SCD_COLOR(255, 128, 183)", 0, 0), (1, "CUI_SCD_COLOR(255, 128, 183)", 1, 1)]
define mas_comfy_ui.music_menu_button_text.dark.insensitive_outlines  = [(3, "CUI_SCD_COLOR(255, 178, 212)", 0, 0), (1, "CUI_SCD_COLOR(255, 178, 212)", 1, 1)]

define mas_comfy_ui.confirm_prompt_text.light.color    = "CUI_PRM_COLOR(64, 64, 64)"
define mas_comfy_ui.confirm_prompt_text.light.outlines = []
define mas_comfy_ui.confirm_prompt_text.dark.color     = "CUI_PRM_COLOR(253, 91, 162)"
define mas_comfy_ui.confirm_prompt_text.dark.outlines  = []

define mas_comfy_ui.dialogue_text.color    = "CUI_PRM_COLOR(248, 248, 248)"
define mas_comfy_ui.dialogue_text.outlines = [(2, "CUI_PRM_COLOR(64, 64, 64)", 0, 0)]

define mas_comfy_ui.quick_button_text.font_size               = 14
define mas_comfy_ui.quick_button_text.light.idle_color        = "CUI_SCD_COLOR(85, 34, 34)"
define mas_comfy_ui.quick_button_text.light.hover_color       = "CUI_SCD_COLOR(255, 204, 204)"
define mas_comfy_ui.quick_button_text.light.selected_color    = "CUI_SCD_COLOR(255, 255, 255)"
define mas_comfy_ui.quick_button_text.light.insensitive_color = "CUI_SCD_COLOR(170, 102, 102)"
define mas_comfy_ui.quick_button_text.light.outlines          = []
define mas_comfy_ui.quick_button_text.dark.idle_color         = "CUI_SCD_COLOR(255, 170, 153)"
define mas_comfy_ui.quick_button_text.dark.hover_color        = "CUI_SCD_COLOR(255, 212, 204)"
define mas_comfy_ui.quick_button_text.dark.selected_color     = "CUI_SCD_COLOR(255, 238, 235)"
define mas_comfy_ui.quick_button_text.dark.insensitive_color  = "CUI_SCD_COLOR(170, 102, 102)"
define mas_comfy_ui.quick_button_text.dark.outlines           = []

define mas_comfy_ui.button_text.light.idle_color        = "CUI_PRM_COLOR(64, 64, 64)"
define mas_comfy_ui.button_text.light.hover_color       = "CUI_PRM_COLOR(255, 170, 153)"
define mas_comfy_ui.button_text.light.selected_color    = "CUI_PRM_COLOR(187, 85, 136)"
define mas_comfy_ui.button_text.light.insensitive_color = "CUI_PRM_COLOR(170, 170, 170, 127)"
define mas_comfy_ui.button_text.light.outlines          = []
define mas_comfy_ui.button_text.dark.idle_color         = "CUI_PRM_COLOR(253, 91, 162)"
define mas_comfy_ui.button_text.dark.hover_color        = "CUI_PRM_COLOR(255, 171, 216)"
define mas_comfy_ui.button_text.dark.selected_color     = "CUI_PRM_COLOR(187, 85, 136)"
define mas_comfy_ui.button_text.dark.insensitive_color  = "CUI_PRM_COLOR(170, 170, 170, 127)"
define mas_comfy_ui.button_text.dark.outlines           = []

define mas_comfy_ui.button_spacing        = 6
define mas_comfy_ui.talk_button_spacing   = 13
define mas_comfy_ui.hotkey_button_spacing = -4



################################################################################
# Init
################################################################################
init python:
    config.font_replacement_map[mas_comfy_ui.common.font, True, False] = (mas_comfy_ui.common.font_bold, False, False)
    config.font_replacement_map[mas_comfy_ui.common.font, False, True] = (mas_comfy_ui.common.font_italic, False, False)



################################################################################
# Labels
################################################################################

# Menu title
style game_menu_label_text:
    font     mas_comfy_ui.menu_font
    kerning  mas_comfy_ui.menu_font_kerning
    size     mas_comfy_ui.menu_title.font_size
    color    mas_comfy_ui.menu_title.light.color
    outlines mas_comfy_ui.menu_title.light.outlines

# Menu title (dark)
style game_menu_label_dark_text:
    font     mas_comfy_ui.menu_font
    kerning  mas_comfy_ui.menu_font_kerning
    size     mas_comfy_ui.menu_title.font_size
    color    mas_comfy_ui.menu_title.dark.color
    outlines mas_comfy_ui.menu_title.dark.outlines

# Menu button
style navigation_button_text:
    font                 mas_comfy_ui.menu_font
    kerning              mas_comfy_ui.menu_font_kerning
    size                 mas_comfy_ui.menu_button_text.font_size
    color                mas_comfy_ui.menu_button_text.light.color
    outlines             mas_comfy_ui.menu_button_text.light.idle_outlines
    hover_outlines       mas_comfy_ui.menu_button_text.light.hover_outlines
    insensitive_outlines mas_comfy_ui.menu_button_text.light.insensitive_outlines

# Menu button (dark)
style navigation_dark_button_text:
    font                 mas_comfy_ui.menu_font
    kerning              mas_comfy_ui.menu_font_kerning
    size                 mas_comfy_ui.menu_button_text.font_size
    color                mas_comfy_ui.menu_button_text.dark.color
    outlines             mas_comfy_ui.menu_button_text.dark.idle_outlines
    hover_outlines       mas_comfy_ui.menu_button_text.dark.hover_outlines
    insensitive_outlines mas_comfy_ui.menu_button_text.dark.insensitive_outlines

# Check button
style check_button_text:
    font              mas_comfy_ui.option_button_text.font
    kerning           mas_comfy_ui.option_button_text.font_kerning
    size              mas_comfy_ui.option_button_text.font_size
    idle_color        mas_comfy_ui.option_button_text.light.idle_color
    hover_color       mas_comfy_ui.option_button_text.light.hover_color
    selected_color    mas_comfy_ui.option_button_text.light.selected_color
    insensitive_color mas_comfy_ui.option_button_text.light.insensitive_color

# Check button (dark)
style check_dark_button_text:
    font              mas_comfy_ui.option_button_text.font
    kerning           mas_comfy_ui.option_button_text.font_kerning
    size              mas_comfy_ui.option_button_text.font_size
    idle_color        mas_comfy_ui.option_button_text.dark.idle_color
    hover_color       mas_comfy_ui.option_button_text.dark.hover_color
    selected_color    mas_comfy_ui.option_button_text.dark.selected_color
    insensitive_color mas_comfy_ui.option_button_text.dark.insensitive_color

# Radio button
style radio_button_text:
    font              mas_comfy_ui.option_button_text.font
    kerning           mas_comfy_ui.option_button_text.font_kerning
    size              mas_comfy_ui.option_button_text.font_size
    idle_color        mas_comfy_ui.option_button_text.light.idle_color
    hover_color       mas_comfy_ui.option_button_text.light.hover_color
    selected_color    mas_comfy_ui.option_button_text.light.selected_color
    insensitive_color mas_comfy_ui.option_button_text.light.insensitive_color

# Radio button (dark)
style radio_dark_button_text:
    font              mas_comfy_ui.option_button_text.font
    kerning           mas_comfy_ui.option_button_text.font_kerning
    size              mas_comfy_ui.option_button_text.font_size
    idle_color        mas_comfy_ui.option_button_text.dark.idle_color
    hover_color       mas_comfy_ui.option_button_text.dark.hover_color
    selected_color    mas_comfy_ui.option_button_text.dark.selected_color
    insensitive_color mas_comfy_ui.option_button_text.dark.insensitive_color

# Main menu version text
style main_menu_version_def:
    font     mas_comfy_ui.common.font
    kerning  mas_comfy_ui.common.font_kerning
    size     mas_comfy_ui.version_label.font_size
    color    mas_comfy_ui.version_label.light.color
    outlines mas_comfy_ui.version_label.light.outlines

# Main menu version text (dark)
style main_menu_version_dark:
    font     mas_comfy_ui.common.font
    kerning  mas_comfy_ui.common.font_kerning
    size     mas_comfy_ui.version_label.font_size
    color    mas_comfy_ui.version_label.dark.color
    outlines mas_comfy_ui.version_label.dark.outlines

# Music menu button
style music_menu_button_text:
    font                 mas_comfy_ui.music_menu_button_text.font
    kerning              mas_comfy_ui.music_menu_button_text.font_kerning
    size                 mas_comfy_ui.music_menu_button_text.font_size
    color                mas_comfy_ui.music_menu_button_text.light.color
    outlines             mas_comfy_ui.music_menu_button_text.light.idle_outlines
    hover_outlines       mas_comfy_ui.music_menu_button_text.light.hover_outlines
    insensitive_outlines mas_comfy_ui.music_menu_button_text.light.insensitive_outlines

# Music menu button (dark)
style music_menu_dark_button_text:
    font                 mas_comfy_ui.music_menu_button_text.font
    kerning              mas_comfy_ui.music_menu_button_text.font_kerning
    size                 mas_comfy_ui.music_menu_button_text.font_size
    color                mas_comfy_ui.music_menu_button_text.dark.color
    outlines             mas_comfy_ui.music_menu_button_text.dark.idle_outlines
    hover_outlines       mas_comfy_ui.music_menu_button_text.dark.hover_outlines
    insensitive_outlines mas_comfy_ui.music_menu_button_text.dark.insensitive_outlines

# Preference label
style pref_def_label_text:
    font     mas_comfy_ui.menu_font
    kerning  mas_comfy_ui.menu_font_kerning
    size     mas_comfy_ui.menu_label.font_size
    color    mas_comfy_ui.menu_label.light.color
    outlines mas_comfy_ui.menu_label.light.outlines

# Preference label (dark)
style pref_dark_label_text:
    font     mas_comfy_ui.menu_font
    kerning  mas_comfy_ui.menu_font_kerning
    size     mas_comfy_ui.menu_label.font_size
    color    mas_comfy_ui.menu_label.dark.color
    outlines mas_comfy_ui.menu_label.dark.outlines

# Confirm prompt
style confirm_prompt_text_def:
    font     mas_comfy_ui.common.font
    kerning  mas_comfy_ui.common.font_kerning
    size     mas_comfy_ui.common.font_size
    color    mas_comfy_ui.confirm_prompt_text.light.color
    outlines mas_comfy_ui.confirm_prompt_text.light.outlines

# Confirm prompt (dark)
style confirm_prompt_text_dark:
    font     mas_comfy_ui.common.font
    kerning  mas_comfy_ui.common.font_kerning
    size     mas_comfy_ui.common.font_size
    color    mas_comfy_ui.confirm_prompt_text.dark.color
    outlines mas_comfy_ui.confirm_prompt_text.dark.outlines



################################################################################
# Dialogue
################################################################################

# Name
style say_label_def:
    font     mas_comfy_ui.menu_font
    kerning  mas_comfy_ui.menu_font_kerning
    size     mas_comfy_ui.menu_label.font_size
    color    mas_comfy_ui.menu_label.light.color
    outlines mas_comfy_ui.menu_label.light.outlines

# Name (dark)
style say_label_dark:
    font     mas_comfy_ui.menu_font
    kerning  mas_comfy_ui.menu_font_kerning
    size     mas_comfy_ui.menu_label.font_size
    color    mas_comfy_ui.menu_label.dark.color
    outlines mas_comfy_ui.menu_label.dark.outlines

# Text
style normal:
    font     mas_comfy_ui.common.font
    kerning  mas_comfy_ui.common.font_kerning
    yoffset  -3
    color    mas_comfy_ui.dialogue_text.color
    outlines mas_comfy_ui.dialogue_text.outlines

# Quick button
style quick_button_text:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.quick_button_text.font_size
    idle_color        mas_comfy_ui.quick_button_text.light.idle_color
    hover_color       mas_comfy_ui.quick_button_text.light.hover_color
    selected_color    mas_comfy_ui.quick_button_text.light.selected_color
    insensitive_color mas_comfy_ui.quick_button_text.light.insensitive_color
    outlines          mas_comfy_ui.quick_button_text.light.outlines

# Quick button (dark)
style quick_dark_button_text:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.quick_button_text.font_size
    idle_color        mas_comfy_ui.quick_button_text.dark.idle_color
    hover_color       mas_comfy_ui.quick_button_text.dark.hover_color
    selected_color    mas_comfy_ui.quick_button_text.dark.selected_color
    insensitive_color mas_comfy_ui.quick_button_text.dark.insensitive_color
    outlines          mas_comfy_ui.quick_button_text.dark.outlines



################################################################################
# History
################################################################################

# Name
style history_name_text:
    font     mas_comfy_ui.common.font
    kerning  mas_comfy_ui.common.font_kerning
    color    mas_comfy_ui.dialogue_text.color
    outlines mas_comfy_ui.dialogue_text.outlines

# Text
style history_text:
    font     mas_comfy_ui.common.font
    kerning  mas_comfy_ui.common.font_kerning
    color    mas_comfy_ui.dialogue_text.color
    outlines mas_comfy_ui.dialogue_text.outlines



################################################################################
# Frames
################################################################################

# Frame
define gui.frame_def_borders = Borders(5, 5, 5, 5)

# Frame (dark)
define gui.frame_dark_borders = Borders(5, 5, 5, 5)

# Confirm frame
define gui.confirm_frame_def_borders = Borders(5, 5, 5, 5)

# Confirm frame (dark)
define gui.confirm_frame_dark_borders = Borders(5, 5, 5, 5)



################################################################################
# Buttons
################################################################################

# Choice button
define gui.choice_button_borders = Borders(25, 5, 25, 5)
define gui.choice_button_height  = None

style choice_button_text:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.common.font_size
    bold              False
    idle_color        mas_comfy_ui.button_text.light.idle_color
    hover_color       mas_comfy_ui.button_text.light.hover_color
    selected_color    mas_comfy_ui.button_text.light.selected_color
    insensitive_color mas_comfy_ui.button_text.light.insensitive_color
    outlines          mas_comfy_ui.button_text.light.outlines

# Choice button (dark)
define gui.choice_dark_button_borders = Borders(25, 5, 25, 5)
define gui.choice_dark_button_height  = None

style choice_dark_button_text:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.common.font_size
    bold              False
    idle_color        mas_comfy_ui.button_text.dark.idle_color
    hover_color       mas_comfy_ui.button_text.dark.hover_color
    selected_color    mas_comfy_ui.button_text.dark.selected_color
    insensitive_color mas_comfy_ui.button_text.dark.insensitive_color
    outlines          mas_comfy_ui.button_text.dark.outlines

# Scrollable menu button
define gui.scrollable_menu_button_borders = Borders(25, 5, 25, 5)
define gui.scrollable_menu_button_height  = None

style scrollable_menu_button_text:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.common.font_size
    bold              False
    idle_color        mas_comfy_ui.button_text.light.idle_color
    hover_color       mas_comfy_ui.button_text.light.hover_color
    selected_color    mas_comfy_ui.button_text.light.selected_color
    insensitive_color mas_comfy_ui.button_text.light.insensitive_color
    outlines          mas_comfy_ui.button_text.light.outlines

# Scrollable menu button (dark)
define gui.scrollable_menu_dark_button_borders = Borders(25, 5, 25, 5)
define gui.scrollable_menu_dark_button_height  = None

style scrollable_menu_dark_button_text:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.common.font_size
    bold              False
    idle_color        mas_comfy_ui.button_text.dark.idle_color
    hover_color       mas_comfy_ui.button_text.dark.hover_color
    selected_color    mas_comfy_ui.button_text.dark.selected_color
    insensitive_color mas_comfy_ui.button_text.dark.insensitive_color
    outlines          mas_comfy_ui.button_text.dark.outlines

# Two-pane scrollable menu button
define gui.twopane_scrollable_menu_button_borders = Borders(25, 5, 25, 5)
define gui.twopane_scrollable_menu_button_height  = None

style twopane_scrollable_menu_button_text:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.common.font_size
    bold              False
    idle_color        mas_comfy_ui.button_text.light.idle_color
    hover_color       mas_comfy_ui.button_text.light.hover_color
    selected_color    mas_comfy_ui.button_text.light.selected_color
    insensitive_color mas_comfy_ui.button_text.light.insensitive_color
    outlines          mas_comfy_ui.button_text.light.outlines

# Two-pane scrollable menu button (dark)
define gui.twopane_scrollable_menu_dark_button_borders = Borders(25, 5, 25, 5)
define gui.twopane_scrollable_menu_dark_button_height  = None

style twopane_scrollable_menu_dark_button_text:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.common.font_size
    bold              False
    idle_color        mas_comfy_ui.button_text.dark.idle_color
    hover_color       mas_comfy_ui.button_text.dark.hover_color
    selected_color    mas_comfy_ui.button_text.dark.selected_color
    insensitive_color mas_comfy_ui.button_text.dark.insensitive_color
    outlines          mas_comfy_ui.button_text.dark.outlines

# Two-pane scrollable menu special button
define gui.twopane_scrollable_menu_special_button_borders = Borders(25, 5, 25, 5)
define gui.twopane_scrollable_menu_special_button_height  = None

style twopane_scrollable_menu_special_button_text:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.common.font_size
    bold              False
    idle_color        mas_comfy_ui.button_text.light.idle_color
    hover_color       mas_comfy_ui.button_text.light.hover_color
    selected_color    mas_comfy_ui.button_text.light.selected_color
    insensitive_color mas_comfy_ui.button_text.light.insensitive_color
    outlines          mas_comfy_ui.button_text.light.outlines

# Two-pane scrollable menu special button (dark)
define gui.twopane_scrollable_menu_dark_special_button_borders = Borders(25, 5, 25, 5)
define gui.twopane_scrollable_menu_dark_special_button_height  = None

style twopane_scrollable_menu_dark_special_button_text:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.common.font_size
    bold              False
    idle_color        mas_comfy_ui.button_text.dark.idle_color
    hover_color       mas_comfy_ui.button_text.dark.hover_color
    selected_color    mas_comfy_ui.button_text.dark.selected_color
    insensitive_color mas_comfy_ui.button_text.dark.insensitive_color
    outlines          mas_comfy_ui.button_text.dark.outlines

# Talk choice button
define gui.talk_choice_button_borders = Borders(25, 5, 25, 5)
define gui.talk_choice_button_height  = None

style talk_choice_button_text:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.common.font_size
    bold              False
    idle_color        mas_comfy_ui.button_text.light.idle_color
    hover_color       mas_comfy_ui.button_text.light.hover_color
    selected_color    mas_comfy_ui.button_text.light.selected_color
    insensitive_color mas_comfy_ui.button_text.light.insensitive_color
    outlines          mas_comfy_ui.button_text.light.outlines

# Talk choice button (dark)
define gui.talk_choice_dark_button_borders = Borders(25, 5, 25, 5)
define gui.talk_choice_dark_button_height  = None

style talk_choice_dark_button_text:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.common.font_size
    bold              False
    idle_color        mas_comfy_ui.button_text.dark.idle_color
    hover_color       mas_comfy_ui.button_text.dark.hover_color
    selected_color    mas_comfy_ui.button_text.dark.selected_color
    insensitive_color mas_comfy_ui.button_text.dark.insensitive_color
    outlines          mas_comfy_ui.button_text.dark.outlines

# Hotkey button (generic)
define gui.hkb_frame_borders = Borders(5, 5, 5, 5)
define gui.hkb_frame_height  = None

style hkb_text:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.common.font_size
    yoffset           -3
    bold              False
    idle_color        mas_comfy_ui.button_text.light.idle_color
    hover_color       mas_comfy_ui.button_text.light.hover_color
    selected_color    mas_comfy_ui.button_text.light.selected_color
    insensitive_color mas_comfy_ui.button_text.light.insensitive_color
    outlines          mas_comfy_ui.button_text.light.outlines

# Hotkey button (generic, dark)
define gui.hkb_dark_frame_borders = Borders(5, 5, 5, 5)
define gui.hkb_dark_frame_height  = None

style hkb_dark_text:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.common.font_size
    yoffset           -3
    bold              False
    idle_color        mas_comfy_ui.button_text.dark.idle_color
    hover_color       mas_comfy_ui.button_text.dark.hover_color
    selected_color    mas_comfy_ui.button_text.dark.selected_color
    insensitive_color mas_comfy_ui.button_text.dark.insensitive_color
    outlines          mas_comfy_ui.button_text.dark.outlines

# Hotkey button (active)
define gui.hkb_button_borders = Borders(5, 5, 5, 5)
define gui.hkb_button_height  = None

style hkb_button_text:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.common.font_size
    yoffset           -3
    bold              False
    idle_color        mas_comfy_ui.button_text.light.idle_color
    hover_color       mas_comfy_ui.button_text.light.hover_color
    selected_color    mas_comfy_ui.button_text.light.selected_color
    insensitive_color mas_comfy_ui.button_text.light.insensitive_color
    outlines          mas_comfy_ui.button_text.light.outlines

# Hotkey button (active, dark)
define gui.hkb_dark_button_borders = Borders(5, 5, 5, 5)
define gui.hkb_dark_button_height  = None

style hkb_dark_button_text:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.common.font_size
    yoffset           -3
    bold              False
    idle_color        mas_comfy_ui.button_text.dark.idle_color
    hover_color       mas_comfy_ui.button_text.dark.hover_color
    selected_color    mas_comfy_ui.button_text.dark.selected_color
    insensitive_color mas_comfy_ui.button_text.dark.insensitive_color
    outlines          mas_comfy_ui.button_text.dark.outlines

# Hotkey button (inactive)
define gui.hkbd_button_borders = Borders(5, 5, 5, 5)
define gui.hkbd_button_height  = None

style hkbd_button_text:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.common.font_size
    yoffset           -3
    bold              False
    idle_color        mas_comfy_ui.button_text.light.idle_color
    hover_color       mas_comfy_ui.button_text.light.hover_color
    selected_color    mas_comfy_ui.button_text.light.selected_color
    insensitive_color mas_comfy_ui.button_text.light.insensitive_color
    outlines          mas_comfy_ui.button_text.light.outlines

# Hotkey button (inactive, dark)
define gui.hkbd_dark_button_borders = Borders(5, 5, 5, 5)
define gui.hkbd_dark_button_height  = None

style hkbd_dark_button_text:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.common.font_size
    yoffset           -3
    bold              False
    idle_color        mas_comfy_ui.button_text.dark.idle_color
    hover_color       mas_comfy_ui.button_text.dark.hover_color
    selected_color    mas_comfy_ui.button_text.dark.selected_color
    insensitive_color mas_comfy_ui.button_text.dark.insensitive_color
    outlines          mas_comfy_ui.button_text.dark.outlines

# Adjustable button
define gui.mas_adjustable_button_def_borders = Borders(5, 5, 5, 5)
define gui.mas_adjustable_button_def_height  = None

style mas_adjustable_button_text_def:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.common.font_size
    bold              False
    idle_color        mas_comfy_ui.button_text.light.idle_color
    hover_color       mas_comfy_ui.button_text.light.hover_color
    selected_color    mas_comfy_ui.button_text.light.selected_color
    insensitive_color mas_comfy_ui.button_text.light.insensitive_color
    outlines          mas_comfy_ui.button_text.light.outlines

# Adjustable button (dark)
define gui.mas_adjustable_button_dark_borders = Borders(5, 5, 5, 5)
define gui.mas_adjustable_button_dark_height  = None

style mas_adjustable_button_text_dark:
    font              mas_comfy_ui.common.font
    kerning           mas_comfy_ui.common.font_kerning
    size              mas_comfy_ui.common.font_size
    bold              False
    idle_color        mas_comfy_ui.button_text.dark.idle_color
    hover_color       mas_comfy_ui.button_text.dark.hover_color
    selected_color    mas_comfy_ui.button_text.dark.selected_color
    insensitive_color mas_comfy_ui.button_text.dark.insensitive_color
    outlines          mas_comfy_ui.button_text.dark.outlines



################################################################################
# Boxes
################################################################################

# Choice box
style choice_vbox:
    spacing mas_comfy_ui.button_spacing

# Choice box (dark)
style choice_dark_vbox:
    spacing mas_comfy_ui.button_spacing

# Scrollable menu box
style scrollable_menu_vbox:
    spacing mas_comfy_ui.button_spacing

# Scrollable menu box (dark)
style scrollable_menu_dark_vbox:
    spacing mas_comfy_ui.button_spacing

# Two-pane scrollable menu box
style twopane_scrollable_menu_vbox:
    spacing mas_comfy_ui.button_spacing

# Two-pane scrollable menu box (dark)
style twopane_scrollable_menu_dark_vbox:
    spacing mas_comfy_ui.button_spacing

# Talk choice box
style talk_choice_vbox:
    spacing mas_comfy_ui.talk_button_spacing

# Talk choice box (dark)
style talk_choice_dark_vbox:
    spacing mas_comfy_ui.talk_button_spacing

# Hotkey button box
style hkb_vbox:
    spacing mas_comfy_ui.hotkey_button_spacing

# Hotkey button box (dark)
style hkb_dark_vbox:
    spacing mas_comfy_ui.hotkey_button_spacing
