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



def showCompleted():
    try:
        if not completedTasks:
            print("no completed tasks")
            return

        for node in completedTasks:
            task = node["data"]
            print("ID:", task["id"], "| Name:", task["name"], "| Status:", task["status"])

    except Exception as e:
        print("Error:", e)