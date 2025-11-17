# /game/2_utils.rpy
# Funzioni di utilità


init python:


    import pygame
    import math
    import io
    import threading
    import time

    # Libreria suoni naturali
    NATURAL_SOUNDS = {
        1: "audio/wow.mp3",
        2: "audio/rauf.mp3",
        3: "audio/cip.mp3",
        4: "audio/bau.mp3"
    }

        # Libreria loop continui
    LOOP_SOUNDS = {
        1: "audio/loop.mp3",
        2: "audio/ambient_loop.mp3",
        3: "audio/nature_loop.mp3"
    }

    def reset_to_debug():
        renpy.scene()  # Pulisce sfondi/personaggi (layer master)
        renpy.hide_screen("*")  # Nasconde TUTTE le screen
        renpy.show_screen("debug_menu_screen")  # Mostra solo il menu
    
    def show_debug_menu():
        renpy.show_screen("debug_menu_screen")
        
    def load_frames(folder_path, prefix="frame-", extension=".gif"):
        frames = []
        i = 1
        while True:
            frame_path = f"{folder_path}{prefix}{i:02d}{extension}"
            if renpy.loadable(frame_path):
                frames.append(frame_path)
                i += 1
            else:
                break
        return frames    

    # Thread audio
    def audio_loop():
        while store.metronome_running:
            try:
                # Ottieni la modalità audio (default "off")
                audio_mode = getattr(store, 'metronome_audio_mode', 'off')
                
                if audio_mode == "off":
                    # Nessun suono
                    pass
                    
                elif audio_mode == "beat":
                    # Suono metronomo beat
                    renpy.sound.stop()
                    if renpy.loadable("audio/metronome_single.mp3"):
                        renpy.sound.play("audio/metronome_single.mp3")
                    else:
                        renpy.sound.play("gui/confirm.wav")  # Fallback
                        
                elif audio_mode == "natural":
                    # Suono naturale da libreria
                    renpy.sound.stop()
                    sound_index = getattr(store, 'natural_sound_index', 1)
                    sound_file = NATURAL_SOUNDS.get(sound_index, "audio/wow.mp3")
                    
                    if renpy.loadable(sound_file):
                        renpy.sound.play(sound_file)
                    else:
                        renpy.sound.play("gui/confirm.wav")  # Fallback
                        
            except Exception as e:
                print(f"Audio loop error: {e}")
                pass
                
            time.sleep(60.0 / store.metronome_bpm)

    # Controlli metronomo
    def start_metronome():
        if not store.metronome_running:
            store.metronome_running = True
            for anim in [metronome_animator, warmup_animator]:
                anim.animation_start = time.time()
                anim.current_frame = 0
               
            # Gestione audio
            audio_mode = getattr(store, 'metronome_audio_mode', 'off')
            
            if audio_mode == "loop":
                # Avvia loop continuo su canale music
                loop_index = getattr(store, 'loop_sound_index', 1)
                loop_file = LOOP_SOUNDS.get(loop_index, "audio/loop.mp3")
                
                if renpy.loadable(loop_file):
                    renpy.music.play(loop_file, channel="music", loop=True, fadein=0.5)
                else:
                    print(f"Loop file non trovato: {loop_file}")
            else:
                # Avvia thread per one-shot
                threading.Thread(target=audio_loop, daemon=True).start()



    def stop_metronome():
        store.metronome_running = False
        # Dai tempo al thread di uscire dal loop
        time.sleep(0.1)
        for anim in [metronome_animator, warmup_animator]:
            anim.current_frame = 0     

        # Ferma TUTTI gli audio
        try:
            renpy.music.stop(channel="music", fadeout=0.5)
            renpy.sound.stop()
        except:
            pass

    def change_audio_mode(mode, sound_index=1):
        """Cambia modalità audio durante l'esecuzione"""
        was_running = store.metronome_running
        
        if was_running:
            stop_metronome()
        
        store.metronome_audio_mode = mode
        
        if mode == "natural":
            store.natural_sound_index = sound_index
        elif mode == "loop":
            store.loop_sound_index = sound_index
        
        if was_running:
            start_metronome()




## ===== FUNZIONI UTILITY =====

init python:
    def quick_roll(sides=6):
        """Lancia un dado e ritorna il risultato senza UI"""
        return dice.roll(sides)
    
    def roll_multiple(num_dice=2, sides=6):
        """Lancia più dadi"""
        results = [random.randint(1, sides) for _ in range(num_dice)]
        return results
    
    def roll_with_modifier(sides=6, modifier=0):
        """Lancia un dado con modificatore"""
        return dice.roll(sides) + modifier

    def get_countdown_rotation(time_remaining, total_time):
        """Calcola la rotazione del cerchio in base al tempo"""
        if total_time <= 0:
            return 0
        progress = time_remaining / total_time
        return int(progress * 360)

    def get_countdown_color(time_remaining):
        """Restituisce il colore in base al tempo rimasto"""
        if time_remaining > 30:
            return "#00ff00"  # Verde
        elif time_remaining > 10:
            return "#ffff00"  # Giallo
        elif time_remaining > 5:
            return "#ff9900"  # Arancione
        else:
            return "#ff0000"  # Rosso

 



 
    