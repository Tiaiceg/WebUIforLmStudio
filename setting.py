import tkinter as tk
from tkinter import messagebox
import re
import subprocess
import os
import signal
import webbrowser

# Global variable to store the process
process = None
main_py_process = None

def update_main_py(lmstudio_url, server_ip, server_port, enable_share):
    with open("main.py", "r", encoding="utf-8") as file:
        content = file.read()
    
    # Update Lmstudio URL
    content = re.sub(r'url = "http://[^/]+/v1', f'url = "{lmstudio_url}/v1', content)
    
    # Update server IP and port
    content = re.sub(r'demo\.launch\(server_name="[^"]+", server_port=\d+', f'demo.launch(server_name="{server_ip}", server_port={server_port}', content)
    
    # Update share parameter
    if enable_share:
        if "share=True" not in content:
            content = re.sub(r'demo\.launch\(([^)]*)\)', r'demo.launch(\1, share=True)', content)
    else:
        content = re.sub(r', share=True', '', content)

    with open("main.py", "w", encoding="utf-8") as file:
        file.write(content)

def run_main_py():
    global process, main_py_process
    # Open main.py in a new terminal window
    if os.name == 'nt':  # Windows
        main_py_process = subprocess.Popen(['python', 'main.py'])
    else:  # macOS, Linux
        main_py_process = subprocess.Popen(['python3', 'main.py'])

def open_webui():
    server_ip = server_ip_entry.get()
    server_port = server_port_entry.get()
    url = f"http://{server_ip}:{server_port}"
    webbrowser.open_new(url)

def save_config():
    lmstudio_url = lmstudio_url_entry.get()
    server_ip = server_ip_entry.get()
    server_port = server_port_entry.get()
    enable_share = enable_share_var.get()
    update_main_py(lmstudio_url, server_ip, server_port, enable_share)
    write_output("配置已保存")

def start_program():
    lmstudio_url = lmstudio_url_entry.get()
    server_ip = server_ip_entry.get()
    server_port = server_port_entry.get()
    enable_share = enable_share_var.get()
    update_main_py(lmstudio_url, server_ip, server_port, enable_share)
    write_output("启动程序中...")
    run_main_py()
    if open_webui_var.get():
        open_webui()

def close_program():
    global process, main_py_process
    if main_py_process:
        if os.name == 'nt':  # Windows
            os.system('taskkill /F /T /PID ' + str(main_py_process.pid))
        else:  # macOS, Linux
            os.killpg(os.getpgid(main_py_process.pid), signal.SIGTERM)
        main_py_process = None
        write_output("程序已关闭")
    root.destroy()

def write_output(text):
    output_text.configure(state=tk.NORMAL)
    output_text.insert(tk.END, text + "\n")
    output_text.configure(state=tk.DISABLED)

root = tk.Tk()
root.title("WebUI参数设置")

tk.Label(root, text="Lmstudio地址设置").grid(row=0, column=0)
lmstudio_url_entry = tk.Entry(root)
lmstudio_url_entry.insert(0, "http://localhost:1234")
lmstudio_url_entry.grid(row=0, column=1, columnspan=2)

tk.Label(root, text="WebUI IP与端口设置").grid(row=1, column=0)
server_ip_entry = tk.Entry(root)
server_ip_entry.insert(0, "127.0.0.1")
server_ip_entry.grid(row=1, column=1)
server_port_entry = tk.Entry(root)
server_port_entry.insert(0, "7860")
server_port_entry.grid(row=1, column=2)

enable_share_var = tk.BooleanVar()
tk.Checkbutton(root, text="是否启用Gradio公网共享", variable=enable_share_var).grid(row=2, columnspan=3)

open_webui_var = tk.BooleanVar()
tk.Checkbutton(root, text="启动时在浏览器打开WebUI", variable=open_webui_var).grid(row=3, columnspan=3)

tk.Button(root, text="保存配置", command=save_config).grid(row=4, column=0)
tk.Button(root, text="启动", command=start_program).grid(row=4, column=1)
tk.Button(root, text="关闭", command=close_program).grid(row=4, column=2)

output_text = tk.Text(root, height=10, width=60, state=tk.DISABLED)
output_text.grid(row=5, columnspan=3)

root.mainloop()
