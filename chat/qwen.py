import dashscope
import random
from http import HTTPStatus
from config import *

dashscope.api_key = qwen_apikey


def call_qwen_online(his,model_choice):
    history = his
    messages = []
    count = 0
    if len(history) % 2 == 0:
        messages.append({'role': 'system', 'content': history[0]})
        history = history[1:]
    for h in history:
        count = count + 1
        if count % 2 == 1:
            messages.append({'role': 'user', 'content': h})
        else:
            messages.append({'role': 'assistant', 'content': h})
    response = None
    if model_choice=="qwen_turbo":
        response = dashscope.Generation.call(
            dashscope.Generation.Models.qwen_turbo,
            messages=messages,
            # set the random seed, optional, default to 1234 if not set
            seed=random.randint(1, 10000),
            result_format='message',  # set the result to be "message" format.
        )
    elif model_choice=="qwen_max":
        response = dashscope.Generation.call(
            dashscope.Generation.Models.qwen_max,
            messages=messages,
            # set the random seed, optional, default to 1234 if not set
            seed=random.randint(1, 10000),
            result_format='message',  # set the result to be "message" format.
        )
    elif model_choice=="qwen_plus":
        response = dashscope.Generation.call(
            dashscope.Generation.Models.qwen_plus,
            messages=messages,
            # set the random seed, optional, default to 1234 if not set
            seed=random.randint(1, 10000),
            result_format='message',  # set the result to be "message" format.
        )
    if response.status_code == HTTPStatus.OK:
        his.append(response['output']['choices'][0]['message']['content'])
        return his
    else:
        return his
