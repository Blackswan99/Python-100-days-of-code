from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=90, pady=50, bg=YELLOW)


photo = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW)
canvas.create_image(101, 113, image=photo)

canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 15, "bold"))
canvas.pack()

window.mainloop()
