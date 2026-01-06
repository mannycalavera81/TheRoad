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


#name, description,tools,  charapter, stages, position
define card_at_the_bar_01 = CardInfo( 
    typecard=CARD_TOP,
    name="Fun at the toilet" , 
    description="She invite you to the bathrom ...you notice that... suddenly you begin to ... and then...", 
    tools=[TOOL_DILDO, TOOL_GAG],
    charapter=FACE_MIA_GIRL,
    position="cowgirl" ,
    stages=[
        ("Blow for 10 sec at 60 bpm", 10, 60 ),
        ("Fuck for 30 sec at 120 bpm", 30, 120 ),
        ("Cum in a  1 min at 120 bpm", 5, 180 )
    ]    
)