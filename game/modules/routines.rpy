# /game/4_routines.rpy
# Routine predefinite

init python:
    routine_warmup = ProgrammedRoutine([
        (10, 40), (15, 60), (15, 90), (15, 120), (5, 150)
    ])
    routine_intense = ProgrammedRoutine([
        (5, 100), (10, 140), (15, 180), (10, 140), (5, 100)
    ])



# ROUTINE WARM UP
define routine_warmup_fitness = Routine("Warm Up", [
    ("Jumping Jacks", 30),
    ("Arm Circles", 20),
    ("Leg Swings", 20),
    ("Torso Twists", 20)
])

define card_at_the_bar_01 = CardInfo( "Fun at the toilet" , "She invite you to the bathrom ...you notice that... suddenly you begin to ... and dthen...", "dildobig", "cowgirl" "Mia", [
    ("Fuck for 1 min at 60 bpm", 1 )
])