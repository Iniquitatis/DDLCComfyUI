################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################

################################################################################
# Common module
################################################################################
init -1 python in comfy_ui:
    from comfy_ui import ThemeManager

    theme_mgr = ThemeManager()

default presistent.comfy_ui_show_preview = False

################################################################################
# Settings pane
################################################################################
label comfy_ui_apply:
    $ persistent.closed_self = True
    $ comfy_ui.theme_mgr.install()
    $ comfy_ui.theme_mgr.save_settings()
    jump _quit

label comfy_ui_disable:
    $ persistent.closed_self = True
    $ comfy_ui.theme_mgr.disable()
    $ comfy_ui.theme_mgr.save_settings()
    jump _quit

screen comfy_ui_settings_pane():
    vbox:
        xfill True
        xpos 370
        ypos 515

        $ theme_count = comfy_ui.theme_mgr.get_theme_count()

        if theme_count > 0:
            $ theme_name = comfy_ui.theme_mgr.get_current_theme_name()
            $ theme_preview = comfy_ui.theme_mgr.get_current_theme_preview()

            hbox:
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

                    hbox:
                        textbutton _("Fonts"):
                            style "check_button"
                            action ToggleDict(comfy_ui.theme_mgr.settings, "use_fonts")

                        textbutton _("Layout"):
                            style "check_button"
                            action ToggleDict(comfy_ui.theme_mgr.settings, "use_layout")

                        textbutton _("HiDPI"):
                            style "check_button"
                            action ToggleDict(comfy_ui.theme_mgr.settings, "use_hidpi")

                        null width 10

                        textbutton _("Preview"):
                            style "check_button"
                            action ToggleField(persistent, "comfy_ui_show_preview")

                    null height 10

                    hbox:
                        textbutton _("Apply"):
                            style "navigation_button"
                            xsize 100
                            action Show(screen = "dialog", message = "The game will be restarted.", ok_action = Jump("comfy_ui_apply"))

                        textbutton _("Disable"):
                            style "navigation_button"
                            xsize 100
                            action Show(screen = "dialog", message = "The game will be restarted.", ok_action = Jump("comfy_ui_disable"))

                if persistent.comfy_ui_show_preview:
                    null width 10

                    add theme_preview ypos 20
        else:
            label _("No themes available.")

# HACK: append the settings pane right to the preferences screen AST
init 999 python:
    screens = renpy.display.screen.screens
    screens[("preferences", None)].ast.children.append(screens[("comfy_ui_settings_pane", None)].ast.children[0])
