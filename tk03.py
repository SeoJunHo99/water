from tkinter import *

window = Tk()
btn = Button(window, bg="#3F7F35", fg="#FF0000", text="버튼", width="80", height="2")
btn.pack()
window.mainloop()

#rgb(레드. 그린. 블루) -> 0 ~ 255 2^8 2 4 8 16 32 64 128 256
#0 1 2 3 4 5 6 7 8 9 a b c d e f 16개
#0 ~ ff #FF0000 #00FF00 #0000FF #000000 #FFFFFF
#red green blue yellow purple skyblue rosegold