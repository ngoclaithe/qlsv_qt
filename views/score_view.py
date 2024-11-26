from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, 
                             QTableWidgetItem, QPushButton, QComboBox, QDoubleSpinBox,
                             QMessageBox, QLabel)
from PyQt6.QtCore import Qt

class ScoreView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        form_layout = QHBoxLayout()

        self.student_dropdown = QComboBox()
        self.student_dropdown.setPlaceholderText("Chọn Sinh Viên")

        self.course_dropdown = QComboBox()
        self.course_dropdown.setPlaceholderText("Chọn Khóa Học")

        self.score_input = QDoubleSpinBox()
        self.score_input.setRange(0, 10)
        self.score_input.setDecimals(1)
        self.score_input.setSingleStep(0.5)

        self.add_btn = QPushButton("Thêm Điểm")
        self.add_btn.clicked.connect(self.add_score)

        self.load_students_to_dropdown()
        self.load_courses_to_dropdown()

        form_layout.addWidget(self.student_dropdown)
        form_layout.addWidget(self.course_dropdown)
        form_layout.addWidget(self.score_input)
        form_layout.addWidget(self.add_btn)

        layout.addLayout(form_layout)

        self.avg_score_label = QLabel("Điểm trung bình: ")
        layout.addWidget(self.avg_score_label)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Sinh Viên", "Khóa Học", "Điểm"])
        
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_scores()

    def load_students_to_dropdown(self):
        students = self.controller.get_students_for_dropdown()
        self.student_dropdown.clear()
        for student in students:
            self.student_dropdown.addItem(student[1], student[0])

    def load_courses_to_dropdown(self):
        courses = self.controller.get_courses_for_dropdown()
        self.course_dropdown.clear()
        for course in courses:
            self.course_dropdown.addItem(course[1], course[0])

    def load_scores(self):
        scores = self.controller.get_all_scores()
        self.table.setRowCount(len(scores))
        
        for row, score in enumerate(scores):
            for col, value in enumerate(score):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.table.setItem(row, col, item)

        if scores:
            avg_scores = [float(score[3]) for score in scores]
            avg_total = sum(avg_scores) / len(avg_scores)
            self.avg_score_label.setText(f"Điểm trung bình: {avg_total:.2f}")
        else:
            self.avg_score_label.setText("Chưa có điểm")

    def add_score(self):
        student_id = self.student_dropdown.currentData()
        course_id = self.course_dropdown.currentData()
        score = self.score_input.value()

        self.controller.add_score(student_id, course_id, score)
        self.load_scores()
        self.clear_inputs()

    def clear_inputs(self):
        self.student_dropdown.setCurrentIndex(0)
        self.course_dropdown.setCurrentIndex(0)
        self.score_input.setValue(0)