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
define mas_comfy_ui.font = "mod_assets/font/Nunito-SemiBold.ttf"
define mas_comfy_ui.font_size = gui.text_size
define mas_comfy_ui.dialogue_text_color = "#f8f8f8"
define mas_comfy_ui.dialogue_text_outlines = [(2, "#444444", 0, 0)]
define mas_comfy_ui.button_text_idle_color = "#484848"
define mas_comfy_ui.button_text_outlines = []
define mas_comfy_ui.button_spacing = 6
define mas_comfy_ui.talk_button_spacing = 12
define mas_comfy_ui.hotkey_button_spacing = -4



################################################################################
# Dialogue
################################################################################

# Text
style normal:
    font mas_comfy_ui.font
    yoffset -3
    color mas_comfy_ui.dialogue_text_color
    outlines mas_comfy_ui.dialogue_text_outlines

# Quick button
style quick_button_text:
    font mas_comfy_ui.font

# Quick button (dark)
style quick_dark_button_text:
    font mas_comfy_ui.font



################################################################################
# History
################################################################################

# Name
style history_name_text:
    font mas_comfy_ui.font

# Text
style history_text:
    font mas_comfy_ui.font



################################################################################
# Buttons
################################################################################

# Choice button
define gui.choice_button_borders = Borders(25, 5, 25, 5)
define gui.choice_button_height = None

style choice_button_text:
    font mas_comfy_ui.font
    size mas_comfy_ui.font_size
    bold False
    idle_color mas_comfy_ui.button_text_idle_color
    outlines mas_comfy_ui.button_text_outlines

# Choice button (dark)
define gui.choice_dark_button_borders = Borders(25, 5, 25, 5)
define gui.choice_dark_button_height = None

style choice_dark_button_text:
    font mas_comfy_ui.font
    size mas_comfy_ui.font_size
    bold False
    outlines mas_comfy_ui.button_text_outlines

# Scrollable menu button
define gui.scrollable_menu_button_borders = Borders(25, 5, 25, 5)
define gui.scrollable_menu_button_height = None

style scrollable_menu_button_text:
    font mas_comfy_ui.font
    size mas_comfy_ui.font_size
    bold False
    idle_color mas_comfy_ui.button_text_idle_color
    outlines mas_comfy_ui.button_text_outlines

# Scrollable menu button (dark)
define gui.scrollable_menu_dark_button_borders = Borders(25, 5, 25, 5)
define gui.scrollable_menu_dark_button_height = None

style scrollable_menu_dark_button_text:
    font mas_comfy_ui.font
    size mas_comfy_ui.font_size
    bold False
    outlines mas_comfy_ui.button_text_outlines

# Two-pane scrollable menu button
define gui.twopane_scrollable_menu_button_borders = Borders(25, 5, 25, 5)
define gui.twopane_scrollable_menu_button_height = None

style twopane_scrollable_menu_button_text:
    font mas_comfy_ui.font
    size mas_comfy_ui.font_size
    bold False
    idle_color mas_comfy_ui.button_text_idle_color
    outlines mas_comfy_ui.button_text_outlines

# Two-pane scrollable menu button (dark)
define gui.twopane_scrollable_menu_dark_button_borders = Borders(25, 5, 25, 5)
define gui.twopane_scrollable_menu_dark_button_height = None

style twopane_scrollable_menu_dark_button_text:
    font mas_comfy_ui.font
    size mas_comfy_ui.font_size
    bold False
    outlines mas_comfy_ui.button_text_outlines

# Two-pane scrollable menu special button
define gui.twopane_scrollable_menu_special_button_borders = Borders(25, 5, 25, 5)
define gui.twopane_scrollable_menu_special_button_height = None

style twopane_scrollable_menu_special_button_text:
    font mas_comfy_ui.font
    size mas_comfy_ui.font_size
    bold False
    idle_color mas_comfy_ui.button_text_idle_color
    outlines mas_comfy_ui.button_text_outlines

# Two-pane scrollable menu special button (dark)
define gui.twopane_scrollable_menu_dark_special_button_borders = Borders(25, 5, 25, 5)
define gui.twopane_scrollable_menu_dark_special_button_height = None

style twopane_scrollable_menu_dark_special_button_text:
    font mas_comfy_ui.font
    size mas_comfy_ui.font_size
    bold False
    outlines mas_comfy_ui.button_text_outlines

# Talk choice button
define gui.talk_choice_button_borders = Borders(25, 5, 25, 5)
define gui.talk_choice_button_height = None

style talk_choice_button_text:
    font mas_comfy_ui.font
    size mas_comfy_ui.font_size
    bold False
    idle_color mas_comfy_ui.button_text_idle_color
    outlines mas_comfy_ui.button_text_outlines

# Talk choice button (dark)
define gui.talk_choice_dark_button_borders = Borders(25, 5, 25, 5)
define gui.talk_choice_dark_button_height = None

style talk_choice_dark_button_text:
    font mas_comfy_ui.font
    size mas_comfy_ui.font_size
    bold False
    outlines mas_comfy_ui.button_text_outlines

# Hotkey button (generic)
define gui.hkb_frame_borders = Borders(5, 5, 5, 5)
define gui.hkb_frame_height = None

style hkb_text:
    font mas_comfy_ui.font
    size mas_comfy_ui.font_size
    yoffset -3
    bold False
    outlines mas_comfy_ui.button_text_outlines

# Hotkey button (generic, dark)
define gui.hkb_dark_frame_borders = Borders(5, 5, 5, 5)
define gui.hkb_dark_frame_height = None

style hkb_dark_text:
    font mas_comfy_ui.font
    size mas_comfy_ui.font_size
    yoffset -3
    bold False
    outlines mas_comfy_ui.button_text_outlines

# Hotkey button (active)
define gui.hkb_button_borders = Borders(5, 5, 5, 5)
define gui.hkb_button_height = None

style hkb_button_text:
    font mas_comfy_ui.font
    size mas_comfy_ui.font_size
    yoffset -3
    bold False
    idle_color mas_comfy_ui.button_text_idle_color
    outlines mas_comfy_ui.button_text_outlines

# Hotkey button (active, dark)
define gui.hkb_dark_button_borders = Borders(5, 5, 5, 5)
define gui.hkb_dark_button_height = None

style hkb_dark_button_text:
    font mas_comfy_ui.font
    size mas_comfy_ui.font_size
    yoffset -3
    bold False
    outlines mas_comfy_ui.button_text_outlines

# Hotkey button (inactive)
define gui.hkbd_button_borders = Borders(5, 5, 5, 5)
define gui.hkbd_button_height = None

style hkbd_button_text:
    font mas_comfy_ui.font
    size mas_comfy_ui.font_size
    yoffset -3
    bold False
    outlines mas_comfy_ui.button_text_outlines

# Hotkey button (inactive, dark)
define gui.hkbd_dark_button_borders = Borders(5, 5, 5, 5)
define gui.hkbd_dark_button_height = None

style hkbd_dark_button_text:
    font mas_comfy_ui.font
    size mas_comfy_ui.font_size
    yoffset -3
    bold False
    outlines mas_comfy_ui.button_text_outlines



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
