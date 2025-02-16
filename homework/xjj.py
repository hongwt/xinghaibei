Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
===== RESTART: C:\Users\pjunl\AppData\Local\Programs\Python\Python311\作业.py ====
Traceback (most recent call last):
  File "<string>", line 8, in circle
  File "C:\Users\pjunl\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1992, in circle
    self._go(l)
  File "C:\Users\pjunl\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Users\pjunl\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 3193, in _goto
    screen._drawline(self.drawingLineItem,
  File "C:\Users\pjunl\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 545, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Users\pjunl\AppData\Local\Programs\Python\Python311\Lib\tkinter\__init__.py", line 2839, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\pjunl\AppData\Local\Programs\Python\Python311\作业.py", line 4, in <module>
    turtle.circle(150)
  File "<string>", line 12, in circle
turtle.Terminator
