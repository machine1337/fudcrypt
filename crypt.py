import os
import platform
import random
import string
import time
if platform.system().startswith("Windows"):
    try:
        from pystyle import *
    except ImportError:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *
elif platform.system().startswith("Linux"):
    try:
        from pystyle import *
    except ImportError:
        os.system("python3 -m pip install pystyle -q -q -q")
        from pystyle import *

banner = Center.XCenter(r"""
**********************************************************************
*     _______ _   _ ____         ____ ______   ______ _______        *
*    / /  ___| | | |  _ \       / ___|  _ \ \ / /  _ \_   _\ \       *
*   | || |_  | | | | | | |_____| |   | |_) \ V /| |_) || |  | |      *
*  < < |  _| | |_| | |_| |_____| |___|  _ < | | |  __/ | |   > >     *
*   | ||_|    \___/|____/       \____|_| \_\|_| |_|    |_|  | |      *
*    \_\                                                   /_/       *
*                       PYTHON BASED FUD OBFUSCATOR                  *
*                          Coded By: Machine1337                     *
**********************************************************************                        
""")
value1 = 1
value2 = 100

hexnum = random.randint(value1, value2)

os.system('cls' if os.name == 'nt' else 'clear')
print(Colorate.Vertical(Colors.red_to_purple, banner, 2))
try:
    input_file = input(Colorate.Vertical(Colors.green_to_yellow, f"\n[*] Enter Path Of Payload File:- ", 2))
    if not os.path.exists(input_file):
        print(Colors.red + "\n[*] Payload File Not Exists")
        exit()
    with open(input_file, "r") as f:
        original_code = f.read()

    varname = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    print(Colors.yellow + "\n[*] File Validation Success!")
    time.sleep(1)


    def encode_text(text, key):
        encoded_text = []
        for character in text:
            encoded_character = ord(character) + key
            encoded_text.append(f"{encoded_character}")
        return ', '.join(encoded_text)


    print(Colors.blue + "\n[*] File Encryption Started....!")
    semicode = encode_text(original_code, hexnum)
    time.sleep(1)
    junk_lines = [''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(50)) for _ in range(10)]
    junk_code = '\n'.join(['# ' + line for line in junk_lines])
    print(Colors.cyan + "\n[*] Adding Junk Code....!")
    output_file = "obfuscated_code.py"
    with open(output_file, "w") as f:
        f.write(f"\n#{junk_code}\n")
        f.write(f"{varname} = [")
        f.write(semicode)
        f.write("]\n")
        f.write(f"{varname} = ''.join([chr(int(x) - {hexnum}) for x in {varname}])\n")
        f.write(f"\n#{junk_code}\n")
        f.write(f"exec({varname})\n")
        f.write(f"\n#{junk_code}\n")
    print(Colorate.Vertical(Colors.green_to_yellow, f"\n[*] File Successfully Encrypted as {output_file}", 2))
except KeyboardInterrupt:
    print(Colors.red+"\n[*] You Pressed The Exit Button!")
