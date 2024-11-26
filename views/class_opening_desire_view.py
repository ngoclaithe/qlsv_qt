from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6.QtCore import Qt


class ClassOpeningDesireView(QWidget):
    def __init__(self, class_desire_controller):
        super().__init__()
        self.class_desire_controller = class_desire_controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        bar_chart = BarChartWidget(data={
            "KTMT": 50,
            "CTDL&DT": 30,
            "HĐH": 20,
            "ITSS": 40,
            "IOT": 25
        })
        layout.addWidget(bar_chart)

        label = QLabel("Nguyện Vọng Mở Lớp Theo Môn Học", alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        self.setLayout(layout)


class BarChartWidget(QWidget):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.data = data

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        margin = 20
        width = self.width() - 2 * margin
        height = self.height() - 2 * margin
        bar_width = width // (len(self.data) * 2)  
        max_value = max(self.data.values())

        colors = [QColor("#4CAF50"), QColor("#2196F3"), QColor("#FFC107"), QColor("#E91E63"), QColor("#9C27B0")]

        x = margin
        y_base = self.height() - margin
        for i, (label, value) in enumerate(self.data.items()):
            bar_height = int((value / max_value) * (height - margin))  
            painter.setBrush(QBrush(colors[i % len(colors)]))
            painter.drawRect(x, y_base - bar_height, bar_width, bar_height)

            painter.drawText(x, y_base + 5, bar_width, margin, Qt.AlignmentFlag.AlignCenter, label)

            x += 2 * bar_width  

        painter.drawLine(margin, y_base, self.width() - margin, y_base)  
        painter.drawLine(margin, y_base, margin, margin) 

        painter.end()
