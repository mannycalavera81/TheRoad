# /game/5_screens.rpy
# Tutte le screen








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
            textbutton "Component Showcase" action Jump("components_showcase") xalign 0.5
            
            null height 40
            textbutton "ESCI DAL DEBUG" action Jump("start") xalign 0.5  # Esce dal loop


screen progress_bar(current, total, width=540, height=14):
    ## current = step attuale (es. 3)
    ## total   = step totali   (es. 6)
    ## width   = larghezza totale barra (adattala alla tua card)
    ## height  = altezza (12-18 px è perfetta)

    frame:
        background None
        xsize width ysize height
        xalign 0.5

        # sfondo grigio scuro
        add Solid("#222222", xsize=width, ysize=height)

        # barra colorata che cresce
        add Solid("#00ff9d", xsize=(width * current / total), ysize=height)

        # bordo sottile
        #add Frame("gui/progress_border.png", 2, 2) xsize width ysize height

        # testo centrato sopra (opzionale ma figo)
        text "[current] / [total]" size 13 color "#ffffff" outlines [(1,"#000000",0,0)]:
            xalign 0.5 yalign 0.5

#Versione ultra-minimal (solo barra colorata senza testo)
screen mini_progress(current, total, w=500, h=8):
    add Solid("#333") xsize w ysize h
    add Solid("#ff00aa", xsize=(w * current / total), ysize=h)

# Versione con pallini (tipo  ●●●○○○ )
screen dots_progress(current, total):
    hbox spacing 6 yalign 0.5 xalign 1.0:
        for i in range(1, total+1):
            add Solid("#00ff9d" if i <= current else "#444444", xsize=12, ysize=12, xysize_ymin=12) radius 6

screen circular_countdown(time_left):
    fixed:
        xysize (160, 160)  # Riduco anche il fixed
        add Solid("#0008ff", xysize=(160, 160))
        
        add Transform("images/gauge/clock-full.png") xalign 0 ypos 0
        if time_left < 40:
            add Transform("images/gauge/clock-q1.png" ) xalign 0 ypos 0
        if time_left < 30:
            add Transform("images/gauge/clock-q2.png" ) xalign 0 ypos 0
        if time_left < 10:
            add Transform("images/gauge/clock-q3.png" ) xalign 0 ypos 0
        if time_left < 1:
            add Transform("images/gauge/clock-empty.png" ) xalign 0 ypos 0

        text "Time left [time_left]" size 14 color "#ffffff" xalign 0.5 yalign 0.5 bold True

screen ultimate_card:
    modal True
    frame:    
        xalign 0.5 yalign 0.1
        background Frame("card-background.png", 25, 25)
        #          Frame dice: "30px di bordo su ogni lato!"
        xsize 607  # Il frame è largo 500px
        ysize 660  # Il frame è alto 400px
        padding [25, 25, 25, 25]
        vbox xsize 556:
            frame xfill True:
                style "empty"
                background "#00ff62"
                has hbox
                #vbox:
                hbox xfill True :
                    hbox:
                        add "dildo.png"  xsize 24 ysize 24 
                        add "dildo.png"  xsize 24 ysize 24
                    text  "AREA Titolo" bold True size 24 color "#151515" xalign 0.5 
                    add Solid("#d9169f") xsize 100 ysize 30 xalign 1.0  
            
            frame xfill True:
                style "empty"
                background "#0008ff" padding (0,0)
                hbox xfill True: 
                    add "face_a.png"  xsize 100 ysize 100
                    text "Descrizione completa . es Lorem ipsum Lorem forgiato est" size 14 xsize 370 color "#fa6712"
                    add "position6.jpg"  xsize 100 ysize 100 xalign 1.0
                 
                    
            add "metronome_anim" xalign 0.5

            frame xfill True yfill True:
                style "empty"
                background "#00d9ff" padding (0,0)
                hbox xfill True:  
                   
                    vbox:
                        text "Stage 1 di 3" size 14 bold True color "#121afa"                         
                        text "Descrizione completa dello stage . es Lorem ipsum Lorem forgiato est" :
                            size 14 color "#fa1212" xsize 370 xalign 0.0
                    use dots_progress( 3, 6)
                    # Testo stage centrato

    hbox:
        use gauge_display_vertical
        use circular_countdown(10)
        imagebutton auto "start_%s.png"
        imagebutton auto "stop_%s.png" 
                    
                    


screen fancy_card:
    vbox xalign 0.5 yalign 0 spacing 20 :
        hbox:
            use gauge_display_vertical
            frame background "#f10909aa" xpadding 50 ypadding 50 :
                vbox spacing 20 xalign 0.5:
                    text "Titolo" size 36 color "#00ff6e"
                    text "Descrizione dettagliata  della challeng" size 18 color "#ff6a00"
                    add "routine_anim" xalign 0.5    
                    text "BPM: [metronome_bpm]" size 32 color "#fff"
                    text "COMPLETATA!" size 28 color "#f00"
            text "Sound area" size 14 color "#00ffa6" 
        hbox spacing 40 xalign 0.5:
            imagebutton auto "start_%s.png" action Show('save')
            imagebutton auto "stop_%s.png" action Show('save')

style card_frame:
    #background Frame("images/frame.png", 40, 40)
    # Oppure usa un colore con alpha:
    background Frame(Solid("#990404cc"), 0, 0)  # Nero semi-trasparente
    padding (50, 40)
    margin (20, 20)
    xsize 500
    ysize 400
    xalign 0.5
    yalign 0.5

screen card_with_shadow:
    zorder 100

    fixed:
        xsize 640 ysize 720                  # dimensione totale della card

        # Ombra morbida (sotto tutto)
        add Solid("#00000022") xoffset 18 yoffset 18 xsize 540 ysize 720
        add Solid("#00000044") xoffset 12 yoffset 12 xsize 540 ysize 720
        add Solid("#00000099") xoffset  6 yoffset  6 xsize 540 ysize 720

        # Il tuo frame dorato ridimensionato alla perfezione
        add "images/frame.png" xsize 540 ysize 720
        # (se vuoi più grande → 0.62, se più piccolo → 0.55)

        # Testo centrato correttamente
        text "Card con ombra!":
            size 40
            color "#ffffff"
            outlines [(3, "#000000", 0, 0)]   # contorno nero per leggibilità
            xanchor 1.0                       # centra orizzontalmente rispetto a xpos

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




    