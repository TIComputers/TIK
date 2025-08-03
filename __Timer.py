def __Timer(hour, minute, secound, sound):
    # --- filter ---
    if hour is None and minute is None and secound is None:
        from __help__ import __help
        __help()
        print("Please Enter Time")
        exit()

    # --- filter ---
    if hour == None: hour = 0
    if minute == None: minute = 0
    if secound == None: secound = 0

    # --- filter ---
    if hour > 10:
        print("Please enter a number less than 10 hour."), exit()
    if minute >=60: 
        print("Please enter a number less than 60 minute."), exit()
    if secound >= 60: 
        print("Please enter a number less than 60 seconds."), exit()

    # -------------------------
    def opration(h, m, s):
        # --- Modules ---
        from datetime import datetime
        from time import sleep
        from __help__ import __os
        import __sound
        import sys
        # --- clean ---
        __os()
        
        # --- print time input ---
        print(f"The specified time is {h}:{m}:{s}\n")

        # --- start time for accurcy ---
        start = datetime.now()

        # --- loop ---
        while True:
            try:
                # --- counter ++ ---
                sleep(0.334)

                # --- opration for accurcy --
                end = datetime.now()
                op = str(end - start)

                # --- print timer ---
                print("\r" + op[0:7], end="")

                # --- stop timer ---
                if int(op[0]) == h:
                    if int(op[2:4]) == m:
                        if int(op[5:7]) == s:
                            print(f"\n\nTime stop to {op[0:7]}")
                            __sound.__Sound(sound)
                            sys.exit()

            # --- press Cltr+C ---    
            except KeyboardInterrupt:
                print(f"\n\nTime stop to {op[0:7]}")
                sys.exit()
        
    opration(hour, minute, secound)