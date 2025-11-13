# /game/3_metronome.rpy
# Metronomo base + displayable

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

image metronome_anim = DynamicDisplayable(metronome_displayable)
image routine_anim = DynamicDisplayable(routine_displayable)