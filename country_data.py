import tkinter as tk, requests

def c_data(c):
    c = c.strip()
    print()
    if c == '':
        return
    try:
        country = [i for i in countries if i['name'].lower() == c.lower() or i['code_iso2'].lower() == c.lower()][0]
        data = {
            'd1': {'data': country['name'], 'entry': tk.Entry(root), 'label': tk.Label(root, text="Country Name:")},
            'd2': {'data': country['code_iso2'], 'entry': tk.Entry(root), 'label': tk.Label(root, text="Code ISO2:")},
            'd3': {'data': country['coordinates'], 'entry': tk.Entry(root), 'label': tk.Label(root, text="Coordinates:")},
            'd4': {'data': country['capital'], 'entry': tk.Entry(root), 'label': tk.Label(root, text="Capital:")},
            'd5': {'data': ', '.join(country['languages']), 'entry': tk.Entry(root), 'label': tk.Label(root, text="Languages:")},
            'd6': {'data': country['continent_name'], 'entry': tk.Entry(root), 'label': tk.Label(root, text="Continent:")},
			'd7': {'data': country['phone_code'], 'entry': tk.Entry(root), 'label': tk.Label(root, text="Phone Code:")}
        }
        tup_dicts = enumerate(sorted(data.items()), 3)
        for k, tup in tup_dicts:
            d_num, data_dict = tup
            print(d_num, data_dict)
            data_dict['label'].configure(font=("Tahoma",10))
            data_dict['entry'].insert(0, data_dict['data'])
            data_dict['entry'].configure(state='readonly', width=100, font=("Tahoma",10, 'bold'))
            data_dict['label'].grid(row=k, sticky='w', padx=(20, 0), pady=(0, 10))
            data_dict['entry'].grid(row=k, column=1, sticky='w', padx=(5, 20), pady=(0, 10))
        labelTxt = 'country found'
        fg = 'green'
    except Exception as exc:
        labelTxt = 'invalid country: {}'.format(c)
        fg = 'red'
    lbl.config(text=labelTxt, fg=fg)

countries = requests.get('https://github.com/Miguel-Frazao/world-data/blob/master/countries.json?raw=true').json()

root = tk.Tk()
root.wm_title("Country API info")
inputCountry = tk.Entry(root)
button = tk.Button(root, text="Get country data", relief="groove", command=lambda: c_data(inputCountry.get()))
root.bind("<Return>", lambda event: c_data(inputCountry.get()))
lbl = tk.Label(root, text="Insert country/code iso2 in english. EX: 'pt'", justify="left", anchor='s', pady=20, padx=20, font=("Tahoma",10, 'bold'))
inputCountry.grid(row=0, columnspan=2, pady=(20, 0))
button.grid(row=1, columnspan=2, pady=(10, 0))
lbl.grid(row=2, columnspan=2)

root.mainloop()
