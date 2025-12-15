# /game/0_init.rpy
# Variabili globali e default
default persistent.debug_mode = False   # DEBUG OFF di default

default metronome_bpm = 120
default metronome_running = False
default active_routine = None

default persistent.warmup_completed = False

define e = Character("Eileen", color="#f44")
define m = Character("Mina", color="#4d0653")
define l = Character("Lea", color="#fa0ac6")
define y = Character("You", color="#120afa")


default player_name = "Hero"
default player_level = 5
default player_hp = 75
default player_energy = 60
default player_strength = 15
default player_intelligence = 12
default player_charisma = 10
default player_money = 1250
default player_fuel = 0  # Valore da -10 a +10

default player_sissy = 0
default player_max_sissy = 200
default player_slut = 0
default player_max_slut = 200
default player_alpha = 0
default player_max_alpha = 10
default player_min_alpha = -10





image bg_pub = "images/bg/pub.jpg"


default active_menu = "none"
default menu_ypos = -400   # il menu parte fuori dallo schermo

# Velocità animazione
define MENU_SPEED = 0.25


