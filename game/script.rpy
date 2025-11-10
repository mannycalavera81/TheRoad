## METRONOMO V10 — Con menu debug e routine programmate

default metronome_bpm = 120
default metronome_running = False

define e = Character("Eileen", color="#f44")

# ============================================
# CLASSI PYTHON E FUNZIONI
# ============================================
init python:
    import threading
    import time
    
    # Lista dei frame per il metronomo base
   
    

    def load_frames(folder_path, prefix="frame-", extension=".gif"):
        """
        Carica automaticamente tutti i frame da una cartella
        es: load_frames("images/warmup/") → carica frame-01.gif, frame-02.gif, ...
        """
        frames = []
        i = 1
        while True:
            frame_path = "{}{}{:02d}{}".format(folder_path, prefix, i, extension)
            if renpy.loadable(frame_path):
                frames.append(frame_path)
                i += 1
            else:
                break
        return frames


    frame_images = load_frames("images/frames/", extension=".gif")
    frame_images_warmup = load_frames("images/warmup/", extension=".png")



    # ============================================
    # THREAD AUDIO - Metronomo base
    # ============================================
    def audio_loop():
        """Thread dedicato SOLO all'audio - batte a tempo preciso"""
        while store.metronome_running:
            try:
                renpy.sound.stop()
                if renpy.loadable("audio/metronome_single.mp3"):
                    renpy.sound.play("audio/metronome_single.mp3")
                else:
                    renpy.sound.play("gui/confirm.wav")
            except:
                pass
            
            beat_duration = 60.0 / store.metronome_bpm
            time.sleep(beat_duration)
    
    # ============================================
    # VIDEO - Metronomo base
    # ============================================
    class MetronomeAnimator:
        def __init__(self, frames_list):  # <-- AGGIUNGI frames_list QUI
            self.frames = frames_list
            self.current_frame = 0
            self.animation_start = time.time()
            self.loaded_images = {}
        
        def get_current_image(self):
            frame_path = self.frames[self.current_frame]
            if frame_path not in self.loaded_images:
                self.loaded_images[frame_path] = renpy.displayable(frame_path)
            return self.loaded_images[frame_path]
        
        def update(self):
            if not store.metronome_running:
                self.current_frame = 0
                return
            
            current_time = time.time()
            beat_duration = 60.0 / store.metronome_bpm
            elapsed = (current_time - self.animation_start) % beat_duration
            
            progress = elapsed / beat_duration
            target_frame = int(progress * len(frame_images))
            target_frame = min(target_frame, len(self.frames) - 1)
            
            self.current_frame = target_frame
    
    metronome_animator = MetronomeAnimator(frame_images)
    warmup_animator = MetronomeAnimator(frame_images_warmup)
    
    def metronome_displayable(st, at):
        metronome_animator.update()
        img = metronome_animator.get_current_image()
        return img, 0.016
    
    # ============================================
    # CONTROLLI - Metronomo base
    # ============================================
    def start_metronome():
        if not store.metronome_running:
            store.metronome_running = True
            metronome_animator.animation_start = time.time()
            metronome_animator.current_frame = 0
            threading.Thread(target=audio_loop, daemon=True).start()
    
    def stop_metronome():
        store.metronome_running = False
        metronome_animator.current_frame = 0
    
    # ============================================
    # ROUTINE PROGRAMMATE - Sistema
    # ============================================
    class ProgrammedRoutine:
        def __init__(self, segments):
            """
            segments = lista di tuple (durata_secondi, bpm)
            es: [(10, 40), (15, 60), (15, 90)]
            """
            self.segments = segments
            self.current_segment = 0
            self.segment_start_time = 0
            self.routine_start_time = 0
            self.total_duration = sum(s[0] for s in segments)
            self.is_running = False
        
        def start(self):
            self.is_running = True
            self.current_segment = 0
            self.routine_start_time = time.time()
            self.segment_start_time = time.time()
            store.metronome_bpm = self.segments[0][1]
        
        def stop(self):
            self.is_running = False
            self.current_segment = 0
        
        def update(self):
            if not self.is_running:
                return
            
            current_time = time.time()
            elapsed_in_segment = current_time - self.segment_start_time
            segment_duration = self.segments[self.current_segment][0]
            
            # Se il segmento è finito, passa al prossimo
            if elapsed_in_segment >= segment_duration:
                self.current_segment += 1
                
                # Se finiti tutti i segmenti, ferma
                if self.current_segment >= len(self.segments):
                    self.stop()
                    store.metronome_running = False
                    return
                
                # Imposta il nuovo BPM
                self.segment_start_time = current_time
                store.metronome_bpm = self.segments[self.current_segment][1]
        
        def get_time_remaining(self):
            """Ritorna secondi rimanenti nel segmento corrente"""
            if not self.is_running:
                return 0
            current_time = time.time()
            elapsed = current_time - self.segment_start_time
            segment_duration = self.segments[self.current_segment][0]
            return max(0, segment_duration - elapsed)
        
        def get_total_time_remaining(self):
            """Ritorna secondi rimanenti totali nella routine"""
            if not self.is_running:
                return 0
            current_time = time.time()
            elapsed_total = current_time - self.routine_start_time
            return max(0, self.total_duration - elapsed_total)
    
    # Crea animator separati
    metronome_animator = MetronomeAnimator(frame_images)
    warmup_animator = MetronomeAnimator(frame_images_warmup)
    
    # Istanze delle routine
    routine_warmup = ProgrammedRoutine([
        (10, 40),   # 10 secondi a 40 BPM
        (15, 60),   # 15 secondi a 60 BPM
        (15, 90),   # 15 secondi a 90 BPM
        (15, 120),  # 15 secondi a 120 BPM
        (5, 150)    # 5 secondi a 150 BPM
    ])
    
    routine_intense = ProgrammedRoutine([
        (5, 100),   # 5 secondi a 100 BPM
        (10, 140),  # 10 secondi a 140 BPM
        (15, 180),  # 15 secondi a 180 BPM
        (10, 140),  # 10 secondi a 140 BPM
        (5, 100)    # 5 secondi a 100 BPM
    ])
    
    def routine_displayable(st, at):
        if hasattr(store, 'active_routine') and store.active_routine:
            store.active_routine.update()
    
        # USA L'ANIMATOR GIUSTO:
        if store.active_routine == routine_warmup:
            animator = warmup_animator
        else:
            animator = metronome_animator
        
        animator.update()
        img = animator.get_current_image()
        return img, 0.016


# ============================================
# IMMAGINI
# ============================================
image metronome_anim = DynamicDisplayable(metronome_displayable)
image routine_anim = DynamicDisplayable(routine_displayable)


# ============================================
# MENU DEBUG - PUNTO DI PARTENZA
# ============================================
label start:
    scene bg room
    
    menu:
        "🔧 DEBUG MENU - Scegli dove andare:"
        
        "Metronomo Base":
            jump metronome_main
        
        "Pagina 2 - GIF Animata":
            jump page2a
        
        "Routine 1 - Warm Up (1 minuto)":
            jump routine_warmup_page
        
        "Routine 2 - Intense (45 secondi)":
            jump routine_intense_page

    
    return


# ============================================
# METRONOMO BASE
# ============================================
label metronome_main:
    scene bg room
    show eileen happy
    
    show screen metronome_screen
    
    e "Questo è il metronomo base con controllo manuale del BPM!"
    
    menu:
        "Torna al menu debug":
            hide screen metronome_screen
            jump start
        
        "Vai alla pagina GIF":
            hide screen metronome_screen
            jump page2a
    
    return

screen metronome_screen():
    on "show" action Function(start_metronome)
    on "hide" action Function(stop_metronome)

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        frame:
            background "#222a"
            xpadding 50
            ypadding 50
            vbox:
                spacing 20
                xalign 0.5

                add "metronome_anim" xalign 0.5 yalign 0.5
                text "BPM: [metronome_bpm]" xalign 0.5 size 32 color "#fff"
                
                if metronome_running:
                    text "Frame: [metronome_animator.current_frame]/38" xalign 0.5 size 20 color "#0f0"
                else:
                    text "FERMO" xalign 0.5 size 20 color "#f00"

                hbox:
                    spacing 20
                    xalign 0.5
                    textbutton "−" action SetVariable("metronome_bpm", max(20, metronome_bpm - 5)) text_size 28
                    textbutton "+" action SetVariable("metronome_bpm", min(240, metronome_bpm + 5)) text_size 28

        hbox:
            spacing 40
            xalign 0.5
            textbutton "Avvia" action Function(start_metronome)
            textbutton "Ferma" action Function(stop_metronome)


# ============================================
# PAGINA 2 - GIF ANIMATA
# ============================================
label page2a:
    scene bg room
    
    show screen gif_control_screen_a
    
    e "Questa è la pagina con la GIF animata!"
    "La velocità si adatta al BPM."
    
    menu:
        "Torna al menu debug":
            hide screen gif_control_screen_a
            jump start
        
        "Vai al metronomo base":
            hide screen gif_control_screen_a
            jump metronome_main
    
    return

screen gif_control_screen_a():
    on "show" action Function(start_metronome)
    on "hide" action Function(stop_metronome)

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        frame:
            background "#222a"
            xpadding 50
            ypadding 50
            vbox:
                spacing 20
                xalign 0.5

                add "metronome_anim" xalign 0.5 yalign 0.5

                text "BPM: [metronome_bpm]" xalign 0.5 size 32 color "#fff"
                text "Velocità: [metronome_bpm/60.0:.2f]x" xalign 0.5 size 20 color "#aaa"

                hbox:
                    spacing 20
                    xalign 0.5
                    textbutton "−" action SetVariable("metronome_bpm", max(20, metronome_bpm - 5)) text_size 28
                    textbutton "+" action SetVariable("metronome_bpm", min(240, metronome_bpm + 5)) text_size 28


# ============================================
# ROUTINE 1 - WARM UP
# ============================================
label routine_warmup_page:
    $ active_routine = routine_warmup
    $ routine_warmup.start()
    $ start_metronome()
    
    scene bg room
    show screen routine_screen(routine_warmup, "Warm Up")
    
    e "Routine Warm Up avviata!"
    "Durata totale: 1 minuto"
    "10s@40bpm → 15s@60bpm → 15s@90bpm → 15s@120bpm → 5s@150bpm"
    
    # Attendi che la routine finisca
    while routine_warmup.is_running:
        pause 0.1
    
    $ stop_metronome()
    hide screen routine_screen
    
    "Routine completata!"
    
    menu:
        "Torna al menu debug":
            jump start
        
        "Ripeti routine":
            jump routine_warmup_page
    
    return


# ============================================
# ROUTINE 2 - INTENSE
# ============================================
label routine_intense_page:
    $ active_routine = routine_intense
    $ routine_intense.start()
    $ start_metronome()
    
    scene bg room
    show screen routine_screen(routine_intense, "Intense")
    
    e "Routine Intense avviata!"
    "Durata totale: 45 secondi"
    "5s@100bpm → 10s@140bpm → 15s@180bpm → 10s@140bpm → 5s@100bpm"
    
    # Attendi che la routine finisca
    while routine_intense.is_running:
        pause 0.1
    
    $ stop_metronome()
    hide screen routine_screen
    
    "Routine completata!"
    
    menu:
        "Torna al menu debug":
            jump start
        
        "Ripeti routine":
            jump routine_intense_page
    
    return


# ============================================
# SCREEN ROUTINE PROGRAMMATE
# ============================================
screen routine_screen(routine, routine_name):
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        frame:
            background "#222a"
            xpadding 50
            ypadding 50
            vbox:
                spacing 20
                xalign 0.5

                text "[routine_name]" xalign 0.5 size 36 color "#ff0"
                
                add "routine_anim" xalign 0.5 yalign 0.5
                
                text "BPM: [metronome_bpm]" xalign 0.5 size 32 color "#fff"
                
                if routine.is_running:
                    text "Segmento [routine.current_segment + 1]/[len(routine.segments)]" xalign 0.5 size 24 color "#0ff"
                    text "Tempo segmento: [int(routine.get_time_remaining())]s" xalign 0.5 size 20 color "#0f0"
                    text "Tempo totale: [int(routine.get_total_time_remaining())]s" xalign 0.5 size 20 color "#0f0"
                else:
                    text "COMPLETATA!" xalign 0.5 size 28 color "#f00"
        
        hbox:
            spacing 40
            xalign 0.5
            textbutton "Ferma" action [Function(routine.stop), Function(stop_metronome)]