import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=800, height=500)

# Label

my_label = tkinter.Label(text="I am a label.", font=("Arial", 10, "bold"))
# my_label.pack(side="left")
my_label.pack(expand=True)

window.mainloop()
