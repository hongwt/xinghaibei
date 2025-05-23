import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# 创建主窗口
root = tk.Tk()
root.title("信息管理系统")

# 存储用户信息的列表
users = []

# 添加用户信息的函数
def add_user():
    name = entry_name.get()
    age = entry_age.get()
    height = entry_height.get()
    
    if not name or not age or not height:
        messagebox.showwarning("警告", "请填写所有字段！")
        return
    
    # 检查名称是否重复
    for user in users:
        if user["名称"] == name:
            messagebox.showwarning("警告", "名称不能重复！")
            return
    
    try:
        age = int(age)
        height = float(height)
    except ValueError:
        messagebox.showwarning("警告", "年龄必须是整数，身高必须是数字！")
        return
    
    user = {"名称": name, "年龄": age, "身高": height}
    users.append(user)
    messagebox.showinfo("成功", "用户信息已添加！")
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    update_table()

# 选中表格中的数据时，将值显示在输入框中
def on_select(event):
    selected_item = tree.selection()
    if not selected_item:
        return
    item = tree.item(selected_item[0])
    values = item["values"]
    entry_name.delete(0, tk.END)
    entry_name.insert(0, values[1])  # 名称
    entry_age.delete(0, tk.END)
    entry_age.insert(0, values[2])  # 年龄
    entry_height.delete(0, tk.END)
    entry_height.insert(0, values[3])  # 身高

# 修改选中用户信息的函数
def update_user():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("警告", "请先选择一个用户！")
        return
    
    name = entry_name.get()
    age = entry_age.get()
    height = entry_height.get()
    
    if not name or not age or not height:
        messagebox.showwarning("警告", "请填写所有字段！")
        return
    
    try:
        age = int(age)
        height = float(height)
    except ValueError:
        messagebox.showwarning("警告", "年龄必须是整数，身高必须是数字！")
        return
    
    # 检查名称是否重复（排除当前选中的用户）
    for user in users:
        if user["名称"] == name and user != users[int(tree.item(selected_item[0])["values"][0]) - 1]:
            messagebox.showwarning("警告", "名称不能重复！")
            return
    
    # 更新用户信息
    idx = int(tree.item(selected_item[0])["values"][0]) - 1
    users[idx] = {"名称": name, "年龄": age, "身高": height}
    messagebox.showinfo("成功", "用户信息已更新！")
    update_table()

# 更新表格数据的函数
def update_table():
    # 清空表格
    for row in tree.get_children():
        tree.delete(row)
    
    # 插入新的用户数据
    for idx, user in enumerate(users, start=1):
        tree.insert("", "end", values=(idx, user["名称"], user["年龄"], user["身高"]))

# 创建输入框和标签
label_name = tk.Label(root, text="名称:")
label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_age = tk.Label(root, text="年龄:")
label_age.grid(row=1, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=5)

label_height = tk.Label(root, text="身高 (cm):")
label_height.grid(row=2, column=0, padx=10, pady=5)
entry_height = tk.Entry(root)
entry_height.grid(row=2, column=1, padx=10, pady=5)

# 创建按钮
button_add = tk.Button(root, text="添加用户", command=add_user)
button_add.grid(row=3, column=0, pady=10)

# 创建修改按钮
button_update = tk.Button(root, text="修改用户", command=update_user)
button_update.grid(row=3, column=2, pady=10)

# 创建表格
columns = ("编号", "名称", "年龄", "身高")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("编号", text="编号")
tree.heading("名称", text="名称")
tree.heading("年龄", text="年龄")
tree.heading("身高", text="身高 (cm)")
tree.column("编号", width=50, anchor="center")
tree.column("名称", width=100, anchor="center")
tree.column("年龄", width=100, anchor="center")
tree.column("身高", width=100, anchor="center")
tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# 绑定表格的选中事件
tree.bind("<<TreeviewSelect>>", on_select)

# 运行主循环
root.mainloop()