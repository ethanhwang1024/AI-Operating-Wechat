def find_control_with_text(top_control, text):
    children = top_control.GetChildren()
    for child in children:
        if text in child.Name:
            return child
        result = find_control_with_text(child, text)
        if result is not None:
            return result
    return None


def find_control_with_text_list(top_control, text_list):
    children = top_control.GetChildren()
    for child in children:
        for text in text_list:
            if text in child.Name:
                return child
        result = find_control_with_text_list(child, text_list)
        if result is not None:
            return result
    return None


def find_control_with_control_type(top_control, control_type):
    children = top_control.GetChildren()
    for child in children:
        if child.ControlTypeName == control_type:
            return child
        result = find_control_with_control_type(child, control_type)
        if result is not None:
            return result
    return None
