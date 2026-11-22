completedTasks = []

def addCompleted(task):
    try:
        node = {}

        node["data"] = task.copy()
        node["next"] = None

        if completedTasks:
            completedTasks[-1]["next"] = node

        completedTasks.append(node)

    except Exception as e:
        print("Error:", e)