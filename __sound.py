def __Sound(sound_time):
    # --- Modules --
    from time import sleep
    import winsound
    import sys

    # --- filter sound ---
    if sound_time is None:
        sys.exit()

    else:
        # -- filter len sound_time --
        if len(sound_time) <= 1:
            sound = "d"
            time = 0
        else:
            sound = sound_time[0]
            time = int(sound_time[1:])
            
    # -------------------------------------------------------------
    # --- Sounds ---
    # - soudn defult -
    def S_d(time) -> None:
        try:
            for i in range(time):
                for f, d in [(800,150), (1000,150), (1200,200)]:
                    winsound.Beep(f, d)
                sleep(0.2)
        except KeyboardInterrupt:
            sys.exit()
            
    # - sound a -
    def S_a(time) -> None:
        try: 
            for i in range(time):
                winsound.Beep(400, 300)
                winsound.Beep(300, 300)
                sleep(0.2)
        except KeyboardInterrupt:
            sys.exit()
            
    # - sound b -
    def S_b(time) -> None:
        try:   
            for i in range(time):
                for freq, dur in [(1000, 200), (1200, 200), (1500, 400)]:
                    winsound.Beep(freq, dur)
            sleep(0.2)
        except KeyboardInterrupt:
            sys.exit()
            
    # - sound c -
    def S_c(time) -> None:
        try:
            for i in range(time):
                for f, d in [(600,150), (900,150), (600,150)]:
                    winsound.Beep(f, d)
            sleep(0.2)
        except KeyboardInterrupt:
            sys.exit()
    # ---------------------------------------------------------------
    
    # --- filter time ---
    if time == 0 or time == None:
        time = 500
    
    # --- filter sound ---
    if sound == None:
        S_d(time)
    
    elif sound == "a":
        S_a(time)
        
    elif sound == "b":
        S_b(time)
    
    elif sound == "c":
        S_c(time)
    
    else: 
        S_d(time)
        
        

