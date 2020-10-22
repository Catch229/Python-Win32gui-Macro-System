from tkinter import *
from tkinter import ttk
import win32gui
import multiprocessing
import macros
from functools import partial


class WindowController:
    def __init__(self, win_one, win_two):
        self.win_one = win_one
        self.win_two = win_two
        self.func_combo = ttk.Combobox()
        self.process = multiprocessing.Process()
        self.running = False
        self.state_label = Label()
        self.status_label = Label()
        self.control_tab = self.create_tab()

    def macro_thread_toggle(self, func):
        if not self.running:
            self.running = True
            print("Creating thread")
            self.process = multiprocessing.Process(target=func, args=(int(self.win_one[:10], 16), int(self.win_two[:10], 16)))
            self.process.start()
            self.state_label['text'] = "State: Running"
        else:
            self.running = False
            print("Killing thread")
            self.process.terminate()
            self.state_label['text'] = "State: Stopped"

    def start_stop_interface(self):
        print(self.func_combo.get())
        self.macro_thread_toggle(getattr(macros, self.func_combo.get()))

    def create_tab(self):
        control_tab = ttk.Frame()

        info_frame = Frame(control_tab)

        win_one_lbl = Label(info_frame, text="Primary Window: " + self.win_one)
        win_one_lbl.pack(anchor=W)

        win_two_lbl = Label(info_frame, text="Secondary Window: " + self.win_two)
        win_two_lbl.pack(anchor=W)

        self.state_label = Label(info_frame, text = "State: Stopped")
        self.state_label.pack(anchor=W)

        self.status_label = Label(info_frame, text="Status: ")
        self.status_label.pack(anchor=W)

        info_frame.pack(side=LEFT, expand=1, fill=BOTH)

        setup_frame = Frame(control_tab)

        Label(setup_frame, text="Macro Function: ").pack(anchor=N, side=LEFT)

        self.func_combo = ttk.Combobox(setup_frame, values=dir(macros)[8:])
        self.func_combo.pack(anchor=W, side=TOP)

        start_stop_btn = Button(control_tab, text="Start/Stop", command=self.start_stop_interface).pack(anchor=N, side=RIGHT)

        setup_frame.pack(side=LEFT, expand=1, fill=BOTH)

        control_tab.pack()

        return control_tab

    def get_control_tab(self):
        return self.control_tab


def set_main():
    main_win_txt.delete(0, END)
    main_win_txt.insert(0, list_box.get(ACTIVE))


def set_sec():
    sec_win_txt.delete(0, END)
    sec_win_txt.insert(0, list_box.get(ACTIVE))


def add_tab():
    control_tabs[len(control_tabs)] = WindowController(main_win_txt.get(), sec_win_txt.get())

    tab_control.add(control_tabs[len(control_tabs)-1].get_control_tab(), text=main_win_txt.get()[13:22])
    tab_control.pack(expand=1, fill='both')


def load_windows():
    list_box.delete(0, END)
    win32gui.EnumWindows(win_enum_handler, None)


def win_enum_handler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        hex_id = hex(hwnd)
        print(hwnd)
        list_box.insert(END, '0x' + hex_id[2:].zfill(8).upper() + ' : ' + win32gui.GetWindowText(hwnd))


control_tabs = {}

window = Tk()
window.geometry('810x300')
window.title("Window Manipulator")

tab_control = ttk.Notebook(window)
home_tab = ttk.Frame()
tab_control.add(home_tab, text="Home")

top_frame = Frame(home_tab)

create_btn = Button(top_frame, text='Load Windows', command=load_windows)
create_btn.pack(side='left', fill=X, expand=1)

control_btn = Button(top_frame, text='Create Control', command=add_tab)
control_btn.pack(side='right', fill=X, expand=1)

top_frame.pack()

list_box = Listbox(home_tab, font=('Courier', 10), width=100)
list_box.pack(fill='both', expand=1)

main_set = Button(home_tab, text="Select Window 1", command=set_main).pack(side='left')

main_win_txt = Entry(home_tab)
main_win_txt.pack(side='left', expand=1, fill='both')

sec_set = Button(home_tab, text="Select Window 2", command=set_sec).pack(side='left')

sec_win_txt = Entry(home_tab)
sec_win_txt.pack(side='left', expand=1, fill='both')

tab_control.pack(expand=1, fill='both')


def main():
    window.mainloop()


if __name__ == '__main__':
    main()
