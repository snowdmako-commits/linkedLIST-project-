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



history = []


def addHistory(text):
    try:
        node = {}

        node["data"] = text
        node["previous"] = None
        node["next"] = None

        if history:
            node["next"] = history[0]
            history[0]["previous"] = node

        history.insert(0, node)

    except Exception as e:
        print("Error:", e)