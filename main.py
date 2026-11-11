import os
import datetime 
import To_Do_List
import calc

comand_data = [] #stores the every input command in runtimme

startTime = datetime.datetime.now()

def main():
    banner()

    while True:
        original = input("@auvrion >> ").strip()

        if not original:
            print("No command entered !!!")
            continue

        parts = original.split()

        cmd = parts[0].lower()
        args = parts[1:]

        comand_data.append(original)

        if cmd in commands:
            result = commands[cmd](args)

            if result is False:
                break

        else:
            print("Invalid command !!")

def banner() :
    print('''
╔══════════════════════════════════════════╗
║                                          ║
║              A U V R I O N               ║
║                                          ║
║         COMMAND ENVIRONMENT v0.1         ║
║          Welcome to AUVRION OS           ║
╚══════════════════════════════════════════╝
    ''')
    print("Type 'help' to view availabe command ")

def about(args):
    print('''
        ==============================
                About Section
        ==============================  
        What is AUVRION OS ? 
          -> Its a CLI based OS ....

        Owner Details :
          Developer Name -> Abhishek 
          Email : abc@gmail.com   
             
          ''')
    
def help_menu(args):
    print('''
        ==============================
                Helping Section
        ==============================      
    
        AUVRION OS command -->
        >> help : view avaivable commands 
        >> exit : exits the cli screen 
        >> about : what is AUVRION OS , developer details , etc
        >> echo : it will return your text , means if >> echo Hello I am coding 
          it will return >> Hello I am coding   
        >> history : It will display your every command input history in 'runtime'
        >> clear : clears the terminal screen 
        >> time : it shows the current time in "hr/min/sec" format
        >> date : it shows the current date in "day , date/month/year" format  
        >> todo : Opens a Todo List for maintaining your daily working records  
        >> calc : opens a scientific calculator to perform mathemetical operations                         
          ''')
    
def echo(args):
    combine = " ".join(args)
    print("  -->", combine)

def clear(args) :
    os.system("cls")
    banner()

def history(args) :
    i = 1
    if not comand_data :
        print("please input a comand first !")
        return
    else :
        for data in comand_data :
            print(i , " " , data)
            i=i+1
        
def time(args) :
    currentTime = datetime.datetime.now()
    print("\nCurrent Time ")
    print("-"*15)
    print(currentTime.strftime("%H : %M : %S"))
    print()

def date(args):
    currentDate = datetime.date.today()
    print("\nTodays Date ")
    print("-"*15)
    print(currentDate.strftime("%A , %d %B %Y"))
    print()

def uptime(args) :
    currentTime = datetime.datetime.now()
    worked = currentTime - startTime
    print("\n Working Time ")
    print("-"*15)
    print(worked)
    print()

def todo(args):
    print("type 'menu' to see all the commands")
    return To_Do_List.todo_main()    

def cal(args):
    return calc.main()    


def exit_cli(args):
    print("Abhishek-CLI-OS exited")
    print(".... Goodbyiii !")
    return False

commands = {
    "help": help_menu,
    "about": about,
    "clear": clear,
    "history": history,
    "time": time,
    "date": date,
    "uptime": uptime,
    "echo": echo,
    "todo": todo,
    "calc": cal,
    "exit": exit_cli
}
main()