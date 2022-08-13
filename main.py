from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    windoow.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps = reps + 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        my_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        my_label.config(text="BREAK", fg=PINK)

    else:
        count_down(WORK_MIN*60)
        my_label.config(text="WORK", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = windoow.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

windoow = Tk()
windoow.title("Pomodoro")
windoow.config(padx=100, pady=50, bg=YELLOW)


my_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
my_label.grid(rows=1, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

button1 = Button(text="Start", highlightthickness=0, command=start_timer)
button1.grid(row=3, column=1)

#check_marks = "✔"
check_marks = Label(bg=YELLOW, fg=GREEN)
check_marks.grid(row=4, column=2)

button2 = Button(text="Restart", highlightthickness=0, command=reset_timer)
button2.grid(row=3, column=3)
windoow.mainloop()