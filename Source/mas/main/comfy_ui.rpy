################################################################################
#
# Copyright (c) 2020 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################

################################################################################
# Submod initialization
################################################################################
init -990 python in mas_submod_utils:
    Submod(
        author          = "Dominus Iniquitatis",
        name            = "Comfy UI",
        description     = "Smooth and customizable UI add-on.",
        version         = "1.2.0",
        dependencies    = {},
        settings_pane   = "comfy_ui_settings_pane",
        version_updates = {}
    )

################################################################################
# Common module
################################################################################
init -1 python in comfy_ui:
    from comfy_ui import ThemeManager

    theme_mgr = ThemeManager()

################################################################################
# Settings pane
################################################################################
label comfy_ui_apply:
    call screen mas_generic_restart
    $ persistent.closed_self = True
    $ comfy_ui.theme_mgr.install()
    $ comfy_ui.theme_mgr.save_settings()
    jump _quit

label comfy_ui_disable:
    call screen mas_generic_restart
    $ persistent.closed_self = True
    $ comfy_ui.theme_mgr.disable()
    $ comfy_ui.theme_mgr.save_settings()
    jump _quit

screen comfy_ui_settings_pane():
    vbox:
        xfill True
        ypos 10

        $ theme_count = comfy_ui.theme_mgr.get_theme_count()

        if theme_count > 0:
            $ theme_name = comfy_ui.theme_mgr.get_current_theme_name()

            vbox:
                xmaximum 300

                label _("Theme: [theme_name]"):
                    style "slider_label"

                bar:
                    style "slider_slider"
                    value DictValue(
                        comfy_ui.theme_mgr.settings,
                        "selected_theme_index",
                        range = theme_count - 1
                    )

                textbutton _("HiDPI"):
                    style "check_button"
                    action ToggleDict(comfy_ui.theme_mgr.settings, "hidpi")

            null height 10

            hbox:
                textbutton _("Apply"):
                    style "navigation_button"
                    xsize 100
                    action Jump("comfy_ui_apply")

                textbutton _("Disable"):
                    style "navigation_button"
                    xsize 100
                    action Jump("comfy_ui_disable")
        else:
            label _("No themes available.")
