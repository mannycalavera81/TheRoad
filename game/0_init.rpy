# /game/0_init.rpy
# Variabili globali e default

default persistent.debug_mode = True

default metronome_bpm = 120
default metronome_running = False
default active_routine = None

define e = Character("Eileen", color="#f44")

init python:
    def reset_to_debug():
        renpy.scene()  # Pulisce sfondi/personaggi (layer master)
        renpy.hide_screen("*")  # Nasconde TUTTE le screen
        renpy.show_screen("debug_menu_screen")  # Mostra solo il menu
