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
init -2 python in comfy_ui:
    import json
    import os

    from zipfile import ZipFile

    game_dir = "game"
    meta_dir = os.path.join(game_dir, "comfy_meta")
    config_path = os.path.join(meta_dir, "settings.json")

    themes = []
    settings = {
        "selected_theme_index": 0,
        "hidpi": False,
        "installed_files": []
    }

    def disable():
        for file_path in settings["installed_files"]:
            full_path = os.path.join(game_dir, file_path)
            if os.path.exists(full_path) and not os.path.isdir(full_path):
                file_name, extension = os.path.splitext(full_path)
                os.remove(full_path)
                if extension == ".rpy":
                    os.remove("%s.rpyc" % file_name)

        settings["selected_theme_index"] = 0
        settings["hidpi"] = False
        settings["installed_files"] = []

    def get_current_theme():
        return themes[settings["selected_theme_index"]]

    def get_current_theme_name():
        return get_current_theme()["name"]

    def get_theme_count():
        return len(themes)

    def initialize():
        _fetch_themes()
        load_settings()

    def install():
        _install_theme(get_current_theme(), settings["hidpi"])

    def load_settings():
        if not os.path.exists(config_path):
            return

        with open(config_path, "r") as file:
            settings.update(json.load(file))

    def save_settings():
        with open(config_path, "w") as file:
            json.dump(settings, file, indent=4, sort_keys=False)

    def _fetch_themes():
        for file_path in os.listdir(meta_dir):
            file_name, extension = os.path.splitext(file_path)
            if extension == ".arc" and not file_name.endswith("_hidpi"):
                themes.append(_get_theme_info(os.path.join(meta_dir, file_path),
                                              os.path.join(meta_dir, "%s_hidpi.arc" % file_name)))

        themes.sort(cmp=lambda x, y: cmp(x["name"], y["name"]))

    def _get_theme_info(file_path, hidpi_path):
        result = {
            "path": file_path,
            "hidpi_path": hidpi_path
        }

        with ZipFile(file_path, "r") as theme_arc:
            with theme_arc.open("info.json", "r") as info_json:
                result.update(json.load(info_json))

        return result

    def _install_theme(theme, hidpi = False):
        log = open(os.path.join(meta_dir, "install.log"), "w")
        theme_arc = ZipFile(theme["path"] if not hidpi else theme["hidpi_path"], "r")

        settings["installed_files"] = []

        for file_path in theme_arc.namelist():
            if os.path.basename(file_path) == "info.json":
                continue
            log.write("Installing %s...\n" % file_path)
            theme_arc.extract(file_path, game_dir)
            settings["installed_files"].append(file_path)

        log.write("Done.\n")

        theme_arc.close()
        log.close()

init -1 python:
    comfy_ui.initialize()

################################################################################
# Settings pane
################################################################################
label comfy_ui_apply:
    call screen mas_generic_restart
    $ persistent.closed_self = True
    $ comfy_ui.install()
    $ comfy_ui.save_settings()
    jump _quit

label comfy_ui_disable:
    call screen mas_generic_restart
    $ persistent.closed_self = True
    $ comfy_ui.disable()
    $ comfy_ui.save_settings()
    jump _quit

screen comfy_ui_settings_pane():
    vbox:
        xfill True
        ypos 10

        $ theme_count = comfy_ui.get_theme_count()

        if theme_count > 0:
            $ theme_name = comfy_ui.get_current_theme_name()

            vbox:
                xmaximum 300

                label _("Theme: [theme_name]"):
                    style "slider_label"

                bar:
                    style "slider_slider"
                    value DictValue(
                        comfy_ui.settings,
                        "selected_theme_index",
                        range=theme_count - 1
                    )

                textbutton _("HiDPI"):
                    style "check_button"
                    action ToggleDict(comfy_ui.settings, "hidpi")

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
