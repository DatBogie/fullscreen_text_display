import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

class FullscreenTextWindow(QWidget):
    def __init__(self, text, screen):
        super().__init__()
        self.text = text
        self.setScreen(screen)
        self.initUI()
        self.setCursor(Qt.CursorShape.BlankCursor)

    def initUI(self):
        self.setWindowTitle('Fullscreen Text Display')
        self.setStyleSheet("background-color: black;")

        layout = QVBoxLayout()
        self.label = QLabel(self.text)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: white; font-size: 72px;") # Adjust font size as needed
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setGeometry(self.screen().geometry())
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.showFullScreen()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            for widget in QApplication.topLevelWidgets():
                if isinstance(widget, FullscreenTextWindow):
                    widget.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    if len(sys.argv) > 1:
        text_to_display = sys.argv[1]
    else:
        text_to_display = "No text provided."
    
    windows = []
    for screen in app.screens():
        window = FullscreenTextWindow(text_to_display,screen)
        windows.append(window)
    sys.exit(app.exec())
