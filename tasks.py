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



def showTasks():
    try:
        if not tasks:
            print("Task list is empty!")
            return
        
        for task in tasks:
            print("ID:", task["id"], "| Name:", task["name"], "| Status:", task["status"])

    except Exception as e:
        print("Error showing tasks:", e)



def findTask(taskID):
    try:
        for task in tasks:
            if task["id"] == taskID:
                return task
        return None
    
    except Exception as e:

        print("Error finding task:", e)
        return None



def update(task, newName):
    try:
        task["name"] = newName
        print("Task updated successfully!")

    except Exception as e:
        print("Error updating task:", e)




def removeTask(task):
    try:
        tasks.remove(task)
        print("Task removed successfully!")

    except Exception as e:
        print("Error removing task:", e)