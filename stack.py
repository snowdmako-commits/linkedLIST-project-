stack = []

def push(tasks, taskQueue):
    try:
        savedTasks = []

        for task in tasks:
            savedTasks.append(task.copy())

        savedQueue = []

        for taskID in taskQueue:
            savedQueue.append(taskID)

        stack.append([savedTasks, savedQueue])
    
    except Exception as e:
        print("Stack error:", e)


def undo(tasks, taskQueue):
    try:
        if len(stack) == 0:

            print("undo history is empty")
            return False

        oldTasks, oldQueue = stack.pop()

        tasks.clear()
        for task in oldTasks:
            tasks.append(task)

        taskQueue.clear()
        for taskID in oldQueue:
            taskQueue.append(taskID)

        print("undo done")
        return True
    
    except Exception as e:

        print("Undo error:", e)
        return False