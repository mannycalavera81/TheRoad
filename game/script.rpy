# /game/script.rpy
label start:
    # Per versione stretta (250px):
    show screen stats_sidebar_narrow
    
    # Oppure per versione larga (640px) - commenta quella sopra e usa questa:
    # show screen stats_sidebar_wide
    
    scene bg room
    
    "Benvenuto! Le tue statistiche sono sulla sinistra."
    $ player_fuel = 1
    "Attenzione! Benzina quasi finita!"

    $ player_hp = 50
    "La salute è diminuita!"
    
    $ player_fuel = -8
    "Attenzione! Benzina quasi finita!"
    
    $ player_fuel = 7
    "Serbatoio rifornito!"



    scene welcome
    with fade
    $ renpy.pause(15.0)
    "Welcome t o th road"
    menu:
        "Vai al tutorial!":
            $ renpy.pause(0.1)
        "Vai ad esempio statistiche!":
            jump statistiche_test
        "Inizia a Giocare!":
            jump chapter_01
        "Vai al menu di debug":
            jump debug_menu
        "Esci subito (non fa per me)":
            jump ending
    scene bg bar
    with fade

    #$ config.developer = True

    # SWITCH: debug o capitolo 1
    #if persistent.debug_mode:
    #     call screen debug_menu_screen   # IL TUO MENU GRAFICO, INALTERATO
    #else:
    #    call chapter_01                 # CAPITOLO 1
    return



label statistiche_test:
    # Mostra lo screen delle statistiche (scegli una delle due versioni)
 
    # Per versione stretta:
    show screen stats_sidebar_narrow
    
    # Oppure per versione larga (commenta quella sopra e usa questa):
    # show screen stats_sidebar_wide
    
    scene bg room
    
    "Benvenuto nel gioco! Le tue statistiche sono visibili sulla sinistra."
    
    "Puoi aggiornare le statistiche in qualsiasi momento modificando le variabili."
    
    $ player_hp = 50  # Esempio di modifica
    
    "La salute è diminuita!"
    
    $ player_fuel = -8  # Esempio: quasi a secco (zona rossa)
    
    "Attenzione! La benzina sta per finire!"
    
    $ player_fuel = 7  # Esempio: pieno (zona verde)
    
    "Serbatoio rifornito!"
    return

label ending:
    "Thank you for playing Episode 1 of the Road, part 2 will be coming out SOON*TM"
        # "Alphaness= [a] \nKinkiness= [k] \nSissiness=[s]"
        
    # This ends the game.

    return