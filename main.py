import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget
from src.views.student_view import StudentView
from src.views.course_view import CourseView
from src.views.class_view import ClassView
from src.views.score_view import ScoreView
from src.views.warning_statistics_view import WarningStatisticsView
from src.views.class_opening_desire_view import ClassOpeningDesireView
from src.views.warning_risk_view import WarningRiskView

from src.controllers.student_controller import StudentController
from src.controllers.course_controller import CourseController
from src.controllers.class_controller import ClassController
from src.controllers.score_controller import ScoreController
from src.controllers.warning_statistics_controller import WarningStatisticsController
from src.controllers.class_opening_desire_controller import ClassOpeningDesireController
from src.controllers.warning_risk_controller import WarningRiskController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hệ Thống Quản Lý Sinh Viên")
        self.setGeometry(100, 100, 1200, 800)
        
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)
        
        student_controller = StudentController()
        course_controller = CourseController()
        class_controller = ClassController()
        score_controller = ScoreController()
        warning_statistics_controller = WarningStatisticsController()
        class_opening_desire_controller = ClassOpeningDesireController()
        warning_risk_controller = WarningRiskController()
        
        student_tab = StudentView(student_controller)
        course_tab = CourseView(course_controller)
        class_tab = ClassView(class_controller)
        score_tab = ScoreView(score_controller)
        warning_statistics_tab = WarningStatisticsView(warning_statistics_controller)
        class_opening_desire_tab = ClassOpeningDesireView(class_opening_desire_controller)
        warning_risk_tab = WarningRiskView(warning_risk_controller)
        
        self.tab_widget.addTab(student_tab, "Sinh Viên")
        self.tab_widget.addTab(course_tab, "Khóa Học")
        self.tab_widget.addTab(class_tab, "Lớp Học")
        self.tab_widget.addTab(score_tab, "Điểm Số")
        self.tab_widget.addTab(warning_statistics_tab, "Thống kê cảnh cáo")
        self.tab_widget.addTab(class_opening_desire_tab, "Nguyện vọng mở lớp")
        self.tab_widget.addTab(warning_risk_tab, "Nguy cơ cảnh cáo")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()