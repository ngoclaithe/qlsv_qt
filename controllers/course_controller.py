from src.models.course_model import CourseModel
from PyQt6.QtWidgets import QMessageBox

class CourseController:
    def __init__(self):
        self.model = CourseModel()

    def add_course(self, name, code, credits):
        try:
            if not all([name, code]):
                QMessageBox.warning(None, "Lỗi", "Vui lòng điền đầy đủ thông tin")
                return False

            self.model.add_course(name, code, credits)
            QMessageBox.information(None, "Thành Công", "Thêm khóa học thành công")
            return True
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể thêm khóa học: {str(e)}")
            return False

    def get_all_courses(self):
        return self.model.get_all_courses()

    def get_course_by_id(self, course_id):
        return self.model.get_course_by_id(course_id)

    def update_course(self, course_id, name, code, credits):
        try:
            self.model.update_course(course_id, name, code, credits)
            QMessageBox.information(None, "Thành Công", "Cập nhật khóa học thành công")
            return True
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể cập nhật khóa học: {str(e)}")
            return False

    def delete_course(self, course_id):
        try:
            self.model.delete_course(course_id)
            QMessageBox.information(None, "Thành Công", "Xóa khóa học thành công")
            return True
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể xóa khóa học: {str(e)}")
            return False