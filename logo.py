import os
import time
import sys


os.system("clear")
print("\n" * 3)

loading_message = "\t\t🔃 Tools Loading..."
for char in loading_message:
    sys.stdout.write("\033[93m" + char + "\033[0m")  # Yellow
    sys.stdout.flush()
    time.sleep(0.1)

print("\n" * 3)
time.sleep(2)

os.system("clear")
print("\n" * 3)

loaded_message = "\t\t✅ Tools Loaded Successfully!"
for char in loaded_message:
    sys.stdout.write("\033[92m" + char + "\033[0m")  # Green
    sys.stdout.flush()
    time.sleep(0.1)

print("\n")

name = input("\033[96m\t\t👤 Enter Your Name: \033[0m")  # Cyan
print("\n")

welcome_message = f"👋 Hey, {name}. Be ethical. This tool is only for educational purposes!"
for char in welcome_message:
    sys.stdout.write("\033[95m" + char + "\033[0m")  # Magenta
    sys.stdout.flush()
    time.sleep(0.08)

time.sleep(3)
print("\n" * 3)
os.system("clear")

banner = f'''\033[91m
▓██   ██▓ ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███  
 ▒██  ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
  ▒██ ██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
  ░ ▐██▓░░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
  ░ ██▒▓░ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
   ██▒▒▒  ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ▓██ ░▒░   ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ▒ ▒ ░░    ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ 
 ░ ░           ░  ░░ ░      ░  ░      ░  ░   ░     
 ░ ░               ░                              
\033[96m
   █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
   █     CYBER PHANTOMS 🛡 | ESTABLISHED 2025     █
   █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
\033[93m
   ⚙️  Owner    : \033[97m{name}
\033[93m   ⚒️  Tool     : \033[97mSMS Bomber
\033[93m   🧩 Version  : \033[97mV1.0
\033[93m======================================================
\033[0m
'''

for char in banner:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.0015)

print("\n")



