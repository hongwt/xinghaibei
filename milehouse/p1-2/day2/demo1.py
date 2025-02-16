import random
import tkinter as tk
def convert_choice(choice):
    if choice == 0:
        return "剪刀"
    elif choice == 1:
        return "石头"
    elif choice == 2:
        return "布"
    else:
        return "无效选择"

def play_game():
    human = int(choice_entry.get())
    computer = random.randint(0, 2)
    human_choice = convert_choice(human)
    human_choice_label.config(text="你的选择是：" + human_choice)
    if human < 0 or human > 2:
        return
    computer_choice = convert_choice(computer)
    computer_choice_label.config(text="电脑的选择是：" + computer_choice)
    if human == computer:
        result_label.config(text="平局")
    elif human == 0 and computer == 2 or human == 1 and computer == 0 or human == 2 and computer == 1:
        result_label.config(text="你赢了")
    else:
        result_label.config(text="你输了")

# Create the main window
window = tk.Tk()
window.title("猜拳小游戏")

# Create the GUI components
choice_label = tk.Label(window, text="请输入您的选择：0剪刀，1石头，2布：")
choice_label.pack()

choice_entry = tk.Entry(window)
choice_entry.pack()

play_button = tk.Button(window, text="开始游戏", command=play_game)
play_button.pack()

human_choice_label = tk.Label(window, text="你的选择是：")
human_choice_label.pack()

computer_choice_label = tk.Label(window, text="电脑的选择是：")
computer_choice_label.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Start the main event loop
window.mainloop()
