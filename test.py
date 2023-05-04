import tkinter as tk

def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')


def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')


root = tk.Tk()

entry_x = tk.Entry(root, width=50)
entry_x.pack(pady=10)
entry_x.insert(0, "Place Holder X")
entry_x.configure(state='disabled')

entry_y = tk.Entry(root, width=50)
entry_y.pack(pady=10)
entry_y.insert(0, "Place Holder Y")
entry_y.configure(state='disabled')

x_focus_in = entry_x.bind('<Button-1>', lambda x: on_focus_in(entry_x))
x_focus_out = entry_x.bind(
    '<FocusOut>', lambda x: on_focus_out(entry_x, 'Place Holder X'))

y_focus_in = entry_y.bind('<Button-1>', lambda x: on_focus_in(entry_y))
y_focus_out = entry_y.bind(
    '<FocusOut>', lambda x: on_focus_out(entry_y, 'Place Holder Y'))

root.mainloop()
