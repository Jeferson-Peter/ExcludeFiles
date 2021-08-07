import os
import datetime
from tkinter import Tk
from tkinter.filedialog import askdirectory

if __name__ == '__main__':
    Tk().withdraw()
    path_to_file = askdirectory()
    for dirpath, dirnames, filenames in os.walk(path_to_file):
        for file in filenames:
            curpath = os.path.join(dirpath, file)
            file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(curpath))
            if datetime.datetime.now() - file_modified > datetime.timedelta(days=90): os.remove(curpath)
