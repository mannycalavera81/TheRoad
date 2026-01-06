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
            textbutton "Frame tryout" action Jump("frame_tryout") xalign 0.5
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



screen pulsantiera(routine, routine_name):
    $ time_left = int(routine.get_total_time_remaining()) if routine.is_running else 0
    $ total_time = routine.get_initial_total_time()  # ← USA IL TEMPO TOTALE INIZIALE
    add "routine_anim" xalign 0.5
    frame:
        background Frame("card-background.png", 25, 25)       # ← il tuo overlay.png è qui, vivo e vegeto
        xalign 0.5 yalign 0.5
        xsize 607  # Il frame è largo 500px
        ysize 350  # Il frame è alto 400px
        padding [25, 25, 25, 25]
        vbox:
            hbox xfill True :
                hbox xalign 0.0:
                    use gauge_display_horizontal
                    vbox:                    
                        #imagebutton idle Transform("button/grey.jpg", size=(30,30))   hover Transform("button/grey.jpg", size=(40,40))   action NullAction() xalign 0.0 yalign 0.0
                        #imagebutton idle Transform("button/grey.jpg", size=(30,30))   hover Transform("button/grey.jpg", size=(40,40))   action NullAction() xalign 0.0 yalign 1.0 
                        textbutton "+" action SetVariable("metronome_bpm", min(240, metronome_bpm + 5)) text_size 28 
                        textbutton "−" action SetVariable("metronome_bpm", max(20, metronome_bpm - 5)) text_size 28
                       

                hbox xalign 0.5:
                    vbox:
                        imagebutton idle Transform("button/wrap-idle.png", size=(60,60)) hover Transform("button/wrap-hover.png" , size=(60,60)) selected Transform("button/wrap-selected.png", size=(60,60)) insensitive Transform("button/wrap-inactive.png" , size=(70,70)) action Function(change_audio_mode, "off")
                        imagebutton idle Transform("button/metronome_idle.png", size=(60,60)) hover Transform("button/metronome_hover.png" , size=(60,60)) selected Transform("button/metronome_selected.png", size=(60,60)) insensitive Transform("button/metronome_inactive.png" , size=(70,70)) action Function(change_audio_mode, "beat") 
                    vbox:
                        imagebutton idle Transform("button/blue.jpg",   size=(60,60)) hover Transform("button/blue.jpg",   size=(70,70)) action Function(change_audio_mode, "natural", 2)                     
                        imagebutton idle Transform("button/green.jpg",  size=(60,60)) hover Transform("button/green.jpg",  size=(70,70)) action Function(change_audio_mode, "natural", 3) 
                    

                hbox xalign 1.0:    
                    vbox:       
                        imagebutton idle Transform("button/blue.jpg", size=(30,30))   hover Transform("button/blue.jpg", size=(40,40))   action NullAction() xalign 1.0 yalign 0.0
                        imagebutton idle Transform("button/green.jpg", size=(30,30))  hover Transform("button/green.jpg", size=(40,40))  action NullAction() xalign 1.0 yalign 1.0
                    vbox:
                        use circular_countdown(time_left)
                        if routine.is_running:
                            text "Segmento [routine.current_segment + 1]/[len(routine.segments)]" size 24 color "#0ff"
                            text "Tempo segmento: [int(routine.get_time_remaining())]s" size 20 color "#0f0"
                            text "Tempo totale: [int(routine.get_total_time_remaining())]s" size 20 color "#0f0"
                        else:
                            text "COMPLETATA!" size 28 color "#f00"
            hbox xfill True:
                imagebutton auto "start_%s.png"  action [  SensitiveIf( not metronome_running ) ,Function(start_metronome)]
                imagebutton auto "stop_%s.png" action [ SensitiveIf( metronome_running ), Function(stop_metronome)]

              

screen ultimate_class_card(card_info):
    if(card_info.position == CARD_BOTTOM):
        $ card_color= "#d9169f"
        $ position_color= "#c4cd2c"
        
        $ card_type= "Bottom card\n(Be the woman)"
    else:
        $ card_color= "#0008ff"
        $ position_color= "#A51255"
        $ card_type= "Top card\n(be the man)"
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
                background card_color
                has hbox
                hbox xfill True :
                    fixed xsize 100 ysize 26 :
                        add Solid(position_color)
                        hbox xalign 0.0:
                            for tool in card_info.tools:
                                add "tools/[tool].png" xsize 24 ysize 24
                    fixed xsize 350 ysize 26 :
                        text  card_info.name bold True  size 24 color "#151515" xalign 0.5 
                    fixed xsize 100 ysize 26 :
                        text  card_type bold True size 12 color position_color xalign 0.5 yalign 1.0


            
            frame xfill True:
                style "empty"
                background card_color padding (0,0)
                hbox xfill True: 
                    add "faces/[card_info.charapter].png"  xsize 100 ysize 100
                    text card_info.description size 14 xsize 370 color "#f3edeb" yalign 0.5
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



# Screen principale con le 3 barre in ORIZZONTALE
screen status_bars():
    # Barra Rosa (Magic)
    hbox:
        xalign 0.5
    
        use progress_bar_slim(
            color_string="pink",
            current=player_sissy, 
            min_value=0, 
            max_value=player_max_sissy,
            bar_color="#d946ef",
            dark_color="#581c87",
            label="Sissy",
            icon_thresholds={
                0: "images/icon/fire.png",
                50: "images/icon/star.png",
                150: "images/icon/flames.png"
            }
        )
        
        # Barra Blu (Experience - può essere negativa)
        #use progress_bar_centered(
        #    x=700, y=10,
        #    current=experience_points, 
        #    max_value=max_experience,
        #    bar_color="#3b82f6",
        #    dark_color="#1e3a8a",
        #    label="Experience"
        #)


        # Barra Rossa (Health)
        use progress_bar_slim(
            color_string="red",
            current=player_slut,
            min_value=0, 
            max_value=player_max_slut,
            bar_color="#ef4444",
            dark_color="#7f1d1d",
            label="Slut",
            icon_thresholds={
                0: "images/icon/heart.png",
                100: "images/icon/heartblack.png"
            }
        )


            # Barra Rossa (experience)
        use progress_bar_slim(
            color_string="blue",
            current=player_alpha, 
            min_value=player_min_alpha,
            max_value=player_max_alpha,
            bar_color="#3b82f6",
            dark_color="#1e3a8a",
            label="Alpha",
            icon_thresholds={
                0: "images/icon/beta.png",
                1: "images/icon/alpha.png"
            }
        )

    # Barra Blu (Experience - può essere negativa)
    #use progress_bar_icon(
    #    x=10, y=300,
    #    current=experience_points, 
    #    max_value=max_experience,
    #    bar_color="#eeff00",
    #    dark_color="#768a1e9c",
    #    label="Realation"
    #)

    #use money_bar(
    #    x=1400 , y=10,
    #    label="Money",
    #    value="1235"
    #)




screen money_bar(x , y, label, value):
    fixed:
        xpos x 
        ypos y
        xysize ( 300, 90)
        frame:
            xpos 45
            ypos 0
            xysize (300, 90)
            background Solid("#1a1a1a")
            padding (0, 0)
            vbox:
                #spacing 4
                xalign 0.0
                yalign 0.5
                
                # Barra superiore (progresso)
                frame:
                    xysize (296, 36)
                    background Solid("#0bc93e")
                    padding (4, 4)
                    hbox:
                        xalign 0.5
                        add "images/icon/heart.png"  xsize 30 ysize 30 
                        add "images/icon/heart.png"  xsize 30 ysize 30 
                    
                       
                
                # Barra inferiore (decorativa scura)
                frame:
                    xysize (296, 28)
                    background Solid("#011005")
                    padding (4, 4)
                    
                    frame:
                        xysize (288, 20)
                        background Solid("#1e6430")
                        # Testo CENTRATO sulla barra

            text "[label]: [value] ":
                xalign 0.5
                yalign 1.0
                size 28
                color "#ffffff"
                outlines [(3, "#000000", 0, 0)]
                bold True

    # Cerchio TONDO con icona
        frame:
            xpos 0
            ypos 0
            xysize (90, 90)
            background None
            padding (0, 0)
            
            add "images/icon/circle_pink.png":
                xysize (90,90)
                

            add "images/icon/heartblack.png":
                xalign 0.5
                yalign 0.5
                fit "contain"
                xysize (50, 50)
    

# Componente barra standard (valori positivi)
screen progress_bar(x, y, color_string, current,min_value, max_value, bar_color, dark_color, label, icon_thresholds=None):
    $ normalized_value = current - min_value  # Es: -50 - (-100) = 50
    $ normalized_range = max_value - min_value  # Es: 100 - (-100) = 200
    $ progress_bar_image = "images/gui/progress_" + color_string + ".png"
    $ circle_image = "images/gui/circle_" +color_string +".png"
    #$ color_string =
    fixed:
        xpos x
        ypos y
        xysize (600, 90)       
        
        
        # Container barra (senza spazio)
        frame:
            xpos 45
            ypos 0
            xysize (590, 90)
            #background Solid("#1a1a1a")
            background None
            padding (0, 0)
            
            vbox:
                #spacing 4
                xalign 0.0
                yalign 0.5
                
                # Barra superiore (progresso)
                frame:
                    xysize (590, 36)
                    background None
                    padding (0, 0)
                    
                    # Bordo esterno
                    frame:
                        xysize (590, 36)
                        background Solid(bar_color)
                        padding (4, 4)
                        
                        # Contenitore barra
                        frame:
                            xysize (582, 28)
                            background Solid(dark_color)
                            padding (0, 0)
                            
                            # Barra di progresso
                            bar:
                                xysize (582, 28)
                                value normalized_value
                                range normalized_range
                                #left_bar Solid(bar_color)                                
                                left_bar Frame(progress_bar_image, 10, 10)
                                right_bar Solid(dark_color)
                                #at transform:
                                #    corner1 (14, 14)
                
                # Barra inferiore (decorativa scura)
                frame:
                    xysize (590, 28)
                    background Solid("#0a0a0a")
                    padding (4, 4)
                    
                    frame:
                        xysize (582, 20)
                        background Solid(dark_color)
                        # Testo CENTRATO sulla barra

            text "[label] score : [current] ":
                xalign 0.5
                yalign 1.0
                size 24
                color "#ffffff"
                outlines [(3, "#000000", 0, 0)]
                bold True

        # Cerchio TONDO con icona
        frame:
            xpos 0
            ypos 0
            xysize (90, 90)
            background None
            padding (0, 0)
            
            add circle_image:
                xysize (90,90)                

            # Icona
            if icon_thresholds:
                $ icon = get_icon_for_level(current, icon_thresholds)
                add icon:
                    xalign 0.5
                    yalign 0.5
                    fit "contain"
                    xysize (50, 50)
            
            
# Componente barra moderna, sottile e trasparente
screen progress_bar_slim(color_string, current, min_value, max_value, bar_color, dark_color, label, icon_thresholds=None):
    $ normalized_value = current - min_value
    $ normalized_range = max_value - min_value
    $ progress_bar_image = "images/gui/progress_" + color_string + ".png"
    $ circle_image = "images/gui/circle_" + color_string + ".png"

    fixed:
        xysize (445, 50)  # Altezza complessiva ridotta

       
        frame:
            xpos 22
            ypos 0
            xysize (400, 50)
            background None
            padding (0, 0)

        
            vbox:
                spacing 0
                xalign 0.0
                yalign 0.0
                text "[label]":
                    size 12
                    color bar_color
                    outlines [(2, "#000000", 0, 0)]
                    bold True
                    xalign 0.5
                    yalign 1.0

                

                # Barra principale sottile
                frame:
                    xysize (380, 20)
                    background Solid("#00000050")  # sfondo semi-trasparente
                    padding (2, 2)

                    
                    bar:
                        xysize (380, 16)
                        value normalized_value
                        range normalized_range
                        left_bar Frame(progress_bar_image, 8, 8)
                        right_bar Solid(dark_color)
                    
                    hbox yalign 0.5 xalign 0.0:
                        text "     Level:":
                            size 12
                            color "#ffffff"
                            outlines [(2, "#000000", 0, 0)]
                            bold False
                            xalign 0.0
                            yalign 0.5
                        
                        text "10 - Tomboy":
                            size 12
                            color "#ffffff"
                            outlines [(2, "#000000", 0, 0)]
                            bold True
                            xalign 0.0
                            yalign 0.5

                    hbox yalign 0.5 xalign 1.0:    
                        text "Score:":
                            size 12
                            color "#ffffff"
                            outlines [(2, "#000000", 0, 0)]
                            bold False
                            xalign 1.0
                            yalign 0.5

                        text "[current]":
                            size 12
                            color "#ffffff"
                            outlines [(2, "#000000", 0, 0)]
                            bold True
                            xalign 1.0
                            yalign 0.5

            
                    

               
              
                    

        # Cerchio TONDO con icona
        frame:
            xpos 0
            ypos 7
            xysize (45, 45)
            background None
            padding (0, 0)
            
            add circle_image:
                xysize (45,45)                

            # Icona
            if icon_thresholds:
                $ icon = get_icon_for_level(current, icon_thresholds)
                add icon:
                    xalign 0.5
                    yalign 0.5
                    fit "contain"
                    xysize (25, 25)
        


# Componente barra centrata (per valori negativi)
screen progress_bar_centered(x, y, current, max_value, bar_color, dark_color, label):
    fixed:
        xpos x
        ypos y
        xysize (700, 90)



        # Container barra PRIMA del cerchio
        frame:
            xpos 0
            ypos 0
            xysize (700, 90)
            background Solid("#1a1a1a")
            padding (0, 0)
            
            
            vbox:
                spacing 0
                xalign 0.5
                yalign 0.5
                
                # Barra superiore con CENTRO
                frame:
                    xysize (696, 36)
                    background None
                    padding (0, 0)
                    
                    # Bordo esterno
                    frame:
                        xysize (696, 36)
                        background Solid(bar_color)
                        padding (4, 4)
                        
                        # Contenitore barra
                        frame:
                            xysize (688, 28)
                            background Solid(dark_color)
                            padding (0, 0)
                            
                            hbox:
                                spacing 0
                                
                                # Parte sinistra (negativi) - riempimento da destra
                                bar:
                                    xysize (340, 28)
                                    value max(0, -current)
                                    range max_value
                                    left_bar Solid(dark_color)
                                    if current < 0 :
                                        right_bar Frame("images/progress_blue.png")
                                    else :
                                        right_bar Solid(dark_color)
                                
                                # Linea centrale
                                add Solid("#ffffff"):
                                    xysize (1, 28)
                                
                                # Parte destra (positivi)
                                bar:
                                    xysize (340, 28)
                                    value max(0, current)
                                    range max_value
                                    #left_bar Solid(bar_color)
                                    if current > 0 :
                                        left_bar Frame("images/progress_blue.png")
                                    else :
                                        left_bar Solid(dark_color)
                                    right_bar Solid(dark_color)
                
                # Barra inferiore
                frame:
                    xysize (696, 28)
                    background Solid("#0a0a0a")
                    padding (4, 4)
                    
                    frame:
                        xysize (688, 20)
                        background Solid(dark_color)
            hbox xfill True:
                yalign 1.0

                # Testo CENTRATO
                text "Beta Male":
                    xalign 0.0
                    yalign 1.0
                    size 24
                    color "#ffffff"
                    outlines [(3, "#000000", 0, 0)]
                    bold True
                            # Cerchio TONDO con icona
                # Testo CENTRATO
                text "Alpha Male":
                    xalign 1.0
                    yalign 1.0
                    size 24
                    color "#ffffff"
                    outlines [(3, "#000000", 0, 0)]
                    bold True
                        # Cerchio TONDO con icona
        frame:
            xpos 300
            ypos 0
            xysize (90, 90)
            background None
            padding (0, 0)
            

            add "images/icon/circle_pink.png":
                xysize (90,90)
                
            # Icona
            add "images/icon/heartblack.png":
                xalign 0.5
                yalign 0.5
                fit "contain"
                xysize (50, 50)




                
# Componente barra centrata (per valori negativi)
screen progress_bar_icon(x, y, current, max_value, bar_color, dark_color, label):
    fixed:
        xpos x
        ypos y
        xysize (400, 90)



        # Container barra PRIMA del cerchio
        frame:
            xpos 0
            ypos 0
            xysize (400, 90)
            background Solid("#1a1a1a")
            padding (0, 0)
            
            
            vbox:
                spacing 0
                xalign 0.5
                yalign 0.5
                
                # Barra superiore con CENTRO
                frame:
                    xysize (400, 36)
                    background None
                    padding (0, 0)
                    
                    # Bordo esterno
                    frame:
                        xysize (400, 36)
                        background Solid(bar_color)
                        padding (4, 4)
                                            
                        
                        hbox:
                            spacing 0
                            xalign 0.0                               
                            add "images/icon/beta.png"  xsize 30 ysize 30 
                            add "images/icon/beta.png"  xsize 30 ysize 30 
                            add "images/icon/beta.png"  xsize 30 ysize 30 
                            add "images/icon/beta.png"  xsize 30 ysize 30 
                            add "images/icon/beta.png"  xsize 30 ysize 30 

                        hbox:
                            spacing 0
                            xalign 1.0                               
                            add "images/icon/alpha.png"  xsize 30 ysize 30 
                            add "images/icon/alpha.png"  xsize 30 ysize 30 
                            add "images/icon/alpha.png"  xsize 30 ysize 30 
                            add "images/icon/alpha.png"  xsize 30 ysize 30 
                            add "images/icon/alpha.png"  xsize 30 ysize 30 
                            
                               
                
                # Barra inferiore
                frame:
                    xysize (400, 28)
                    background Solid("#0a0a0a")
                    padding (4, 4)
                    
                    frame:
                        xysize (392, 20)
                        background Solid(dark_color)
            hbox xfill True:
                yalign 1.0

                # Testo CENTRATO
                text "Beta Male":
                    xalign 0.0
                    yalign 1.0
                    size 24
                    color "#ffffff"
                    outlines [(3, "#000000", 0, 0)]
                    bold True
                            # Cerchio TONDO con icona
                # Testo CENTRATO
                text "Alpha Male":
                    xalign 1.0
                    yalign 1.0
                    size 24
                    color "#ffffff"
                    outlines [(3, "#000000", 0, 0)]
                    bold True
                        # Cerchio TONDO con icona
        frame:
            xpos 155
            ypos 0
            xysize (90, 90)
            background None
            padding (0, 0)
            

            add "images/icon/circle_pink.png":
                xysize (90,90)
                
            # Icona
            add "images/icon/heartblack.png":
                xalign 0.5
                yalign 0.5
                fit "contain"
                xysize (50, 50)
        
       

screen top_menus():

    # --- TABS ---
    hbox:
        spacing 20
        xpos 20
        ypos 20

        textbutton "Statistiche" action SetVariable("active_menu", "stats")
        textbutton "Accessori"  action SetVariable("active_menu", "acc")
        textbutton "Negozi"     action SetVariable("active_menu", "shop")
        textbutton "Perks"      action SetVariable("active_menu", "perks")
        textbutton "Nascondi"   action SetVariable("active_menu", "none")


    # --- MENU A COMPARSA ---
    frame:
        xysize (1800, 380)
        xpos 60
        ypos menu_ypos
        background "#2228"

        # Contenuto menu
        vbox:
            spacing 15
            xalign 0.5
            yalign 0.5

            if active_menu == "stats":
                text "STATISTICHE DISPONIBILI"
                bar value 0.4 range 1.0
                bar value 0.7 range 1.0

            elif active_menu == "acc":
                text "ACCESSORI DISPONIBILI"
            elif active_menu == "shop":
                text "NEGOZIO"
            elif active_menu == "perks":
                text "PERKS DISPONIBILI"

    # --- ANIMAZIONE ---
    timer 0.01 action Function(update_menu_anim) repeat True


screen menu_accessori():
    vbox:
        spacing 20
        xalign 0.5
        text "Accessori" size 45

screen menu_stats():
    vbox:
        spacing 20
        xalign 0.5
        yalign 0.1
        text "Statistiche" size 45

screen menu_negozi():
    vbox:
        spacing 20
        xalign 0.5
        text "Negozi" size 45

screen menu_perks():
    vbox:
        spacing 20
        xalign 0.5
        text "Perks" size 45


transform slide_down:
    yoffset -600
    linear 0.3 yoffset 0

transform slide_up:
    yoffset 0
    linear 0.3 yoffset -600

