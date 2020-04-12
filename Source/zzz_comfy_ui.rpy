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
define mas_comfy_ui.font         = "mod_assets/font/Nunito-SemiBold.ttf"
define mas_comfy_ui.font_bold    = "mod_assets/font/Nunito-Bold.ttf"
define mas_comfy_ui.font_italic  = "mod_assets/font/Nunito-SemiBoldItalic.ttf"
define mas_comfy_ui.font_size    = gui.text_size
define mas_comfy_ui.font_kerning = 0.0

define mas_comfy_ui.dialogue_text_color    = "#f8f8f8"
define mas_comfy_ui.dialogue_text_outlines = [(2, "#404040", 0, 0)]

define mas_comfy_ui.light.quick_button_text_idle_color        = "#522"
define mas_comfy_ui.light.quick_button_text_hover_color       = "#fcc"
define mas_comfy_ui.light.quick_button_text_selected_color    = "#ffffff"
define mas_comfy_ui.light.quick_button_text_insensitive_color = "#a66"
define mas_comfy_ui.light.quick_button_text_outlines          = []

define mas_comfy_ui.dark.quick_button_text_idle_color        = "#ffaa99"
define mas_comfy_ui.dark.quick_button_text_hover_color       = "#ffd4cc"
define mas_comfy_ui.dark.quick_button_text_selected_color    = "#ffeeeb"
define mas_comfy_ui.dark.quick_button_text_insensitive_color = "#a66"
define mas_comfy_ui.dark.quick_button_text_outlines          = []

define mas_comfy_ui.light.button_text_idle_color        = "#404040"
define mas_comfy_ui.light.button_text_hover_color       = "#fa9"
define mas_comfy_ui.light.button_text_selected_color    = "#bb5588"
define mas_comfy_ui.light.button_text_insensitive_color = "#aaaaaa7f"
define mas_comfy_ui.light.button_text_outlines          = []

define mas_comfy_ui.dark.button_text_idle_color        = "#fd5ba2"
define mas_comfy_ui.dark.button_text_hover_color       = "#ffabd8"
define mas_comfy_ui.dark.button_text_selected_color    = "#bb5588"
define mas_comfy_ui.dark.button_text_insensitive_color = "#aaaaaa7f"
define mas_comfy_ui.dark.button_text_outlines          = []

define mas_comfy_ui.button_spacing        = 6
define mas_comfy_ui.talk_button_spacing   = 13
define mas_comfy_ui.hotkey_button_spacing = -4



################################################################################
# Init
################################################################################
init python:
    config.font_replacement_map[mas_comfy_ui.font, True, False] = (mas_comfy_ui.font_bold, False, False)
    config.font_replacement_map[mas_comfy_ui.font, False, True] = (mas_comfy_ui.font_italic, False, False)



################################################################################
# Dialogue
################################################################################

# Text
style normal:
    font     mas_comfy_ui.font
    kerning  mas_comfy_ui.font_kerning
    yoffset  -3
    color    mas_comfy_ui.dialogue_text_color
    outlines mas_comfy_ui.dialogue_text_outlines

# Quick button
style quick_button_text:
    font              mas_comfy_ui.font
    kerning           mas_comfy_ui.font_kerning
    idle_color        mas_comfy_ui.light.quick_button_text_idle_color
    hover_color       mas_comfy_ui.light.quick_button_text_hover_color
    selected_color    mas_comfy_ui.light.quick_button_text_selected_color
    insensitive_color mas_comfy_ui.light.quick_button_text_insensitive_color
    outlines          mas_comfy_ui.light.quick_button_text_outlines

# Quick button (dark)
style quick_dark_button_text:
    font              mas_comfy_ui.font
    kerning           mas_comfy_ui.font_kerning
    idle_color        mas_comfy_ui.dark.quick_button_text_idle_color
    hover_color       mas_comfy_ui.dark.quick_button_text_hover_color
    selected_color    mas_comfy_ui.dark.quick_button_text_selected_color
    insensitive_color mas_comfy_ui.dark.quick_button_text_insensitive_color
    outlines          mas_comfy_ui.dark.quick_button_text_outlines



################################################################################
# History
################################################################################

# Name
style history_name_text:
    font     mas_comfy_ui.font
    kerning  mas_comfy_ui.font_kerning
    color    mas_comfy_ui.dialogue_text_color
    outlines mas_comfy_ui.dialogue_text_outlines

# Text
style history_text:
    font     mas_comfy_ui.font
    kerning  mas_comfy_ui.font_kerning
    color    mas_comfy_ui.dialogue_text_color
    outlines mas_comfy_ui.dialogue_text_outlines



################################################################################
# Buttons
################################################################################

# Choice button
define gui.choice_button_borders = Borders(25, 5, 25, 5)
define gui.choice_button_height  = None

style choice_button_text:
    font              mas_comfy_ui.font
    size              mas_comfy_ui.font_size
    kerning           mas_comfy_ui.font_kerning
    bold              False
    idle_color        mas_comfy_ui.light.button_text_idle_color
    hover_color       mas_comfy_ui.light.button_text_hover_color
    selected_color    mas_comfy_ui.light.button_text_selected_color
    insensitive_color mas_comfy_ui.light.button_text_insensitive_color
    outlines          mas_comfy_ui.light.button_text_outlines

# Choice button (dark)
define gui.choice_dark_button_borders = Borders(25, 5, 25, 5)
define gui.choice_dark_button_height  = None

style choice_dark_button_text:
    font              mas_comfy_ui.font
    size              mas_comfy_ui.font_size
    kerning           mas_comfy_ui.font_kerning
    bold              False
    idle_color        mas_comfy_ui.dark.button_text_idle_color
    hover_color       mas_comfy_ui.dark.button_text_hover_color
    selected_color    mas_comfy_ui.dark.button_text_selected_color
    insensitive_color mas_comfy_ui.dark.button_text_insensitive_color
    outlines          mas_comfy_ui.dark.button_text_outlines

# Scrollable menu button
define gui.scrollable_menu_button_borders = Borders(25, 5, 25, 5)
define gui.scrollable_menu_button_height  = None

style scrollable_menu_button_text:
    font              mas_comfy_ui.font
    size              mas_comfy_ui.font_size
    kerning           mas_comfy_ui.font_kerning
    bold              False
    idle_color        mas_comfy_ui.light.button_text_idle_color
    hover_color       mas_comfy_ui.light.button_text_hover_color
    selected_color    mas_comfy_ui.light.button_text_selected_color
    insensitive_color mas_comfy_ui.light.button_text_insensitive_color
    outlines          mas_comfy_ui.light.button_text_outlines

# Scrollable menu button (dark)
define gui.scrollable_menu_dark_button_borders = Borders(25, 5, 25, 5)
define gui.scrollable_menu_dark_button_height  = None

style scrollable_menu_dark_button_text:
    font              mas_comfy_ui.font
    size              mas_comfy_ui.font_size
    kerning           mas_comfy_ui.font_kerning
    bold              False
    idle_color        mas_comfy_ui.dark.button_text_idle_color
    hover_color       mas_comfy_ui.dark.button_text_hover_color
    selected_color    mas_comfy_ui.dark.button_text_selected_color
    insensitive_color mas_comfy_ui.dark.button_text_insensitive_color
    outlines          mas_comfy_ui.dark.button_text_outlines

# Two-pane scrollable menu button
define gui.twopane_scrollable_menu_button_borders = Borders(25, 5, 25, 5)
define gui.twopane_scrollable_menu_button_height  = None

style twopane_scrollable_menu_button_text:
    font              mas_comfy_ui.font
    size              mas_comfy_ui.font_size
    kerning           mas_comfy_ui.font_kerning
    bold              False
    idle_color        mas_comfy_ui.light.button_text_idle_color
    hover_color       mas_comfy_ui.light.button_text_hover_color
    selected_color    mas_comfy_ui.light.button_text_selected_color
    insensitive_color mas_comfy_ui.light.button_text_insensitive_color
    outlines          mas_comfy_ui.light.button_text_outlines

# Two-pane scrollable menu button (dark)
define gui.twopane_scrollable_menu_dark_button_borders = Borders(25, 5, 25, 5)
define gui.twopane_scrollable_menu_dark_button_height  = None

style twopane_scrollable_menu_dark_button_text:
    font              mas_comfy_ui.font
    size              mas_comfy_ui.font_size
    kerning           mas_comfy_ui.font_kerning
    bold              False
    idle_color        mas_comfy_ui.dark.button_text_idle_color
    hover_color       mas_comfy_ui.dark.button_text_hover_color
    selected_color    mas_comfy_ui.dark.button_text_selected_color
    insensitive_color mas_comfy_ui.dark.button_text_insensitive_color
    outlines          mas_comfy_ui.dark.button_text_outlines

# Two-pane scrollable menu special button
define gui.twopane_scrollable_menu_special_button_borders = Borders(25, 5, 25, 5)
define gui.twopane_scrollable_menu_special_button_height  = None

style twopane_scrollable_menu_special_button_text:
    font              mas_comfy_ui.font
    size              mas_comfy_ui.font_size
    kerning           mas_comfy_ui.font_kerning
    bold              False
    idle_color        mas_comfy_ui.light.button_text_idle_color
    hover_color       mas_comfy_ui.light.button_text_hover_color
    selected_color    mas_comfy_ui.light.button_text_selected_color
    insensitive_color mas_comfy_ui.light.button_text_insensitive_color
    outlines          mas_comfy_ui.light.button_text_outlines

# Two-pane scrollable menu special button (dark)
define gui.twopane_scrollable_menu_dark_special_button_borders = Borders(25, 5, 25, 5)
define gui.twopane_scrollable_menu_dark_special_button_height  = None

style twopane_scrollable_menu_dark_special_button_text:
    font              mas_comfy_ui.font
    size              mas_comfy_ui.font_size
    kerning           mas_comfy_ui.font_kerning
    bold              False
    idle_color        mas_comfy_ui.dark.button_text_idle_color
    hover_color       mas_comfy_ui.dark.button_text_hover_color
    selected_color    mas_comfy_ui.dark.button_text_selected_color
    insensitive_color mas_comfy_ui.dark.button_text_insensitive_color
    outlines          mas_comfy_ui.dark.button_text_outlines

# Talk choice button
define gui.talk_choice_button_borders = Borders(25, 5, 25, 5)
define gui.talk_choice_button_height  = None

style talk_choice_button_text:
    font              mas_comfy_ui.font
    size              mas_comfy_ui.font_size
    kerning           mas_comfy_ui.font_kerning
    bold              False
    idle_color        mas_comfy_ui.light.button_text_idle_color
    hover_color       mas_comfy_ui.light.button_text_hover_color
    selected_color    mas_comfy_ui.light.button_text_selected_color
    insensitive_color mas_comfy_ui.light.button_text_insensitive_color
    outlines          mas_comfy_ui.light.button_text_outlines

# Talk choice button (dark)
define gui.talk_choice_dark_button_borders = Borders(25, 5, 25, 5)
define gui.talk_choice_dark_button_height  = None

style talk_choice_dark_button_text:
    font              mas_comfy_ui.font
    size              mas_comfy_ui.font_size
    kerning           mas_comfy_ui.font_kerning
    bold              False
    idle_color        mas_comfy_ui.dark.button_text_idle_color
    hover_color       mas_comfy_ui.dark.button_text_hover_color
    selected_color    mas_comfy_ui.dark.button_text_selected_color
    insensitive_color mas_comfy_ui.dark.button_text_insensitive_color
    outlines          mas_comfy_ui.dark.button_text_outlines

# Hotkey button (generic)
define gui.hkb_frame_borders = Borders(5, 5, 5, 5)
define gui.hkb_frame_height  = None

style hkb_text:
    font              mas_comfy_ui.font
    size              mas_comfy_ui.font_size
    kerning           mas_comfy_ui.font_kerning
    yoffset           -3
    bold              False
    idle_color        mas_comfy_ui.light.button_text_idle_color
    hover_color       mas_comfy_ui.light.button_text_hover_color
    selected_color    mas_comfy_ui.light.button_text_selected_color
    insensitive_color mas_comfy_ui.light.button_text_insensitive_color
    outlines          mas_comfy_ui.light.button_text_outlines

# Hotkey button (generic, dark)
define gui.hkb_dark_frame_borders = Borders(5, 5, 5, 5)
define gui.hkb_dark_frame_height  = None

style hkb_dark_text:
    font              mas_comfy_ui.font
    size              mas_comfy_ui.font_size
    kerning           mas_comfy_ui.font_kerning
    yoffset           -3
    bold              False
    idle_color        mas_comfy_ui.dark.button_text_idle_color
    hover_color       mas_comfy_ui.dark.button_text_hover_color
    selected_color    mas_comfy_ui.dark.button_text_selected_color
    insensitive_color mas_comfy_ui.dark.button_text_insensitive_color
    outlines          mas_comfy_ui.dark.button_text_outlines

# Hotkey button (active)
define gui.hkb_button_borders = Borders(5, 5, 5, 5)
define gui.hkb_button_height  = None

style hkb_button_text:
    font              mas_comfy_ui.font
    size              mas_comfy_ui.font_size
    kerning           mas_comfy_ui.font_kerning
    yoffset           -3
    bold              False
    idle_color        mas_comfy_ui.light.button_text_idle_color
    hover_color       mas_comfy_ui.light.button_text_hover_color
    selected_color    mas_comfy_ui.light.button_text_selected_color
    insensitive_color mas_comfy_ui.light.button_text_insensitive_color
    outlines          mas_comfy_ui.light.button_text_outlines

# Hotkey button (active, dark)
define gui.hkb_dark_button_borders = Borders(5, 5, 5, 5)
define gui.hkb_dark_button_height  = None

style hkb_dark_button_text:
    font              mas_comfy_ui.font
    size              mas_comfy_ui.font_size
    kerning           mas_comfy_ui.font_kerning
    yoffset           -3
    bold              False
    idle_color        mas_comfy_ui.dark.button_text_idle_color
    hover_color       mas_comfy_ui.dark.button_text_hover_color
    selected_color    mas_comfy_ui.dark.button_text_selected_color
    insensitive_color mas_comfy_ui.dark.button_text_insensitive_color
    outlines          mas_comfy_ui.dark.button_text_outlines

# Hotkey button (inactive)
define gui.hkbd_button_borders = Borders(5, 5, 5, 5)
define gui.hkbd_button_height  = None

style hkbd_button_text:
    font              mas_comfy_ui.font
    size              mas_comfy_ui.font_size
    kerning           mas_comfy_ui.font_kerning
    yoffset           -3
    bold              False
    idle_color        mas_comfy_ui.light.button_text_idle_color
    hover_color       mas_comfy_ui.light.button_text_hover_color
    selected_color    mas_comfy_ui.light.button_text_selected_color
    insensitive_color mas_comfy_ui.light.button_text_insensitive_color
    outlines          mas_comfy_ui.light.button_text_outlines

# Hotkey button (inactive, dark)
define gui.hkbd_dark_button_borders = Borders(5, 5, 5, 5)
define gui.hkbd_dark_button_height  = None

style hkbd_dark_button_text:
    font              mas_comfy_ui.font
    size              mas_comfy_ui.font_size
    kerning           mas_comfy_ui.font_kerning
    yoffset           -3
    bold              False
    idle_color        mas_comfy_ui.dark.button_text_idle_color
    hover_color       mas_comfy_ui.dark.button_text_hover_color
    selected_color    mas_comfy_ui.dark.button_text_selected_color
    insensitive_color mas_comfy_ui.dark.button_text_insensitive_color
    outlines          mas_comfy_ui.dark.button_text_outlines



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
