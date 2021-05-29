################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################

################################################################################
# Init
################################################################################
init python:
    config.font_replacement_map[comfy_ui.common.font_regular, False, True] = (comfy_ui.common.font_italic, False, False)
    config.font_replacement_map[comfy_ui.common.font_regular, True, False] = (comfy_ui.common.font_bold, False, False)
    config.font_replacement_map[comfy_ui.common.font_regular, True, True] = (comfy_ui.common.font_bold_italic, False, False)



################################################################################
# Definitions
################################################################################
define gui.default_font = comfy_ui.common.font
