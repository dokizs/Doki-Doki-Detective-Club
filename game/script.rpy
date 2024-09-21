# Entry point
define config.developer = True

$ default_mouse = "spin"

image mouse spin:
    "gui/spin0.png"
    rotate 0.0
    linear 1.0 rotate 360.0

    # Pause so image prediction can happen.
    pause 1.0

    repeat

define config.mouse_displayable = MouseDisplayable(
    "gui/arrow.png", 0, 0).add("spin", "mouse spin", 9.9, 9.9)

label start:

    # ID of this playtrhoguh
    $ anticheat = persistent.anticheat

    # keep track of chapter
    $ chapter = 0

    # if they quit during a pause, we have to set _dismiss_pause to false again
    $ _dismiss_pause = config.developer

    # girl names
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True


    call story #story is the label.

    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
