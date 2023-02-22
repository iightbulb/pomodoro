
import tkinter
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FF87B2"
CREAM = "#FFE6E6"
BLUE = "#7A86B6"
PURPLE = "#5C2E7E"
BLACK = "#000000"
RED = "#B25068"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = None
testing_commits = None
blah_hlah = 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    window.after_cancel(time)
    canvas.itemconfig(timer, text="00:00")
    label.config(text="")
    checkmark.config(text="")
    global reps
    reps = 0

    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    
    if reps == 8:
        countdown(long_break_secs)
        label.config(text="Long break")
    elif reps % 2 == 1:
        countdown(work_sec)
        label.config(text="Work")
    else:
        countdown(short_break_secs)
        label.config(text="Short break")
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global time
        time = window.after(1000, countdown, count - 1)
    else:
        start()
        global work_sessions
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            checkmark.config(text=marks)
   

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=60, pady=40, bg=CREAM)

canvas = tkinter.Canvas(width=200, height=224, bg=CREAM, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
fg=BLACK
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(101, 130, text="00:00", font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=1)

#timer label
label = tkinter.Label(text="", bg=CREAM, font=(FONT_NAME, 22))
label.grid(column=1, row=0)
label.config(padx=-200, pady=30)

#if timer = 0, add checkmark
checkmark = tkinter.Label(text="")
checkmark.grid(column=1, row=3)

#start button
button1 = tkinter.Button(text="Start", highlightthickness=0, command=start)
button1.grid(column=0, row=2)

#reset button
button2 = tkinter.Button(text="Reset", highlightthickness=0, command=reset)
button2.grid(column=2, row=2)

window.mainloop()


