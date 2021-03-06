import sys
from PySide.QtGui import *

from WinGui_PySide import Ui_MainWindow
from GuiInterface import MainWindow

class Error:
    def __init__(self, master):
        master = tk.Tk()
        self.master = master
        self.master.title('ERROR')

        self.frame = Frame(master)
        self.frame.pack(ipadx=40, ipady=10)
        self.exit_button = Button(self.frame, text='Exit', command=the_end)
        self.exit_button.pack(side='bottom', ipadx=10, pady=10)
        self.message = Label(self.frame, text='Connection Failed ' +
                                              'Please Check Dongle Connection.')
        self.message.pack(side='bottom')






if __name__ == "__main__":
    lib = Falcon_lib()
    script = 'Falcon_CHRIS2.txt'

    try:
        lib.connect()
    except BaseException:
        Error(root)
    else:
        lib.Falcon_Software_Reset()
        time.sleep(0.5)
        lib.LoadScript(script)
        time.sleep(0.5)
        lib.Falcon_Logic_Reset()
        app = QApplication(sys.argv)
        window = MainWindow(QMainWindow,Ui_MainWindow,lib)#MyApp()
        window.refresh_GUI()
        window.show()
        sys.exit(app.exec_())
