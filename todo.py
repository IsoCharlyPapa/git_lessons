tasks = []

def add_task(title):
    tasks.append({"title": title, "done": False})

def list_tasks():
    for i, task in enumerate(tasks):
        status = "x" if task["done"] else " "
        print(f"[{status}] {i}: {task['title']}")

def complete_task(index):
    tasks[index]["done"] = True

if __name__ == "__main__":
    add_task("Git lernen")
    add_task("Branches verstehen")
    list_tasks()
