from PyQt5.QtWidgets import *
from qtpy.QtCore import Qt
import sys
import os

current_script_path = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_script_path)
sys.path.append(parent_dir)

from outputFile.wordFormat import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Study Better')
        screen_geometry = QDesktopWidget().screenGeometry()
        self.setFixedSize(screen_geometry.width(), screen_geometry.height())
        self.showFullScreen()

        self.stackedWidget = QStackedWidget()
        self.pageOne = LandingPage(self)
        self.pageTwo = PageLoading(self)
        self.pageThree = PageDone(self)

        self.stackedWidget.addWidget(self.pageOne)
        self.stackedWidget.addWidget(self.pageTwo)
        self.stackedWidget.addWidget(self.pageThree)

        mainLayout = QVBoxLayout()
        self.setStyleSheet("background-color: green;")
        mainLayout.addWidget(self.stackedWidget)
        self.setLayout(mainLayout)

    def showPageOne(self):
        self.stackedWidget.setCurrentWidget(self.pageOne)

    def showPageTwo(self):
        self.stackedWidget.setCurrentWidget(self.pageTwo)

    def showPageThree(self):
        self.stackedWidget.setCurrentWidget(self.pageThree)
    
    def showPopup(self):
        popup = PopupDialog(self)
        mainWindowCenter = self.frameGeometry().center()
        popup.move(mainWindowCenter - popup.rect().center())
        popup.exec_()

class LandingPage(QWidget):
    def __init__(self, main_window=None):
        super().__init__(main_window)
        self.selectedFileName = None
        self.main_window = main_window
    
        layout = QVBoxLayout()
        self.setLayout(layout)

        titleLayout = QHBoxLayout()
        titleLabel = QLabel('Study Better', self)
        titleLabel.setAlignment(Qt.AlignCenter)
        titleLabel.setStyleSheet("font-size: 240pt; font-weight: bold;")
        titleLayout.addWidget(titleLabel)
        layout.addLayout(titleLayout)

        sloganLayout = QHBoxLayout()
        sloganLabel = QLabel('The note enhancing app',self)
        sloganLabel.setStyleSheet("font-size: 120pt")
        sloganLabel.setAlignment(Qt.AlignCenter)
        sloganLayout.addWidget(sloganLabel)
        layout.addLayout(sloganLayout)

        welcomeLayout = QHBoxLayout()
        welcomeLabel = QLabel('Welcome to Study Better, please select a png file to begin', self)
        welcomeLabel.setStyleSheet("font-size: 40pt")
        welcomeLabel.setAlignment(Qt.AlignCenter)
        welcomeLayout.addWidget(welcomeLabel)
        layout.addLayout(welcomeLayout)

        buttonLayout = QHBoxLayout()
        buttonLayout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        buttonLayout.setSpacing(0)  # Remove spacing

        self.openFileButton = QPushButton('Select a file to enhance', self)
        self.openFileButton.clicked.connect(self.openFileNameDialog)
        self.openFileButton.clicked.connect(self.checkFileType)
        self.openFileButton.clicked.connect(main_word)
        self.openFileButton.clicked.connect(self.goToPageThree)
        
        self.openFileButton.setStyleSheet("""
            QPushButton {
                color : black;
                border: 2px solid black;
                border-radius: 10px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color : beige;
            }
        """)

        # Add the button to the layout
        buttonLayout.addWidget(self.openFileButton)

        # Add button layout to the main layout
        layout.addLayout(buttonLayout)

    def goToPageThree(self):
        self.main_window.showPageThree()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)
        self.selectedFileName = file_name

    def checkFileType(self):
        file_extension = os.path.splitext(self.selectedFileName)[1]
        print(file_extension)
        if file_extension.lower() in ['.png']:
            self.main_window.showPageTwo()
        else:
            self.main_window.showPopup()

class PopupDialog(QDialog):
    def __init__(self, main_window=None):
        super().__init__(main_window)
        self.setWindowTitle('Error')
        self.setGeometry(200, 200, 200, 200)
        self.setStyleSheet("background-color: white; color:black;")
        layout = QVBoxLayout()
        message_label = QLabel('You have selected a non-compatible file type. Please select a .png', self)
        layout.addWidget(message_label)
        closeButton = QPushButton('Close', self)
        closeButton.setStyleSheet("border: 2px solid black; border-radius: 10px; padding: 6px;")
        closeButton.clicked.connect(self.close)  
        layout.addWidget(closeButton)
        self.setLayout(layout)
    
    
class PageLoading(QWidget):
    def __init__(self, main_window=None):
        super().__init__(main_window)
    
        layout = QVBoxLayout()
        self.setLayout(layout)

        sloganLayout = QHBoxLayout()
        sloganLabel = QLabel('Loading',self)
        sloganLabel.setStyleSheet("font-size: 100pt")
        sloganLabel.setAlignment(Qt.AlignCenter)
        sloganLayout.addWidget(sloganLabel)
        layout.addLayout(sloganLayout)

        dotLayout = QHBoxLayout()
        dotLabel = QLabel('. . .',self)
        dotLabel.setStyleSheet("font-size: 100pt")
        dotLabel.setAlignment(Qt.AlignCenter)
        dotLayout.addWidget(dotLabel)
        layout.addLayout(dotLayout)

class PageDone(QWidget):
    def __init__(self,main_window=None):
        super().__init__(main_window)
        self.main_window = main_window

        layout = QVBoxLayout()
        self.setLayout(layout)

        textLayout = QHBoxLayout()
        textLabel = QLabel("All done, you can now checkout your enhanced notes from Study Better")
        textLabel.setStyleSheet("font-size:100pt")
        textLabel.setAlignment(Qt.AlignCenter)
        textLabel.setWordWrap(True)
        textLayout.addWidget(textLabel)
        layout.addLayout(textLayout)

        precisionLayout = QHBoxLayout()
        precisionLabel = QLabel("If the word document does not open automatically, you can find it at the root of this program")
        precisionLabel.setStyleSheet("font-size:40pt")
        precisionLabel.setWordWrap(True)
        precisionLabel.setAlignment(Qt.AlignCenter)
        precisionLayout.addWidget(precisionLabel)
        layout.addLayout(precisionLayout)
        
def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()