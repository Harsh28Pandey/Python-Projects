def task():
    tasks = []# Empty task
    print("Welcome to The Task Management App")

    total_task = int(input("Enter how many task you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's Tasks are\n{tasks}")

    while True:
        operation = int(input("Enter 1-Add Task \n2-Update Task \n3-Delete Task \n4-View Task \n5-Exit To-Do App"))
        if(operation == 1):
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")

        elif(operation == 2):
            update_val = input("Enter the task you want to update = ")
            if(update_val in tasks):
                update = input("Enter the updated task = ")
                index = tasks.index(update_val)
                tasks[index] = update
                print(f"Task {update_val} has been successfully updated to {update}...")

        elif(operation == 3):
            delete_val = input("Enter the task you want to delete = ")
            if(delete_val in tasks):
                index = tasks.index(delete_val)
                del tasks[index]
                print(f"Task {delete_val} has been successfully deleted...")

        elif(operation == 4):
            print(f"Today's Tasks are\n{tasks}")
        
        elif(operation == 5):
            print("Thank you for using the Task Management App")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

task()