# /game/4_routines.rpy
# Routine predefinite

init python:
    routine_warmup = ProgrammedRoutine([
        (10, 40), (15, 60), (15, 90), (15, 120), (5, 150)
    ])
    routine_intense = ProgrammedRoutine([
        (5, 100), (10, 140), (15, 180), (10, 140), (5, 100)
    ])