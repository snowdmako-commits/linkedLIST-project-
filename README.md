Task Manager

A simple command-line task manager written in Python. It shows how three data structures work in a real program:

Queue: tasks wait in line and are completed in order (first in, first out)
Stack: every change is saved, so the last action can be undone (last in, first out)
Linked list: stores the history of actions and the list of completed tasks
Features
Add, update, remove and show tasks
Add tasks to a queue and complete them one by one
Undo the last operation
View the history of actions and the completed tasks
Error handling with try/except, so the program does not crash
Project Structure
File	Purpose
main.py	Starts the program, shows the menu and calls the menu functions
menu.py	The menu text and one function for each menu option
tasks.py	Task list: add, show, find, update, remove
myQueue.py	Queue: enqueue, dequeue, show queue
stack.py	Stack: save the current state (push) and restore it (undo)
linkedList.py	Linked lists for completed tasks and history

Note: If your queue file is named queue.py, rename it to myQueue.py. The name queue is also a built-in Python module and can cause import problems. After renaming, change the import in menu.py:

python
from myQueue import taskQueue, enqueue, dequeue, showQueue
Requirements
Python 3.6 or newer
No external libraries
How to Run
Put all files in the same folder.
Open a terminal in that folder.
Run:
bash
python main.py
Menu
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
How to Use
Choose 1 to add a task. Each task gets an ID automatically.
Choose 5 and enter a task ID to put it in the queue.
Choose 9 to see the queue.
Choose 6 to complete the first task in the queue.
Choose 8 to see the history and the completed tasks.
Choose 7 to undo the last change.
How It Works

Task is a dictionary:

python
{"id": 1, "name": "Buy milk", "status": "Pending"}

Queue is a list of task IDs. New IDs go to the end and the first ID is completed first.

Stack saves a copy of the tasks and the queue before every change. undo takes the last saved copy and puts it back.

Linked list nodes are dictionaries:

python
{"data": ..., "next": ...}
Completed tasks: new items are added to the end.
History: new items are added to the front, so the newest action is shown first.
Known Limitations
Undo restores the tasks and the queue only. It does not restore the history or the completed tasks list.
Data is stored in memory only. When the program closes, everything is lost.
