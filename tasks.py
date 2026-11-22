tasks = []
nextID = 1

def addTask(name):
    global nextID
    try:
        task = {"id": nextID, "name": name, "status": "Pending"}
        tasks.append(task)
        nextID += 1

        print("Task added successfully!")

    except Exception as e:
        print("Error adding task:", e)