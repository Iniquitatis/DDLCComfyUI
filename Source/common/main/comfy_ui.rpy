################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################
label comfy_ui_apply:
    $ comfy_ui.theme_mgr.install()
    $ comfy_ui.theme_mgr.save_settings()
    $ renpy.quit()

label comfy_ui_disable:
    $ comfy_ui.theme_mgr.disable()
    $ comfy_ui.theme_mgr.save_settings()
    $ renpy.quit()

screen comfy_ui_ddlc_settings_pane():
    vbox:
        xfill True
        xpos 370
        ypos 515

        use comfy_ui_settings_pane("comfy_ui_apply", "comfy_ui_disable")

# HACK: append the settings pane right to the preferences screen AST
init 999 python:
    screens = renpy.display.screen.screens
    screens[("preferences", None)].ast.children.append(screens[("comfy_ui_ddlc_settings_pane", None)].ast.children[0])
