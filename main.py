import gradio as gr
import requests
import json

# Initialize chat history
chat_history = []

def chat_with_server(system_message, user_message, user_name, server_name, temperature, frequency_penalty, presence_penalty):
    global chat_history
    url = "http://localhost:1234/v1/chat/completions"
    headers = {
        "Authorization": "Bearer lm-studio",
        "Content-Type": "application/json"
    }
    data = {
        "model": "Publisher/Repository",
        "messages": chat_history + [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ],
        "temperature": temperature,
        "frequency_penalty": frequency_penalty,
        "presence_penalty": presence_penalty
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        result = response.json()
        reply = result['choices'][0]['message']['content']
        chat_history.append({"role": "user", "content": user_message})
        chat_history.append({"role": "assistant", "content": reply})
        return chat_history_to_display(user_name, server_name)
    else:
        return "Error: Unable to get response from the server."

def chat_history_to_display(user_name, server_name):
    display_history = []
    for message in chat_history:
        role = message['role']
        content = message['content']
        if role == "user":
            display_history.append((f"{user_name}: {content}", ""))
        else:
            display_history.append((f"{server_name}: {content}", ""))
    return display_history

def send_message(system_message, user_name, server_name, user_message, temperature, frequency_penalty, presence_penalty):
    return chat_with_server(system_message, user_message, user_name, server_name, temperature, frequency_penalty, presence_penalty)

def recall_message(user_name, server_name):
    global chat_history
    if len(chat_history) > 1:
        chat_history.pop()  # Remove the last server message
        chat_history.pop()  # Remove the last user message
    return chat_history_to_display(user_name, server_name)

def resend_message(system_message, user_name, server_name, temperature, frequency_penalty, presence_penalty):
    if len(chat_history) > 0:
        last_user_message = chat_history[-2]['content']
        return send_message(system_message, user_name, server_name, last_user_message, temperature, frequency_penalty, presence_penalty)
    return chat_history_to_display(user_name, server_name)

def clear_history():
    global chat_history
    chat_history = []
    return []

# UI layout
with gr.Blocks() as demo:
    gr.Markdown("# 标题")
    
    user_name = gr.Textbox(label="用户代称(只是用于区分对话气泡,不会影响实际对话内容,请勿空白)", placeholder="此处输入名字")
    server_name = gr.Textbox(label="模型代称(只是用于区分对话气泡,不会影响实际对话内容,请勿空白)", placeholder="此处输入名字")
    
    system_message = gr.Textbox(label="身份信息和对话要求(System_message,请勿空白)", placeholder="此处输入信息")
    
    chat_history_box = gr.Chatbot(label="Chat History")

    user_message = gr.Textbox(label="输入框", placeholder="此处编辑要发送的消息")
    send_button = gr.Button("发送")
    
    with gr.Row():
        recall_button = gr.Button("撤回")
        resend_button = gr.Button("重发")
        clear_button = gr.Button("清空记录")
    
    with gr.Accordion("高级设置"):
        temperature = gr.Slider(0, 1, value=0.8, label="temperature")
        frequency_penalty = gr.Slider(0, 2, value=0, label="frequency_penalty")
        presence_penalty = gr.Slider(0, 2, value=0, label="presence_penalty")

    send_button.click(
        lambda sm, un, sn, um, t, fp, pp: send_message(sm, un, sn, um, t, fp, pp),
        [system_message, user_name, server_name, user_message, temperature, frequency_penalty, presence_penalty],
        chat_history_box
    )
    recall_button.click(
        lambda un, sn: recall_message(un, sn),
        [user_name, server_name],
        chat_history_box
    )
    resend_button.click(
        lambda sm, un, sn, t, fp, pp: resend_message(sm, un, sn, t, fp, pp),
        [system_message, user_name, server_name, temperature, frequency_penalty, presence_penalty],
        chat_history_box
    )
    clear_button.click(clear_history, outputs=chat_history_box)

demo.launch(share=True)
