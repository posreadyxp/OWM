# Imports
from pyowm import OWM
import time

logo_list = ["....................................................................................",
             ".............:-=+**#####***+=-:......................:-=++**#####**+=-:.............",
             ".........:=*#%%%%%%%%%%%%%%%%%%#+-................-+#%%%%%%%%%%%%%%%%%%#*=:.........",
             ".......-*%%%%%%%%##******##%%%%%%%#+:..........:+#%%%%%%%%#*******#%%%%%%%%*=:......",
             ".....-#%%%%%%#+-:..........:=+#%%%%%%*:......:+%%%%%%#+=:..........:-+*%%%%%%#=.....",
             "...:+%%%%%%+:..................-*%%%%%%+:...:#%%%%%#=:.................:+#%%%%%*:...",
             "..:#%%%%%*:......................-*%%%%%#-...-#%%#-......................:+%%%%%#:..",
             "..*%%%%%+..........................=%%%%%%+...:+=..........................+%%%%%*..",
             ".:%%%%%#:...........................:*%%%%%*:...............................*%%%%%-.",
             ".-%%%%%+..............................+%%%%%#-..............................=%%%%%=.",
             ".-%%%%%*...............................=%%%%%%=.............................=%%%%%=.",
             ".:#%%%%%:..........................:-...-#%%%%%*:..........................:#%%%%%-.",
             "..=%%%%%#:........................-#%=...:*%%%%%#=........................:*%%%%%+..",
             "...+%%%%%#=:....................-*%%%%*:...=#%%%%%*-.....................-#%%%%%+...",
             "....-#%%%%%#+:...............:-*%%%%%%*:....:*%%%%%%#=:...............:=#%%%%%#=....",
             ".....:+#%%%%%%#+=-::....::-+*#%%%%%%*-........-*%%%%%%%*+--:....::-=+#%%%%%%%+:.....",
             ".......:=*%%%%%%%%%%%%%%%%%%%%%%%#+-............:+#%%%%%%%%%%%%%%%%%%%%%%%*=:.......",
             "..........:-+*%%%%%%%%%%%%%%%#*+-.......SUDEV......-=*#%%%%%%%%%%%%%%%#+=:..........",
             "...............:-==+++++===-:..........................:--==+++++==-:...............",
             "...................................................................................."]


def art(logo):
    for i in logo:
        print(i)
        time.sleep(0.2)


art(logo_list)


# Funcs
def menu_print():
    print('1)Show status.')
    print('2)Show wind info.')
    print('3)Show temperature.')
    print('4)Show cloud percent.')
    print('5)Show humidity info.')


def show_status():
    print(w.detailed_status)


def wind_info():
    print(w.wind())


def temperature(choose):
    if choose == 'celsius':
        print(w.temperature('celsius'))
    elif choose == 'fahrenheit':
        print(w.temperature('fahrenheit'))
    else:
        print("Err!")


def cloud_per():
    print(w.clouds, '%')


def humidity():
    print(w.humidity)


# Settings
owm_key = input('Enter key: ')
owm = OWM(owm_key)
mgr = owm.weather_manager()
city_input = input('Enter city name: ')
observation = mgr.weather_at_place(city_input)
w = observation.weather

# Work
menu_print()
menu_choose = int(input("Choose (1-5): "))
while True:
    if menu_choose == 1:
        print("===RESULT===")
        show_status()
    elif menu_choose == 2:
        print("===RESULT===")
        wind_info()
    elif menu_choose == 3:
        print("===RESULT===")
        temperature()
    elif menu_choose == 4:
        print("===RESULT===")
        cloud_per()
    elif menu_choose == 5:
        print("===RESULT===")
        humidity()
    con_choose = input("Do you want continue (Yes/No): ")
    if con_choose == "Yes":
        pass
    elif con_choose == "No":
        print("Bye :3")
        break
    else:
        print("Err!")
