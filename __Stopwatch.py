def __Stopwatch(hour, minute, second, sound):
    # --- Modules ---
    from time import sleep
    import __sound
    import sys

    # --- clean terminal ---
    from __help__ import __os
    __os()

    # --- filter input ---
    if hour == None: hour = 0
    if minute == None: minute = 0
    if second == None: second = 0

    # --- proof time ---
    hor = hour
    min = minute
    sec = second

    # --- print during ---
    print(f"during:  {hour}:{minute}:{second}\n")

    # --- loop ---
    while True: 
        try:   
            # --- filter to stop time ---
            if second == 0:
                if minute == 0:
                    if hour == 0:
                        print(f"\n\ntime stop\nduring:  {hor}:{min}:{sec}")
                        sleep(0.1)
                        __sound.__Sound(sound)
                        sys.exit()
            
            # --- filter second ---
            if second <= 0:
                second = 60
                minute -= 1
                
            # --- filter minute ---
            if minute <= -1:
                minute = 59
                hour -= 1

            # --- counter second ---
            sleep(0.999998)
            second -= 1
            
            # --- filter second less 10 ---
            if second < 10: stable = f"0{second}"
            else: stable = second
                
            
            # --- print time ---
            print(f"\r{hour}:{minute}:{stable}", end="")
            
        # --- prese Ctrl+C ---    
        except KeyboardInterrupt:
            print(f"\n\ntime stop\nduring:  {hor}:{min}:{sec}")
            sys.exit()