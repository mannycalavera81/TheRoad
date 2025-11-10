label metronome_main:
    scene bg room
    show eileen happy
    show screen metronome_screen
    e "Metronomo base!"
    menu:
        "Torna al debug":
            hide screen metronome_screen
            return  # Torna a call screen → LOOP!
        "Vai GIF":
            hide screen metronome_screen
            jump page2a
    return

label page2a:
    scene bg room
    show screen gif_control_screen_a
    e "GIF animata!"
    menu:
        "Torna al debug":
            hide screen gif_control_screen_a
            return
        "Metronomo":
            hide screen gif_control_screen_a
            jump metronome_main
    return

label routine_warmup_page:
    $ active_routine = routine_warmup
    $ routine_warmup.start()
    $ start_metronome()
    scene bg room
    show screen routine_screen(routine_warmup, "Warm Up")
    e "Warm Up!"
    while routine_warmup.is_running:
        pause 0.1
    $ stop_metronome()
    hide screen routine_screen
    "Completata!"
    menu:
        "Torna al debug":
            return
        "Ripeti":
            jump routine_warmup_page
    return

label routine_intense_page:
    # Stesso di sopra...
    menu:
        "Torna al debug":
            return
        "Ripeti":
            jump routine_intense_page
    return