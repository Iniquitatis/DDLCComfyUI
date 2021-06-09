################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################
screen comfy_ui_islands_event_button_fix:
    hbox:
        xalign 0.96
        yalign 0.98

        # MASFIX: using ToggleVariable turns normal button into a "checkbox"
        if _mas_island_window_open:
            textbutton "Close Window" action SetVariable("_mas_island_window_open", False)
        else:
            textbutton "Open Window" action SetVariable("_mas_island_window_open", True)

        textbutton "Go Back" action Return(False)

init 999 python:
    screens = renpy.display.screen.screens
    screens[("mas_show_islands", None)].ast.children[2] = screens[("comfy_ui_islands_event_button_fix", None)].ast.children[0]
