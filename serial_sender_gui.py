```python
import serial
import time
import datetime
from tkinter import *
port = '/dev/ttyUSB2'
ser = serial.Serial(port)
now = datetime.datetime.now()


print("Maxutka™️ Technologies™️ SerialSender™️")
print("by maxutka99")
print("-------------------------------")
print("Serial ready on " + port)
print(now)
print("-------------------------------")
def enable():
    now = datetime.datetime.now()
    print(now)
    print("[log] 1 sended to " + port)
    ser.write(b'1')
def disable():
    now = datetime.datetime.now()
    print(now)
    print("[log] 0 sended to " + port)
    ser.write(b'0')

root = Tk()
root.title("Управление Умным домом")
root.geometry("150x100")

label1 = Label(text="SerialSender™️", font="Arial 14")
label1.pack()
btn = Button(text="1", padx="2", pady="2", command=enable)
btn1 = Button(text="0", padx="2", pady="2", command=disable)
btn1.pack(side=BOTTOM)
btn.pack(side=BOTTOM)

root.mainloop()
```
