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
define comfy_ui.common.font             = "CUI_MAIN_FONT()"
define comfy_ui.common.font_italic      = "CUI_MAIN_FONT_ITALIC()"
define comfy_ui.common.font_bold        = "CUI_MAIN_FONT_BOLD()"
define comfy_ui.common.font_bold_italic = "CUI_MAIN_FONT_BOLD_ITALIC()"
define comfy_ui.common.font_kerning     = 0.0
define comfy_ui.common.font_size        = 24

define comfy_ui.menu_font         = "CUI_MENU_FONT()"
define comfy_ui.menu_font_kerning = 0.0

define comfy_ui.menu_title.font_size      = 38
define comfy_ui.menu_title.light.color    = "CUI_SCD_COLOR(255, 255, 255)"
define comfy_ui.menu_title.light.outlines = [(6, "CUI_SCD_COLOR(187, 85, 153)", 0, 0), (3, "CUI_SCD_COLOR(187, 85, 153)", 2, 2)]
define comfy_ui.menu_title.dark.color     = "CUI_SCD_COLOR(255, 217, 232)"
define comfy_ui.menu_title.dark.outlines  = [(6, "CUI_SCD_COLOR(222, 54, 126)", 0, 0), (3, "CUI_SCD_COLOR(222, 54, 126)", 2, 2)]

define comfy_ui.menu_label.font_size      = 24
define comfy_ui.menu_label.light.color    = "CUI_SCD_COLOR(255, 255, 255)"
define comfy_ui.menu_label.light.outlines = [(3, "CUI_SCD_COLOR(187, 85, 153)", 0, 0), (1, "CUI_SCD_COLOR(187, 85, 153)", 1, 1)]
define comfy_ui.menu_label.dark.color     = "CUI_SCD_COLOR(255, 217, 232)"
define comfy_ui.menu_label.dark.outlines  = [(3, "CUI_SCD_COLOR(222, 54, 126)", 0, 0), (1, "CUI_SCD_COLOR(222, 54, 126)", 1, 1)]

define comfy_ui.menu_text.font_size      = 16
define comfy_ui.menu_text.light.color    = "CUI_SCD_COLOR(56, 56, 56)"
define comfy_ui.menu_text.light.outlines = []
define comfy_ui.menu_text.dark.color     = "CUI_SCD_COLOR(253, 91, 162)"
define comfy_ui.menu_text.dark.outlines  = []

define comfy_ui.menu_button_text.font_size                  = 24
define comfy_ui.menu_button_text.light.color                = "CUI_SCD_COLOR(255, 255, 255)"
define comfy_ui.menu_button_text.light.idle_outlines        = [(4, "CUI_SCD_COLOR(187, 85, 153)", 0, 0), (2, "CUI_SCD_COLOR(187, 85, 153)", 2, 2)]
define comfy_ui.menu_button_text.light.hover_outlines       = [(4, "CUI_SCD_COLOR(255, 170, 204)", 0, 0), (2, "CUI_SCD_COLOR(255, 170, 204)", 2, 2)]
define comfy_ui.menu_button_text.light.insensitive_outlines = [(4, "CUI_SCD_COLOR(255, 204, 238)", 0, 0), (2, "CUI_SCD_COLOR(255, 204, 238)", 2, 2)]
define comfy_ui.menu_button_text.dark.color                 = "CUI_SCD_COLOR(255, 217, 232)"
define comfy_ui.menu_button_text.dark.idle_outlines         = [(4, "CUI_SCD_COLOR(222, 54, 126)", 0, 0), (2, "CUI_SCD_COLOR(222, 54, 126)", 2, 2)]
define comfy_ui.menu_button_text.dark.hover_outlines        = [(4, "CUI_SCD_COLOR(255, 128, 183)", 0, 0), (2, "CUI_SCD_COLOR(255, 128, 183)", 2, 2)]
define comfy_ui.menu_button_text.dark.insensitive_outlines  = [(4, "CUI_SCD_COLOR(255, 178, 212)", 0, 0), (2, "CUI_SCD_COLOR(255, 178, 212)", 2, 2)]

define comfy_ui.music_menu_button_text.font                       = "mod_assets/font/mplus-2p-regular.ttf"
define comfy_ui.music_menu_button_text.font_kerning               = 0.0
define comfy_ui.music_menu_button_text.font_size                  = 24
define comfy_ui.music_menu_button_text.light.color                = "CUI_SCD_COLOR(255, 255, 255)"
define comfy_ui.music_menu_button_text.light.idle_outlines        = [(3, "CUI_SCD_COLOR(187, 85, 153)", 0, 0), (1, "CUI_SCD_COLOR(187, 85, 153)", 1, 1)]
define comfy_ui.music_menu_button_text.light.hover_outlines       = [(3, "CUI_SCD_COLOR(255, 170, 204)", 0, 0), (1, "CUI_SCD_COLOR(255, 170, 204)", 1, 1)]
define comfy_ui.music_menu_button_text.light.insensitive_outlines = [(3, "CUI_SCD_COLOR(255, 204, 238)", 0, 0), (1, "CUI_SCD_COLOR(255, 204, 238)", 1, 1)]
define comfy_ui.music_menu_button_text.dark.color                 = "CUI_SCD_COLOR(255, 217, 232)"
define comfy_ui.music_menu_button_text.dark.idle_outlines         = [(3, "CUI_SCD_COLOR(222, 54, 126)", 0, 0), (1, "CUI_SCD_COLOR(222, 54, 126)", 1, 1)]
define comfy_ui.music_menu_button_text.dark.hover_outlines        = [(3, "CUI_SCD_COLOR(255, 128, 183)", 0, 0), (1, "CUI_SCD_COLOR(255, 128, 183)", 1, 1)]
define comfy_ui.music_menu_button_text.dark.insensitive_outlines  = [(3, "CUI_SCD_COLOR(255, 178, 212)", 0, 0), (1, "CUI_SCD_COLOR(255, 178, 212)", 1, 1)]

define comfy_ui.confirm_prompt_text.light.color    = "CUI_PRM_COLOR(56, 56, 56)"
define comfy_ui.confirm_prompt_text.light.outlines = []
define comfy_ui.confirm_prompt_text.dark.color     = "CUI_PRM_COLOR(253, 91, 162)"
define comfy_ui.confirm_prompt_text.dark.outlines  = []

define comfy_ui.dialogue_text.vertical_offset = CUI_DLG_VERT_OFFSET()
define comfy_ui.dialogue_text.color           = "CUI_PRM_COLOR(248, 248, 248)"
define comfy_ui.dialogue_text.outlines        = [(2, "CUI_PRM_COLOR(48, 48, 48)", 0, 0)]

define comfy_ui.quick_button_text.font_size               = 14
define comfy_ui.quick_button_text.light.idle_color        = "CUI_SCD_COLOR(85, 34, 34)"
define comfy_ui.quick_button_text.light.hover_color       = "CUI_SCD_COLOR(255, 204, 204)"
define comfy_ui.quick_button_text.light.selected_color    = "CUI_SCD_COLOR(255, 255, 255)"
define comfy_ui.quick_button_text.light.insensitive_color = "CUI_SCD_COLOR(170, 102, 102)"
define comfy_ui.quick_button_text.light.outlines          = []
define comfy_ui.quick_button_text.dark.idle_color         = "CUI_SCD_COLOR(255, 170, 153)"
define comfy_ui.quick_button_text.dark.hover_color        = "CUI_SCD_COLOR(255, 212, 204)"
define comfy_ui.quick_button_text.dark.selected_color     = "CUI_SCD_COLOR(255, 238, 235)"
define comfy_ui.quick_button_text.dark.insensitive_color  = "CUI_SCD_COLOR(170, 102, 102)"
define comfy_ui.quick_button_text.dark.outlines           = []

define comfy_ui.button_text.light.idle_color        = "CUI_PRM_COLOR(56, 56, 56)"
define comfy_ui.button_text.light.hover_color       = "CUI_PRM_COLOR(255, 170, 153)"
define comfy_ui.button_text.light.selected_color    = "CUI_PRM_COLOR(187, 85, 136)"
define comfy_ui.button_text.light.insensitive_color = "CUI_PRM_COLOR(170, 170, 170, 127)"
define comfy_ui.button_text.light.outlines          = []
define comfy_ui.button_text.dark.idle_color         = "CUI_PRM_COLOR(253, 91, 162)"
define comfy_ui.button_text.dark.hover_color        = "CUI_PRM_COLOR(255, 171, 216)"
define comfy_ui.button_text.dark.selected_color     = "CUI_PRM_COLOR(187, 85, 136)"
define comfy_ui.button_text.dark.insensitive_color  = "CUI_PRM_COLOR(170, 170, 170, 127)"
define comfy_ui.button_text.dark.outlines           = []

define comfy_ui.option_button_text.font                    = "CUI_OPTION_FONT()"
define comfy_ui.option_button_text.font_kerning            = 0.0
define comfy_ui.option_button_text.font_size               = 24
define comfy_ui.option_button_text.light.idle_color        = "CUI_SCD_COLOR(170, 170, 170)"
define comfy_ui.option_button_text.light.hover_color       = "CUI_SCD_COLOR(204, 102, 153)"
define comfy_ui.option_button_text.light.selected_color    = "CUI_SCD_COLOR(187, 85, 136)"
define comfy_ui.option_button_text.light.insensitive_color = "CUI_SCD_COLOR(170, 170, 170, 127)"
define comfy_ui.option_button_text.dark.idle_color         = "CUI_SCD_COLOR(170, 170, 170)"
define comfy_ui.option_button_text.dark.hover_color        = "CUI_SCD_COLOR(255, 128, 183)"
define comfy_ui.option_button_text.dark.selected_color     = "CUI_SCD_COLOR(222, 54, 126)"
define comfy_ui.option_button_text.dark.insensitive_color  = "CUI_SCD_COLOR(170, 170, 170, 127)"

define comfy_ui.button_spacing        = 6
define comfy_ui.choice_button_spacing = 12
define comfy_ui.talk_button_spacing   = 16
define comfy_ui.hotkey_button_spacing = 5



################################################################################
# Init
################################################################################
init python:
    config.font_replacement_map[comfy_ui.common.font, False, True] = (comfy_ui.common.font_italic, False, False)
    config.font_replacement_map[comfy_ui.common.font, True, False] = (comfy_ui.common.font_bold, False, False)
    config.font_replacement_map[comfy_ui.common.font, True, True] = (comfy_ui.common.font_bold_italic, False, False)



################################################################################
# Labels
################################################################################

# Menu title
style game_menu_label_text:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_title.font_size
    color    comfy_ui.menu_title.light.color
    outlines comfy_ui.menu_title.light.outlines

style game_menu_label_dark_text:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_title.font_size
    color    comfy_ui.menu_title.dark.color
    outlines comfy_ui.menu_title.dark.outlines

# Preference label
style pref_def_label_text:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_label.font_size
    color    comfy_ui.menu_label.light.color
    outlines comfy_ui.menu_label.light.outlines

style pref_dark_label_text:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_label.font_size
    color    comfy_ui.menu_label.dark.color
    outlines comfy_ui.menu_label.dark.outlines

# Main menu version text
# NOTE: this style is also used for the tooltips at the bottom of the menu screen
style main_menu_version_def:
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    size     comfy_ui.menu_text.font_size
    color    comfy_ui.menu_text.light.color
    outlines comfy_ui.menu_text.light.outlines

style main_menu_version_dark:
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    size     comfy_ui.menu_text.font_size
    color    comfy_ui.menu_text.dark.color
    outlines comfy_ui.menu_text.dark.outlines

# Menu button
style navigation_button_text:
    font                 comfy_ui.menu_font
    kerning              comfy_ui.menu_font_kerning
    size                 comfy_ui.menu_button_text.font_size
    color                comfy_ui.menu_button_text.light.color
    outlines             comfy_ui.menu_button_text.light.idle_outlines
    hover_outlines       comfy_ui.menu_button_text.light.hover_outlines
    insensitive_outlines comfy_ui.menu_button_text.light.insensitive_outlines

style navigation_dark_button_text:
    font                 comfy_ui.menu_font
    kerning              comfy_ui.menu_font_kerning
    size                 comfy_ui.menu_button_text.font_size
    color                comfy_ui.menu_button_text.dark.color
    outlines             comfy_ui.menu_button_text.dark.idle_outlines
    hover_outlines       comfy_ui.menu_button_text.dark.hover_outlines
    insensitive_outlines comfy_ui.menu_button_text.dark.insensitive_outlines

# Music menu button
style music_menu_button_text:
    font                 comfy_ui.music_menu_button_text.font
    kerning              comfy_ui.music_menu_button_text.font_kerning
    size                 comfy_ui.music_menu_button_text.font_size
    color                comfy_ui.music_menu_button_text.light.color
    outlines             comfy_ui.music_menu_button_text.light.idle_outlines
    hover_outlines       comfy_ui.music_menu_button_text.light.hover_outlines
    insensitive_outlines comfy_ui.music_menu_button_text.light.insensitive_outlines

style music_menu_dark_button_text:
    font                 comfy_ui.music_menu_button_text.font
    kerning              comfy_ui.music_menu_button_text.font_kerning
    size                 comfy_ui.music_menu_button_text.font_size
    color                comfy_ui.music_menu_button_text.dark.color
    outlines             comfy_ui.music_menu_button_text.dark.idle_outlines
    hover_outlines       comfy_ui.music_menu_button_text.dark.hover_outlines
    insensitive_outlines comfy_ui.music_menu_button_text.dark.insensitive_outlines



################################################################################
# Dialogue
################################################################################

# Name
style say_label_def:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_label.font_size
    color    comfy_ui.menu_label.light.color
    outlines comfy_ui.menu_label.light.outlines

style say_label_dark:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_label.font_size
    color    comfy_ui.menu_label.dark.color
    outlines comfy_ui.menu_label.dark.outlines

# Text
style normal:
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    yoffset  comfy_ui.dialogue_text.vertical_offset
    color    comfy_ui.dialogue_text.color
    outlines comfy_ui.dialogue_text.outlines

# Quick button
style quick_button_text:
    font              comfy_ui.common.font
    kerning           comfy_ui.common.font_kerning
    size              comfy_ui.quick_button_text.font_size
    idle_color        comfy_ui.quick_button_text.light.idle_color
    hover_color       comfy_ui.quick_button_text.light.hover_color
    selected_color    comfy_ui.quick_button_text.light.selected_color
    insensitive_color comfy_ui.quick_button_text.light.insensitive_color
    outlines          comfy_ui.quick_button_text.light.outlines

style quick_dark_button_text:
    font              comfy_ui.common.font
    kerning           comfy_ui.common.font_kerning
    size              comfy_ui.quick_button_text.font_size
    idle_color        comfy_ui.quick_button_text.dark.idle_color
    hover_color       comfy_ui.quick_button_text.dark.hover_color
    selected_color    comfy_ui.quick_button_text.dark.selected_color
    insensitive_color comfy_ui.quick_button_text.dark.insensitive_color
    outlines          comfy_ui.quick_button_text.dark.outlines



################################################################################
# History
################################################################################

# Name
style history_name_text:
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    color    comfy_ui.dialogue_text.color
    outlines comfy_ui.dialogue_text.outlines

# Text
style history_text:
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    color    comfy_ui.dialogue_text.color
    outlines comfy_ui.dialogue_text.outlines



################################################################################
# Frames
################################################################################

# Frame
define gui.frame_def_borders = Borders(5, 5, 5, 5)

define gui.frame_dark_borders = Borders(5, 5, 5, 5)

# Confirm frame
define gui.confirm_frame_def_borders = Borders(5, 5, 5, 5)

define gui.confirm_frame_dark_borders = Borders(5, 5, 5, 5)

style confirm_prompt_text_def:
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    size     comfy_ui.common.font_size
    color    comfy_ui.confirm_prompt_text.light.color
    outlines comfy_ui.confirm_prompt_text.light.outlines

style confirm_prompt_text_dark:
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    size     comfy_ui.common.font_size
    color    comfy_ui.confirm_prompt_text.dark.color
    outlines comfy_ui.confirm_prompt_text.dark.outlines



################################################################################
# Containers
# NOTE: none of them can be inherited from base style for now
################################################################################

# Choice box
style choice_vbox:
    spacing comfy_ui.choice_button_spacing

style choice_dark_vbox:
    spacing comfy_ui.choice_button_spacing

# Scrollable menu box
style scrollable_menu_vbox:
    spacing comfy_ui.button_spacing

style scrollable_menu_dark_vbox:
    spacing comfy_ui.button_spacing

# Two-pane scrollable menu box
style twopane_scrollable_menu_vbox:
    spacing comfy_ui.button_spacing

style twopane_scrollable_menu_dark_vbox:
    spacing comfy_ui.button_spacing

# Talk choice box
style talk_choice_vbox:
    spacing comfy_ui.talk_button_spacing

style talk_choice_dark_vbox:
    spacing comfy_ui.talk_button_spacing

# Hotkey button box
style hkb_vbox:
    spacing comfy_ui.hotkey_button_spacing

style hkb_dark_vbox:
    spacing comfy_ui.hotkey_button_spacing



################################################################################
# Buttons
################################################################################

# Generic button
style generic_button_base:
    padding        (5, 5, 5, 5)
    hover_sound    gui.hover_sound
    activate_sound gui.activate_sound

style generic_button_lt is generic_button_base:
    background Frame("mod_assets/comfy_ui/button/[prefix_]bg_lt.png", Borders(5, 5, 5, 5))

style generic_button_dk is generic_button_base:
    background Frame("mod_assets/comfy_ui/button/[prefix_]bg_dk.png", Borders(5, 5, 5, 5))

style generic_button_text_base:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size
    align   (0.5, 0.5)

style generic_button_text_lt is generic_button_text_base:
    idle_color        comfy_ui.button_text.light.idle_color
    hover_color       comfy_ui.button_text.light.hover_color
    selected_color    comfy_ui.button_text.light.selected_color
    insensitive_color comfy_ui.button_text.light.insensitive_color
    outlines          comfy_ui.button_text.light.outlines

style generic_button_text_dk is generic_button_text_base:
    idle_color        comfy_ui.button_text.dark.idle_color
    hover_color       comfy_ui.button_text.dark.hover_color
    selected_color    comfy_ui.button_text.dark.selected_color
    insensitive_color comfy_ui.button_text.dark.insensitive_color
    outlines          comfy_ui.button_text.dark.outlines

# Generic inactive button
# FIXME: the following styles are just a bunch of hacks (mostly for "hkbd_" styles)
style generic_inactive_button_base is generic_button_base

style generic_inactive_button_lt is generic_inactive_button_base:
    background Frame("mod_assets/comfy_ui/button/insensitive_bg_lt.png", Borders(5, 5, 5, 5))

style generic_inactive_button_dk is generic_inactive_button_base:
    background Frame("mod_assets/comfy_ui/button/insensitive_bg_dk.png", Borders(5, 5, 5, 5))

style generic_inactive_button_text_base is generic_button_text_base

style generic_inactive_button_text_lt is generic_inactive_button_text_base:
    color comfy_ui.button_text.light.insensitive_color

style generic_inactive_button_text_dk is generic_inactive_button_text_base:
    color comfy_ui.button_text.dark.insensitive_color

# Choice button
style choice_button is generic_button_lt:
    clear
    xysize  (420, None)
    padding (25, 5, 25, 5)

style choice_dark_button is generic_button_dk:
    clear
    xysize  (420, None)
    padding (25, 5, 25, 5)

style choice_button_text is generic_button_text_lt:
    clear

style choice_dark_button_text is generic_button_text_dk:
    clear

# Scrollable menu button 
style scrollable_menu_button is generic_button_lt:
    clear
    xysize  (560, None)
    padding (25, 5, 25, 5)

style scrollable_menu_dark_button is generic_button_dk:
    clear
    xysize  (560, None)
    padding (25, 5, 25, 5)

style scrollable_menu_button_text is generic_button_text_lt:
    clear
    align (0.0, 0.0)

style scrollable_menu_dark_button_text is generic_button_text_dk:
    clear
    align (0.0, 0.0)

# Two-pane scrollable menu button
style twopane_scrollable_menu_button is generic_button_lt:
    clear
    xysize  (250, None)
    padding (20, 5, 20, 5)

style twopane_scrollable_menu_dark_button is generic_button_dk:
    clear
    xysize  (250, None)
    padding (20, 5, 20, 5)

style twopane_scrollable_menu_button_text is generic_button_text_lt:
    clear
    align (0.0, 0.0)

style twopane_scrollable_menu_dark_button_text is generic_button_text_dk:
    clear
    align (0.0, 0.0)

# Talk choice button
style talk_choice_button is choice_button:
    clear

style talk_choice_dark_button is choice_dark_button:
    clear

style talk_choice_button_text is choice_button_text:
    clear

style talk_choice_dark_button_text is choice_dark_button_text:
    clear

# Hotkey button (generic)
style hkb_frame is generic_button_lt:
    clear
    xysize (120, 35)

style hkb_dark_frame is generic_button_dk:
    clear
    xysize (120, 35)

style hkb_text is generic_button_text_lt:
    clear

style hkb_dark_text is generic_button_text_dk:
    clear

# Hotkey button (active)
style hkb_button is generic_button_lt:
    clear
    xysize (120, 35)

style hkb_dark_button is generic_button_dk:
    clear
    xysize (120, 35)

style hkb_button_text is generic_button_text_lt:
    clear

style hkb_dark_button_text is generic_button_text_dk:
    clear

# Hotkey button (inactive)
style hkbd_button is generic_inactive_button_lt:
    clear
    xysize (120, 35)

style hkbd_button is generic_inactive_button_dk:
    clear
    xysize (120, 35)

style hkbd_button_text is generic_inactive_button_text_lt:
    clear

style hkbd_dark_button_text is generic_inactive_button_text_dk:
    clear

# Adjustable button
style mas_adjustable_button_def is generic_button_lt:
    clear
    xysize (None, None)

style mas_adjustable_button_dark is generic_button_dk:
    clear
    xysize (None, None)

style mas_adjustable_button_text_def is generic_button_text_lt:
    clear

style mas_adjustable_button_text_dark is generic_button_text_dk:
    clear



################################################################################
# Option buttons
################################################################################

# Generic option button
style generic_option_button_base

style generic_option_button_lt is generic_option_button_base:
    foreground "gui/button/check_[prefix_]foreground.png"
    padding    (28, 4, 4, 4)

style generic_option_button_dk is generic_option_button_base:
    foreground "gui/button/check_[prefix_]foreground_d.png"
    padding    (28, 4, 4, 4)

style generic_option_button_text_base:
    font     comfy_ui.option_button_text.font
    kerning  comfy_ui.option_button_text.font_kerning
    size     comfy_ui.option_button_text.font_size
    outlines []

style generic_option_button_text_lt is generic_option_button_text_base:
    idle_color        comfy_ui.option_button_text.light.idle_color
    hover_color       comfy_ui.option_button_text.light.hover_color
    selected_color    comfy_ui.option_button_text.light.selected_color
    insensitive_color comfy_ui.option_button_text.light.insensitive_color

style generic_option_button_text_dk is generic_option_button_text_base:
    idle_color        comfy_ui.option_button_text.dark.idle_color
    hover_color       comfy_ui.option_button_text.dark.hover_color
    selected_color    comfy_ui.option_button_text.dark.selected_color
    insensitive_color comfy_ui.option_button_text.dark.insensitive_color

# Check button
style check_button is generic_option_button_lt:
    clear

style check_dark_button is generic_option_button_dk:
    clear

style check_button_text is generic_option_button_text_lt:
    clear

style check_dark_button_text is generic_option_button_text_dk:
    clear

# Radio button
style radio_button is generic_option_button_lt:
    clear

style radio_dark_button is generic_option_button_dk:
    clear

style radio_button_text is generic_option_button_text_lt:
    clear

style radio_dark_button_text is generic_option_button_text_dk:
    clear

# Outfit check button
# NOTE or FIXME: its text has different color from the standard check button
style outfit_check_button is generic_option_button_lt:
    clear

style outfit_check_dark_button is generic_option_button_dk:
    clear

style outfit_check_button_text is generic_option_button_text_lt:
    clear
    color          "#bfbfbf"
    hover_color    "#ffaa99"
    selected_color "#ffeeeb"

style outfit_check_dark_button_text is generic_option_button_text_dk:
    clear
    color          "#bfbfbf"
    hover_color    "#ffaa99"
    selected_color "#ffeeeb"
