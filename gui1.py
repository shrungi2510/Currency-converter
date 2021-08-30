import sys
import tkinter as tk
from tkinter import *
import urllib.request
from tkinter import Tk, StringVar, ttk

ids = {"US Dollar": 'USD', "Euros": 'EUR', "Indian Rupees": 'INR', "Swedish krona": 'SEK', "Swiss franc": 'CHF',
       "Arab Emirates Dirham": 'AED', "Pound Sterling": 'GBP', "Japanese Yen": 'JPY', "Yuan Renminbi": 'CNY'}


def convert(amt, frm, to):
    html = urllib.request.urlopen(
        "http://www.exchangerate-api.com/%s/%s/%f?k=a28d653d2d4fd2727003e437" % (frm, to, amt))
    return html.read().decode('utf-8')


def callback():
    try:
        amt = float(in_field.get())

    except ValueError:
        out_amt.set('Invalid input')
        return None
    if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
        out_amt.set('Input or output unit not chosen')
        return None
    else:
        frm = ids[in_unit.get()]
        to = ids[out_unit.get()]
        out_amt.set(convert(amt, frm, to))


root = Tk()
root.title("Currency Converter")

# initiate frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.pack(fill=BOTH, expand=1)
titleLabel = Label(mainframe, text="Currency Converter", font=("Arial", 12, "bold"), justify=CENTER).grid(column=1,
                                                                                                          row=1)
in_amt = StringVar()
in_amt.set('0')
out_amt = StringVar()

in_unit = StringVar()
out_unit = StringVar()
in_unit.set('Select Unit')
out_unit.set('Select Unit')

# Add input field
in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
in_field.grid(row=1, column=2, sticky=(W, E))

# Add drop-down for input unit
in_select = OptionMenu(mainframe, in_unit, "US Dollar", "Euros", "Indian Rupees", "Swedish krona", "Swiss franc",
                       "Arab Emirates Dirham", "Pound Sterling", "Japanese Yen", "Yuan Renminbi").grid(column=3, row=1,
                                                                                                       sticky=W)

# Add output field and drop-down
ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3, sticky=(W, E))
in_select = OptionMenu(mainframe, out_unit, "US Dollar", "Euros", "Indian Rupees", "Swedish krona", "Swiss franc",
                       "Arab Emirates Dirham", "Pound Sterling", "Japanese Yen", "Yuan Renminbi").grid(column=3, row=3,
                                                                                                       sticky=W)

calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2, sticky=E)

root.mainloop()