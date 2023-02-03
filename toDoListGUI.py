# Author: Paweł Paciorkowski
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class ToDoList(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Lista Zadań - GUI")

        # Create widgets
        self.task_list = QListWidget()
        self.add_task_label = QLabel("Dodaj do listy:")
        self.add_task_input = QLineEdit()
        self.add_task_button = QPushButton("Dodaj")
        self.add_task_button.clicked.connect(self.add_task)
        self.edit_task_label = QLabel("Edytuj listę:")
        self.edit_task_input = QLineEdit()
        self.edit_task_button = QPushButton("Edytuj")
        self.edit_task_button.clicked.connect(self.edit_task)
        self.delete_task_button = QPushButton("Usuń")
        self.delete_task_button.clicked.connect(self.delete_task)
        self.save_button = QPushButton("Zapisz")
        self.save_button.clicked.connect(self.save_task)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.task_list)
        layout.addWidget(self.add_task_label)
        layout.addWidget(self.add_task_input)
        layout.addWidget(self.add_task_button)
        layout.addWidget(self.edit_task_label)
        layout.addWidget(self.edit_task_input)
        layout.addWidget(self.edit_task_button)
        layout.addWidget(self.delete_task_button)
        layout.addWidget(self.save_button)

        # Create central widget and set layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        
    #  Create methods

    def add_task(self): # add task
        task = self.add_task_input.text()
        self.task_list.addItem(task)
        self.add_task_input.clear()

    def edit_task(self): # edit task
        task = self.edit_task_input.text()
        current_item = self.task_list.currentItem()
        if current_item:
            current_item.setText(task)
            self.edit_task_input.clear()

    def delete_task(self): # delete task
        current_item = self.task_list.currentItem()
        if current_item:
            self.task_list.takeItem(self.task_list.row(current_item))

    def save_task(self): # save tasks to file
        with open("tasks.txt", "w") as file:
            for index in range(self.task_list.count()):
                file.write(self.task_list.item(index).text() + "\n")


# Run app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_list = ToDoList()
    todo_list.show()
    sys.exit(app.exec())
