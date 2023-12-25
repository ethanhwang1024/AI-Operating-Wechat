def is_notify(chat_shot):
    chat_shot_inner = chat_shot.GetChildren()[0]
    if len(chat_shot_inner.GetChildren()) >= 3:
        return True
    else:
        return False


def is_notify_with_text(chat_shot):
    chat_shot_inner = chat_shot.GetChildren()[0]
    if len(chat_shot_inner.GetChildren()) >= 3:
        if chat_shot_inner.GetChildren()[2].ControlTypeName == 'TextControl':
            return True
    return False
