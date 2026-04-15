import subprocess, random

def check_stricter_values(value:str) ->str:
    s = value.lstrip().strip()[:4]
    if not s:
        return ""
    for char in s:
        if not (char.isalpha() or char == '.'):
            return ""
    return s

def check_values(value:str) ->str:
    s = value.lstrip().strip()[:13]
    if not s:
        return ""
    for char in s:
        if not (char.isalpha() or char == '.'):
            return ""
    return s

def check_operands(value:str) ->int:
    s = value.lstrip().strip()[:2]
    operators = ['+', '-', '*', '/', '%', '=', 'x', 'o', 'b']

    if any(op in s for op in operators):
        return 0
    else:
        try:
            evaluated = eval(s)
            return evaluated
        except:
            return 0

def execute(bin:str, switch:str, compl:str, mode=0):
    try:
        result = subprocess.run(
            [bin, switch, compl],
            capture_output=True,
            text=True,
            timeout=2
        )

        partial_output = result.stdout.strip()[:2] if result.stdout else ":("

        # MUHIM PATCH
        return str(result.returncode * mode), partial_output

    except:
        return "error", "error"

globs = {
    "__builtins__": {},
    "run": execute
}

locs = {}

def check_win(switches, args, mode, bin):
    debug = []

    if switches[0] and args[0] and isinstance(mode, int) and bin:
        z1, letter1 = eval(f"run('{bin}', '{switches[0]}', '{args[0]}', {mode})", globs, locs)
    else:
        z1, letter1 = random.choice(["AAA","BBB","CCC"]), "empty"

    debug.append(z1)

    if switches[1] and args[1] and isinstance(mode, int) and bin:
        z2, letter2 = eval(f"run('{bin}', '{switches[1]}', '{args[1]}', {mode})", globs, locs)
    else:
        z2, letter2 = random.choice(["DDD","EEE","FFF"]), "empty"

    debug.append(z2)

    if debug[0] != debug[1] and hash(debug[0]) == hash(debug[1]) and isinstance(debug[0], type(debug[1])):
        print("FLAG:", open("flag.txt").read())
    else:
        print(f"Partial output: {letter1} - {letter2}")

def main():
    switches,args = ['', ''], ['', '']
    bn, mode = '', ''

    while True:
        print("""
1. Create your mode
2. Add it to the bin
3. Research your arguments
4. Let go of your beliefs
5. Beat the competitor
""")

        choice = int(input("> "))

        if choice == 1:
            mode = check_operands(input('(mode)> '))
        elif choice == 2:
            bn = check_stricter_values(input('(bin)> '))
        elif choice == 3:
            args = [check_values(x) for x in input('(arg1,arg2)> ').split(',')]
        elif choice == 4:
            switches = [check_values(x) for x in input('(switch1,switch2)> ').split(',')]
        elif choice == 5:
            check_win(switches, args, mode, bn)            [bin, switch, compl],
            capture_output=True,
            text=True,
            timeout=2
        )
        partial_output = result.stdout.strip()[:2] if result.stdout and result.stdout.strip() else ':('
        return result.returncode * mode, partial_output
    except Exception as e:
        return -126, 'error'

globs = {
    "__builtins__": {},
    "run": execute
}

locs = {}

def check_win(switches, args, mode, bin):
    debug = []
    if switches[0] and args[0] and isinstance(mode, int) and bin:
        z1, letter1 = eval(f"run('{bin}', '{switches[0]}', '{args[0]}', {mode})", globs, locs)
    else:
        z1, letter1 = random.choice(["This is our world now...", 0xd3adb335, b"HTB{"]), "empty"

    debug.append(z1)

    if switches[1] and args[1] and isinstance(mode, int) and bin:  
        z2, letter2 = eval(f"run('{bin}', '{switches[1]}', '{args[1]}', {mode})", globs, locs)
    else:
        z2, letter2 = random.choice(["My crime is that of curiosity", 0xd3adc0d3, b"}BTH"]), "empty"

    debug.append(z2)

    if debug[0] != debug[1] and str(debug[0]) != str(debug[1]) and hash(debug[0]) == hash(debug[1]) and isinstance(debug[0], type(debug[1])) :
        print("What an awesome player! You have beaten the competitor, you deserve this:", open('flag.txt').read())
    else:
        print(f"Partial output is: {letter1} - {letter2}")

    debug.clear()

banner = r"""
 ███▄    █  ▒█████  ▄▄▄█████▓    ██▓███   ▒█████    ██████  ██▓▒██   ██▒▄▄▄█████▓ ██▓ ██▒   █▓▓█████ 
 ██ ▀█   █ ▒██▒  ██▒▓  ██▒ ▓▒   ▓██░  ██▒▒██▒  ██▒▒██    ▒ ▓██▒▒▒ █ █ ▒░▓  ██▒ ▓▒▓██▒▓██░   █▒▓█   ▀ 
▓██  ▀█ ██▒▒██░  ██▒▒ ▓██░ ▒░   ▓██░ ██▓▒▒██░  ██▒░ ▓██▄   ▒██▒░░  █   ░▒ ▓██░ ▒░▒██▒ ▓██  █▒░▒███   
▓██▒  ▐▌██▒▒██   ██░░ ▓██▓ ░    ▒██▄█▓▒ ▒▒██   ██░  ▒   ██▒░██░ ░ █ █ ▒ ░ ▓██▓ ░ ░██░  ▒██ █░░▒▓█  ▄ 
▒██░   ▓██░░ ████▓▒░  ▒██▒ ░    ▒██▒ ░  ░░ ████▓▒░▒██████▒▒░██░▒██▒ ▒██▒  ▒██▒ ░ ░██░   ▒▀█░  ░▒████▒
░ ▒░   ▒ ▒ ░ ▒░▒░▒░   ▒ ░░      ▒▓▒░ ░  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ▒▒ ░ ░▓ ░  ▒ ░░   ░▓     ░ ▐░  ░░ ▒░ ░
░ ░░   ░ ▒░  ░ ▒ ▒░     ░       ░▒ ░       ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░░   ░▒ ░    ░     ▒ ░   ░ ░░   ░ ░  ░
   ░   ░ ░ ░ ░ ░ ▒    ░         ░░       ░ ░ ░ ▒  ░  ░  ░   ▒ ░ ░    ░    ░       ▒ ░     ░░     ░   
         ░     ░ ░                           ░ ░        ░   ░   ░    ░            ░        ░     ░  ░
                                                                                          ░          
"""

def menu():
    print()
    print("1. Create your mode")
    print("2. Add it to the bin")
    print("3. Research your arguments")
    print("4. Let go of your beliefs")
    print("5. ! Beat the competitor !")
    print()
    option = input("> ")
    return option

def main():
    switches,args = ['', ''], ['', '']
    bn, mode = '', ''
    print(f"\n{banner}\n")
    while True:
        choice = int(menu())
        if choice == 1:
            mode = check_operands(input('(mode)> ').strip())
        elif choice == 2:
            bn = check_stricter_values(input('(bin)> ').strip())
        elif choice == 3:
            args = [check_values(x) for x in input('(arg1,arg2)> ').strip().split(',') ]
        elif choice == 4:
            switches = [check_values(x) for x in input('(switch1,switch2)> ').strip().split(',') ]
        elif choice == 5:
            check_win(switches, args, mode, bn)
        else:
            print('See you later.')
            exit(1)

if __name__ == "__main__":
    main()
