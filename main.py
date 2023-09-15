import sqlite3
import os
from colorama import init
from termcolor import colored
import cu

init()

green = 'green'
cyan = 'cyan'

print(colored("Medusa Script", 'magenta'))
print(colored("version: 23.1", 'magenta'))
print(colored("by Mikey.dev", 'magenta'))
print()

while 1:
    commands = input(colored(f"{cu.cu} ", green))
    if commands.startswith('d '):
        try:
            db = sqlite3.connect('base.db')
            sql = db.cursor()

            sql.execute(f"{commands[2:]}")
            db.commit()
        except Exception as e:
            print('Error: ' + e)

    elif commands.startswith('g '):
        try:
            db = sqlite3.connect('base.db')
            sql = db.cursor()
        
            data = sql.execute(f"{commands[2:]}").fetchall()
            print(f'{data}')
        except Exception as e:
            print('Error: ' + e)

    elif commands.startswith('3 '):
        try:
            db = sqlite3.connect('base.db')
            sql = db.cursor()
            print()
            for data in sql.execute(f"{commands[2:]}").fetchall():
                print(colored(f'{data[0]}.', green), colored(f'{data[1]} {data[2]}', cyan))
        except Exception as e:
            print('Error: ' + e)

    elif commands.startswith('2 '):
        try:
            db = sqlite3.connect('base.db')
            sql = db.cursor()
            print()
        
            for data in sql.execute(f"{commands[2:]}").fetchall():
                print(colored(f'{data[0]}.', green), colored(f'{data[1]}', cyan))

        except Exception as e:
            print('Error: ' + e)

    elif commands.startswith('4 '):
        try:
            db = sqlite3.connect('base.db')
            sql = db.cursor()
            print()
        
            for data in sql.execute(f"{commands[2:]}").fetchall():
                print(colored(f'{data[0]}.', green), colored(f'{data[1]} {data[2]} {data[3]}', cyan))

        except Exception as e:
            print('Error: ' + e)

    elif commands == 'cl':
        os.system('clear')


    elif commands == 'clr':
        os.system('cls')

    elif commands == 'ec':
        edit_cu = input("$: ")
        with open('cu.py', 'w') as f:
            f.write(f"cu = '{edit_cu}'")

    elif commands == 'ddb':
        os.rm('base.db')

    else: 
        print("xz " + commands)