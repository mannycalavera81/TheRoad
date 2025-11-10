# /game/5_screens.rpy
# Tutte le screen

screen metronome_screen():
    on "show" action Function(start_metronome)
    on "hide" action Function(stop_metronome)

    vbox xalign 0.5 yalign 0.5 spacing 30:
        frame background "#222a" xpadding 50 ypadding 50:
            vbox spacing 20 xalign 0.5:
                add "metronome_anim" xalign 0.5
                text "BPM: [metronome_bpm]" xalign 0.5 size 32 color "#fff"
                if metronome_running:
                    text "Frame: [metronome_animator.current_frame]/38" size 20 color "#0f0"
                else:
                    text "FERMO" size 20 color "#f00"
                hbox spacing 20 xalign 0.5:
                    textbutton "−" action SetVariable("metronome_bpm", max(20, metronome_bpm - 5)) text_size 28
                    textbutton "+" action SetVariable("metronome_bpm", min(240, metronome_bpm + 5)) text_size 28
        hbox spacing 40 xalign 0.5:
            textbutton "Avvia" action Function(start_metronome)
            textbutton "Ferma" action Function(stop_metronome)

screen gif_control_screen_a():
    on "show" action Function(start_metronome)
    on "hide" action Function(stop_metronome)

    vbox xalign 0.5 yalign 0.5 spacing 30:
        frame background "#222a" xpadding 50 ypadding 50:
            vbox spacing 20 xalign 0.5:
                add "metronome_anim" xalign 0.5
                text "BPM: [metronome_bpm]" size 32 color "#fff"
                text "Velocità: [metronome_bpm/60.0:.2f]x" size 20 color "#aaa"
                hbox spacing 20 xalign 0.5:
                    textbutton "−" action SetVariable("metronome_bpm", max(20, metronome_bpm - 5)) text_size 28
                    textbutton "+" action SetVariable("metronome_bpm", min(240, metronome_bpm + 5)) text_size 28

screen routine_screen(routine, routine_name):
    vbox xalign 0.5 yalign 0.5 spacing 30:
        frame background "#222a" xpadding 50 ypadding 50:
            vbox spacing 20 xalign 0.5:
                text "[routine_name]" size 36 color "#ff0"
                add "routine_anim" xalign 0.5
                text "BPM: [metronome_bpm]" size 32 color "#fff"
                if routine.is_running:
                    text "Segmento [routine.current_segment + 1]/[len(routine.segments)]" size 24 color "#0ff"
                    text "Tempo segmento: [int(routine.get_time_remaining())]s" size 20 color "#0f0"
                    text "Tempo totale: [int(routine.get_total_time_remaining())]s" size 20 color "#0f0"
                else:
                    text "COMPLETATA!" size 28 color "#f00"
        hbox spacing 40 xalign 0.5:
            textbutton "Ferma" action [Function(routine.stop), Function(stop_metronome)]

screen debug_menu_screen():
    # SFONDO NERO COMPLETO (fix "cagare")
    add Solid("#000000") 
    
    modal True  # Blocca tutto sotto
    
    frame:
        xalign 0.5 yalign 0.3
        background "#222222dd"  # Scuro elegante
        padding (50, 50)
        vbox:
            spacing 30
            text "🔧 DEBUG MENU" size 50 xalign 0.5 color "#ffcc00" outlines [(3, "#000", 0, 0)]
            
            textbutton "Metronomo Base" action Jump("metronome_main") xalign 0.5
            textbutton "GIF Animata" action Jump("page2a") xalign 0.5
            textbutton "Routine Warm Up" action Jump("routine_warmup_page") xalign 0.5
            textbutton "Routine Intense" action Jump("routine_intense_page") xalign 0.5
            
            null height 40
            textbutton "ESCI DAL DEBUG" action Return() xalign 0.5  # Esce dal loop

style large_button:
    xminimum 500
    background "#333333"
    hover_background "#555555"
    padding (20, 15)