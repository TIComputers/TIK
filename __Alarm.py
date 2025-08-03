def __Alarm(hour, minute, second, zone, sound):
    # --- Module ---
    import sys
    
    # ------------------------------------------
    if hour == None: hour = 0
    if minute == None: minute = 0
    if second == None: second = 0
    if zone == None: zone = None
    # ------------------------------------------
    if hour > 24:
        print("Please enter a number less than 24 hour."), sys.exit()
    if minute >= 60: 
        print("Please enter a number less than 60 minute."), sys.exit()
    if second >= 60: 
        print("Please enter a number less than 60 seconds."), sys.exit()
    # ------------------------------------------
    def opration(h, m, s, z):
        # --- Modules ---
        from datetime import datetime
        from __help__ import __os
        from time import sleep
        import pytz
        import __sound
        
        # --- clean terminal ---
        __os()
        
        # --- start tik ----
        if zone == None:
            zone_area_s = str(datetime.now())
        else:
            area_s = pytz.timezone(z)
            utc_s = datetime.now(pytz.UTC)
            zone_area_s = str(utc_s.astimezone(area_s))
            
        # --- user input time ---
        print(f"The specified time is {hour}:{minute}:{second}\n")   
        
        # --- loop ----
        while True:
            try:
                # --------------------------------
                if zone == None:
                    zone_area = datetime.now()
                else:
                    area = pytz.timezone(z)
                    utc = datetime.now(pytz.UTC)
                    zone_area = utc.astimezone(area)
                # --------------------------------
                time = str(zone_area)
                time_hour = int(time[11:13])
                time_minute = int(time[14:16])
                time_seconde = int(time[17:19])
                
                # --- print per second ---
                sleep(0.334)
                print("\r" + time[11:19], end="")
                
                # --- The specified time ---
                if time_hour == h:
                    if time_minute == m:
                        if time_seconde == s:
                            print(f"\n\n{zone_area_s[11:19]}  {time_hour}:{time_minute}:{time_seconde}  {h}:{m}:{s}")
                            __sound.__Sound(sound)
                            sys.exit()
                            
                
            # --- press Cltr+C ---
            except KeyboardInterrupt:
                print(f"\n\n{zone_area_s[11:19]}  {time_hour}:{time_minute}:{time_seconde}  {h}:{m}:{s}")
                sys.exit()
                
    opration(hour, minute, second, zone)