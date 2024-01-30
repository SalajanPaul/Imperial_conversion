from tkinter import *

x = input("Do you want to convert meters to inches[m] or inches to meters[i]? ")


window = Tk()
window.title("Meters to inches converter")
window.geometry("500x300+550+355")
exit_button = Button(window, text="Exit", command=window.destroy)
exit_button.place(x=450,y=255)


def conversion_to_inches():
    if x.lower() == "m":
        e1 = Label(window, text="Enter length in meters", bg="light gray")
        e1.grid(row=0, column=0, padx=10, pady=10)

        e2_value = StringVar()
        e2 = Entry(window, textvariable=e2_value)
        e2.grid(row=0, column=1, pady=10, padx=10)

        # inch = float(e2_value.get()) * 39.37
        i = Label(window, text='inch', bg="light gray")
        i.grid(row=2, column=0, pady=10, padx=10)

        t = Text(window, height=1, width=15)
        t.grid(row=2, column=1, pady=10, padx=10)
        t.delete("1.0", END)
        # t.insert(END, inch)

    elif x.lower() == "i":
        e1 = Label(window, text="Enter length in inches", bg="light gray")
        e1.grid(row=0, column=0, padx=10, pady=10)

        e2_value = StringVar()
        e2 = Entry(window, textvariable=e2_value)
        e2.grid(row=0, column=1, pady=10, padx=10)

        # inch = float(e2_value.get()) * 39.37
        i = Label(window, text='inch', bg="light gray")
        i.grid(row=2, column=0, pady=10, padx=10)

        t = Text(window, height=1, width=15)
        t.grid(row=2, column=1, pady=10, padx=10)
        t.delete("1.0", END)
        # t.insert(END, inch)

    b = Button(window, text="Convert", command=conversion_to_inches)
    b.grid(row=1, column=1, padx=10, pady=10)



conversion_to_inches()

window.mainloop()






# def conversion():
#     x = input("Do you want meters to inches[m] or inches to meters[i] ? ")
#     x = x.lower()
#
#     if x == "m":
#         default = 39.3700787
#         calculate = int(input("How much meters do you want to convert ? ")) * default
#         print(calculate, "inches")
#     elif x == "i":
#         default2 = 0.0254
#         calculate2 = int(input()) * default2
#         print(calculate2, "meters")
#     else:
#         print("Please enter a valid letter!")
#
#
# conversion()

