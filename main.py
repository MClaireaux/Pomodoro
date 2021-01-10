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
img_nb = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(tomato_canvas, image=my_tomatoes[0])
    window.after_cancel(timer)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global img_nb
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    canvas.itemconfig(tomato_canvas, image=PhotoImage(file=f"tomato1.png"))

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text = "Break!", fg = RED)
        canvas.itemconfig(tomato_canvas, image=my_tomatoes[img_nb])
        img_nb = 0
    elif reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work", fg = GREEN)
        canvas.itemconfig(tomato_canvas, image=my_tomatoes[img_nb])
    else:
        count_down(short_break_sec)
        timer_label.config(text="Break!", fg = PINK)
        canvas.itemconfig(tomato_canvas, image=my_tomatoes[img_nb])
        img_nb += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps

    #Format the text of the timer following a 00:00 format
    min = math.floor(count / 60) #Round down
    sec = count % 60
    if sec < 10:
        sec = f"0{count % 60}"
    if min < 10:
        min = f"0{math.floor(count / 60)}"

    canvas.itemconfig(timer_text, text=f'{min}:{sec}') # Change the object timer_text in the canvas

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)  # Calls a certain fonction after a certain amount of time in ms. takes time, function name, and then function arguments
    else:
        start_timer()

    # We need to create a self-calling function, that calls itself every second

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

canvas = Canvas(width =400, height =430, bg = YELLOW, highlightthickness= 0) #In pixel

my_tomatoes = [PhotoImage(file = f"tomato{nb}.png") for nb in range(1,5)]

start_img = PhotoImage(file="start.png")# Import image
reset_img = PhotoImage(file="reset.png")# Import image

tomato_canvas = canvas.create_image(200,215, image=my_tomatoes[img_nb]) #Put image in the center
timer_text = canvas.create_text(210, 250, text = "00:00", fill = "white",font=(FONT_NAME, 45,"bold"))

timer_label = Label(text = "Timer", fg= GREEN, font = (FONT_NAME, 60), bg = YELLOW)
start_button = Button(window, borderwidth= 0, command = start_timer)
reset_button = Button(window, borderwidth= 0, command = reset_timer)

start_button.config(image = start_img, bg = YELLOW, highlightthickness= 0)
reset_button.config(image = reset_img, bg = YELLOW, highlightthickness= 0)


#Layout
timer_label.grid(column= 1, row=0)
canvas.grid(column = 1, row = 1)
start_button.grid(column = 0, row = 2)
reset_button.grid(column = 2, row = 2)

window.mainloop()