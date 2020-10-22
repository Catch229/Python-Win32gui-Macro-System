import win32gui
import win32con
import win32api
import time


class NoxAutomate:

    def __init__(self, hwnd_s, hwnd_t, speed):
        self.hwnd_s = hwnd_s
        self.hwnd_t = hwnd_t
        self.speed = speed
        self.h = None
        self.w = None

    def __str__(self):
        rect = win32gui.GetWindowRect(self.hwnd_s)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        return "Window {}: \nLocation: {} {} \nSize: {} {}".format(win32gui.GetWindowText(self.hwnd_s), x, y, w, h)

    def update_l_w(self):
        rect = win32gui.GetWindowRect(self.hwnd_s)
        x = rect[0]
        y = rect[1]
        self.w = rect[2] - x
        self.h = rect[3] - y

    def click_point(self, x, y):
        win32gui.SendMessage(self.hwnd_s, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        win32gui.SendMessage(self.hwnd_s, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))
        time.sleep(self.speed)
        win32gui.SendMessage(self.hwnd_s, win32con.WM_LBUTTONUP, 0000, win32api.MAKELONG(x, y))

    def back(self):
        self.update_l_w()
        if self.w < self.h:
            x = 35
            y = 926
        else:
            x = 32
            y = 485
        win32gui.SendMessage(self.hwnd_s, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        win32gui.SendMessage(self.hwnd_t, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))
        time.sleep(self.speed)
        win32gui.SendMessage(self.hwnd_t, win32con.WM_LBUTTONUP, 0000, win32api.MAKELONG(x, y))
        time.sleep(self.speed)

    def home(self):
        self.update_l_w()
        if self.w < self.h:
            x = 35
            y = 955
        else:
            x = 27
            y = 528
        win32gui.SendMessage(self.hwnd_s, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        win32gui.SendMessage(self.hwnd_t, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))
        time.sleep(self.speed)
        win32gui.SendMessage(self.hwnd_t, win32con.WM_LBUTTONUP, 0000, win32api.MAKELONG(x, y))
        time.sleep(self.speed)

    def clean(self):
        win32gui.SendMessage(self.hwnd_s, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        win32gui.SendMessage(self.hwnd_t, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(13, 330))
        time.sleep(self.speed)
        win32gui.SendMessage(self.hwnd_t, win32con.WM_LBUTTONUP, 0000, win32api.MAKELONG(13, 330))
        time.sleep(self.speed)


def watch_ads(nox):
    print("Starting ads")
    counter = 0
    nox.home()
    time.sleep(2)
    nox.clean()
    time.sleep(2)
    nox.click_point(59, 360)
    time.sleep(22)
    print("First ad")
    nox.click_point(416, 513)
    time.sleep(2)
    nox.click_point(389, 442)
    time.sleep(55)
    nox.back()
    time.sleep(3)
    print("Starting ad loop")
    while counter < 19:
        nox.click_point(600, 416)
        time.sleep(55)
        nox.back()
        time.sleep(3)
        counter = counter + 1
    nox.clean()


def home_open(nox):
    nox.home()
    time.sleep(1)
    nox.clean()
    time.sleep(2)
    nox.click_point(59, 360)
    time.sleep(22)
    nox.click_point(27, 38)
    time.sleep(2)
    nox.click_point(672, 200)
    time.sleep(4)
    nox.click_point(650, 283)
    time.sleep(1)
    nox.click_point(80, 80)
    time.sleep(1)
    nox.click_point(606, 381)
    time.sleep(1)


def reset_log(nox):
    nox.home()
    time.sleep(1)
    nox.clean()
    time.sleep(2)
    nox.click_point(163, 347)  # open app terminal
    time.sleep(2)
    nox.click_point(163, 347)  # click twice to open keyboard
    time.sleep(0.5)
    nox.click_point(113, 788)  # key strokes
    time.sleep(0.01)
    nox.click_point(345, 713)
    time.sleep(0.01)
    nox.click_point(493, 925)
    time.sleep(0.01)
    nox.click_point(185, 713)
    time.sleep(0.01)
    nox.click_point(134, 713)
    time.sleep(0.01)
    nox.click_point(113, 788)
    time.sleep(0.01)
    nox.click_point(134, 713)
    time.sleep(0.01)
    nox.click_point(237, 713)
    time.sleep(0.01)
    nox.click_point(294, 713)
    time.sleep(0.01)
    nox.click_point(451, 713)
    time.sleep(0.01)
    nox.click_point(426, 852)
    time.sleep(0.01)
    nox.click_point(451, 713)
    time.sleep(0.01)
    nox.click_point(493, 925)
    time.sleep(5)
    nox.back()


def unlock_window(hwnd, hwnd2):
    win32gui.EnableWindow(hwnd, True)
    win32gui.EnableWindow(hwnd2, True)


def run_lucky7(hwnd, hwnd2):
    hnox = hwnd
    h_toolbar = hwnd2
    h_screen = win32gui.FindWindowEx(hnox, 0, None, "ScreenBoardClassWindow")
    nox = NoxAutomate(h_screen, h_toolbar, 0.1)
    print(nox)

    time.sleep(5)

    counter = 0
    while True:
        reset_log(nox)
        home_open(nox)
        nox.click_point(403, 371)
        nox.click_point(903, 488)
        time.sleep(1)
        nox.click_point(403, 371)
        for x in range(50000):
            nox.click_point(909, 533)
            nox.click_point(492, 373)
            nox.click_point(492, 430)
            time.sleep(0.1)
            counter = counter + 1
            print("Count: " + str(counter), end="\n", flush=False)
        watch_ads(nox)
