label debug_menu:
    call screen debug_menu_screen

label metronome_main:
    "Che tipo di suono vuoi durante l'esercizio?"
    menu:        
        
        "Nessun suono":
            $ metronome_audio_mode = "off"
            
        "Metronomo classico (ogni battito)":
            $ metronome_audio_mode = "beat"
            
        "Loop continuo - Base":
            $ metronome_audio_mode = "loop"
            $ loop_sound_index = 1
            
        "Loop continuo - Ambient":
            $ metronome_audio_mode = "loop"
            $ loop_sound_index = 2
            
        "Loop continuo - Nature":
            $ metronome_audio_mode = "loop"
            $ loop_sound_index = 3
            
        "Suono naturale - Wow (ogni battito)":
            $ metronome_audio_mode = "natural"
            $ natural_sound_index = 1
            
        "Suono naturale - Bau (ogni battito)":
            $ metronome_audio_mode = "natural"
            $ natural_sound_index = 4

    hide screen debug_menu_screen
    scene bg room
    #show eileen happy
    #e "Metronomo base! Premi il tasto avvia quando sei pronto"
    show screen metronome_screen
    window hide  # ← NASCONDE la banda nera del dialogo
    
    pause 5.0
    while metronome_running:
        pause 0.1

    window show  # ← RIMOSTRA la dialogue window per il resto
    "Completata!"
    hide screen metronome_screen

    menu:
        "Torna al debug":
            
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
    $ metronome_audio_mode = "beat"
    #$ metronome_audio_mode = "natural"
    $ natural_sound_index = 1  # wow.mp3
    $ start_metronome()
    scene bg room
    show screen routine_screen(routine_warmup, "Warm Up")
    window hide  # ← NASCONDE la banda nera del dialogo
    
    while routine_warmup.is_running:
        pause 0.1
    $ stop_metronome()
    hide screen routine_screen
    window show  # ← RIMOSTRA la dialogue window per il resto
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
    $ metronome_audio_mode = "beat"
    #$ natural_sound_index = 1  # wow.mp3
    $ start_metronome()
    scene bg room
    show screen routine_screen_with_clock(routine_intense, "Intense")
    window hide  # ← NASCONDE la banda nera del dialogo
    
    # Ora puoi mettere pause o testo senza mostrare la window
    # e "Intense!"  ← Commentato o rimosso
    while routine_intense.is_running:
        pause 0.1
    $ stop_metronome()
    hide screen routine_screen_with_clock
    window show  # ← RIMOSTRA la dialogue window per il resto
    "Completata!"
    menu:
        "Torna al debug":
            jump debug_menu
        "Ripeti":
            jump routine_intense_page
    return



label frame_tryout:
    $ active_routine = routine_warmup
    $ routine_warmup.start()
    $ metronome_audio_mode = "beat"
    #$ metronome_audio_mode = "natural"
    $ natural_sound_index = 1  # wow.mp3
    $ start_metronome()
    scene bg room
    show screen pulsantiera(routine_warmup, "Intense")
    window hide  # ← NASCONDE la banda nera del dialogo
    
    while routine_warmup.is_running:
        pause 0.1
    $ stop_metronome()
    hide screen pulsantiera
    window show  # ← RIMOSTRA la dialogue window per il resto
    "Completata!"
    menu:
        "Torna al debug":
            jump debug_menu
        "Ripeti":
            jump frame_tryout
    return



label components_showcase:

label .loop:  # ← Punto di ripartenza
    # Stesso di sopra...
    menu:
        "Prova il gauge... ":
            call gauge_tryout
            jump .loop  # ← Dopo il return, torna al menu!
        "...e il countdown clock... ":
            call countdown_tryout
            jump .loop  # ← Dopo il return, torna al menu!
        "Screen della scheda":
            call card_tryout            
            jump .loop  # ← Dopo il return, torna al menu!
        "Screen con cornice":
            call frame_tryout
            jump .loop  # ← Dopo il return, torna al menu!
        "Clock":
            call clock_tryout            
            jump .loop  # ← Dopo il return, torna al menu!
        "ProgressMenu":
            call persolnalmenu
            jump .loop  # ← Dopo il return, torna al menu!
        "Debug menu":
            jump debug_menu


label gauge_tryout:
    # Stesso di sopra...
    show screen gauge_display_horizontal
    "Ok!"
    "Adesso lo porto al max!"
    $ metronome_bpm = 240
    "Adesso lo porto al 60!"
    $ metronome_bpm = 180
    "Adesso lo porto al 20!"
    $ metronome_bpm = 80
    "Adesso lo porto al 0!"
    $ metronome_bpm = 40
    hide screen gauge_display_horizontal
    return



label countdown_tryout:
    $ active_routine = routine_intense
    $ routine_intense.start()
    # Stesso di sopra...
    $ metronome_audio_mode = "beat"
    #$ natural_sound_index = 1  # wow.mp3
    $ start_metronome()
    show screen countdown_display(routine_intense, "Intense")
    while routine_intense.is_running:
        pause 0.1
    $ stop_metronome()
    "Ok!"
    "Adesso lo porto al max!"
    hide screen countdown_display
    return


label card_tryout:
    #$ routine_warmup_fitness.start()
    #$ start_metronome()
    scene bg room
    window hide
    show screen fancy_card  
    "Ti piace ???"
    window show
    hide screen fancy_card
    return

label clock_tryout:
    $ active_routine = routine_intense
    $ routine_intense.start()
    $ metronome_audio_mode = "beat"
    $ start_metronome()
    scene bg room
    show screen routine_screen_with_clock(routine_intense, "Intense")
    window hide  # ← NASCONDE la banda nera del dialogo
    
    # Ora puoi mettere pause o testo senza mostrare la window
    # e "Intense!"  ← Commentato o rimosso
    while routine_intense.is_running:
        pause 0.1
    $ stop_metronome()
    "Ti piace ???"
    window show
    hide screen routine_screen_with_clock
    return



# Esempio di utilizzo nel gioco
label persolnalmenu:
    # Inizializza le variabili
    scene bg girlatthebar
    
    # Mostra le barre
    show screen status_bars
    
    "Le barre sono ora visibili!"
    
    # Modifica i valori
    $ player_sissy = 120
    $ player_slut = 48
    $ player_alpha = 5
    
    "I valori sono cambiati!"
    

    # Modifica i valori
    $ player_sissy = 10
    $ player_slut = 108
    $ player_alpha = -5
    
    "I valori sono cambiati di nuovo !"

    hide screen status_bars
    
    return

# Esempio di utilizzo nel gioco
label progressmenu:
    show screen top_menus
    "Prova il menu a comparsa!"
    "Clicca i tab."
   