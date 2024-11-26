from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, 
                             QTableWidgetItem, QPushButton, QLineEdit, QLabel, 
                             QMessageBox, QDateEdit)
from PyQt6.QtCore import Qt, QDate

class StudentView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        form_layout = QHBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Tên sinh viên")
        
        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText("Mã sinh viên")
        
        self.birthday_input = QDateEdit()
        self.birthday_input.setCalendarPopup(True)
        
        self.gender_input = QLineEdit()
        self.gender_input.setPlaceholderText("Giới tính")
        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Số điện thoại")

        self.add_btn = QPushButton("Thêm Sinh Viên")
        self.add_btn.clicked.connect(self.add_student)

        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.code_input)
        form_layout.addWidget(self.birthday_input)
        form_layout.addWidget(self.gender_input)
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(self.phone_input)
        form_layout.addWidget(self.add_btn)

        layout.addLayout(form_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["ID", "Tên", "Mã SV", "Ngày Sinh", "Giới Tính", "Email", "SĐT"])
        
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_students()

    def load_students(self):
        students = self.controller.get_all_students()
        self.table.setRowCount(len(students))
        
        for row, student in enumerate(students):
            for col, value in enumerate(student):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.table.setItem(row, col, item)

    def add_student(self):
        name = self.name_input.text()
        code = self.code_input.text()
        birthday = self.birthday_input.date().toString("yyyy-MM-dd")
        gender = self.gender_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()

        self.controller.add_student(name, code, birthday, gender, email, phone)
        self.load_students()
        self.clear_inputs()

    def clear_inputs(self):
        self.name_input.clear()
        self.code_input.clear()
        self.birthday_input.setDate(QDate.currentDate())
        self.gender_input.clear()
        self.email_input.clear()
        self.phone_input.clear()