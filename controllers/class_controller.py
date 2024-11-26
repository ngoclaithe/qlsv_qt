from src.models.class_model import ClassModel
from PyQt6.QtWidgets import QMessageBox

class ClassController:
    def __init__(self):
        self.model = ClassModel()

    def add_class(self, name, code, course_id):
        try:
            if not all([name, code, course_id]):
                QMessageBox.warning(None, "Lỗi", "Vui lòng điền đầy đủ thông tin")
                return False

            self.model.add_class(name, code, course_id)
            QMessageBox.information(None, "Thành Công", "Thêm lớp học thành công")
            return True
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể thêm lớp học: {str(e)}")
            return False

    def get_all_classes(self):
        return self.model.get_all_classes()

    def get_class_by_id(self, class_id):
        return self.model.get_class_by_id(class_id)

    def update_class(self, class_id, name, code, course_id):
        try:
            self.model.update_class(class_id, name, code, course_id)
            QMessageBox.information(None, "Thành Công", "Cập nhật lớp học thành công")
            return True
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể cập nhật lớp học: {str(e)}")
            return False

    def delete_class(self, class_id):
        try:
            self.model.delete_class(class_id)
            QMessageBox.information(None, "Thành Công", "Xóa lớp học thành công")
            return True
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể xóa lớp học: {str(e)}")
            return False

    def get_courses_for_dropdown(self):
        return self.model.get_courses_for_dropdown()