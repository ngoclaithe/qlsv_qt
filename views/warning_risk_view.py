from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import Qt


class WarningRiskView(QWidget):
    def __init__(self, warning_risk_controller):
        super().__init__()
        self.warning_risk_controller = warning_risk_controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        line_chart = LineChartWidget(data=[
            (0, 10),   
            (1, 15),   
            (2, 20),   
            (3, 25),   
            (4, 30),   
            (5, 35)    
        ])
        layout.addWidget(line_chart)

        label = QLabel("Nguy Cơ Cảnh Cáo Theo Học Kỳ", alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        self.setLayout(layout)


class LineChartWidget(QWidget):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.data = data

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        margin = 30
        width = self.width() - 2 * margin
        height = self.height() - 2 * margin

        max_x = max(point[0] for point in self.data)
        max_y = max(point[1] for point in self.data)
        x_scale = width / max_x if max_x > 0 else 1
        y_scale = height / max_y if max_y > 0 else 1

        painter.setPen(QPen(Qt.GlobalColor.black, 2))
        painter.drawLine(margin, self.height() - margin, self.width() - margin, self.height() - margin)  
        painter.drawLine(margin, self.height() - margin, margin, margin) 

        painter.setPen(QPen(QColor(255, 0, 0), 2))  
        last_point = None
        for x, y in self.data:
            x_pos = margin + int(x * x_scale)
            y_pos = self.height() - margin - int(y * y_scale)
            if last_point:
                painter.drawLine(last_point[0], last_point[1], x_pos, y_pos)
            last_point = (x_pos, y_pos)

            painter.setBrush(QColor(0, 0, 255))
            painter.drawEllipse(x_pos - 3, y_pos - 3, 6, 6)

        painter.setPen(QPen(Qt.GlobalColor.black))
        painter.drawText(self.width() - margin + 5, self.height() - margin + 10, "Học Kỳ") 
        painter.drawText(margin - 20, margin - 10, "Số Lượng Sinh Viên")  

        painter.end()
