# Struttura 
```
/game/
├── 0_init.rpy               # init python, store, default variabili globali
├── 1_classes.rpy            # Tutte le tue classi (MetronomeAnimator, ecc.)
├── 2_metronome.rpy          # Metronomo base + screen metronome()
├── 3_routines.rpy           # ProgrammedRoutine, routine predefinite
├── 4_screens.rpy            # Tutte le screen (menu, debug, routine selector)
├── 
├── chapters/
│   ├── chapter_01.rpy       # label chapter1, eventi, dialoghi
│   ├── chapter_02.rpy
│   └── common.rpy           # transizioni, setup comune tra capitoli
│
├── debug/
│   ├── menu.rpy             # menu principale di debug
│   └── tools.rpy            # comandi rapidi, skip, ecc.
│
└── main.rpy                 # label start, splashscreen, menu iniziale
```