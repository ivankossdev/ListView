import csv

def write_file(li_1, li_2="empty"):
    with open("task.csv", "w", newline='') as csvFile:
        task_header = ["List_1", "List_2"]
        writer_file = csv.DictWriter(csvFile, fieldnames=task_header)
        writer_file.writeheader()
        for x in li_1:
            writer_file.writerow({"List_1": x, "List_2": li_2})

def read_file():
    try:
        with open("task.csv", "r", newline="") as file:
            reader = csv.reader(file)
            buffer = []
            for x in reader:
                buffer.append(x)
            return buffer
    except FileNotFoundError:
        write_file([])

def list_convertor(item):
    list_widget = []
    list_widget_2 = []
    for y in range(1, len(item)):
        for x in range(2):
            if x == 0:
                list_widget.append(item[y][x])
            else:
                list_widget_2.append(item[y][x])
    return list_widget, list_widget_2
