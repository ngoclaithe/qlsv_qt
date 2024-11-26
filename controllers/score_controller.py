from src.models.score_model import ScoreModel
from PyQt6.QtWidgets import QMessageBox

class ScoreController:
    def __init__(self):
        self.model = ScoreModel()

    def add_score(self, student_id, course_id, score):
        try:
            if not all([student_id, course_id]):
                QMessageBox.warning(None, "Lỗi", "Vui lòng chọn sinh viên và khóa học")
                return False


            if not (0 <= score <= 10):
                QMessageBox.warning(None, "Lỗi", "Điểm số phải nằm trong khoảng 0-10")
                return False

            self.model.add_score(student_id, course_id, score)
            QMessageBox.information(None, "Thành Công", "Thêm điểm thành công")
            return True
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể thêm điểm: {str(e)}")
            return False

    def get_all_scores(self):
        return self.model.get_all_scores()

    def get_score_by_id(self, score_id):
        return self.model.get_score_by_id(score_id)

    def update_score(self, score_id, student_id, course_id, score):
        try:

            if not (0 <= score <= 10):
                QMessageBox.warning(None, "Lỗi", "Điểm số phải nằm trong khoảng 0-10")
                return False

            self.model.update_score(score_id, student_id, course_id, score)
            QMessageBox.information(None, "Thành Công", "Cập nhật điểm thành công")
            return True
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể cập nhật điểm: {str(e)}")
            return False

    def delete_score(self, score_id):
        try:
            self.model.delete_score(score_id)
            QMessageBox.information(None, "Thành Công", "Xóa điểm thành công")
            return True
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể xóa điểm: {str(e)}")
            return False

    def get_students_for_dropdown(self):
        return self.model.get_students_for_dropdown()

    def get_courses_for_dropdown(self):
        return self.model.get_courses_for_dropdown()

    def get_student_average_score(self, student_id):
        result = self.model.get_student_average_score(student_id)
        return result[0] if result else 0

    def get_course_average_score(self, course_id):
        result = self.model.get_course_average_score(course_id)
        return result[0] if result else 0