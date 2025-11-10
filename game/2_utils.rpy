# /game/2_utils.rpy
# Funzioni di utilità

init python:
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

    # Caricamento frame
    frame_images = load_frames("images/frames/", extension=".gif")
    frame_images_warmup = load_frames("images/warmup/", extension=".png")

    # Thread audio
    def audio_loop():
        while store.metronome_running:
            try:
                renpy.sound.stop()
                if renpy.loadable("audio/metronome_single.mp3"):
                    renpy.sound.play("audio/metronome_single.mp3")
                else:
                    renpy.sound.play("gui/confirm.wav")
            except:
                pass
            time.sleep(60.0 / store.metronome_bpm)

    # Controlli metronomo
    def start_metronome():
        if not store.metronome_running:
            store.metronome_running = True
            for anim in [metronome_animator, warmup_animator]:
                anim.animation_start = time.time()
                anim.current_frame = 0
            threading.Thread(target=audio_loop, daemon=True).start()

    def stop_metronome():
        store.metronome_running = False
        for anim in [metronome_animator, warmup_animator]:
            anim.current_frame = 0