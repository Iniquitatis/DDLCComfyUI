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
    comfy_ui.common.font_regular                 , 0x0020, 0x00ff).add( # Main
    "mod_assets/font/SourceHanSansK-Regular.otf" , 0xac00, 0xd7a3).add( # Korean
    "mod_assets/font/SourceHanSansSC-Regular.otf", 0x4e00, 0x9faf).add( # Simplified chinese
    "mod_assets/font/mplus-2p-regular.ttf"       , 0x3000, 0x4dff).add( # Japanese and others
    "gui/font/Aller_Rg.ttf"                      , 0x0000, 0xffff)      # Fallback
define comfy_ui.common.font_kerning     = CUI_MAIN_FONT_KERNING()
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
define comfy_ui.dialogue_text.line_spacing    = CUI_DLG_LINE_SPACING()
define comfy_ui.dialogue_text.color           = "CUI_PRM_COLOR(248, 248, 248)"
define comfy_ui.dialogue_text.outlines        = [(2, "CUI_PRM_COLOR(40, 40, 40)", 0, 0)]

define comfy_ui.history_name.color    = "CUI_PRM_COLOR(248, 248, 248)"
define comfy_ui.history_name.outlines = [(2, "CUI_PRM_COLOR(40, 40, 40)", 0, 0)]

define comfy_ui.history_text.color    = "CUI_PRM_COLOR(255, 255, 255)"
define comfy_ui.history_text.outlines = [(2, "CUI_PRM_COLOR(40, 40, 40)", 0, 0)]

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

define comfy_ui.scrollable_menu_button_spacing = 6
define comfy_ui.choice_button_spacing          = 12
define comfy_ui.talk_button_spacing            = 16
define comfy_ui.hotkey_button_spacing          = 5



################################################################################
# Init
################################################################################
init python:
    config.font_replacement_map[comfy_ui.common.font_regular, False, True] = (comfy_ui.common.font_italic, False, False)
    config.font_replacement_map[comfy_ui.common.font_regular, True, False] = (comfy_ui.common.font_bold, False, False)
    config.font_replacement_map[comfy_ui.common.font_regular, True, True] = (comfy_ui.common.font_bold_italic, False, False)



################################################################################
# Definitions
# FIXME: eventually all this stuff needs to be removed
################################################################################
define gui.default_font                           = comfy_ui.common.font
define mas_ui.light_button_text_idle_color        = comfy_ui.button_text.light.idle_color
define mas_ui.light_button_text_hover_color       = comfy_ui.button_text.light.hover_color
define mas_ui.light_button_text_insensitive_color = comfy_ui.button_text.light.insensitive_color
define mas_ui.dark_button_text_idle_color         = comfy_ui.button_text.dark.idle_color
define mas_ui.dark_button_text_hover_color        = comfy_ui.button_text.dark.hover_color
define mas_ui.dark_button_text_insensitive_color  = comfy_ui.button_text.dark.insensitive_color



################################################################################
# Generic styles
################################################################################

# Button
style generic_button_base:
    padding        (5, 5, 5, 5)
    hover_sound    gui.hover_sound
    activate_sound gui.activate_sound

style generic_button_lt is generic_button_base:
    background Frame(Transform("comfy_ui/button/[prefix_]bg_lt.png", zoom=CUI_SCALE_INV()), Borders(5, 5, 5, 5))

style generic_button_dk is generic_button_base:
    background Frame(Transform("comfy_ui/button/[prefix_]bg_dk.png", zoom=CUI_SCALE_INV()), Borders(5, 5, 5, 5))

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

# Option button
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

# Scrollbars
style generic_horizontal_scrollbar_base:
    ysize        18
    unscrollable "hide"
    bar_invert   True

style generic_horizontal_scrollbar_lt is generic_horizontal_scrollbar_base:
    base_bar Frame(Transform("comfy_ui/scrollbar/horizontal_bar_lt.png", zoom=CUI_SCALE_INV()))
    thumb    Frame(Transform("comfy_ui/scrollbar/horizontal_[prefix_]thumb_lt.png", zoom=CUI_SCALE_INV()), Borders(6, 6, 6, 6))

style generic_horizontal_scrollbar_dk is generic_horizontal_scrollbar_base:
    base_bar Frame(Transform("comfy_ui/scrollbar/horizontal_bar_dk.png", zoom=CUI_SCALE_INV()))
    thumb    Frame(Transform("comfy_ui/scrollbar/horizontal_[prefix_]thumb_dk.png", zoom=CUI_SCALE_INV()), Borders(6, 6, 6, 6))

style generic_vertical_scrollbar_base:
    xsize        18
    unscrollable "hide"
    bar_vertical True
    bar_invert   True

style generic_vertical_scrollbar_lt is generic_vertical_scrollbar_base:
    base_bar Frame(Transform("comfy_ui/scrollbar/vertical_bar_lt.png", zoom=CUI_SCALE_INV()))
    thumb    Frame(Transform("comfy_ui/scrollbar/vertical_[prefix_]thumb_lt.png", zoom=CUI_SCALE_INV()), Borders(6, 6, 6, 6))

style generic_vertical_scrollbar_dk is generic_vertical_scrollbar_base:
    base_bar Frame(Transform("comfy_ui/scrollbar/vertical_bar_dk.png", zoom=CUI_SCALE_INV()))
    thumb    Frame(Transform("comfy_ui/scrollbar/vertical_[prefix_]thumb_dk.png", zoom=CUI_SCALE_INV()), Borders(6, 6, 6, 6))



################################################################################
# Option buttons
################################################################################

# Check button
style check_button is generic_option_button_lt:
    clear

style check_button_dark is generic_option_button_dk:
    clear

style check_button_text is generic_option_button_text_lt:
    clear

style check_button_text_dark is generic_option_button_text_dk:
    clear

# Radio button
style radio_button is generic_option_button_lt:
    clear

style radio_button_dark is generic_option_button_dk:
    clear

style radio_button_text is generic_option_button_text_lt:
    clear

style radio_button_text_dark is generic_option_button_text_dk:
    clear

# Outfit check button
# NOTE or FIXME: its text has different color from the standard check button
style outfit_check_button is generic_option_button_lt:
    clear

style outfit_check_button_dark is generic_option_button_dk:
    clear

style outfit_check_button_text is generic_option_button_text_lt:
    clear
    color          "#bfbfbf"
    hover_color    "#ffaa99"
    selected_color "#ffeeeb"

style outfit_check_button_text_dark is generic_option_button_text_dk:
    clear
    color          "#bfbfbf"
    hover_color    "#ffaa99"
    selected_color "#ffeeeb"



################################################################################
# Bars
################################################################################

# Classroom vertical scrollbar
style classroom_vscrollbar is generic_vertical_scrollbar_lt:
    clear

style classroom_vscrollbar_dark is generic_vertical_scrollbar_dk:
    clear

# Selector vertical scrollbar
style mas_selector_sidebar_vbar is generic_vertical_scrollbar_lt:
    clear

style mas_selector_sidebar_vbar_dark is generic_vertical_scrollbar_dk:
    clear



################################################################################
# Game menu
################################################################################

# Images
image menu_bg:
    topleft
    ConditionSwitch(
        "not mas_globals.dark_mode", Transform("gui/menu_bg.png", zoom=CUI_SCALE_INV()),
        "mas_globals.dark_mode", Transform("gui/menu_bg_d.png", zoom=CUI_SCALE_INV()))
    menu_bg_move

image game_menu_bg:
    topleft
    ConditionSwitch(
        "not mas_globals.dark_mode", Transform("gui/menu_bg.png", zoom=CUI_SCALE_INV()),
        "mas_globals.dark_mode", Transform("gui/menu_bg_d.png", zoom=CUI_SCALE_INV()))
    menu_bg_loop

image menu_nav:
    ConditionSwitch(
        "not mas_globals.dark_mode", Transform("gui/overlay/main_menu.png", zoom=CUI_SCALE_INV()),
        "mas_globals.dark_mode", Transform("gui/overlay/main_menu_d.png", zoom=CUI_SCALE_INV()))
    menu_nav_move

# Frame
style game_menu_outer_frame:
    background Transform("gui/overlay/game_menu.png", zoom=CUI_SCALE_INV())

style game_menu_outer_frame_dark:
    background Transform("gui/overlay/game_menu_d.png", zoom=CUI_SCALE_INV())

# Title
style game_menu_label_text:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_title.font_size
    color    comfy_ui.menu_title.light.color
    outlines comfy_ui.menu_title.light.outlines

style game_menu_label_text_dark:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_title.font_size
    color    comfy_ui.menu_title.dark.color
    outlines comfy_ui.menu_title.dark.outlines

# Preference label
style pref_label_text:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_label.font_size
    color    comfy_ui.menu_label.light.color
    outlines comfy_ui.menu_label.light.outlines

style pref_label_text_dark:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_label.font_size
    color    comfy_ui.menu_label.dark.color
    outlines comfy_ui.menu_label.dark.outlines

# Version text
# NOTE: this style is also used for the tooltips at the bottom of the menu screen
style main_menu_version:
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

style navigation_button_text_dark:
    font                 comfy_ui.menu_font
    kerning              comfy_ui.menu_font_kerning
    size                 comfy_ui.menu_button_text.font_size
    color                comfy_ui.menu_button_text.dark.color
    outlines             comfy_ui.menu_button_text.dark.idle_outlines
    hover_outlines       comfy_ui.menu_button_text.dark.hover_outlines
    insensitive_outlines comfy_ui.menu_button_text.dark.insensitive_outlines

# File menu
style page_label_text:
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    color    comfy_ui.menu_text.light.color
    outlines comfy_ui.menu_text.light.outlines

style page_label_text_dark:
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    color    comfy_ui.menu_text.dark.color
    outlines comfy_ui.menu_text.dark.outlines

style slot_time_text is generic_button_text_lt:
    size 16

style slot_time_text_dark is generic_button_text_dk:
    size 16

style slot_name_text is generic_button_text_lt:
    size 16

style slot_name_text_dark is generic_button_text_dk:
    size 16

style page_button_text is generic_button_text_lt

style page_button_text_dark is generic_button_text_dk



################################################################################
# Music menu
################################################################################

# Frame
style music_menu_outer_frame:
    background Transform("mod_assets/music_menu.png", zoom=CUI_SCALE_INV())

style music_menu_outer_frame_dark:
    background Transform("mod_assets/music_menu_d.png", zoom=CUI_SCALE_INV())

# Music menu button
style music_menu_button_text:
    font                 comfy_ui.music_menu_button_text.font
    kerning              comfy_ui.music_menu_button_text.font_kerning
    size                 comfy_ui.music_menu_button_text.font_size
    color                comfy_ui.music_menu_button_text.light.color
    outlines             comfy_ui.music_menu_button_text.light.idle_outlines
    hover_outlines       comfy_ui.music_menu_button_text.light.hover_outlines
    insensitive_outlines comfy_ui.music_menu_button_text.light.insensitive_outlines

style music_menu_button_text_dark:
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

# Name box
style namebox:
    background Frame(Transform("gui/namebox.png", zoom=CUI_SCALE_INV()), gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)

style namebox_dark:
    background Frame(Transform("gui/namebox_d.png", zoom=CUI_SCALE_INV()), gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)

# Box
style window:
    background Transform(Image("gui/textbox.png", xalign=0.5, yalign=1.0), zoom=CUI_SCALE_INV())

style window_dark:
    background Transform(Image("gui/textbox_d.png", xalign=0.5, yalign=1.0), zoom=CUI_SCALE_INV())

style window_monika:
    background Transform(Image("gui/textbox_monika.png", xalign=0.5, yalign=1.0), zoom=CUI_SCALE_INV())

style window_monika_dark:
    background Transform(Image("gui/textbox_monika_d.png", xalign=0.5, yalign=1.0), zoom=CUI_SCALE_INV())

# Name
style say_label:
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
    font         comfy_ui.common.font
    kerning      comfy_ui.common.font_kerning
    yoffset      comfy_ui.dialogue_text.vertical_offset
    line_spacing comfy_ui.dialogue_text.line_spacing
    color        comfy_ui.dialogue_text.color
    outlines     comfy_ui.dialogue_text.outlines

# CTC
image ctc:
    xalign 0.81
    yalign 0.98
    xoffset -5
    alpha 0.0
    subpixel True
    Transform("gui/ctc.png", zoom=CUI_SCALE_INV())
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat

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

style quick_button_text_dark:
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
    xpos     0
    ypos     5
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    size     comfy_ui.common.font_size
    bold     True
    color    comfy_ui.history_name.color
    outlines comfy_ui.history_name.outlines

# Text
style history_text:
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

style frame:
    background Frame(Transform("gui/frame.png", zoom=CUI_SCALE_INV()), gui.frame_borders, tile=gui.frame_tile)
    padding    gui.frame_borders.padding

style frame_dark:
    background Frame(Transform("gui/frame_d.png", zoom=CUI_SCALE_INV()), gui.frame_borders, tile=gui.frame_tile)
    padding    gui.frame_borders.padding

# Confirm frame
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)

style confirm_frame:
    background Frame(Transform("gui/frame.png", zoom=CUI_SCALE_INV()), gui.confirm_frame_borders, tile=gui.frame_tile)
    padding    gui.confirm_frame_borders.padding

style confirm_frame_dark:
    background Frame(Transform("gui/frame_d.png", zoom=CUI_SCALE_INV()), gui.confirm_frame_borders, tile=gui.frame_tile)
    padding    gui.confirm_frame_borders.padding

style confirm_prompt_text:
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
# Choice menu
################################################################################
style choice_vbox:
    spacing comfy_ui.choice_button_spacing

style choice_button is generic_button_lt:
    clear
    xysize  (420, None)
    padding (25, 5, 25, 5)

style choice_button_dark is generic_button_dk:
    clear
    xysize  (420, None)
    padding (25, 5, 25, 5)

style choice_button_text is generic_button_text_lt:
    clear

style choice_button_text_dark is generic_button_text_dk:
    clear



################################################################################
# Scrollable menu
################################################################################
style scrollable_menu_vbox:
    spacing comfy_ui.scrollable_menu_button_spacing

style scrollable_menu_button is generic_button_lt:
    clear
    xysize  (560, None)
    padding (25, 5, 25, 5)

style scrollable_menu_button_dark is generic_button_dk:
    clear
    xysize  (560, None)
    padding (25, 5, 25, 5)

style scrollable_menu_button_text is generic_button_text_lt:
    clear
    align (0.0, 0.0)

style scrollable_menu_button_text_dark is generic_button_text_dk:
    clear
    align (0.0, 0.0)



################################################################################
# Two-pane scrollable menu
################################################################################
style twopane_scrollable_menu_vbox:
    spacing comfy_ui.scrollable_menu_button_spacing

style twopane_scrollable_menu_button is generic_button_lt:
    clear
    xysize  (250, None)
    padding (20, 5, 20, 5)

style twopane_scrollable_menu_button_dark is generic_button_dk:
    clear
    xysize  (250, None)
    padding (20, 5, 20, 5)

style twopane_scrollable_menu_button_text is generic_button_text_lt:
    clear
    align (0.0, 0.0)

style twopane_scrollable_menu_button_text_dark is generic_button_text_dk:
    clear
    align (0.0, 0.0)



################################################################################
# Talk choice menu
################################################################################
style talk_choice_vbox:
    spacing comfy_ui.talk_button_spacing

style talk_choice_button is choice_button:
    clear

style talk_choice_button_dark is choice_button_dark:
    clear

style talk_choice_button_text is choice_button_text:
    clear

style talk_choice_button_text_dark is choice_button_text_dark:
    clear



################################################################################
# Hotkey button menu
################################################################################
style hkb_vbox:
    spacing comfy_ui.hotkey_button_spacing

style hkb_button is generic_button_lt:
    clear
    xysize (120, 35)

style hkb_button_dark is generic_button_dk:
    clear
    xysize (120, 35)

style hkb_button_text is generic_button_text_lt:
    clear

style hkb_button_text_dark is generic_button_text_dk:
    clear



################################################################################
# Island buttons
################################################################################
style island_hbox:
    spacing 5

style island_button is generic_button_lt:
    xysize (205, 35)

style island_button_dark is generic_button_dk:
    xysize (205, 35)

style island_button_text is generic_button_text_lt

style island_button_text_dark is generic_button_text_dk



################################################################################
# Extras menu
################################################################################
style mas_extra_menu_frame:
    background Frame("mod_assets/frames/trans_pink2pxborder100.png", Borders(5, 5, 5, 5, pad_top=2, pad_bottom=4))

style mas_extra_menu_frame_dark:
    background Frame("mod_assets/frames/trans_pink2pxborder100_d.png", Borders(5, 5, 5, 5, pad_top=2, pad_bottom=4))

style mas_extra_menu_label_text:
    color "#f8f8f8"

style mas_extra_menu_label_text_dark:
    color comfy_ui.button_text.dark.idle_color

style mas_adjust_vbar:
    xsize        18
    base_bar     Frame(Transform("comfy_ui/scrollbar/vertical_bar_lt.png", zoom=CUI_SCALE_INV()), Borders(4, 4, 4, 4))
    thumb        Transform("comfy_ui/slider/vertical_[prefix_]thumb_lt.png", zoom=CUI_SCALE_INV())
    bar_vertical True

style mas_adjust_vbar_dark:
    xsize        18
    base_bar     Frame(Transform("comfy_ui/scrollbar/vertical_bar_dk.png", zoom=CUI_SCALE_INV()), Borders(4, 4, 4, 4))
    thumb        Transform("comfy_ui/slider/vertical_[prefix_]thumb_dk.png", zoom=CUI_SCALE_INV())
    bar_vertical True

style mas_adjustable_button is generic_button_lt:
    clear
    xysize (None, None)

style mas_adjustable_button_dark is generic_button_dk:
    clear
    xysize (None, None)

style mas_adjustable_button_text is generic_button_text_lt:
    clear

style mas_adjustable_button_text_dark is generic_button_text_dk:
    clear
