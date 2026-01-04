# 主程序入口
import tkinter as tk
from tkinter import messagebox, simpledialog
import data
import logic
import voice
import threading

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("校园AI指路小助手")
        self.root.geometry("900x650")
        
        # 初始化语音助手
        self.ai_voice = voice.VoiceAssistant()
        
        # 初始化界面
        self.setup_ui()
        
        # 绘制初始地图
        self.draw_map()
        
        # 欢迎语
        self.root.after(1000, lambda: self.ai_voice.speak("你好，我是校园指路小助手，请告诉我你要找谁？"))

    def setup_ui(self):
        # 标题
        self.label_title = tk.Label(self.root, text="校园AI指路小助手", font=("微软雅黑", 24, "bold"), fg="#333")
        self.label_title.pack(pady=15)
        
        # 地图区域 (Canvas)
        self.canvas_frame = tk.Frame(self.root, bd=2, relief=tk.SUNKEN)
        self.canvas_frame.pack(pady=10)
        self.canvas = tk.Canvas(self.canvas_frame, width=800, height=450, bg="#f0f8ff") # 淡蓝色背景
        self.canvas.pack()
        
        # 控制区域
        self.frame_controls = tk.Frame(self.root)
        self.frame_controls.pack(pady=20)
        
        self.btn_speak = tk.Button(self.frame_controls, text="🎤 按住说话", font=("微软雅黑", 14), bg="#4CAF50", fg="white", command=self.on_speak)
        self.btn_speak.pack(side=tk.LEFT, padx=20)
        
        tk.Label(self.frame_controls, text="或者输入名字:", font=("微软雅黑", 12)).pack(side=tk.LEFT)
        
        self.entry_name = tk.Entry(self.frame_controls, font=("微软雅黑", 14), width=10)
        self.entry_name.pack(side=tk.LEFT, padx=10)
        
        self.btn_search = tk.Button(self.frame_controls, text="🔍 查询", font=("微软雅黑", 14), bg="#2196F3", fg="white", command=self.on_search)
        self.btn_search.pack(side=tk.LEFT, padx=10)
        
        self.btn_reset = tk.Button(self.frame_controls, text="🔄 重置", font=("微软雅黑", 14), command=self.reset_map)
        self.btn_reset.pack(side=tk.LEFT, padx=10)

        # 状态栏
        self.status_var = tk.StringVar()
        self.status_var.set("准备就绪")
        self.status_bar = tk.Label(self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def draw_map(self):
        self.canvas.delete("all")
        
        # 绘制连线
        for node, neighbors in data.MAP_GRAPH.items():
            x1, y1 = data.NODE_COORDS[node]
            for neighbor in neighbors:
                if neighbor in data.NODE_COORDS:
                    x2, y2 = data.NODE_COORDS[neighbor]
                    self.canvas.create_line(x1, y1, x2, y2, fill="#ccc", width=3, tags="map_line")

        # 绘制节点
        for name, (x, y) in data.NODE_COORDS.items():
            # 不同的节点颜色不同
            color = "#FFC107" # 默认黄色
            radius = 15
            if "班" in name or "-" in name: # 教室
                color = "#8BC34A" # 绿色
            elif name == "校门口":
                color = "#FF5722" # 红色
                radius = 20
            
            self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color, outline="white", width=2, tags="map_node")
            self.canvas.create_text(x, y+radius+15, text=name, font=("微软雅黑", 10, "bold"), tags="map_text")

    def reset_map(self):
        self.canvas.delete("path") # 删除路径
        self.canvas.delete("walker") # 删除行人
        self.entry_name.delete(0, tk.END)
        self.status_var.set("地图已重置")

    def on_speak(self):
        self.status_var.set("正在听...")
        self.root.update()
        
        # 在新线程中运行语音识别，防止界面卡死
        threading.Thread(target=self._listen_thread).start()

    def _listen_thread(self):
        text = self.ai_voice.listen()
        if text:
            # 使用 after 方法在主线程更新 UI
            self.root.after(0, lambda: self.entry_name.delete(0, tk.END))
            self.root.after(0, lambda: self.entry_name.insert(0, text))
            self.root.after(0, self.on_search) # 回到主线程执行搜索
        else:
            self.root.after(0, lambda: self.status_var.set("未识别到语音"))
            # 如果没有语音库，提示手动输入
            if not voice.ASR_AVAILABLE:
                 self.root.after(0, lambda: messagebox.showinfo("提示", "语音识别不可用，请手动输入名字。"))

    def on_search(self):
        name = self.entry_name.get().strip()
        if not name:
            messagebox.showwarning("提示", "请输入名字")
            return
            
        self.status_var.set(f"正在查找: {name}...")
        results = logic.find_student(name, data.STUDENTS)
        
        if not results:
            msg = f"抱歉，没有找到叫 {name} 的同学。"
            self.status_var.set(msg)
            self.ai_voice.speak(msg)
            messagebox.showinfo("结果", msg)
            return
            
        if len(results) == 1:
            student = results[0]
            self.confirm_and_navigate(name, student)
        else:
            # 处理重名
            self.handle_duplicate_names(name, results)

    def handle_duplicate_names(self, name, results):
        msg = f"找到了 {len(results)} 个叫 {name} 的同学。"
        self.ai_voice.speak(msg + "请选择是哪个班级的？")
        
        # 弹出选择框
        options = [f"{s['grade']}年级{s['class']}班" for s in results]
        choice = simpledialog.askstring("重名确认", f"找到了多个 {name}，请输入序号(1-{len(results)})或完整班级名:\n" + "\n".join([f"{i+1}. {opt}" for i, opt in enumerate(options)]))
        
        if choice:
            # 简单的解析逻辑：如果是数字，取索引；如果是文字，模糊匹配
            selected_student = None
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(results):
                    selected_student = results[idx]
            else:
                for s in results:
                    if str(s['grade']) in choice and str(s['class']) in choice:
                        selected_student = s
                        break
            
            if selected_student:
                self.confirm_and_navigate(name, selected_student)
            else:
                self.ai_voice.speak("选择无效，请重新查询。")

    def confirm_and_navigate(self, name, student):
        target_loc = student['location']
        grade_class = f"{student['grade']}年级{student['class']}班"
        
        msg = f"找到了，{name} 在 {grade_class}。"
        self.status_var.set(msg)
        self.ai_voice.speak(msg + "正在为您规划路线。")
        
        # 开始导航
        self.start_navigation("校门口", target_loc)

    def start_navigation(self, start, end):
        path = logic.find_path(start, end, data.MAP_GRAPH)
        if not path:
            self.ai_voice.speak("抱歉，无法计算路径。")
            return
            
        self.draw_path_animation(path)

    def draw_path_animation(self, path):
        self.canvas.delete("path")
        self.canvas.delete("walker")
        
        # 绘制静态红线
        points = []
        for node in path:
            points.extend(data.NODE_COORDS[node])
        
        self.canvas.create_line(points, fill="red", width=5, arrow=tk.LAST, tags="path", dash=(5, 2))
        
        # 动画效果：一个小圆点沿着路径移动
        self.animate_walker(path, 0)
        
        self.ai_voice.speak("请跟随红色路线前往。")

    def animate_walker(self, path, index):
        if index >= len(path) - 1:
            return
            
        start_node = path[index]
        end_node = path[index+1]
        
        x1, y1 = data.NODE_COORDS[start_node]
        x2, y2 = data.NODE_COORDS[end_node]
        
        # 创建或移动 walker
        if index == 0:
            self.walker = self.canvas.create_oval(x1-5, y1-5, x1+5, y1+5, fill="blue", tags="walker")
        
        # 简单的插值动画
        steps = 20
        dx = (x2 - x1) / steps
        dy = (y2 - y1) / steps
        
        def step_move(s):
            if s < steps:
                self.canvas.move(self.walker, dx, dy)
                self.root.after(50, lambda: step_move(s+1))
            else:
                self.animate_walker(path, index+1)
                
        step_move(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
