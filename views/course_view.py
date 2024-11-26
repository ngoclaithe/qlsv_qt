from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, 
                             QTableWidgetItem, QPushButton, QLineEdit, QLabel, 
                             QMessageBox, QSpinBox)
from PyQt6.QtCore import Qt

class CourseView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        form_layout = QHBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Tên khóa học")
        
        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText("Mã khóa học")
        
        self.credits_input = QSpinBox()
        self.credits_input.setRange(1, 10)
        self.credits_input.setPrefix("Số tín chỉ: ")

        self.add_btn = QPushButton("Thêm Khóa Học")
        self.add_btn.clicked.connect(self.add_course)

        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.code_input)
        form_layout.addWidget(self.credits_input)
        form_layout.addWidget(self.add_btn)

        layout.addLayout(form_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Tên Khóa Học", "Mã Khóa Học", "Số Tín Chỉ"])
        
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_courses()

    def load_courses(self):
        courses = self.controller.get_all_courses()
        self.table.setRowCount(len(courses))
        
        for row, course in enumerate(courses):
            for col, value in enumerate(course):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.table.setItem(row, col, item)

    def add_course(self):
        name = self.name_input.text()
        code = self.code_input.text()
        credits = self.credits_input.value()

        self.controller.add_course(name, code, credits)
        self.load_courses()
        self.clear_inputs()

    def clear_inputs(self):
        self.name_input.clear()
        self.code_input.clear()
        self.credits_input.setValue(1)