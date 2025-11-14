  # Per versione stretta (250px):
label tutorial:

    scene bg stage
    with fade
    show mina normal at center
    m "Benvenuto a the road...io sono Mina "
    m "Il primo gioco interativo basato sul capolovoro del maestro Vulkanov."
    m "Se vuoi fare un tutorial , la mia amica Eleen sarà felice di illustrati ... scegli la voce del menu "
    m "Se invece sei gia esperto dei giochi renpy puoi saltare direttamente all'inizio della storia "
    m "A te la scelta ... buon divertimento!"

    show screen stats_sidebar_narrow
    

    # Oppure per versione larga (640px) - commenta quella sopra e usa questa:
    # show screen stats_sidebar_wide

    scene bg room
    
    show lea normal at center
    l "Benvenuto! Le tue statistiche sono sulla sinistra."
    $ player_fuel = 1
    "Attenzione! Benzina quasi finita!"

    $ player_hp = 50
    "La salute è diminuita!"
    
    $ player_fuel = -8
    "Attenzione! Benzina quasi finita!"
    
    $ player_fuel = 7
    "Serbatoio rifornito!"

    l "...bene proviamo adesso ad usare l'altro menu"
    
    show lea normal at right
    # Per versione stretta:
    hide screen stats_sidebar_narrow
    
    # Oppure per versione larga (commenta quella sopra e usa questa):
    show screen stats_sidebar_wide
    
    scene bg room
    
    "Benvenuto nel gioco! Le tue statistiche sono visibili sulla sinistra."
    
    "Puoi aggiornare le statistiche in qualsiasi momento modificando le variabili."
    
    $ player_hp = 55  # Esempio di modifica
    
    "La salute è diminuita!"
    
    $ player_fuel = -4  # Esempio: quasi a secco (zona rossa)
    
    "Attenzione! La benzina sta per finire!"
    
    $ player_fuel = 10  # Esempio: pieno (zona verde)
    
    "Serbatoio rifornito!"

    m "A te la scelta ... buon divertimento!"

    hide screen stats_sidebar_narrow
    jump main_menu
    return

