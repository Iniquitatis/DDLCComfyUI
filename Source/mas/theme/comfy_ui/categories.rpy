################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################
label comfy_ui_category_fix:
    python:
        unlocked_events = Event.filterEvents(
            evhand.event_database,
            unlocked = True,
            pool = pool,
            aff = mas_curr_affection,
            flag_ban = EV_FLAG_HFM
        )

        main_cat_list = list()
        no_cat_list = list()

        for key in unlocked_events:
            event = unlocked_events[key]

            if event.category:
                evhand.addIfNew(event.category, main_cat_list)
            else:
                no_cat_list.append(event)

        main_cat_list.sort()
        no_cat_list.sort(key = Event.getSortPrompt)

        # MASFIX: map category IDs to the actual human-readable names
        cat_names = {
            "ddlc": "DDLC",
        }
        dis_cat_list = [(cat_names.get(x, x.capitalize()) + "...", x) for x in main_cat_list]

        no_cat_list = [(x.prompt, x.eventlabel) for x in no_cat_list]

        dis_cat_list.extend(no_cat_list)

        cat_lists.append(evhand._NT_CAT_PANE(dis_cat_list, main_cat_list))

init 999 python:
    namemap = renpy.game.script.namemap
    namemap["prompts_categories"].block[4].code = namemap["comfy_ui_category_fix"].block[0].code
