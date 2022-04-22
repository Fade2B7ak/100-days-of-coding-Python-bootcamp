from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text='00:00')
    timer_label.config(text='Timer')
    check.config(text='')
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_secs = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text='Break', fg=RED)
        count_down(long_break)

    elif reps % 2 == 0:
        timer_label.config(text='Break', fg=PINK)
        count_down(short_break)

    else:
        timer_label.config(text='Work', fg=GREEN)
        count_down(work_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_secs = count % 60
    if count_secs < 10:
        count_secs = f'0{count_secs}'

    canvas.itemconfig(time_text, text=f"{count_min}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(REPS/2)
        for rep in range(work_sessions):
            marks += '✔'
        check.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Work-Break Timer')
window.config(padx=70, pady=35, bg=YELLOW)


# Creating and fixing the pixels for the background, importing an image for the BG, changing the BG color
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg = PhotoImage(file='tomato.png')
canvas.create_image(100, 111, image=bg)
time_text = canvas.create_text(102, 130, text='00:00', fill=GREEN, font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2, row=2)



# Buttons
button1 = Button(text='Start', command=start_timer)
button1.grid(column=0, row=4)
button1 = Button(text='Reset', command=reset_timer)
button1.grid(column=4, row=4)

# Timer Label
timer_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(GREEN, 35, 'italic'))
timer_label.grid(column=2, row=0)
# The Check mark symbol
check = Label(fg=GREEN, bg=YELLOW, font=(GREEN, 15, 'bold'))
check.grid(column=2, row=4)

window.mainloop()
