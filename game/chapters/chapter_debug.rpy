label debug_menu:
    call screen debug_menu_screen

label metronome_main:
    hide screen debug_menu_screen
    scene bg room
    show eileen happy
    e "Metronomo base! Premi il tasto avvia quando sei pronto"
    show screen metronome_screen
   
    menu:
        "Torna al debug":
            hide screen metronome_screen
            jump debug_menu
        "Ripeti":
            jump metronome_main
    return

label page2a:
    scene bg room
    show screen gif_control_screen_a
    e "GIF animata!"
    menu:
        "Torna al debug":
            hide screen gif_control_screen_a
            jump debug_menu
        "Ripeti":
            jump page2a
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
            jump debug_menu
        "Ripeti":
            jump routine_warmup_page
    return

label routine_intense_page:
    # Stesso di sopra...
    $ active_routine = routine_intense
    $ routine_intense.start()
    $ start_metronome()
    scene bg room
    show screen routine_screen(routine_intense, "Intense")
    e "Intense!"
    while routine_intense.is_running:
        pause 0.1
    $ stop_metronome()
    hide screen routine_screen
    "Completata!"
    menu:
        "Torna al debug":
            jump debug_menu
        "Ripeti":
            jump routine_intense_page
    return