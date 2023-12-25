import time

from chat.qwen import *


def do_chat(model_choice, his):
    while True:
        if "qwen" in model_choice:
            size = len(his)
            his = call_qwen_online(his,model_choice)
            if size == len(his):
                time.sleep(1)
                continue
            return his


def do_chat_until_status(model_choice, his):
    while True:
        size = len(his)
        his = do_chat(model, his)
        if size == len(his):
            time.sleep(1)
            continue
        if not his[-1].isdigit():
            time.sleep(1)
            continue
        return his
