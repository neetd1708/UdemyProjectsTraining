import functions as f

while True:
    user_input = input("Enter Action (e.g. add drink water, done 3, edit 2, show, exit):").lower()
    f.display_tasks()
    if user_input == "exit":
        break
    elif user_input.startswith("add"):
        task = user_input.split(" ")[1:][0]
        print(f"Item to be added: {task}")
        f.add_task(task)
    elif user_input.startswith("edit"):
        taskNum = int(user_input.split(" ")[1:]) -1
        with open("todofile.txt","w+") as file:
            contents_list = file.readlines()
            new_task = input(f"Enter new task for {contents_list[taskNum]}:")
            contents_list[taskNum] = new_task
            file.write(contents_list)
            file.write("\n")
    elif user_input.startswith("done"):
        taskNum = int(user_input.split(" ")[1:]) -1
        with open("todofile.txt","w+") as file:
            contents_list = file.readlines()
            contents_list.pop(taskNum)
            file.write(contents_list)
    elif user_input.startswith("show"):
        f.display_tasks()
    else:
        print("Invalid input")




