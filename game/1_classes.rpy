# /game/1_classes.rpy
# Classi Python

init python:
    import threading
    import time

    class MetronomeAnimator:
        def __init__(self, frames_list):
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
            target_frame = int(progress * len(self.frames))
            target_frame = min(target_frame, len(self.frames) - 1)
            self.current_frame = target_frame


    class ProgrammedRoutine:
        def __init__(self, segments):
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
            store.active_routine = self
        
        def stop(self):
            self.is_running = False
            self.current_segment = 0
            store.active_routine = None
        
        def update(self):
            if not self.is_running:
                return
            
            current_time = time.time()
            elapsed_in_segment = current_time - self.segment_start_time
            segment_duration = self.segments[self.current_segment][0]
            
            if elapsed_in_segment >= segment_duration:
                self.current_segment += 1
                if self.current_segment >= len(self.segments):
                    self.stop()
                    store.metronome_running = False
                    return
                self.segment_start_time = current_time
                store.metronome_bpm = self.segments[self.current_segment][1]
        
        def get_time_remaining(self):
            if not self.is_running:
                return 0
            current_time = time.time()
            elapsed = current_time - self.segment_start_time
            segment_duration = self.segments[self.current_segment][0]
            return max(0, segment_duration - elapsed)
        
        def get_total_time_remaining(self):
            if not self.is_running:
                return 0
            current_time = time.time()
            elapsed_total = current_time - self.routine_start_time
            return max(0, self.total_duration - elapsed_total)