import tkinter as tk
from HexToDex import *

window = tk.Tk(className=" HEX to DEX")
window.geometry("400x100")
window.resizable(width=False, height=False)

L1 = tk.Label(window, text="HEX")
L1.pack(side=tk.LEFT)
EIn = tk.Entry(window, bd=5)
EIn.pack(side=tk.LEFT)

L2 = tk.Label(window, text="= DEX")
L2.pack(side=tk.LEFT)

EOut_text = tk.StringVar()
EOut = tk.Entry(window, bd=5, textvariable=EOut_text)
EOut.pack(side=tk.LEFT)


def call_result(event):
    HEX = (EIn.get())
    result = hexadecimalToDecimal(HEX)
    print(result)
    EOut_text.set(result)


window.bind('<Return>', call_result)

window.mainloop()
