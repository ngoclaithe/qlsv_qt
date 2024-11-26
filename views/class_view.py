from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, 
                             QTableWidgetItem, QPushButton, QLineEdit, QComboBox,
                             QMessageBox)
from PyQt6.QtCore import Qt

class ClassView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        form_layout = QHBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Tên lớp")
        
        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText("Mã lớp")

        self.course_dropdown = QComboBox()
        self.load_courses_to_dropdown()

        self.add_btn = QPushButton("Thêm Lớp")
        self.add_btn.clicked.connect(self.add_class)

        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.code_input)
        form_layout.addWidget(self.course_dropdown)
        form_layout.addWidget(self.add_btn)

        layout.addLayout(form_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Tên Lớp", "Mã Lớp", "Khóa Học"])
        
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_classes()

    def load_courses_to_dropdown(self):
        courses = self.controller.get_courses_for_dropdown()
        self.course_dropdown.clear()
        for course in courses:
            self.course_dropdown.addItem(course[1], course[0])

    def load_classes(self):
        classes = self.controller.get_all_classes()
        self.table.setRowCount(len(classes))
        
        for row, class_item in enumerate(classes):
            for col, value in enumerate(class_item):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.table.setItem(row, col, item)

    def add_class(self):
        name = self.name_input.text()
        code = self.code_input.text()
        course_id = self.course_dropdown.currentData()

        self.controller.add_class(name, code, course_id)
        self.load_classes()
        self.clear_inputs()

    def clear_inputs(self):
        self.name_input.clear()
        self.code_input.clear()
        self.course_dropdown.setCurrentIndex(0)