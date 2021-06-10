################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################

# MASFIX: monkey patch for selector image buttons
init 999 python in comfy_ui.selector:
    from renpy.display.im import Image
    from renpy.display.imagelike import Borders, Frame
    from renpy.display.transform import Transform
    from store import MASSelectableImageButtonDisplayable, mas_getTimeFile

    old_init = MASSelectableImageButtonDisplayable.__init__

    def monkey_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)

        self.thumb_overlay = Image(mas_getTimeFile("mod_assets/frames/selector_overlay.png"))
        self.thumb_overlay_locked = Image(mas_getTimeFile("mod_assets/frames/selector_overlay_disabled.png"))
        self.hover_overlay = Image(mas_getTimeFile("mod_assets/frames/selector_overlay_hover.png"))
        self.top_frame = Frame(mas_getTimeFile("mod_assets/frames/selector_top_frame.png"), Borders(10, 10, 10, 10))
        self.top_frame_selected = Frame(mas_getTimeFile("mod_assets/frames/selector_top_frame_selected.png"), Borders(10, 10, 10, 10))
        self.top_frame_locked = Frame(mas_getTimeFile("mod_assets/frames/selector_top_frame_disabled.png"), Borders(10, 10, 10, 10))

    def monkey_render_bottom_frame(self, hover, st, at):
        thumb = Transform(self.thumb, pos = (3, 3), crop = (3, 3, self.WIDTH - 6, self.SELECTOR_HEIGHT - 6))
        thumb_render = renpy.Render(self.WIDTH, self.SELECTOR_HEIGHT)
        thumb_render.place(thumb)

        renders = [thumb_render]

        if hover:
            renders.append(self._render_bottom_frame_piece(self.hover_overlay, st, at))
        else:
            renders.append(self._render_bottom_frame_piece(self.thumb_overlay, st, at))

        return renders

    MASSelectableImageButtonDisplayable.__init__ = monkey_init
    MASSelectableImageButtonDisplayable._render_bottom_frame = monkey_render_bottom_frame

# MASFIX: broken layout in the clothing/hairstyle selector
screen comfy_ui_selector_fix:
    frame:
        area (1075, 50, 200, sel_frame_vsize - 45)
        background Frame(store.mas_ui.sel_sb_frame, Borders(10, 10, 10, 10))
        ypadding 10

        vbox:
            xsize 200
            xalign 0.5
            spacing 5

            viewport id "sidebar_scroll":
                mousewheel True
                arrowkeys True

                vbox:
                    xsize 200
                    spacing 10

                    if remover is not None:
                        add remover:
                            xalign 0.5

                    for selectable in flt_items:
                        add selectable:
                            xalign 0.5

            null height 5

            if mailbox.read_outfit_checkbox_visible():
                $ ocb_checked = mailbox.read_outfit_checkbox_checked()

                textbutton _("Outfit Mode"):
                    style "generic_fancy_check_button"
                    xsize 200
                    activate_sound gui.activate_sound
                    action [
                        ToggleField(persistent, "_mas_setting_ocb"),
                        Function(
                            mailbox.send_outfit_checkbox_checked,
                            not ocb_checked
                        )
                    ]
                    selected ocb_checked

        vbar value YScrollValue("sidebar_scroll"):
            style "mas_selector_sidebar_vbar"
            xoffset -25
            # NOTE: compensating the frame padding
            yoffset -10
            ysize (sel_frame_vsize - 45)

    vbox:
        style_prefix "hkb"
        xpos 1115
        yanchor 1.0
        ypos 715

        if mailbox.read_conf_enable():
            textbutton _("Confirm") action Jump(confirm)
        else:
            textbutton _("Confirm")

        if mailbox.read_restore_enable():
            textbutton _("Restore") action Jump(restore)
        else:
            textbutton _("Restore")

        textbutton _("Cancel") action Jump(cancel)

init 999 python:
    screens = renpy.display.screen.screens
    screens[("mas_selector_sidebar", None)].ast.children[2].keyword[4] = (
        "background", "Frame('mod_assets/frames/search_bar.png', Borders(5, 5, 5, 5))"
    )
    screens[("mas_selector_sidebar", None)].ast.children[3] = screens[("comfy_ui_selector_fix", None)].ast.children[0]
    screens[("mas_selector_sidebar", None)].ast.children.append(screens[("comfy_ui_selector_fix", None)].ast.children[1])
