################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################
init -990 python in mas_submod_utils:
    Submod(
        author          = "Dominus Iniquitatis",
        name            = "Comfy UI",
        description     = "Smooth and customizable UI add-on.",
        version         = "2.0.1",
        dependencies    = {},
        settings_pane   = "comfy_ui_mas_settings_pane",
        version_updates = {}
    )

label comfy_ui_apply:
    $ persistent.closed_self = True
    $ comfy_ui.theme_mgr.install()
    $ comfy_ui.theme_mgr.save_settings()
    $ renpy.quit()

label comfy_ui_disable:
    $ persistent.closed_self = True
    $ comfy_ui.theme_mgr.disable()
    $ comfy_ui.theme_mgr.save_settings()
    $ renpy.quit()

screen comfy_ui_mas_settings_pane():
    vbox:
        xfill True
        ypos 10

        use comfy_ui_settings_pane("comfy_ui_apply", "comfy_ui_disable")
