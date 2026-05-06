def display_tasks(filename=r"C:\Users\navne\PycharmProjects\PythonProject\todo_app\todofile.txt"):
    with open(filename, "r") as f:
        todo_list = f.readlines()
        if len(todo_list) == 0:
            print("No tasks found")
        else:
            for item in todo_list:
                print(item+'\n')

def get_tasks(filename=r"C:\Users\navne\PycharmProjects\PythonProject\todo_app\todofile.txt"):
    with open(filename, "r") as f:
        todo_list = f.readlines()
    return todo_list



def add_task(tasks, filename=r"C:\Users\navne\PycharmProjects\PythonProject\todo_app\todofile.txt"):
    with open(filename, "w") as file:
        print(["Checkpoint3"] + tasks)
        file.writelines(tasks)

    with open(filename, "r") as f:
        print("Checkpoint4")
        print(f.readlines())



