from tkinter import *

ws = Tk()
frame = Frame(ws)
Label(frame,text='Enter Word to Find:').pack(side=LEFT)
search_entry = Entry(frame)

search_entry.pack(side=LEFT, fill=BOTH, expand=1)

search_entry.focus_set()

search_button = Button(frame, text='Find')
search_button.pack(side=RIGHT)
frame.pack(side=TOP)

txt = Text(ws)

txt.insert('1.0','''Enter here...''')
txt.pack(side=BOTTOM)


def find():
	
	txt.tag_remove('found', '1.0', END)
	ser = search_entry.get()
	if ser:
		idx = '1.0'
		while 1:
			idx = txt.search(ser, idx, nocase=1,
							stopindex=END)
			if not idx: break
			lastidx = '%s+%dc' % (idx, len(ser))
			
			txt.tag_add('found', idx, lastidx)
			idx = lastidx
		txt.tag_config('found', foreground='blue')
	search_entry.focus_set()
search_button.config(command=find)

ws.mainloop()