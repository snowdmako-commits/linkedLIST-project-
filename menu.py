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