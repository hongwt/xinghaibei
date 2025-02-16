import random

print("姓名：________________           日期：________________")

for _ in range(25):
    line = ""
    for _ in range(4):
        operation = random.choice([1, 2])
        if operation == 1:
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
            expr = f'{num1} × {num2} ='
            line += expr.ljust(len(expr) + 8)
        else:
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
            if num2 == 0:
                num2 = random.randint(1, 99)
            expr = f'{num1} ÷ {num2} ='
            line += expr.ljust(len(expr) + 8)
    print(line)
from tkinter import Tk, Button, Text
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_content_and_print():
    content = text_area.get("1.0", "end-1c")
    c = canvas.Canvas("output.pdf", pagesize=A4)
    c.drawString(100, 700, content)
    c.save()

root = Tk()

# 创建文本输入区域
text_area = Text(root, height=10, width=50)
text_area.pack()

# 创建打印按钮
print_button = Button(root, text="打印", command=generate_content_and_print)
print_button.pack()
import win32print
import win32ui

def print_text(text):
    hprinter = win32print.OpenPrinter(None)
    try:
        hdc = win32ui.CreateDC()
        printer_info = win32print.GetPrinter(hprinter, 2)
        printer_name = printer_info['pPrinterName']
        hdc.CreatePrinterDC(printer_name)
        hdc.StartDoc('My Document')
        hdc.StartPage()
        hdc.DrawText(text, (0, 0, 1000, 1000), win32con.DT_LEFT)
        hdc.EndPage()
        hdc.EndDoc()
    finally:
        win32print.ClosePrinter(hprinter)

text_to_print = "This is the text to be printed."
print_text(text_to_print)

