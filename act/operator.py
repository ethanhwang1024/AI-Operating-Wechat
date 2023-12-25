import pyautogui as gui


def scroll_up(times, long):
    for t in range(0, times):
        gui.scroll(long)
