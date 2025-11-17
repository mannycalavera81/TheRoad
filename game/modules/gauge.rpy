# /game/2_utils.rpy
# Funzioni per gauge





# Transform per ruotare la lancetta
transform gauge_needle(fuel_value):
    rotate (fuel_value * 13.5 -90)
    anchor (0.5, 0.9)
    around (100, 100)


# Nel file con i transform (3a_gauge.rpy)
transform gauge_needle_range(value, min_val, max_val):
    # Mappa value da [min_val, max_val] a [-135, 135] gradi
    rotate ((value - min_val) / (max_val - min_val) * 270 - 135)
    anchor (0.5, 0.5)

screen gauge_display_vertical():
    fixed:
        xysize (160, 160)  # Riduco anche il fixed
        add Solid("#0008ff", xysize=(160, 160))
        
        add Transform("images/gauge/gauge_arc_red.png") xalign 0 ypos 0
        add Transform("images/gauge/gauge_arc_yellow.png" ) xalign 0 ypos 0
        add Transform("images/gauge/gauge_arc_green.png") xalign 0 ypos 0
        add Transform("images/gauge/gauge_marks.png") xalign 0 ypos 0
        add Solid("#502c2d", xysize=(20, 20)) xalign 0.5 ypos 75
        #add Transform("images/gauge/lancetta-orizzontale.png", rotate=(player_fuel * 13.5 ), anchor=(0.5, 0.5)) xalign 0.5 ypos 80
        add "images/gauge/lancetta-orizzontale.png" at gauge_needle_range(metronome_bpm, 40, 240) xalign 0.5 ypos 80
        text "[metronome_bpm] BPM" size 16 bold True color "#ecf0f1" xpos 90 ypos 70 