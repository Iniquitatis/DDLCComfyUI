################################################################################
#
# Copyright (c) 2020 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################
import json
import os

from zipfile import ZipFile

game_dir = "game"
meta_dir = os.path.join(game_dir, "comfy_meta")
config_path = os.path.join(meta_dir, "settings.json")

default_settings = {
    "selected_theme_index": 0,
    "layout": True,
    "hidpi": False,
    "installed_files": []
}

class ThemeManager:
    def __init__(self):
        self.settings = {}
        self.settings.update(default_settings)
        self.themes = []
        self._fetch_themes()
        self.load_settings()

    def disable(self):
        self._remove_current_theme()
        self.settings.update(default_settings)

    def get_current_theme(self):
        return self.themes[self.settings["selected_theme_index"]]

    def get_current_theme_name(self):
        return self.get_current_theme()["name"]

    def get_theme_count(self):
        return len(self.themes)

    def install(self):
        self._install_theme(self.get_current_theme(), self.settings["hidpi"])

    def load_settings(self):
        if not os.path.exists(config_path):
            return

        with open(config_path, "r") as file:
            self.settings.update(json.load(file))

    def save_settings(self):
        with open(config_path, "w") as file:
            json.dump(self.settings, file, indent = 4, sort_keys = False)

    def _fetch_themes(self):
        for file_path in os.listdir(meta_dir):
            file_name, extension = os.path.splitext(file_path)
            if extension == ".arc" and not file_name.endswith("_hidpi"):
                self.themes.append(self._get_theme_info(os.path.join(meta_dir, file_path),
                                                        os.path.join(meta_dir, "%s_hidpi.arc" % file_name)))

        # FIXME: there should be a better way to put the Default theme above the others
        def comparator(key):
            name = key["name"]
            if name == "Default":
                return "  %s" % name
            elif name == "Classic":
                return " %s" % name
            return name

        self.themes.sort(key = comparator)

    def _get_theme_info(self, file_path, hidpi_path):
        result = {
            "path": file_path,
            "hidpi_path": hidpi_path
        }

        with ZipFile(file_path, "r") as theme_arc:
            with theme_arc.open("info.json", "r") as info_json:
                result.update(json.load(info_json))

        return result

    def _install_theme(self, theme, hidpi=False):
        log = open(os.path.join(meta_dir, "install.log"), "w")
        theme_arc = ZipFile(theme["path"] if not hidpi else theme["hidpi_path"], "r")

        self.settings["installed_files"] = []

        for file_path in theme_arc.namelist():
            if os.path.basename(file_path) == "info.json":
                continue
            log.write("Installing %s...\n" % file_path)
            theme_arc.extract(file_path, game_dir)
            self.settings["installed_files"].append(file_path)

        if not self.settings["layout"]:
            layout_rpy = os.path.join(game_dir, "comfy_ui", "layout.rpy")
            layout_rpyc = os.path.join(game_dir, "comfy_ui", "layout.rpyc")

            if os.path.exists(layout_rpy):
                log.write("Removing %s...\n" % layout_rpy)
                os.remove(layout_rpy)

                if layout_rpy in self.settings["installed_files"]:
                    self.settings["installed_files"].remove(layout_rpy)

            if os.path.exists(layout_rpyc):
                log.write("Removing %s...\n" % layout_rpyc)
                os.remove(layout_rpyc)

        log.write("Done.\n")

        theme_arc.close()
        log.close()

    def _remove_current_theme(self):
        for file_path in self.settings["installed_files"]:
            full_path = os.path.join(game_dir, file_path)
            if os.path.exists(full_path) and not os.path.isdir(full_path):
                file_name, extension = os.path.splitext(full_path)
                os.remove(full_path)
                if extension == ".rpy":
                    os.remove("%s.rpyc" % file_name)
