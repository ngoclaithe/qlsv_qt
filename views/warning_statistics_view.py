import sys
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6.QtCore import Qt

class WarningStatisticsView(QWidget):
    def __init__(self, warning_controller):
        super().__init__()
        self.warning_controller = warning_controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        pie_chart = PieChartWidget(data={"Mức độ 1": 15, "Mức độ 2": 10, "Mức độ 3": 5})
        layout.addWidget(pie_chart)

        label = QLabel("Thống Kê Cảnh Cáo Theo Mức Độ", alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        self.setLayout(layout)


class PieChartWidget(QWidget):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.data = data

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        total = sum(self.data.values())
        start_angle = 0
        radius = min(self.width(), self.height()) // 2 - 10
        center_x, center_y = self.width() // 2, self.height() // 2

        colors = [QColor("#FF6666"), QColor("#66B2FF"), QColor("#66FF66")]
        color_index = 0

        for label, value in self.data.items():
            angle_span = int(360 * (value / total))
            painter.setBrush(QBrush(colors[color_index % len(colors)]))
            painter.drawPie(center_x - radius, center_y - radius, 2 * radius, 2 * radius, start_angle * 16, angle_span * 16)
            start_angle += angle_span
            color_index += 1

        painter.end()


if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    controller = None  
    view = WarningStatisticsView(controller)
    view.resize(400, 300)
    view.show()
    sys.exit(app.exec())
