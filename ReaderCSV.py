import csv

def init_file(li):
    with open("task.csv", "w", newline='') as csvFile:
        task_header = ["List_1", "List_2"]
        writer_file = csv.DictWriter(csvFile, fieldnames=task_header)
        writer_file.writeheader()
        for x in li:
            writer_file.writerow({"List_1": x, "List_2": ""})

def read_file():
    with open("task.csv", "r", newline="") as file:
        reader = csv.reader(file)
        bufer = []
        for x in reader:
            bufer.append(x)
        return bufer

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
