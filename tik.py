import argparse
import __help__
import sys

# --- func excutble ---
def tik():
# --help
    if "--help" in sys.argv:
        __help__.__help()
        sys.exit() 

    # Display timezone
    if "--zone" in sys.argv:
        __help__.__zone()
        sys.exit()
        
    # --- Main Modes ---
    parser = argparse.ArgumentParser(description="tik", add_help=False)
    parser.add_argument("--update", action="store_true", help="isntall and upgrade pip and other pkage (pytz , colorama , ...)")
    parser.add_argument("-W", action="store_true", help="Display World Clock")
    parser.add_argument("-A", action="store_true", help="Set the Alarm")
    parser.add_argument("-S", action="store_true", help="Set the Stopwatch")
    parser.add_argument("-T", action="store_true", help="Set the Timer")

    # --- Time Settings ---
    parser.add_argument("-h", type=int, help="Set hours in the selected mode")
    parser.add_argument("-m", type=int, help="Set minutes in the selected mode")
    parser.add_argument("-s", type=int, help="Set seconds in the selected mode")
    parser.add_argument("-z", type=str, help="Set timezone for World Clock")
    parser.add_argument("-Z", type=str, help="Display timezone area -> Countries")

    # --- Sound Settings ---
    parser.add_argument("-sd", type=str, help=" Enable sound for Alarm and Stopwatch")

    # --- Set time & date ---
    parser.add_argument("--settime", action="store_true", help="Set times your computer -> Only works on Windows for now.")
    parser.add_argument("--setdate", action="store_true", help="Set dates your computer -> Only works on Windows for now.")

    args = parser.parse_args()

    # install and update path
    if args.update:
        import os
        os.system("python __path.py")

    # Display timezone
    if args.Z:
        __help__.__zone_area(args.Z)
        sys.exit()
        
    # Call func World Clock       
    if args.W:
        if args.z is not None or args.z is None or args.h is None or args.m is None or args.s is None:
            import __World_Clock
            __World_Clock.__World_Clock(args.z)    
        
    # Call func Alarm  
    if args.A:
        if args.h is not None or args.m is not None or args.s is not None or args.z is not None or args.sd is None or args.sd is not None:
            import __Alarm
            __Alarm.__Alarm(args.h, args.m, args.s, args.z, args.sd)  

    # Call func Stopwatch
    if args.S:
        if args.h is not None or args.m is not None or args.s is not None or args.sd is None or args.sd is not None:
            import __Stopwatch
            __Stopwatch.__Stopwatch(args.h, args.m, args.s, args.sd)
            
    # Call func Timer
    if args.T:
        if args.h is not None or args.m is not None or args.s is not None or args.h is None or args.m is None or args.s is None or args.sd is None or args.sd is not None:
            import __Timer
            __Timer.__Timer(args.h, args.m, args.s, args.sd)
            
    # Call func Set-time
    if args.settime:
        if args.h is not None or args.m is not None or args.s is not None or args.h is None or args.m is None or args.s is None or args.z is not None or args.z is None:
            import __Set_time
            __Set_time.__set_time(args.h, args.m, args.s, args.z)
        
    # Call func Set-date
    if args.setdate:
        if args.z is not None or args.z is None:
            import __Set_date
            __Set_date.__set_date(args.z)




# ---- main ----
if __name__ == "__main__":
    tik()