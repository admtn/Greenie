from tkinter import *
from tkinter import ttk
import ctypes
import Estimate

def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')


def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')
        
# Function to perform the search
def perform_search(event=None):  # Modified to accept an event parameter
    # Clear the table
    taskMgr.delete(*taskMgr.get_children())
    loadingRowiid = 999
    taskMgr.insert(parent='', index='end', iid=loadingRowiid, text='',
               values=("Loading....", "", "", "", "", ""))
    

    # Get the search keyword from the entry widget
    keyword = search_entry.get().lower()

    # Call the estimatePower function with the search keyword
    taskMgr.after(10, lambda: Estimate.estimatePower(keyword, taskMgr))
    taskMgr.after(100, lambda: taskMgr.delete(loadingRowiid))


# Set DPI awareness
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Create the main window
ws = Tk()
ws.title('Greenie')
ws.geometry('800x800')


# Create the frame and pack it
frame = Frame(ws)
frame.pack(fill=BOTH, expand=True)

# Create the search entry widget
search_entry = Entry(frame, width=30)
search_entry.grid(row=0, column=0, padx=10, pady=10)

# Bind the <Return> event to perform_search()
search_entry.bind("<Return>", perform_search)

# Create the search button
search_button = Button(frame, text='Search', command=perform_search)
search_button.grid(row=0, column=1, padx=10, pady=10)

# Create the task manager table
taskMgr = ttk.Treeview(frame)
taskMgr['columns'] = ('process_id', 'process_name', 'cpu', 'memory', 'gpu', 'power')
w = 90
taskMgr.column("#0", width=0, stretch=NO)
taskMgr.column("process_id", anchor=CENTER, width=w)
taskMgr.column("process_name", anchor=CENTER, width=w)
taskMgr.column("cpu", anchor=CENTER, width=w)
taskMgr.column("memory", anchor=CENTER, width=w)
taskMgr.column("gpu", anchor=CENTER, width=w)
taskMgr.column("power", anchor=CENTER, width=w)

taskMgr.heading("#0", text="", anchor=CENTER)
taskMgr.heading("process_id", text="PID", anchor=CENTER)
taskMgr.heading("process_name", text="Process Name", anchor=CENTER)
taskMgr.heading("cpu", text="CPU %", anchor=CENTER)
taskMgr.heading("memory", text="Memory %", anchor=CENTER)
taskMgr.heading("gpu", text="GPU Usage %", anchor=CENTER)
taskMgr.heading("power", text="Power Consumption", anchor=CENTER)

# Call the estimatePower function to populate the table initially
Estimate.estimatePower("initialise_with_no_processes", taskMgr)

# Create a vertical scroll bar
scrollbar = Scrollbar(frame, orient=VERTICAL, command=taskMgr.yview)
scrollbar.grid(row=1, column=1, sticky='ns')

# Configure the Treeview widget to use the scrollbar
taskMgr.configure(yscrollcommand=scrollbar.set)

# Grid the task manager table and configure weights
taskMgr.grid(row=1, column=0, sticky='nsew')
frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Start the main event loop
ws.mainloop()
