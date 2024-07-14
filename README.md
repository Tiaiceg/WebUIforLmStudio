
### WebUI for LmStudio

本项目旨在提供一个LmStudio的简单WebUI，实现远程连接到LmStudio的Local Server的目的。

This project aims to provide a simple web UI for LmStudio, enabling remote connection to LmStudio's local server.

您可以在本地运行WebUI并使用域名映射等方法或者Gradio提供的共享服务（Launch中添加share=True参数，默认已经添加）实现公网访问。这种情况下您需要检查main.py中第10行url的IP与端口是否与您的Local Server的IP与端口是否匹配。或者也可以将LmStudio的Local Server映射到公网来实现公网访问。

You can run the WebUI locally and use domain mapping methods or the sharing service provided by Gradio (add share=True parameter in Launch, already added by default) to achieve public network access. In this case, you need to check whether the IP and port in line 10 of main.py match the IP and port of your local server. Alternatively, you can map the LmStudio local server to the public network for public access.

---

### 特性 / Features

- **聊天界面**: 以对话形式发送和接收消息。
- **可调参数**: 调整温度、频率惩罚和存在惩罚，以控制模型的响应。
- **聊天记录**: 查看和管理聊天记录，提供撤回、重发和清除消息的选项。
- **用户自定义**: 设置用户和服务器名称，以实现个性化的聊天互动。

- **Chat Interface**: Send and receive messages in a conversational format.
- **Adjustable Parameters**: Modify temperature, frequency penalty, and presence penalty to control the model's responses.
- **Chat History**: View and manage chat history with options to recall, resend, and clear messages.
- **User Customization**: Set user and server names for personalized chat interactions.

---

### 安装 / Installation

1. **克隆仓库 / Clone the Repository**:
    ```bash
    git clone https://github.com/<your-username>/WebUIforLmStudio.git
    cd WebUIforLmStudio
    ```

2. **安装依赖 / Install Dependencies**:
    确保你已经安装了Python，然后运行以下命令:
    Ensure you have Python installed, then run:
    ```bash
    pip install -r requirements.txt
    ```

3. **启动服务器 / Start the Server**:
    ```bash
    python app.py
    ```

---

### 使用 / Usage

1. **打开界面 / Open the Interface**:
    启动服务器后，打开你的浏览器并访问提供的URL（默认: `http://127.0.0.1:7860`）。
    After starting the server, open your web browser and go to the provided URL (default: `http://127.0.0.1:7860`).

2. **输入用户和服务器名称 / Enter User and Server Names**:
    填写“用户名”和“服务器名称”字段以个性化你的聊天。
    Fill in the "User Name" and "Server Name" fields to personalize your chat.

3. **发送消息 / Send a Message**:
    - 在“你的消息”字段中输入你的消息。
    - 点击“发送”按钮提交你的消息。
    - Type your message in the "Your Message" field.
    - Click the "Send" button to submit your message.

4. **调整设置 / Adjust Settings**:
    - 使用“设置”部分的滑块调整温度、频率惩罚和存在惩罚。
    - Use the sliders in the "Settings" section to adjust the temperature, frequency penalty, and presence penalty.

5. **管理聊天记录 / Manage Chat History**:
    - **撤回**: 点击“撤回”按钮以删除最后的用户和服务器消息。
    - **重发**: 点击“重发”按钮以当前设置重新发送最后的用户消息。
    - **清除**: 点击“清除”按钮以清除整个聊天记录。
    - **Recall**: Click the "Recall" button to remove the last user and server message from the history.
    - **Resend**: Click the "Resend" button to resend the last user message with current settings.
    - **Clear**: Click the "Clear" button to clear the entire chat history.

---

### 代码说明 / Code Explanation

- **chat_with_server**: 使用当前聊天记录和新的用户消息向LmStudio服务器发送请求。
- **chat_history_to_display**: 格式化聊天记录以在UI中显示。
- **send_message**: 发送用户消息并更新聊天记录。
- **recall_message**: 从聊天记录中撤回最后的用户和服务器消息。
- **resend_message**: 重发最后的用户消息。
- **clear_history**: 清除整个聊天记录。
- **UI布局**: 使用Gradio创建带有各种组件（文本框，按钮，滑块）的网页界面。

- **chat_with_server**: Sends a request to the LmStudio server with the current chat history and new user message.
- **chat_history_to_display**: Formats the chat history for display in the UI.
- **send_message**: Sends a user message and updates the chat history.
- **recall_message**: Recalls the last user and server message from the chat history.
- **resend_message**: Resends the last user message.
- **clear_history**: Clears the entire chat history.
- **UI Layout**: Uses Gradio to create the web interface with various components (textbox, buttons, sliders).

---

### 环境要求 / Requirements

- Python 3.x
- Gradio
- Requests

安装所需的包 / Install the required packages using:
```bash
pip install gradio requests
```

---

### 待办事项 / To-Do List

1. 添加启动时修改IP和端口的功能。
2. 添加更多的可调参数。
3. 气泡总是出现在右侧，未来会尝试修改为左右气泡来区分角色。
4. 多语言支持。

1. Add the ability to modify IP and port at startup.
2. Add more adjustable parameters.
3. The bubbles always appear on the right side, in the future, we will try to modify them to distinguish roles with left and right bubbles.
4. Multi-language support.

---

### 贡献 / Contributing

欢迎提出issue或pull request来提出修改意见。

Contributions are welcome! Feel free to submit an issue or pull request with your suggestions for improvements.

---

### 许可证 / License

本项目使用MIT许可证。

This project is licensed under the MIT License.

---

### 联系方式 / Contact

如有任何问题或需要支持，请联系 [your-email@example.com]。

For questions or support, please contact [your-email@example.com].

---

### requirements.txt

```
gradio
requests
```
