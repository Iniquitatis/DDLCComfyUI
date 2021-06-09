################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################
init 999 transform hangman_hangman:
    xanchor 0
    yanchor 0
    # MASFIX: hangman sensitive mode image
    xpos (880 if not persistent._mas_sensitive_mode else 836)
    ypos 125
