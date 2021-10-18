import os
import socket
os.system("sshd")

def ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


banner ="""
 \033[32m

  ______    ______        
 /      \  /      \ |  \  |  \\
|  $$$$$$\|  $$$$$$\| $$  | $$
| $$___\$$| $$___\$$| $$__| $$
 \$$    \  \$$    \ | $$    $$
 _\$$$$$$\ _\$$$$$$\| $$$$$$$$
|  \__| $$|  \__| $$| $$  | $$s
 \$$    $$ \$$    $$| $$  | $$
  \$$$$$$   \$$$$$$  \$$   \$$


"""
print(banner)
print("\033[34mSet password for ssh\n\n")

print("\033[33m")
os.system("passwd")
print("\n\033[34mThis is your username \033[34m")

print("\033[33m")
os.system("whoami")
print("\n")

print("\033[34mWrite this in another terminal for connecting\n")
print("\033[31m"+"ssh "+os.getlogin() + "@" + ip() + "   -p8022" + "\n")

