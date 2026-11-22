from tasks import *
from stack import push, undo
from queue import taskQueue, enqueue, dequeue, showQueue
from linkedList import *


def showMenu():
    print("""
1. Add task
2. Update task
3. Remove task
4. Show all tasks
5. Add task to queue (QUEUE)
6. Complete next task (LINKED LIST)
7. Undo operation (STACK)
8. Task history (LINKED LIST)
9. Show queue (QUEUE)
0. Exit
""")



def getTask():
    try:
        text = input("enter task ID: ")

        if not text.isdigit():
            print("please enter a valid number")
            return None

        task = findTask(int(text))

        if task == None:
            print("task not found")

        return task
    except Exception as e:

        print("Error:", e)
        return None



def menuAdd():
    try:
        name = input("enter task name: ").strip()

        if name == "":
            print("task name cannot be empty")
            return

        push(tasks, taskQueue)
        addTask(name)
        addHistory("Added: " + name)

    except Exception as e:
        print("Error:", e)



def menuUpdate():
    try:
        task = getTask()

        if task == None:
            return

        newName = input("enter new task name: ").strip()

        if newName == "":
            print("task name cannot be empty")
            return

        push(tasks, taskQueue)
        update(task, newName)
        addHistory("Updated: " + newName)

    except Exception as e:
        print("Error:", e)



def menuRemove():
    try:
        task = getTask()

        if task == None:
            return

        push(tasks, taskQueue)
        removeTask(task)

        if task["id"] in taskQueue:
            taskQueue.remove(task["id"])

        addHistory("Removed: " + task["name"])

    except Exception as e:
        print("Error:", e)




def menuShow():
    try:
        showTasks()

    except Exception as e:
        print("Error:", e)



def menuAddToQueue():
    try:
        task = getTask()

        if task == None:
            return

        if task["status"] == "Completed":
            print("task is already completed")
            return

        push(tasks, taskQueue)

        if enqueue(task["id"]):
            addHistory("Added to queue: " + task["name"])

    except Exception as e:
        print("Error:", e)




def menuComplete():
    try:
        if len(taskQueue) == 0:
            print("queue is empty")
            return

        push(tasks, taskQueue)

        taskID = dequeue()
        task = findTask(taskID)

        task["status"] = "Completed"
        addCompleted(task)

        print("Completed: " + task["name"])
        addHistory("Completed: " + task["name"])

    except Exception as e:
        print("Error:", e)



def menuUndo():
    try:
        if undo(tasks, taskQueue):
            addHistory("Undo operation")

    except Exception as e:
        print("Error:", e)



def menuHistory():
    try:
        print("\n--- Task History ---")
        showHistory()

        print("\n--- Completed Tasks ---")
        showCompleted()

    except Exception as e:
        print("Error:", e)



def menuShowQueue():
    try:
        print("\n--- Task Queue ---")
        showQueue()

    except Exception as e:
        print("Error:", e)