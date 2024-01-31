from tkinter import *
from tkinter import messagebox

x = input("Do you want to convert meters to inches[m] or inches to meters[i]? ")


window = Tk()
window.title("Meters to inches converter")
window.geometry("500x300+550+355")


e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=0, column=1, pady=10, padx=10)

i = Label(window, text='inch', bg="light gray")
i.grid(row=2, column=0, pady=10, padx=10)

e1 = Label(window, text="Enter length in meters", bg="light gray")
e1.grid(row=0, column=0, padx=10, pady=10)

t = Text(window, height=1, width=15)
t.grid(row=2, column=1, pady=10, padx=10)
t.delete("1.0", END)

def conversion_to_inches():
    if x.lower() == "m":
        length_in_meters = float(e2_value.get())
        inch = length_in_meters * 39.37
        e1 = Label(window, text="Enter length in meters", bg="light gray")
        e1.grid(row=0, column=0, padx=10, pady=10)

        t.delete("1.0", END)
        t.insert(END, inch)


    elif x.lower() == "i":
        length_in_inches = float(e2_value.get())
        meters = length_in_inches * 0.0254
        e_inches = Label(window, text="Enter length in inches", bg="light gray")
        e_inches.grid(row=0, column=0, padx=10, pady=10)

        i = Label(window, text='meters', bg="light gray")
        i.grid(row=2, column=0, pady=10, padx=10)

        t.delete("1.0", END)
        t.insert(END, meters)


b = Button(window, text="Convert", command=conversion_to_inches)
b.grid(row=1, column=1, padx=10, pady=10)

def on_closing():
    if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
        window.destroy()


exit_button = Button(window, text="Exit", command=on_closing)
exit_button.place(x=450,y=255)

window.mainloop()


