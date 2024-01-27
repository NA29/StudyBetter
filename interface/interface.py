from PyQt5.QtWidgets import *
from qtpy.QtWidgets import QWidgetAction
import sys

class FileExplorerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Explorer Example')
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.filePathLabel = QLabel('File path will appear here', self)
        layout.addWidget(self.filePathLabel)

        self.openFileButton = QPushButton('Open File Explorer', self)
        self.openFileButton.clicked.connect(self.openFileNameDialog)
        layout.addWidget(self.openFileButton)

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