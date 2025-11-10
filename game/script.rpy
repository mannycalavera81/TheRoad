# /game/script.rpy
label start:
    $ config.developer = True
    default persistent.debug_mode = True
    
    if persistent.debug_mode:
        call screen debug_menu_screen  # LOOP: torna sempre qui dopo Jump!
    else:
        call chapter_01
    return