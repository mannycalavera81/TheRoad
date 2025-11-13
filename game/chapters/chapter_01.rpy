# /game/chapters/chapter_01.rpy
# CAPITOLO 1: INTRO + METRONOMO + ROUTINE

label chapter_01:
    scene bg pub with fade
   

    "It's Friday night. You're at the bar on the far side of town."
    "Things haven't exactly been going great, and after the week you just had, you need a drink."
    "All the regular bars by you are overflowing with assholes lately and you just want a quiet place to get away for a little bit and maybe find someone to talk to that isn't a total mess."
    
    show mina normal at right
    m "Benvenuto nel Capitolo 1."
    "As you sip your drink, a blue-haired girl approaches you smiling and says:"
    m "Hey there stranger!"
    m "You're not from around here, are you?"
    m "I feel like I would have noticed you before."

    "She has an amazingly tight body and she sits as if she wants you to notice it."
    "It's been way too long since you've had any kind of attention from the fairer sex, so getting chatted up by a hottie like her is more than welcome."

    l "Oggi iniziamo con il riscaldamento guidato dal metronomo."
    hide mina

    scene bg girlatthebar with fade
    e "Pronta?"

    menu:
        "Sì, andiamo!":
            jump start_warmup
        "No, torno al debug":
            return  # Torna al debug_menu (se chiamato da lì)

label start_warmup:
    # PULIZIA TOTALE
    scene black
    hide eileen
    hide screen metronome_screen

    # AVVIO METRONOMO
    $ metronome_bpm = 120
    $ start_metronome()

    # AVVIO ROUTINE
    $ active_routine = routine_warmup
    $ routine_warmup.start()

    scene bg gym with dissolve



    show screen routine_screen(routine_warmup, "Warm Up")
    show eileen coach at center

    e "Inizia il riscaldamento! Segui il ritmo."
    "Metronomo: [metronome_bpm] BPM"

    # LOOP FINCHÉ LA ROUTINE È ATTIVA
    while routine_warmup.is_running:
        pause 0.1

    # FINE ROUTINE
    $ stop_metronome()
    hide screen routine_screen

    # SALVATAGGIO COMPLETAMENTO
    $ persistent.warmup_completed = True
    $ renpy.save_persistent()

    show eileen happy
    e "Ottimo lavoro! Hai completato il Warm Up."
    e "Vuoi continuare con il Capitolo 2?"

    menu:
        "Sì, prossimo capitolo":
            call chapter_02  # Da creare dopo
            return
        "Torna al menu principale":
            return

    return