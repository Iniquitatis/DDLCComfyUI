################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################
init -1 python in comfy_ui:
    from comfy_ui import ThemeManager

    theme_mgr = ThemeManager()

default presistent.comfy_ui_show_preview = False

label comfy_ui_glitch:
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    hide screen tear
    stop sound

screen comfy_ui_settings_pane(apply_label, disable_label):
    $ theme_count = comfy_ui.theme_mgr.get_theme_count()

    if theme_count > 0:
        $ theme_name = comfy_ui.theme_mgr.get_current_theme_name()
        $ theme_preview = comfy_ui.theme_mgr.get_current_theme_preview()

        hbox:
            vbox:
                xmaximum 350

                hbox:
                    xfill True

                    label _("Theme: [theme_name]"):
                        style "slider_label"

                    textbutton _("Preview"):
                        style "check_button"
                        xalign 1.0
                        ypos 15
                        action ToggleField(persistent, "comfy_ui_show_preview")

                bar:
                    style "slider_slider"
                    value DictValue(
                        comfy_ui.theme_mgr.settings,
                        "selected_theme_index",
                        range = theme_count - 1
                    )

                grid 3 1:
                    xfill True

                    textbutton _("Fonts"):
                        style "check_button"
                        action ToggleDict(comfy_ui.theme_mgr.settings, "use_fonts")

                    textbutton _("Layout"):
                        style "check_button"
                        action ToggleDict(comfy_ui.theme_mgr.settings, "use_layout")

                    textbutton _("HiDPI"):
                        style "check_button"
                        action ToggleDict(comfy_ui.theme_mgr.settings, "use_hidpi")

                null height 10

                hbox:
                    $ glitch_chance = 1.0 / 400.0
                    $ glitch_action = Jump("comfy_ui_glitch")

                    $ apply_glitched = renpy.random.random() < glitch_chance
                    $ apply_name = _("Apply") if not apply_glitched else glitchtext(10)
                    $ apply_width = 100 if not apply_glitched else 150
                    $ apply_action = Show(screen = "dialog", message = "The game will be restarted.", ok_action = Jump(apply_label))

                    $ disable_glitched = renpy.random.random() < glitch_chance
                    $ disable_name = _("Disable") if not disable_glitched else glitchtext(10)
                    $ disable_width = 100 if not disable_glitched else 150
                    $ disable_action = Show(screen = "dialog", message = "The game will be restarted.", ok_action = Jump(disable_label))

                    textbutton apply_name:
                        style "navigation_button"
                        xsize apply_width
                        action If(apply_glitched, glitch_action, apply_action)

                    textbutton disable_name:
                        style "navigation_button"
                        xsize disable_width
                        action If(disable_glitched, glitch_action, disable_action)

            if persistent.comfy_ui_show_preview:
                add theme_preview:
                    xpos 10
                    ypos 20

    else:
        label _("No themes available.")
