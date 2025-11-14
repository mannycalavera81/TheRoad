# 1. CLASSE



# 2. VARIABILI GLOBALI
# Istanza globale del dado
default dice = DiceRoller()


# 3. ASSETS (immagini/video)
# Dichiarazione immagini
image dice_rolling = Movie(play="images/dice_rolling.webm", loop=True)
image dice_1 = "images/dice_1.gif"
image dice_2 = "images/dice_2.gif"
image dice_3 = "images/dice_3.gif"
image dice_4 = "images/dice_4.gif"
image dice_5 = "images/dice_5.gif"
image dice_6 = "images/dice_6.gif"


# 4. TRANSFORMS/ANIMAZIONI
# Transform per l'entrata della finestra
transform dice_window_entrance:
    alpha 0.0 zoom 0.8
    easein 0.3 alpha 1.0 zoom 1.0

# Transform per il bounce del risultato finale
transform dice_result_bounce:
    zoom 0.7
    easein 0.15 zoom 1.15
    easeout 0.15 zoom 1.0

# Transform per le particelle
transform sparkle:
    alpha 0.0 zoom 0.5 rotate 0
    parallel:
        easein 0.3 alpha 1.0
        easeout 0.5 alpha 0.0
    parallel:
        linear 0.8 zoom 1.5
    parallel:
        linear 0.8 rotate 360


# 5. SCREENS
                       

# Schermo principale del dado
screen dice_roller_gif(sides=6, dice_size=250):
    modal True
    
    # Sfondo semi-trasparente
    #add "#000000cc"
    
    # Container principale
    frame:
        align (0.5, 0.5)
        padding (60, 60)
        background "#2c3e50"
        at dice_window_entrance
        
        vbox:
            spacing 40
            
            # Titolo
            text "🎲 LANCIA IL DADO 🎲":
                size 45
                color "#f39c12"
                xalign 0.5
                bold True
            
            # Area del dado (CUORE DEL SISTEMA)
            frame:
                background "#ffffff"
                padding (50, 50)
                xalign 0.5
                xysize (dice_size + 100, dice_size + 100)
                
                # Layer per il dado
                fixed:
                    align (0.5, 0.5)
                    xysize (dice_size, dice_size)
                    
                    # ANIMAZIONE: GIF che rotola
                    if dice.is_rolling:
                        add "dice_rolling":
                            align (0.5, 0.5)
                            size (dice_size, dice_size)
                        
                        # Timer che ferma l'animazione e mostra il risultato
                        timer 1.8 action SetField(dice, "is_rolling", False)
                    
                    # RISULTATO: Immagine statica della faccia
                    elif dice.last_result > 0:
                        # Mostra la faccia corrispondente
                        if dice.last_result == 1:
                            add "dice_1":
                                align (0.5, 0.5)
                                size (dice_size, dice_size)
                                at dice_result_bounce
                        elif dice.last_result == 2:
                            add "dice_2":
                                align (0.5, 0.5)
                                size (dice_size, dice_size)
                                at dice_result_bounce
                        elif dice.last_result == 3:
                            add "dice_3":
                                align (0.5, 0.5)
                                size (dice_size, dice_size)
                                at dice_result_bounce
                        elif dice.last_result == 4:
                            add "dice_4":
                                align (0.5, 0.5)
                                size (dice_size, dice_size)
                                at dice_result_bounce
                        elif dice.last_result == 5:
                            add "dice_5":
                                align (0.5, 0.5)
                                size (dice_size, dice_size)
                                at dice_result_bounce
                        elif dice.last_result == 6:
                            add "dice_6":
                                align (0.5, 0.5)
                                size (dice_size, dice_size)
                                at dice_result_bounce
                        
                        # Particelle decorative
                        fixed:
                            xysize (dice_size + 100, dice_size + 100)
                            text "✨" size 40 pos (20, 30) at sparkle
                            text "✨" size 40 pos (dice_size + 60, 50) at sparkle
                            text "⭐" size 35 pos (40, dice_size + 40) at sparkle
                            text "⭐" size 35 pos (dice_size + 40, dice_size + 30) at sparkle
                    
                    # STATO INIZIALE: Punto interrogativo
                    else:
                        text "?":
                            size 180
                            color "#95a5a6"
                            align (0.5, 0.5)
                            bold True
            
            # Info dado (opzionale)
            if sides != 6 and not dice.is_rolling:
                text "Dado a [sides] facce":
                    size 25
                    color "#bdc3c7"
                    xalign 0.5
            
            # Bottoni
            hbox:
                spacing 25
                xalign 0.5
                
                # Bottone LANCIA
                if not dice.is_rolling:
                    textbutton "🎲 LANCIA!":
                        action Function(dice.start_roll, sides)
                        style "dice_button_launch"
                else:
                    textbutton "Lancio in corso...":
                        action NullAction()
                        style "dice_button_disabled"
                
                textbutton "✕ Continua":
                    action Return(dice.last_result)

# 6. STYLE
# Stili bottoni
style dice_button_launch:
    background "#e74c3c"
    hover_background "#c0392b"
    padding (30, 15)
    xsize 200

style dice_button_launch_text:
    size 28
    color "#ecf0f1"
    hover_color "#ffffff"
    bold True
    xalign 0.5

style dice_button_close:
    background "#7f8c8d"
    hover_background "#95a5a6"
    padding (30, 15)
    xsize 200

style dice_button_close_text:
    size 28
    color "#ecf0f1"
    hover_color "#ffffff"
    bold True
    xalign 0.5

style dice_button_disabled:
    background "#34495e"
    padding (30, 15)
    xsize 200

style dice_button_disabled_text:
    size 28
    color "#7f8c8d"
    bold True
    xalign 0.5


# 7. UTILITY FUNCTION
init python:
    def animate_dice_roll(sides):
        # Risultato finale immediato
        dice.roll(sides)
        dice.current_display = dice.last_result
        renpy.timeout(2)  # Durata animazione
        dice.is_rolling = False