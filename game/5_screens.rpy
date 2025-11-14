# /game/5_screens.rpy
# Tutte le screen

screen metronome_screen():
    #on "show" action Function(start_metronome)
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
        padding [50, 50, 50, 50]
        vbox:
            spacing 30
            text "🔧 DEBUG MENU" size 50 xalign 0.5 color "#ffcc00" outlines [(3, "#000", 0, 0)]
            
            textbutton "Metronomo Base" action Jump("metronome_main") xalign 0.5
            textbutton "GIF Animata" action Jump("page2a") xalign 0.5
            textbutton "Routine Warm Up" action Jump("routine_warmup_page") xalign 0.5
            textbutton "Routine Intense" action Jump("routine_intense_page") xalign 0.5
            
            null height 40
            textbutton "ESCI DAL DEBUG" action Jump("start") xalign 0.5  # Esce dal loop



screen routine_screen_fitness(routine, title):
    frame:
        xalign 0.5 yalign 0.1
        background "#000000aa"
        padding [20, 20, 20, 20]
        text "[title] - Esercizio [routine.current+1]/[len(routine.exercises)]" size 28 color "#ffcc00"

    if routine.is_running:
        $ ex = routine.exercises[routine.current]
        frame:
            xalign 0.5 yalign 0.5
            background None
            text "[ex[0]]" size 40 color "#ffffff"
            text "[ex[1]] secondi" size 32 color "#00ff00"



screen gauge_display():
    fixed:
        xysize (200, 115)  # Riduco anche il fixed
        add Solid("#ff0000", xysize=(200, 115))
        
        add Transform("gauge_arc_red.png", rotate=180) xalign 0.5 ypos -5
        add Transform("gauge_arc_yellow.png", rotate=180) xalign 0.5 ypos -5
        add Transform("gauge_arc_green.png", rotate=180) xalign 0.5 ypos -5
        add Transform("gauge_marks.png", rotate=90) xalign 0.5 ypos -5
        add Solid("#502c2d", xysize=(20, 20)) xalign 0.5 ypos 85
        add Transform("lancetta.png", rotate=(player_fuel * 13.5), anchor=(0.5, 0.5)) xpos 100 ypos 95
        text "[player_fuel]" size 20 bold True color "#ecf0f1" xalign 0.5 ypos 110

screen stats_sidebar_narrow():
    tag stats_screen
    zorder 100
    
    frame:
        xalign 0.0
        yalign 0.0
        xsize 250
        ysize 1080
        padding (15, 20)
        background "#2c3e50e6"
        
        vbox:
            spacing 15
            
            text "STATISTICHE" style "stats_title"
            null height 10
            
            hbox:
                spacing 5
                text "Nome:" style "stats_label"
                text "[player_name]" style "stats_value"
            
            hbox:
                spacing 5
                text "Livello:" style "stats_label"
                text "[player_level]" style "stats_value"
            
            null height 15
            
            vbox:
                spacing 5
                text "Salute" style "stats_label"
                hbox:
                    spacing 10
                    bar value player_hp range 100 xsize 180 ysize 20
                    text "[player_hp]/100" style "stats_value_small"
            
            vbox:
                spacing 5
                text "Energia" style "stats_label"
                hbox:
                    spacing 10
                    bar value player_energy range 100 xsize 180 ysize 20
                    text "[player_energy]/100" style "stats_value_small"
            
            null height 15
            
            vbox:
                spacing 0
                text "Benzina" style "stats_label"
                use gauge_display
            
            null height 15
            
            text "ATTRIBUTI" style "stats_subtitle"
            
            hbox:
                spacing 5
                text "Forza:" style "stats_label"
                text "[player_strength]" style "stats_value"
            
            hbox:
                spacing 5
                text "Intelligenza:" style "stats_label"
                text "[player_intelligence]" style "stats_value"
            
            hbox:
                spacing 5
                text "Carisma:" style "stats_label"
                text "[player_charisma]" style "stats_value"
            
            null height 15
            
            hbox:
                spacing 5
                text "Denaro:" style "stats_label"
                text "[player_money]$" style "stats_value_gold"


# ==================================================
# VERSIONE 2: PANNELLO LATERALE LARGO (640px)
# ==================================================

screen stats_sidebar_wide():
    tag stats_screen
    zorder 100
    
    frame:
        xalign 0.0
        yalign 0.0
        xsize 640
        ysize 1080
        padding (30, 40)
        background "#2c3e50e6"
        
        vbox:
            spacing 20
            xfill True
            
            text "STATISTICHE PERSONAGGIO" style "stats_title_wide"
            null height 20
            
            frame:
                background "#34495eaa"
                padding (20, 15)
                xfill True
                
                vbox:
                    spacing 10
                    xfill True
                    
                    text "INFORMAZIONI BASE" style "stats_subtitle"
                    
                    hbox:
                        spacing 10
                        xfill True
                        text "Nome:" style "stats_label"
                        text "[player_name]" style "stats_value" xalign 1.0
                    
                    hbox:
                        spacing 10
                        xfill True
                        text "Livello:" style "stats_label"
                        text "[player_level]" style "stats_value" xalign 1.0
            
            frame:
                background "#34495eaa"
                padding (20, 15)
                xfill True
                
                vbox:
                    spacing 15
                    xfill True
                    
                    text "STATISTICHE VITALI" style "stats_subtitle"
                    
                    vbox:
                        spacing 8
                        xfill True
                        hbox:
                            spacing 10
                            xfill True
                            text "Salute" style "stats_label"
                            text "[player_hp]/100" style "stats_value" xalign 1.0
                        bar value player_hp range 100 xsize 550 ysize 25
                    
                    vbox:
                        spacing 8
                        xfill True
                        hbox:
                            spacing 10
                            xfill True
                            text "Energia" style "stats_label"
                            text "[player_energy]/100" style "stats_value" xalign 1.0
                        bar value player_energy range 100 xsize 550 ysize 25
            
            frame:
                background "#34495eaa"
                padding (20, 15)
                xfill True
                
                vbox:
                    spacing 10
                    xfill True
                    
                    text "CARBURANTE" style "stats_subtitle"                    
                    hbox:
                        xalign 0.5
                        use gauge_display
            
            frame:
                background "#34495eaa"
                padding (20, 15)
                xfill True
                
                vbox:
                    spacing 10
                    xfill True
                    
                    text "ATTRIBUTI" style "stats_subtitle"
                    
                    hbox:
                        spacing 10
                        xfill True
                        text "Forza:" style "stats_label"
                        text "[player_strength]" style "stats_value" xalign 1.0
                    
                    hbox:
                        spacing 10
                        xfill True
                        text "Intelligenza:" style "stats_label"
                        text "[player_intelligence]" style "stats_value" xalign 1.0
                    
                    hbox:
                        spacing 10
                        xfill True
                        text "Carisma:" style "stats_label"
                        text "[player_charisma]" style "stats_value" xalign 1.0
            
            frame:
                background "#f39c12aa"
                padding (20, 15)
                xfill True
                
                hbox:
                    spacing 10
                    xfill True
                    text "Denaro:" style "stats_label"
                    text "[player_money]$" style "stats_value_gold" xalign 1.0


# ==================================================
# STILI PERSONALIZZATI
# ==================================================

style large_button:
    xminimum 500
    background "#333333"
    hover_background "#555555"
    padding [20, 15, 20, 15]


style stats_title:
    size 24
    bold True
    color "#ecf0f1"

style stats_title_wide:
    size 32
    bold True
    color "#ecf0f1"
    xalign 0.5

style stats_subtitle:
    size 18
    bold True
    color "#3498db"

style stats_label:
    size 16
    color "#bdc3c7"

style stats_value:
    size 16
    bold True
    color "#ecf0f1"

style stats_value_small:
    size 14
    color "#ecf0f1"

style stats_value_gold:
    size 18
    bold True
    color "#f1c40f"




    