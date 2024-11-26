from src.models.student_model import StudentModel
from PyQt6.QtWidgets import QMessageBox

class StudentController:
    def __init__(self):
        self.model = StudentModel()

    def add_student(self, name, code, birthday, gender, email, phone):
        try:
            if not all([name, code, birthday]):
                QMessageBox.warning(None, "Lỗi", "Vui lòng điền đầy đủ thông tin")
                return False

            self.model.add_student(name, code, birthday, gender, email, phone)
            QMessageBox.information(None, "Thành Công", "Thêm sinh viên thành công")
            return True
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể thêm sinh viên: {str(e)}")
            return False

    def get_all_students(self):
        return self.model.get_all_students()

    def get_student_by_id(self, student_id):
        return self.model.get_student_by_id(student_id)

    def update_student(self, student_id, name, code, birthday, gender, email, phone):
        try:
            self.model.update_student(student_id, name, code, birthday, gender, email, phone)
            QMessageBox.information(None, "Thành Công", "Cập nhật sinh viên thành công")
            return True
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể cập nhật sinh viên: {str(e)}")
            return False

    def delete_student(self, student_id):
        try:
            self.model.delete_student(student_id)
            QMessageBox.information(None, "Thành Công", "Xóa sinh viên thành công")
            return True
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể xóa sinh viên: {str(e)}")
            return False