# TOOL TESTED ON WINDOWS 10 PRO OS ONLY
import os.path, os, colorama
from colorama import Fore, init
# import shutil to monitor disk space
import shutil
from datetime import datetime
# importing colors
init()
_red_ = Fore.RED
_blue_ = Fore.BLUE
_yellow_ = Fore.YELLOW
_cyan_ = Fore.CYAN
_lightcyan_ = Fore.LIGHTCYAN_EX
print(f"{_blue_} FILE COPY AND DRIVE DETECTING SYSTEM codded by V3N0M")
def diff(list1, list2):
    list_difference = [item for item in list1 if item not in list2]
    return list_difference


def foo():
    print(f"{_blue_}New dive introduced at {datetime.now()}")


def ham():
    print(f"{_red_}A drive disconnected at {datetime.now()}")


dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
print(f'''{_yellow_}
THE FOLLOWING DRIVES WERE DETECTED ON PROGRAM RUN
            {drives}'''.upper())
while True:
    uncheckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    x = diff(uncheckeddrives, drives)
    if x:
        x_index = str(x)[str(x).index("'") + 1: str(x).rindex("'")]
        # root path
        path = f"{x_index}/"
        print(f"{_cyan_}New drive(s):  {x_index}/   ")
        foo()
        # Get the disk usage statistics
        # about the given path
        stat = shutil.disk_usage(path)
  
        # Print disk usage statistics
        print(f"{_red_}Disk usage statistics:")
        print(stat)
        # directory listing
        entries = os.listdir(f'{x_index}/')
        # automatic copy file
        _cpfile_ = "F:/usb.py" # source
        _cpdest_ = f"{x_index}/" #destination
        shutil.copy2(_cpfile_, _cpdest_) # keeps everything in the file metadata too
        progress = 0
        while progress <= 100:
            print(f"{_yellow_}."*progress,f"{progress}%")
            progress += 20
        else:
            print(f"{_blue_} COPY COMPLETE")
        for entry in entries:
        # sub dir listing
            try:
                _entry_ = os.listdir(f"{x_index}/{entry}")
                print(f'{_cyan_}{entry}')                
                for subentry in _entry_:
                    try:
                        _entry1_ = os.listdir(f"{x_index}/{entry}/{subentry}")
                        print(f'    {_cyan_}{_entry1_}')                
                        for subentry1 in _entry_:
                            print(f"        {_lightcyan_}{subentry1}")
                    except NotADirectoryError:
                        print(f"    {subentry} is a file")
            except NotADirectoryError:
                print(f"{entry} is a file")
    y = diff(drives, uncheckeddrives)
    if y:
        y_index = str(y)[str(y).index("'") + 1: str(y).rindex("'")]
        print(f"{_red_}Removed drive(s): {y_index}")
        ham()
    drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
