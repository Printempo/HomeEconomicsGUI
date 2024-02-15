import sys
from PyQt5.QtWidgets import QApplication
from gui_setup import EconomicsGUI

def main():
    app = QApplication(sys.argv)
    gui = EconomicsGUI()
    gui.setWindowTitle("Economics")
    gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
