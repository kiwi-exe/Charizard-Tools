import requests
import os

logo = """ 
\033[38;2;255;0m ██████████                                                       ███████████                   ████         
\033[38;2;255;128;0m░░███░░░░███                                                     ░█░░░███░░░█                  ░░███         
\033[38;2;255;255;0m ░███   ░░███ ████████   ██████    ███████  ██████  ████████     ░   ░███  ░   ██████   ██████  ░███   █████ 
\033[38;2;128;255;0m ░███    ░███░░███░░███ ░░░░░███  ███░░███ ███░░███░░███░░███        ░███     ███░░███ ███░░███ ░███  ███░░  
\033[38;2;0;255;0m ░███    ░███ ░███ ░░░   ███████ ░███ ░███░███ ░███ ░███ ░███        ░███    ░███ ░███░███ ░███ ░███ ░░█████ 
\033[38;2;0;255;128m ░███    ███  ░███      ███░░███ ░███ ░███░███ ░███ ░███ ░███        ░███    ░███ ░███░███ ░███ ░███  ░░░░███
\033[38;2;0;128;255m ██████████   █████    ░░████████░░███████░░██████  ████ █████       █████   ░░██████ ░░██████  █████ ██████ 
\033[38;2;255;255;255m░░░░░░░░░░   ░░░░░      ░░░░░░░░  ░░░░░███ ░░░░░░  ░░░░ ░░░░░       ░░░░░     ░░░░░░   ░░░░░░  ░░░░░ ░░░░░░  
"""
red = "\033[38;2;255;0;0m"
white = "\033[38;2;255;255;255m"
blue = "\033[38;2;0;128;255m"
reset = "\033[0m"


def cool_input(prompt):
    return input(f"{red}┌──({white}Dragon Tools{red})[{blue}~{red}] \n└─$ {reset}{prompt}")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    clear_screen()
    print(logo)
    print("[1] IP Lookup")	
    print("[2] Port Scanner")
    print("[3] DNS Lookup")
    print("[4] Exit")
    
    x = cool_input("Enter the tool you want to use: ")

    if x == "1":
        clear_screen()
        print("IP Lookup\n")
        ip = cool_input("Enter the IP Address: ")
        
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}")
            data = response.json()
            
            if data["status"] == "success":
                print("\nRESULTS\n")
                print(f"\033[38;2;255;255;255mCountry:\033[38;2;255;255;255m {data.get('country', 'N/A')}")
                print(f"\033[38;2;255;255;255mCity:\033[38;2;255;255;255m {data.get('city', 'N/A')}")
                print(f"\033[38;2;255;255;255mRegion:\033[38;2;255;255;255m {data.get('regionName', 'N/A')}")
                print(f"\033[38;2;255;255;255mTimezone:\033[38;2;255;255;255m {data.get('timezone', 'N/A')}")
                print(f"\033[38;2;255;255;255mISP:\033[38;2;255;255;255m {data.get('isp', 'N/A')}")
                print(f"\033[38;2;255;255;255mAS:\033[38;2;255;255;255m {data.get('as', 'N/A')}")
                print(f"\033[38;2;255;255;255mLatitude:\033[38;2;255;255;255m {data.get('lat', 'N/A')}")
                print(f"\033[38;2;255;255;255mLongitude:\033[38;2;255;255;255m {data.get('lon', 'N/A')}")
            else:
                print("\nError: Invalid IP or API limit reached.")

        except Exception as e:
            print(f"\nError: {e}")

        input("\nPress Enter to return...") 

    elif x == "4":
        break



