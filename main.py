
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
text = ''


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def type_number(n):
    global text
    text = text + n
    canvas.itemconfig(input_text, text=text)


def type_clear():
    global text
    text = ''
    canvas.itemconfig(history_text, text='')
    canvas.itemconfig(input_text, text=text)


def type_back():
    global text
    text = text[:-1]
    canvas.itemconfig(input_text, text=text)


def type_percent():
    global text
    text = text + "/100"
    calc()


def calc():
    global text
    canvas.itemconfig(history_text, text=text)
    text = text.replace("×", "*")
    text = text.replace("^", "**")
    try:
        re = eval(text)
    except ZeroDivisionError:
        canvas.itemconfig(input_text, text="ZeroDivErr")
    else:
        if isinstance(re, float):
            re = round(float(re), 6)
        if len(str(re)) > 8:
            re = format(re, ".1E")
        canvas.itemconfig(input_text, text=re)
        text = str(re)


window = Tk()
window.geometry("360x640")
window.configure(bg="#FCFFE7")
window.title("Calculator")

canvas = Canvas(
    window,
    bg="#FCFFE7",
    height=640,
    width=360,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

history_text = canvas.create_text(
    16.0,
    32.0,
    anchor="nw",
    text="",
    fill="#675858",
    font=("FontAwesome5Free Regular", 36 * -1)
)

input_text = canvas.create_text(
    19.0,
    111.0,
    anchor="nw",
    text=text,
    fill="#000000",
    font=("Inter", 64 * -1)
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: type_number('7'),
    relief="flat"
)
button_1.place(
    x=110.0,
    y=320.0,
    width=55.0,
    height=60.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: type_number('8'),
    relief="flat"
)
button_2.place(
    x=199.0,
    y=320.0,
    width=55.0,
    height=60.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: type_number('9'),
    relief="flat"
)
button_3.place(
    x=288.0,
    y=320.0,
    width=55.0,
    height=60.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: type_number('×'),
    relief="flat"
)
button_4.place(
    x=16.0,
    y=320.0,
    width=60.0,
    height=60.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=type_percent,
    relief="flat"
)
button_5.place(
    x=110.0,
    y=241.0,
    width=55.0,
    height=60.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=type_clear,
    relief="flat"
)
button_6.place(
    x=288.0,
    y=241.0,
    width=55.0,
    height=60.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: type_number('/'),
    relief="flat"
)
button_7.place(
    x=16.0,
    y=241.0,
    width=60.0,
    height=60.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: type_number('4'),
    relief="flat"
)
button_8.place(
    x=110.0,
    y=399.0,
    width=55.0,
    height=60.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: type_number('5'),
    relief="flat"
)
button_9.place(
    x=199.0,
    y=399.0,
    width=55.0,
    height=60.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: type_number('6'),
    relief="flat"
)
button_10.place(
    x=288.0,
    y=399.0,
    width=55.0,
    height=60.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: type_number('+'),
    relief="flat"
)
button_11.place(
    x=16.0,
    y=399.0,
    width=60.0,
    height=60.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: type_number('1'),
    relief="flat"
)
button_12.place(
    x=110.0,
    y=478.0,
    width=55.0,
    height=60.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: type_number('2'),
    relief="flat"
)
button_13.place(
    x=199.0,
    y=478.0,
    width=55.0,
    height=60.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: type_number('3'),
    relief="flat"
)
button_14.place(
    x=288.0,
    y=478.0,
    width=55.0,
    height=60.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: type_number("-"),
    relief="flat"
)
button_15.place(
    x=16.0,
    y=478.0,
    width=60.0,
    height=60.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: type_number('^'),
    relief="flat"
)
button_16.place(
    x=110.0,
    y=557.0,
    width=55.0,
    height=60.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: type_number('0'),
    relief="flat"
)
button_17.place(
    x=199.0,
    y=557.0,
    width=55.0,
    height=60.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: type_number("."),
    relief="flat"
)
button_18.place(
    x=288.0,
    y=557.0,
    width=55.0,
    height=60.0
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=calc,
    relief="flat"
)
button_19.place(
    x=16.0,
    y=557.0,
    width=60.0,
    height=60.0
)

canvas.create_rectangle(
    19.0,
    222.0,
    340.0,
    222.0,
    fill="#000000",
    outline="")

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=type_back,
    relief="flat"
)
button_20.place(
    x=199.0,
    y=241.0,
    width=55.0,
    height=60.0
)


window.resizable(False, False)
window.mainloop()
