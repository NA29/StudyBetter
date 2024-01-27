from PyQt5.QtWidgets import *
from qtpy.QtCore import Qt
import sys
import os


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Study Better')
        self.showFullScreen()

        self.stackedWidget = QStackedWidget()
        self.pageOne = LandingPage(self)
        self.pageTwo = PageLoading(self)

        self.stackedWidget.addWidget(self.pageOne)
        self.stackedWidget.addWidget(self.pageTwo)

        mainLayout = QVBoxLayout()
        self.setStyleSheet("background-color: green;")
        mainLayout.addWidget(self.stackedWidget)
        self.setLayout(mainLayout)

    def showPageOne(self):
        self.stackedWidget.setCurrentWidget(self.pageOne)

    def showPageTwo(self):
        self.stackedWidget.setCurrentWidget(self.pageTwo)

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
        welcomeLabel = QLabel('Welcome to Study Better, please select an image file to begin', self)
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


        # Label to display file path
        # filePathLayout = QHBoxLayout()
        # self.filePathLabel = QLabel('File path will appear here', self)
        # filePathLayout.addWidget(self.filePathLabel, alignment=Qt.AlignCenter)
        # layout.addLayout(filePathLayout)


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)
        self.selectedFileName = file_name

    def checkFileType(self):
        file_extension = os.path.splitext(self.selectedFileName)[1]
        print(file_extension)
        if file_extension.lower() in ['.png']:
            self.main_window.showPageTwo()
        
        
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

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()