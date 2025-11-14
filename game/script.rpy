# /game/script.rpy


label splashscreen:
    scene welcome
    with fade
    $ renpy.pause(15.0)
    return

label start:  

    scene welcome
    with fade
    $ renpy.pause(15.0)
    "Welcome to the road"   
    
    jump main_menu

    #$ config.developer = True

    # SWITCH: debug o capitolo 1
    #if persistent.debug_mode:
    #     call screen debug_menu_screen   # IL TUO MENU GRAFICO, INALTERATO
    #else:
    #    call chapter_01                 # CAPITOLO 1
    return


label main_menu:
    menu:
        "Vai al tutorial!":
            jump tutorial
        "Inizia a Giocare!":
            jump chapter_01
        "Vai al menu di debug":
            jump debug_menu
        "Prova il dado":           
            jump dice_enchanted   
        "Esci subito (questo gioco non fa per me)":
            jump ending



label dice_test:
    scene bg room  # Sostituisci con il tuo background
    
    "Benvenuto nel sistema di lancio dado!"
    
    "Premi per lanciare un dado a 6 facce:"
    
    # Mostra l'interfaccia del dado
    call screen dice_roller(6)
    
    # Usa il risultato
    "Hai ottenuto [dice.last_result]!"
    
    if dice.last_result >= 5:
        "Ottimo tiro!"
    elif dice.last_result >= 3:
        "Non male."
    else:
        "Poteva andare meglio..."
    
    # Esempio con dado diverso
    "Ora proviamo con un dado a 20 facce (D20):"
    
    call screen dice_roller(20)
    
    "Risultato D20: [dice.last_result]"
    
    # Esempio di uso diretto in Python
    python:
        risultato = dice.roll(10)
    
    "Ho lanciato un D10 in background: [risultato]"
    
    return


label dice_enchanted:
    
    scene bg room
    
    "Benvenuto nel sistema di lancio dado con GIF!"
    
    "Guarda che figata questa animazione:"
    
    call screen dice_roller_gif(6)
    # Usa il risultato
    "Hai ottenuto [dice.last_result]!"
    
    if dice.last_result == 6:
        "JACKPOT! 🎉"
    elif dice.last_result >= 4:
        "Ottimo tiro! 👍"
    elif dice.last_result >= 3:
        "Non male! 😊"
    else:
        "Riprova! 🤞"
    
    # Altro esempio
    "Vuoi lanciare di nuovo?"
    
    call screen dice_roller_gif(6)
    
    "Secondo lancio: [dice.last_result]"
    jump main_menu
    return

label ending:
    "Thank you for playing Episode 1 of the Road, part 2 will be coming out SOON*TM"
        # "Alphaness= [a] \nKinkiness= [k] \nSissiness=[s]"
        
    # This ends the game.

    return