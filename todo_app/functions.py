def display_tasks(filename="todofile.txt"):
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



def add_task(task, filename="todofile.txt"):
    with open("todofile.txt", "w") as file:
        contents_list = get_tasks()
        contents_list.append(task)
        for item in contents_list:
            file.write(item)



