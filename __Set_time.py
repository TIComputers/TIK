def __set_time(hour, minute, second, zone):
    # --- clean ---
    import __help__
    __help__.__os()
    
    # -- filter input func ---
    if hour == None: hour = 0
    if minute == None: minute = 0
    if second == None: second = 0
        
    # --- func timezone ---
    def time_zone(area_zone):
        # --- Modules ---
        from datetime import datetime
        import pytz
        import os
        
        area = pytz.timezone(area_zone)
        utc = datetime.now(pytz.UTC)
        new_time = str(utc.astimezone(area))
        print(new_time[11:19])
        input()
        os.system(f"time {new_time[11:19]}")


    # --- func handing ---
    def handing(h, m, s):
        # --- Modules ---
        import os
        import sys
        
        # --- filter ---
        if hour > 24:
            print("Please enter a number less than 24 hour."), sys.exit()
        if minute >= 60: 
            print("Please enter a number less than 60 minute."), sys.exit()
        if second >= 60: 
            print("Please enter a number less than 60 seconds."), sys.exit()

        # --- filter ---
        if h < 10: h = f"0{h}"
        else: h = f"{h}"
        if m < 10: m = f"0{m}"
        else: m = f"{m}"
        if s < 10: s = f"0{s}"
        else: s = f"{s}"
        os.system(f"time {h}:{m}:{s}")
        
    # --- func Accsse root ---    
    def __Admin():
        import ctypes, sys
        if not ctypes.windll.shell32.IsUserAnAdmin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 0); sys.exit()

    
    if zone is not None:
        __Admin()
        time_zone(zone)
    else: 
        __Admin()
        handing(hour, minute, second)
    
    
    
    