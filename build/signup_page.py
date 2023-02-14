
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/jordanemccalla/Downloads/Software Engineering/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("829x654")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 654,
    width = 829,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    572.3466796875,
    140.26365661621094,
    image=image_image_1
)

canvas.create_rectangle(
    364.0,
    279.0,
    773.0,
    530.0,
    fill="#FFFFFF",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    146.0,
    327.0,
    image=image_image_2
)

canvas.create_text(
    521.0,
    279.0,
    anchor="nw",
    text="Sign Up",
    fill="#2578A9",
    font=("Kreon Bold", 30 * -1)
)

canvas.create_text(
    373.0,
    353.0,
    anchor="nw",
    text="Username",
    fill="#2578A9",
    font=("Kreon Bold", 20 * -1)
)

canvas.create_text(
    390.0,
    405.0,
    anchor="nw",
    text="First",
    fill="#2578A9",
    font=("Kreon Bold", 20 * -1)
)

canvas.create_text(
    391.0,
    457.0,
    anchor="nw",
    text="Last ",
    fill="#2578A9",
    font=("Kreon Bold", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    573.0,
    364.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=493.0,
    y=345.0,
    width=160.0,
    height=36.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    573.0,
    417.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=493.0,
    y=398.0,
    width=160.0,
    height=36.0
)

entrySign_25 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
)
entrySign_25.place(
    x=493.0,
    y=395.0,
    width=160.0,
    height=36.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    573.0,
    470.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=493.0,
    y=451.0,
    width=160.0,
    height=36.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=509.0,
    y=519.0,
    width=127.5384521484375,
    height=40.875
)
window.resizable(False, False)
window.mainloop()
