# /game/2_utils.rpy
# Funzioni per gauge


# Transform per ruotare la lancetta
transform gauge_needle(fuel_value):
    rotate (fuel_value * 13.5 -90)
    anchor (0.5, 0.9)
    around (100, 100)