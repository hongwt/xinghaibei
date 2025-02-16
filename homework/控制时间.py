import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import threading
import time
import os

class GameTimeController:
    def __init__(self, root):
        self.root = root
        self.root.title("游戏时间控制器")
        self.root.geometry("400x250")

        # 游戏可执行文件选择
        self.game_label = tk.Label(root, text="选择游戏可执行文件（.exe）：")
        self.game_label.pack()

        self.game_path_var = tk.StringVar(root)
        self.game_path_var.set("未选择游戏文件")
        self.game_path_entry = tk.Entry(root, textvariable=self.game_path_var, state="readonly", width=50)
        self.game_path_entry.pack()

        self.browse_button = tk.Button(root, text="浏览", command=self.browse_game_exe)
        self.browse_button.pack()

        # 设置时间
        self.time_label = tk.Label(root, text="设置游戏时间（分钟）：")
        self.time_label.pack()

        self.time_entry = tk.Entry(root)
        self.time_entry.pack()

        # 启动按钮
        self.start_button = tk.Button(root, text="开始游戏", command=self.start_game)
        self.start_button.pack()

        # 停止按钮
        self.stop_button = tk.Button(root, text="停止游戏", command=self.stop_game)
        self.stop_button.pack()

        # 游戏进程
        self.game_process = None
        self.timer_thread = None

    def browse_game_exe(self):
        # 允许用户从任意路径选择游戏的可执行文件
        file_path = filedialog.askopenfilename(
            title="选择游戏可执行文件",
            filetypes=[("可执行文件", "*.exe"), ("所有文件", "*.*")],
            initialdir="/"  # 默认打开根目录，用户可以自由选择盘符
        )
        if file_path:
            self.game_path_var.set(file_path)

    def start_game(self):
        game_path = self.game_path_var.get()
        if game_path == "未选择游戏文件":
            messagebox.showwarning("警告", "请选择一个游戏可执行文件！")
            return

        try:
            time_limit = int(self.time_entry.get())
            if time_limit <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("警告", "请输入有效的游戏时间！")
            return

        # 启动游戏
        try:
            self.game_process = subprocess.Popen(game_path)
            self.start_timer(time_limit * 60)  # 将分钟转换为秒
        except Exception as e:
            messagebox.showerror("错误", f"无法启动游戏：{e}")

    def start_timer(self, time_limit):
        self.timer_thread = threading.Thread(target=self.run_timer, args=(time_limit,))
        self.timer_thread.start()

    def run_timer(self, time_limit):
        start_time = time.time()
        while time.time() - start_time < time_limit:
            time.sleep(1)
            if not self.game_process.poll() is None:  # 检查游戏是否已经关闭
                break
        else:
            try:
                self.game_process.terminate()
                self.root.after(0, lambda: messagebox.showinfo("提示", "游戏时间到，请注意休息眼睛！"))
            except Exception as e:
                print(f"Error terminating game: {e}")

    def stop_game(self):
        if self.game_process:
            try:
                self.game_process.terminate()
                self.game_process = None
                if self.timer_thread:
                    self.timer_thread.join()
                    self.timer_thread = None
                messagebox.showinfo("提示", "游戏已停止！")
            except Exception as e:
                messagebox.showerror("错误", f"无法停止游戏：{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GameTimeController(root)
    root.mainloop()
