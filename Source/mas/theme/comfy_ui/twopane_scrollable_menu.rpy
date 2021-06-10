################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################
init 999 python:
    # MASFIX: replace basic search bar Solid() by an actual image
    screens = renpy.display.screen.screens
    screens[("twopane_scrollable_menu", None)].ast.children[3].keyword[4] = (
        "background", "Frame('mod_assets/frames/search_bar.png', Borders(5, 5, 5, 5))"
    )
