# --- clean terminal ---
def __os():
    from platform import system
    import os
    if system() == "Windows":
        return os.system("cls")
    else:
        return os.system("clear")
    
# --- animation tik tik tik ---
def __tik(time, speed):
    from time import sleep
    for i in range(time):
        sleep(0.1)
        for j in range(1, 4):
            print(f"\r{"." * j}", end="")
            sleep(0.2)
    print("")
   
def __help():
    __tik(1, 0.13)
    __os()
    menu = '''
 tik                      Start tik program
 --help                   Display options for tik
 --update                 isntall and upgrade pip and other pkage (pytz , colorama , ...)
 
--- Main Modes ---
 -W                       Display World Clock
 -A                       Set the Alarm 
 -S                       Set the Stopwatch
 -T                       Set the Timer

--- Time Settings ---
 -h                       Set hours in the selected mode
 -m                       Set minutes in the selected mode
 -s                       Set seconds in the selected mode
 -z                       Set timezone for World Clock & Alarm
 --settime                Set times your computer -> Only works on Windows for now
 --setdate                Set dates your computer -> Only works on Windows for now
 --zone                   Display available timezones

--- Display Timezones ---
 --zone                   Show timezone continents -> Countries and cities
 -Z Asia                  Display Asia timezones
 -Z Europe                Display Europe timezones
 -Z America               Display America timezones
 -Z Africa                Display Africa timezones
 -Z Australia             Display Australia & Pacific timezones
 -Z North                 Display North Pole timezone (Arctic - unofficial)
 -Z South                 Display South Pole timezones (Antarctica)

--- Sound Options ---
 -sd                      Enable sound for Alarm and Stopwatch & Timer (plya defult sound)
 -sd a3                   Play sound a for play 3 time
 -sd b2                   Play sound b for play 2 time
 -sd c                    Play sound c for plya unlimite time
 
--- Usage Examples ---
 tik -A -h 1              Set Alarm for 1 hour
 tik -T -m 30             Set Timer for 30 minutes
 tik -Z Asia              Display Asia timezones
 tik -W -z Europe/Athens  Display time in the Europe/Athens

Notes:
- Please first Enter command `--update` for install and update path 
- Font options can be placed anywhere in the command
- Use the `--zone` section alone to explore all timezone categories
- If you get an error Use `--update`
- Defult font: `NormalFont`
- To stop tik, press (Ctrl+C)
- For set time please enter all command (-h -m -s)
- You have 4 sound effect -> -sd `a`, `b`, `c`, `defult (Other words)` 
- Enter command four sound Please follow the order
- For set date time please enter timezone ( --setdate -z Europe/Amsterdam )
'''
    print(menu)
    
    
    
    
def __zone():
    __os()
    zones = '''
--- Display Timezones ---
 --zone                   Show timezone continents --> Countries and cities
 -Z Asia                  Display Asia timezones
 -Z Europe                Display Europe timezones
 -Z America               Display America timezones
 -Z Africa                Display Africa timezones
 -Z Australia             Display Australia & Pacific timezones
 -Z North                 Display North Pole timezone (Arctic - unofficial)
 -Z South '''
    print(zones)




def __Asia():
    __os()
    zones = '''
 -z Asia/Almaty
 -z Asia/Baghdad
 -z Asia/Baku
 -z Asia/Bangkok
 -z Asia/Dhaka
 -z Asia/Dubai
 -z Asia/Hong_Kong
 -z Asia/Islamabad        Not IANA official, use Asia/Karachi
 -z Asia/Jakarta
 -z Asia/Jerusalem
 -z Asia/Kabul
 -z Asia/Karachi
 -z Asia/Kathmandu
 -z Asia/Kolkata
 -z Asia/Manila
 -z Asia/Novosibirsk
 -z Asia/Riyadh
 -z Asia/Seoul
 -z Asia/Shanghai
 -z Asia/Singapore
 -z Asia/Tehran
 -z Asia/Tbilisi
 -z Asia/Tokyo
 -z Asia/Urumqi
 -z Asia/Yerevan

Please copy this...'''
    print(zones)
    
    
def __Africa():
    __os()
    zones = '''
 -z Africa/Accra
 -z Africa/Addis_Ababa
 -z Africa/Algiers
 -z Africa/Bamako
 -z Africa/Cairo
 -z Africa/Casablanca
 -z Africa/Dakar
 -z Africa/Harare
 -z Africa/Johannesburg
 -z Africa/Khartoum
 -z Africa/Lagos
 -z Africa/Luanda
 -z Africa/Nairobi
 -z Africa/Tripoli
 -z Africa/Tunis
 -z Africa/Windhoek

Please copy this...'''
    print(zones)


def __Australia():
    __os()
    zones = '''
 -z Australia/Adelaide
 -z Australia/Brisbane
 -z Australia/Darwin
 -z Australia/Hobart
 -z Australia/Melbourne
 -z Australia/Perth
 -z Australia/Sydney
 -z Pacific/Auckland           New Zealand
 -z Pacific/Fiji
 -z Pacific/Guam
 -z Pacific/Port_Moresby

Please copy this...'''
    print(zones)


def __America():
    __os()
    zones = '''
 -z America/Anchorage
 -z America/Argentina/Buenos_Aires
 -z America/Bogota
 -z America/Caracas
 -z America/Chicago
 -z America/Denver
 -z America/El_Salvador
 -z America/Guatemala
 -z America/Halifax
 -z America/Lima
 -z America/Los_Angeles
 -z America/Managua
 -z America/Mexico_City
 -z America/Montevideo
 -z America/New_York
 -z America/Phoenix
 -z America/Sao_Paulo
 -z America/Toronto
 -z America/Vancouver

Please copy this...'''
    print(zones)


def __Europe():
    __os()
    zones = '''
 -z Europe/Amsterdam
 -z Europe/Athens
 -z Europe/Belgrade
 -z Europe/Berlin
 -z Europe/Bucharest
 -z Europe/Copenhagen
 -z Europe/Helsinki
 -z Europe/Istanbul
 -z Europe/Kiev
 -z Europe/Lisbon
 -z Europe/London
 -z Europe/Madrid
 -z Europe/Moscow
 -z Europe/Oslo
 -z Europe/Paris
 -z Europe/Prague
 -z Europe/Rome
 -z Europe/Sofia
 -z Europe/Stockholm
 -z Europe/Vienna
 -z Europe/Warsaw
 -z Europe/Zurich

Please copy this...'''
    print(zones)


def __South_Pole():
    __os()
    zones = '''
 -z Antarctica/McMurdo         Uses New Zealand Time (NZT)
 -z Antarctica/Palmer          Based on South American Time (e.g., UTC−3)
 -z Antarctica/South_Pole      Usually follows UTC or New Zealand Time (NZT)

Please copy this...'''
    print(zones)


def __North_Pole():
    __os()
    zones = '''
 -z Arctic/Longyearbyen       Often used for North Pole; based on Europe/Oslo

Please copy this...'''
    print(zones)


def __zone_area(zone):
    __os()
    if zone == "Asia":
        __Asia()
    elif zone == "Europe":
        __Europe()
    elif zone == "America":
        __America()
    elif zone == "Africa":
        __Africa()
    elif zone == "Australia":
        __Australia()
    elif zone == "North":
        __North_Pole()
    elif zone == "South":
        __South_Pole()    
    else:
        print(f"'{zone}' is not a recognized zone.")