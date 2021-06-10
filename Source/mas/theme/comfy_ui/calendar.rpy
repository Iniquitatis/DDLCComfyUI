################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################

# MASFIX: monkey patch for calendar close button
init 999 python in comfy_ui.calendar:
    from renpy.text.text import Text
    from store import MASCalendar

    old_init = MASCalendar.__init__

    def monkey_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)

        empty_text = Text("")

        btn = self.button_exit
        btn._button_states = {k: (empty_text, v[1]) for k, v in btn._button_states.items()}

    MASCalendar.__init__ = monkey_init
