def __World_Clock(timezone):
    # --- Modules ---
    from datetime import datetime
    from __help__ import  __os
    from time import sleep
    import pytz
    import sys
    # --- clean terminal ---
    __os()
    # --- loop ---
    while True:
        try:
            if timezone == None: # --- computer time
                zone = str(datetime.now())
            else: # --- zone time
                area = pytz.timezone(timezone)
                utc = datetime.now(pytz.UTC)
                zone = str(utc.astimezone(area))
            
            # --- print time ---
            print(f"\r{zone[11:19]}", end="")
            sleep(1)

        # --- press Cltr+C ---
        except KeyboardInterrupt:
            print(f"\n\nStop to {zone[11:19]}")
            sys.exit()