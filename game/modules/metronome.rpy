# /game/3_metronome.rpy



# 1. CLASSE

# 2. VARIABILI GLOBALI

image metronome_anim = DynamicDisplayable(metronome_displayable)
image routine_anim = DynamicDisplayable(routine_displayable)

# 3. ASSETS (immagini/video)

# 4. TRANSFORMS/ANIMAZIONI

# 5. SCREENS

screen metronome_screen():
    #on "show" action Function(start_metronome)
    on "hide" action Function(stop_metronome)

    vbox xalign 0.5 yalign 0.5 spacing 30:
        frame background "#222a" xpadding 50 ypadding 50:
            vbox spacing 20 xalign 0.5:
                add "metronome_anim" xalign 0.5
                text "BPM: [metronome_bpm]" xalign 0.5 size 32 color "#fff"
                if metronome_running:
                    text "Frame: [metronome_animator.current_frame]/38" size 20 color "#0f0"
                else:
                    text "FERMO" size 20 color "#f00"
                hbox spacing 20 xalign 0.5:
                    textbutton "−" action SetVariable("metronome_bpm", max(20, metronome_bpm - 5)) text_size 28
                    textbutton "+" action SetVariable("metronome_bpm", min(240, metronome_bpm + 5)) text_size 28
                hbox spacing 20 xalign 0.5:
                    textbutton "No Sound" action Function(change_audio_mode, "off") text_size 28
                    textbutton "Standard Beat" action Function(change_audio_mode, "beat") text_size 28
                    textbutton "Natural 1 sound" action Function(change_audio_mode, "natural", 3) text_size 28
                hbox spacing 20 xalign 0.5:
                    textbutton "Loop Sound" action Function(change_audio_mode, "loop", 1) text_size 28
                    textbutton "Loop Sound" action Function(change_audio_mode, "loop", 2) text_size 28
                    textbutton "Loop Sound" action Function(change_audio_mode, "loop", 3) text_size 28
        hbox spacing 40 xalign 0.5:
            textbutton "Avvia" action Function(start_metronome)
            textbutton "Ferma" action Function(stop_metronome)



screen gif_control_screen_a():
    on "show" action Function(start_metronome)
    on "hide" action Function(stop_metronome)

    vbox xalign 0.5 yalign 0.5 spacing 30:
        frame background "#222a" xpadding 50 ypadding 50:
            vbox spacing 20 xalign 0.5:
                add "metronome_anim" xalign 0.5
                text "BPM: [metronome_bpm]" size 32 color "#fff"
                text "Velocità: [metronome_bpm/60.0:.2f]x" size 20 color "#aaa"
                hbox spacing 20 xalign 0.5:
                    textbutton "No Sound" action Function(change_audio_mode, "off") text_size 28
                    textbutton "Standard Beat" action Function(change_audio_mode, "beat") text_size 28
                    textbutton "Natural 1 sound" action Function(change_audio_mode, "natural", 3) text_size 28
                hbox spacing 20 xalign 0.5:
                    textbutton "Loop Sound" action Function(change_audio_mode, "loop", 1) text_size 28
                    textbutton "Loop Sound" action Function(change_audio_mode, "loop", 2) text_size 28
                    textbutton "Loop Sound" action Function(change_audio_mode, "loop", 3) text_size 28

screen routine_screen(routine, routine_name):
    vbox xalign 0.5 yalign 0.5 spacing 30:
        frame background "#222a" xpadding 50 ypadding 50:
            vbox spacing 20 xalign 0.5:
                text "[routine_name]" size 36 color "#ff0"
                add "routine_anim" xalign 0.5
                text "BPM: [metronome_bpm]" size 32 color "#fff"
                if routine.is_running:
                    text "Segmento [routine.current_segment + 1]/[len(routine.segments)]" size 24 color "#0ff"
                    text "Tempo segmento: [int(routine.get_time_remaining())]s" size 20 color "#0f0"
                    text "Tempo totale: [int(routine.get_total_time_remaining())]s" size 20 color "#0f0"
                else:
                    text "COMPLETATA!" size 28 color "#f00"
        hbox spacing 40 xalign 0.5:            
            textbutton "Ferma" action [Function(routine.stop), Function(stop_metronome)]



screen routine_screen_with_clock(routine, routine_name):
    $ time_left = int(routine.get_total_time_remaining()) if routine.is_running else 0
    $ total_time = routine.get_initial_total_time()  # ← USA IL TEMPO TOTALE INIZIALE
    $ rotation = get_countdown_rotation(time_left, total_time)
    $ color = get_countdown_color(time_left)
    
    vbox xalign 0.5 yalign 0.5 spacing 30:
        frame background "#222a" xpadding 50 ypadding 50:
            vbox spacing 20 xalign 0.5:
                text "[routine_name]" size 36 color "#ff0"
                
                # COUNTDOWN CIRCOLARE
                fixed xysize (200, 200) xalign 0.5:
                    # Cerchio di sfondo (grigio)
                    add Solid("#333333", xysize=(180, 180)) at transform:
                        xalign 0.5
                        yalign 0.5
                        corner1 (0.5, 0.5)
                        corner2 (0.5, 0.5)
                        rotate 0
                    
                    # Cerchio progressivo (colorato)
                    add Solid(color, xysize=(180, 180)) at transform:
                        xalign 0.5
                        yalign 0.5
                        rotate rotation
                        crop (0, 0, 180, 180)
                    
                    # Numero centrale
                    text "[time_left]" size 72 color "#ffffff" xalign 0.5 yalign 0.5 bold True
                
                text "BPM: [metronome_bpm]" size 32 color "#fff"
                if routine.is_running:
                    text "Segmento [routine.current_segment + 1]/[len(routine.segments)]" size 24 color "#0ff"
                    text "Tempo totale: [int(routine.get_total_time_remaining())]s" size 20 color "#0f0"
                else:
                    text "COMPLETATA!" size 28 color "#f00"
        
        hbox spacing 40 xalign 0.5:
            textbutton "Ferma" action [Function(routine.stop), Function(stop_metronome)]
                
# 6. STILi PERSONALIZZATI


# 7. UTILITY FUNCTION


init python:
    # Caricamento frame
    frame_images = load_frames("images/frames/", extension=".gif")
    frame_images_warmup = load_frames("images/warmup/", extension=".png")
    
    metronome_animator = MetronomeAnimator(frame_images)
    warmup_animator = MetronomeAnimator(frame_images_warmup)

    def metronome_displayable(st, at):
        metronome_animator.update()
        return metronome_animator.get_current_image(), 0.016

    def routine_displayable(st, at):
        if store.active_routine:
            store.active_routine.update()
        animator = warmup_animator if store.active_routine == routine_warmup else metronome_animator
        animator.update()
        return animator.get_current_image(), 0.016

