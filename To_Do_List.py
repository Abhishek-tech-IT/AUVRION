tasks = []
def add_task():
    task_name = input(">> todo >> Enter task : ").strip().lower()
    for task in tasks :
        if task["name"] == task_name :
            print("Already the task is added ")
            return
    new_task = {"name" : task_name , "status" : False}
    tasks.append(new_task)
    print(f"Added '{task_name}' in your TO-DO-List  ")

def view_task():
    i = 1
    print("------ Your Task List ------")
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks :
        if task["status"] == False :
            symbol = "❌"
        else :
            symbol = "✔"  
        print(i, "." , task["name"] , "-->> Status :", symbol) 
        i = i + 1    

def del_task():
    if not tasks:
        print("No tasks available.")
        return
    view_task()
    print("Choose which number you want to delete")
    del_choice=int(input(">> todo >> Enter your choice : "))
    if del_choice >= 1 and del_choice <= len(tasks) :  # if 1 <= del_choice <= len(tasks): both has same meaning 
        index = del_choice - 1
        tasks.pop(index)  # else can use : del tasks[index]
        print("Task deleted successfully.")
    else :
        print("The task doesn't exists ")    
    
def mark_complete():
    if not tasks:
        print("No tasks available.")
        return
    view_task()
    com_choice = int(input(">> todo >> Which task have you completed ? : "))
    if com_choice >= 1 and com_choice <= len(tasks) :  # if 1 <= com_choice <= len(tasks): both has same meaning 
        index = com_choice - 1
        tasks[index]["status"] = True 
        print("Task marked as completed !! ")
    else :
        print("The task doesn't exists ") 

def menu():
    print("="*35)
    #print("==== TO DO LIST =====")
    print("------ TYPE ------")
    print(" 'Add' for Add-Task")
    print(" 'View' for View-Tasks")
    print(" 'Delete' for Deleting-Task")
    print(" 'Mark' for Completed-Tasks")
    print(" 'Exit' for Exit the TODO Lists ")
    print("="*35)

def todo_main():
    while True :
        choice=input("@ >> todo >> Enter your command : ").lower().strip()
        if choice == "menu" :
            menu()
        elif choice == "add" :
            add_task()
        elif choice == "view" :
            view_task()
        elif choice == "delete" :
            del_task()
        elif choice == "mark" :
            mark_complete()
        elif choice == "exit" :
            print(">> todo >> Exited todo ... byiii")
            break
        else :
            print("!!! Invalid Choice !!!")                


        