################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################

# HACK: monkey patch for handling an image scaling/replacement
init -999 python in comfy_ui:
    import os

    from renpy.display.im import Image
    from renpy.display.transform import Transform

    def monkey_new(cls, filename = "", **properties):
        has_replacement = os.path.exists(os.path.join("game", "comfy_ui", "replacers", filename))
        is_comfy_asset = filename.startswith("comfy_ui") or has_replacement

        if has_replacement:
            filename = "comfy_ui/replacers/%s" % filename

        new_instance = super(Image, cls).__new__(cls, filename, **properties)
        new_instance.__init__(filename, **properties)

        if is_comfy_asset:
            return Transform(new_instance, zoom = CUI_SCALE_INV())

        return new_instance

    Image.__new__ = staticmethod(monkey_new)
