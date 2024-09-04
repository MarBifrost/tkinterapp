import tkinter as tk
from tkinter import ttk
import requests

def get_rate(from_currency, to_currency):
    my_api_key = "8b004f30b0bd91bc04c0995b"
    url = f"https://v6.exchangerate-api.com/v6/{my_api_key}/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    rate = data['conversion_rates'][to_currency]
    return rate

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combo.get()
        to_currency = to_currency_combo.get()
        rate = get_rate(from_currency, to_currency)
        result = amount * rate
        result_label.config(text=f'{amount} {from_currency} არის {result:.2f} {to_currency}')
    except:
        result_label.config(text=f'თანხის ველი ცარიელია!')




def entry_placeholder_del(event):
    if amount_entry.get() == "შეიყვანეთ თანხა...":
        amount_entry.delete(0, tk.END)
        # amount_entry.config(bg="red")


def entry_placeholder(event):
    if amount_entry.get() == "":
        amount_entry.insert(0, "შეიყვანეთ თანხა...")
        # amount_entry.config(bg="purple")



def refresh_button():
    amount_entry.delete(0, tk.END)
    from_currency_combo.delete(0, tk.END)
    to_currency_combo.delete(0, tk.END)
    from_currency_combo.current(3)
    to_currency_combo.current(0)
    result_label.config(text="")





root = tk.Tk()
root.title("ვალუტის კონვერტორი")
root.geometry("335x400+0+0")
root.resizable(False, False)
root.configure(bg="#7FA1C3")

tk.Label(root, text="შეიყვანეთ თანხა, \nაირჩიეთ სასურველი ვალუტა ჩამოსაშლელ მენიუში\nდა დააკლიკეთ კონვერტაციის ღილაკს", bg='#7FA1C3', fg='#201E43').grid()
amount_entry = tk.Entry(root, width=25)
amount_entry.insert(0, "შეიყვანეთ თანხა...")
amount_entry.grid(row=1, column=0,  padx=20, pady=20)
amount_entry.bind("<FocusIn>", entry_placeholder_del)
amount_entry.bind("<FocusOut>", entry_placeholder)


tk.Label(root).grid(row=2, column=0, padx=10, pady=10)
from_currency_combo = ttk.Combobox(root, values=["USD", "EUR", "GBP", "GEL"])
from_currency_combo.grid(row=2, column=0, padx=10, pady=10)
from_currency_combo.current(3)



tk.Label(root).grid(row=3, column=0, padx=10, pady=10)
to_currency_combo = ttk.Combobox(root, values=["USD", "EUR", "GBP", "GEL"])
to_currency_combo.grid(row=3, column=0, padx=10, pady=10)
to_currency_combo.current(0)



convert_button = tk.Button(root, text="კონვერტაცია", command=convert_currency)
convert_button.grid(row=5, column=0, columnspan=2, pady=15)

result_label = tk.Label(root, text="", bg='#7FA1C3')
result_label.grid(row=4, column=0, pady=20)

refresh_button= tk.Button(root, text="გასუფთავება", command=refresh_button, width=15).grid(row=6, column=0, pady=5, padx=5)
root.mainloop()
