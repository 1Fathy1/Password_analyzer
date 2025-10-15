import math
import secrets
import string
import argparse
import datetime

import pyfiglet
from colorama import Fore, init
from datetime import datetime

init(autoreset=True)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def character_range(password):

    have_digit = 0
    have_lower = 0
    have_upper = 0
    have_symple = 0

    for char in password :
        if char.isdigit():
            have_digit = 10
        elif char.isalpha():
            if char.isupper():
                have_upper = 26
            else:
                have_lower = 26
        else:
            ## symple
            have_symple = 32

        if have_digit and have_upper and have_lower and have_symple:
            break

    total_range = have_digit + have_lower + have_symple + have_upper
    result = {
         "have_digit": bool(have_digit),
         "have_lower": bool(have_lower) ,
         "have_symple": bool(have_symple),
         "have_upper": bool(have_upper),
         "total_range" : total_range
    }

    return result

def cal_bit_of_entropy(length, total_character_range):
    return length * math.log2(total_character_range)

def password_strength(bit):
    if bit < 40.0:
        return "weak"
    elif bit < 70.0:
        return "Moderate"
    elif bit < 90.0:
        return "Strong"

    return "Very Strong"

def why_weak_password(information_password, password) :
        print(f"[-] Why your password is weak")
        reason = ''
        if not information_password['have_digit'] :
            reason += "[-] Your Password no have any digit.\n"

        if not information_password['have_lower']:
            reason += "[-] Your Password no have any lowercase letter.\n"

        if not information_password['have_upper'] :
            reason += "[-] Your Password no have any uppercase.\n"

        if not information_password['have_symple'] :
            reason += "[-] Your Password no have any symple.\n"

        if len(password) < 8:
            reason += "[-] Your Password have a small length.\n"

        print(reason)

def main_process(password, admin_mode = False):

    password = password.strip()
    information_password = character_range(password)
    bit_of_enr = cal_bit_of_entropy(len(password), information_password['total_range'])

    print(f"[+] Password is {password}")
    print(f"[+] Length of password is {len(password)}")
    print(f'[+] Bit of Entropy is {bit_of_enr}')
    print(f'[+] Password Strength is {password_strength(bit_of_enr)}')
    print(f'[+] Hacker need to try {math.pow(2, bit_of_enr):.0f} times to crack your password')
    print()

    if bit_of_enr < 40.0:
        why_weak_password(information_password, password)

    if admin_mode:
        print(f"[+] suggest strong passwords")
        print(generate_password(12))
        print(generate_password(12))
        print(generate_password(12))

    print("You can see your history in file `log`, or try python3 main.py --history")

    print("__________________________")
    print()

    try:
       with open("log", "a", encoding='utf-8') as f:
          f.write(f"Password: {password} | Entropy: {bit_of_enr:.2f} | Strength: {password_strength(bit_of_enr)} | at time {datetime.now()}\n")
    except FileNotFoundError:
        print("File not found!")


def banner():
    ascii_banner = pyfiglet.figlet_format("PASSWORD ANALYZER")
    print(Fore.RED + ascii_banner)

    print(Fore.YELLOW  + "=" * 60)
    print(Fore.GREEN   + "[*]  Password Strength Analyzer v1.0")
    print(Fore.YELLOW  + "[*]  Developed by Fathy Moamen")
    print(Fore.CYAN    + f"[*]  Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(Fore.MAGENTA + "[*]  GitHub: https://github.com/1Fathy1")
    print(Fore.YELLOW  + "=" * 60)



def main():
    banner()
    parser = argparse.ArgumentParser(description="Password Strength Analyzer")

    parser.add_argument("--password", type= str, help="- Password to analyze")
    parser.add_argument("--file", type= str, help="- List of password to analyze")
    parser.add_argument("--history", action="store_true" , help="- Show history password")
    parser.add_argument("--admin", action="store_true", help="- Make administrator password")
    parser.add_argument("--clear", action="store_true", help="- Clear log file")

    args = parser.parse_args()
    args.history = True

    if args.password :
        password = args.password
        main_process(password)

    elif args.file :
        try:
            with open(args.file, mode= 'r', encoding= 'utf-8') as file:
                for line in file:
                    password = line.strip()

                    if password:
                        main_process(password)
                file.close()
        except FileNotFoundError:
            print("File not found!")

    elif args.admin:
        print(f"[+] Enter admin mode")
        password = generate_password(15)
        main_process(password)

    elif args.history:
        print("[+] You history : ")
        print("-----------------------------\n")
        with open('log', 'r', encoding='utf-8') as file :
            for line in file:
                print(f"[+] {line}")
    elif args.clear:
        print("[-] you will deleted log file, after this option you can't recover it")
        fl = input("Are you sure ? Y/N")
        if fl == 'Y' :
            with open("log", 'w', encoding='utf-8') as file:
                file.write("")
                file.close()
            print("[+] delted history success")

        elif fl == 'N':
            exit()
        else:
            print("Invalid option, please try agin")

    else:
        print("[-] Please provide any flag\n[-] Try `python3 main.py --help` to more information")

if __name__ == '__main__' :
	main()

