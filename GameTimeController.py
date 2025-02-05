import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import subprocess
import threading
import time
import os
import psutil

class GameTimeController:
    def get_running_processes():
        processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            processes.append(proc.info['name'])
        return processes

    def __init__(self, root):
        self.root = root
        self.root.title("游戏时间控制器")
        self.root.geometry("400x80")

        # 第一行容器
        self.row1_frame = tk.Frame(root)
        self.row1_frame.pack()

        self.game_label = tk.Label(self.row1_frame, text="游戏进程名：")
        self.game_label.pack(side=tk.LEFT)

        self.game_path_var = tk.StringVar(root)
        self.game_path_var.set("请选择游戏进程")
        self.game_path_combobox = ttk.Combobox(self.row1_frame, textvariable=self.game_path_var, state="readonly", width=25)
        self.game_path_combobox['values'] = self.get_running_processes()
        self.game_path_combobox.pack(side=tk.LEFT)

        self.refresh_button = tk.Button(self.row1_frame, text="刷新进程", command=self.refresh_processes)
        self.refresh_button.pack(side=tk.LEFT)

        # 第二行容器
        self.row2_frame = tk.Frame(root)
        self.row2_frame.pack()

        self.time_label = tk.Label(self.row2_frame, text="设置游戏时间（分钟）：")
        self.time_label.pack(side=tk.LEFT)

        self.time_entry = tk.Entry(self.row2_frame)
        self.time_entry.pack(side=tk.LEFT)

        self.start_button = tk.Button(self.row2_frame, text="开始计时", command=self.start_counting_time)
        self.start_button.pack(side=tk.LEFT)

        self.game_process = None
        self.timer_thread = None

    def get_running_processes(self):
        processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            process_name = proc.info['name'].lower()
            if process_name.endswith('.exe') and process_name not in ['svchost.exe', 'explorer.exe', 'taskmgr.exe',
                                             '3dexperience.exe', 'acwebbrowser.exe', 'code.exe', 
                                             'curseforge.exe', 'runtimebroker.exe', 'browser.exe',
                                               'cmd.exe', 'conhost.exe']:
                processes.append(process_name)
        processes.sort()  # Sort the processes alphabetically
        return processes

    def refresh_processes(self):
        self.game_path_combobox['values'] = self.get_running_processes()

    def start_counting_time(self):
        game_path = self.game_path_var.get()
        if game_path == "请选择游戏进程":
            messagebox.showwarning("警告", "请选择一个游戏进程！")
            return

        try:
            time_limit = int(self.time_entry.get())
            if time_limit <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("警告", "请输入有效的游戏时间！")
            return
        self.start_timer(time_limit)

    def start_timer(self, time_limit):
        self.timer_thread = threading.Thread(target=self.run_timer, args=(time_limit,))
        self.timer_thread.start()

    def run_timer(self, time_limit):
        start_time = time.time()
        time_limit *= 60  # Convert time_limit to minutes
        while time.time() - start_time < time_limit:
            time.sleep(1)
            if self.game_process is not None and not self.game_process.poll() is None:  # 检查游戏是否已经关闭
                break
        else:
            try:
                if self.game_process is not None:
                    self.game_process.terminate()
                self.root.after(0, lambda: messagebox.showinfo("提示", "游戏时间到，请注意休息眼睛！"))
            except Exception as e:
                print(f"Error terminating game: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GameTimeController(root)
    root.mainloop()
