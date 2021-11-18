from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
import ui
# pyside6-uic UI.ui -o ui.py --star-imports

class Window(QWidget, ui.Ui_Form):
    def __init__(self):
        super().__init__(windowTitle='Git и желтые окружности')
        self.setupUi(self)
        self.pushButton.clicked.connect(self.repaint)
        self.random = QRandomGenerator()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(self.random.generate()))
        diameter = self.random.bounded(10, 200)
        painter.drawEllipse(
            self.random.bounded(self.width() - diameter),
            self.random.bounded(self.height() - diameter),
            diameter, diameter)


app = QApplication()
window = Window()
window.show()
app.exec()
