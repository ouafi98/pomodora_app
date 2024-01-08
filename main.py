""" Pomodoro App"""

from tkinter import *
from playsound import playsound



# --------------------------- constants ------------------
WORKING_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

count_id = None

# -------------------------- countdown -----------------------------

def play_sound():
    playsound("./sounds/doorbell2-6450.mp3", block=False)

def raise_above_all(window):
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

def start_timer():
    global reps
    reps += 1
    
    if reps%8 == 0:
        raise_above_all(window=window)
        play_sound()
        long_break_sec = LONG_BREAK_MIN * 60
        title_label.config(text="Break", fg="#1B4242")
        count_down(long_break_sec)
    elif reps%2 == 0:
        raise_above_all(window=window)
        play_sound()
        short_break_sec = SHORT_BREAK_MIN * 60
        title_label.config(text="Break", fg="#9EC8B9")
        count_down(short_break_sec)
    elif reps%2 != 0 :
        work_sec = WORKING_MIN * 60
        title_label.config(text="Work", fg="#A35709")
        count_down(work_sec)
    



def reset_timer():
    global count_id
    global reps
    reps = 0
    window.after_cancel(count_id)
    title_label.config(text="Timer", fg="#A35709")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="✔")
    


def count_down(count):
    global count_id
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
       count_id = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps//2):
            marks += "✔"
        check_marks.config(text=marks)

# -------------------------- UI Setup ----------------------------
window = Tk()
window.title("Pomodoro App")
# window.config(bg="black")
window.config(padx=100, pady=50, bg="black")




#--- menubar ----
def donothing():
   t = Toplevel(window)
   t.title('Config Menu')
   t.label()
   work_time_label = Label(text="Work Time in minute")


menubar = Menu(window, tearoff=0)
appmenu = Menu(menubar, name="menu", tearoff=0)
menubar.add_cascade(label='Menu', menu=appmenu)
appmenu.add_command(label="Config", command=donothing)
appmenu.add_separator()
appmenu.add_command(label='About...')
# menubar.add_cascade(menu=appmenu)
window['menu'] = menubar # <=> window.config(menu=menubar)





title_label = Label(text="Timer", fg="#A35709", bg="black", font=("Courier", 65, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=388, height=394, bg="black", highlightthickness=0)
img = PhotoImage(file="./image/lion.png")
canvas.create_image((194,197), image=img)
timer_text = canvas.create_text((210,220), text="00:00", fill="#F0E3CA", font=("Courier", 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset",  highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", fg="#A35709", bg="black", font=("",30))
check_marks.grid(column=1, row=3)



window.mainloop()