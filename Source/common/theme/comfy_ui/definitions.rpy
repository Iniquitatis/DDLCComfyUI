################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
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

define comfy_ui.button.height_adjustment = CUI_BTN_HEIGHT_ADJUSTMENT()

define comfy_ui.button_text.vertical_offset   = CUI_BTN_TEXT_VERT_OFFSET()
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

define comfy_ui.poem_game_text.color          = "CUI_PRM_COLOR(56, 56, 56)"
define comfy_ui.poem_game_text.outlines       = []
define comfy_ui.poem_game_text.hover_outlines = [(3, "CUI_PRM_COLOR(255, 238, 255)", 0, 0), (2, "CUI_PRM_COLOR(255, 204, 255)", 0, 0), (1, "CUI_PRM_COLOR(255, 170, 255)", 0, 0)]

define comfy_ui.choice_button_spacing = 22

define comfy_ui.input_caret_color = "CUI_SCD_COLOR(187, 85, 153)"
