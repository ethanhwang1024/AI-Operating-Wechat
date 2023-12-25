import uiautomation as auto
from uiautomation.uiautomation import Bitmap
from config import warn_word


def send_msg(edit_name, window, content, msg_type=1):
    content = content + warn_word
    edit = window.EditControl(Name=edit_name)
    send_button = window.ButtonControl(Name='发送(S)', Depth=14)
    if msg_type:
        auto.SetClipboardText(content)
    else:
        auto.SetClipboardBitmap(Bitmap.FromFile(content))
    edit.Click(simulateMove=False, waitTime=0.6)
    edit.SendKeys('{Ctrl}v', waitTime=0.1)
    send_button.Click(simulateMove=False, waitTime=0.3)
