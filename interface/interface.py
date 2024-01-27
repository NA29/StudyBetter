from PyQt5.QtWidgets import *
from qtpy.QtCore import Qt
import sys

class FileExplorerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Explorer')
        self.showFullScreen()

        layout = QVBoxLayout()
        layout.setSpacing(10)
        self.setLayout(layout)

        titleLayout = QHBoxLayout()
        titleLabel = QLabel('Study Better', self)
        titleLabel.setAlignment(Qt.AlignCenter)
        titleLabel.setStyleSheet("font-size: 24pt; font-weight: bold;")
        titleLayout.addWidget(titleLabel, alignment=Qt.AlignCenter)
        layout.addLayout(titleLayout)

        welcomeLayout = QHBoxLayout()
        welcomeLabel = QLabel('Welcome to Study Better, select an image file to begin', self)
        welcomeLabel.setAlignment(Qt.AlignCenter)
        welcomeLayout.addWidget(welcomeLabel, alignment=Qt.AlignCenter)
        layout.addLayout(welcomeLayout)

        buttonLayout = QHBoxLayout()
        self.openFileButton = QPushButton('Open File Explorer', self)
        self.openFileButton.clicked.connect(self.openFileNameDialog)
        buttonLayout.addWidget(self.openFileButton, alignment=Qt.AlignCenter)
        layout.addLayout(buttonLayout)


        # Label to display file path
        # filePathLayout = QHBoxLayout()
        # self.filePathLabel = QLabel('File path will appear here', self)
        # filePathLayout.addWidget(self.filePathLabel, alignment=Qt.AlignCenter)
        # layout.addLayout(filePathLayout)


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)
        print(file_name)
        if file_name:
            self.filePathLabel.setText(file_name)  # Update the label with the file path

def main():
    app = QApplication(sys.argv)
    ex = FileExplorerWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()