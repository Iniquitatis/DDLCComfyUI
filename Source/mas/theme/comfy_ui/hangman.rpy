################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################
init 999 transform hangman_board:
    xanchor 0
    yanchor 0
    xpos 675
    ypos 100
    alpha 1.0

init 999 transform hangman_hangman:
    xanchor 0
    yanchor 0
    # MASFIX: hangman sensitive mode image
    xpos (880 if not persistent._mas_sensitive_mode else 836)
    ypos 125

init 999 python in mas_hangman:
    WORD_FONT = "mod_assets/font/m1_fixed.ttf"
    WORD_SIZE = 36
    WORD_COLOR = "#202020"
    WORD_COLOR_GET = "#000000"
