from act.Entry import *
from chat.Entry import *
from config import *
from datetime import datetime

auto.uiautomation.SetGlobalSearchTimeout(1)

window = get_window()
chat_list_panel = get_chat_list_panel(window)
chat_list = chat_list_panel.GetChildren()
notify_list = []
name = None
chat_shot = None
history = init_history
chat_text = ""


def execute(num):
    global window
    global chat_list_panel
    global chat_list
    global notify_list
    global name
    global chat_shot
    global history
    global chat_text
    if num == "0":
        # 重新获得新消息
        time.sleep(1)
        window = get_window()
        chat_list_panel = get_chat_list_panel(window)
        chat_list = chat_list_panel.GetChildren()
        notify_list = []
        for chat_shot in chat_list:
            if is_notify_with_text(chat_shot):
                name = find_control_with_control_type(chat_shot, "ButtonControl").Name
                if name in name_exclude:
                    continue
                notify_list.append(chat_shot)
        if len(notify_list) == 0:
            return "0"
        else:
            return "1"
    elif num == "1":
        # 点击chat_shot
        for chat_shot_inner in notify_list:
            name = find_control_with_control_type(chat_shot_inner, "ButtonControl").Name
            if name in name_exclude:
                continue
            chat_shot = chat_shot_inner
            return "2"
    elif num == "2":
        history = init_history
        new_message_coming_prompt = new_message_coming_prompt_tp.format(name, name)
        history.append(new_message_coming_prompt)
        history = do_chat_until_status(model, history)
        status = history[-1]
        return status
    elif num == "3":
        chat_shot.Click(simulateMove=False, waitTime=1)
        try:
            window.EditControl(Name=name)
        except:
            # 退回状态2
            return "2"
        chat_text = get_chat_text(window)
        return "4"
    elif num == "4":
        history_message_prompt = history_message_prompt_tp.format(name, datetime.now(),
                                                                  chat_text, name)
        history.append(history_message_prompt)
        history = do_chat_until_status(model, history)
        status = history[-1]
        return status
    elif num == "5":
        input_prompt = input_prompt_tp
        history.append(input_prompt)
        history = do_chat(model, history)
        try:
            send_msg(name, window, history[-1])
        except:
            return "0"
        if len(notify_list) <= 1:
            notify_list = []
            fileup = auto.ButtonControl(Name="文件传输助手")
            fileup.Click(simulateMove=False, waitTime=1)
            return "0"
        else:
            notify_list = notify_list[1:]
            return "1"
