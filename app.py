from colorama import Fore, Back, Style, init
import os
import time

init()

name = input (Fore.GREEN + 'Введіть ваше імя: ')
fam = input (Fore.GREEN + 'Фамілія: ')
room = input (Fore.GREEN + 'В якому в класі: ')
school = input (Fore.GREEN + 'Назва школи: ')
city = input (Fore.GREEN + 'Ваше місто: ')

os.system('cls')

print(Fore.BLUE + """

██████╗░██╗██████╗░██╗░░░░░░█████╗░███╗░░░███╗
██╔══██╗██║██╔══██╗██║░░░░░██╔══██╗████╗░████║
██║░░██║██║██████╔╝██║░░░░░██║░░██║██╔████╔██║
██║░░██║██║██╔═══╝░██║░░░░░██║░░██║██║╚██╔╝██║
██████╔╝██║██║░░░░░███████╗╚█████╔╝██║░╚═╝░██║
╚═════╝░╚═╝╚═╝░░░░░╚══════╝░╚════╝░╚═╝░░░░░╚═╝
\n\n""")

print(Fore.BLUE + f"""     Диплом
     переможця конкурсу \"Байтик\"
     Нагороджується
     {fam} {name}""")
print(Fore.YELLOW + f"""     учень {room} класу
     {school} 
     міста {city}
""")

time.sleep(2)
os.system('cls')
print(Fore.GREEN + 'Зробив за хвилин 5')
time.sleep(2)
print(Fore.GREEN + 'На олімпіади не кличте, не люблю всякі заходи')
time.sleep(2)
print(Fore.GREEN + 'Якщо не перетворю цю програму на .exe то код можна буде подивитись у файлі')
time.sleep(2)
while True:
    ocinka = input('Яка ваша оцінка?: ')
    if ocinka.isdigit() and int(ocinka) <= 12:
        if ocinka == '12':
            print(Fore.GREEN + 'О! чудово, програма закриється сама через 3 секунди')
            time.sleep(3)
            quit()
        else:
            print(Fore.RED + f"""
Ви напевно перепутали 12 з {ocinka}, даю вам ще одну спробу поставити 12
            """)
    else:
        print(Fore.RED + "Переграти мене хочте? в мене є if на перевірку числа. поставьте нормальну оцінку")

while True:
    input ()