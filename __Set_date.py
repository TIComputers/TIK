def __set_date(zone):
    # --- Modules ---
    from datetime import datetime
    import pytz, os, sys
    
    # --- filter ---
    if zone == None:
        print("please enter a timezone"), sys.exit()
            
    # --- func Accsse root ---    
    def __Admin():
        import ctypes
        if not ctypes.windll.shell32.IsUserAnAdmin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 0); sys.exit()

    # --- accsse root ---
    __Admin()
    
    # --- set timezone ---
    area = pytz.timezone(zone)
    utc = datetime.now(pytz.UTC)
    timezone = str(utc.astimezone(area))
    datezone = timezone[0:10]
    os.system(f"date {datezone}")
