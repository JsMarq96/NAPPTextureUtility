from tkinter import Label, Entry, Button, Tk, filedialog, messagebox, END
from PIL import Image, ImageTk
from Text_Split import split_text
from os import path
import os
import time

'''
    GUI with tkinter for easier use without the command line
    by Juan S. Marquerie
'''

VERSION = '0.65'


HORRIBLE_BACKGROUND = True

def splitter_GUI(tk_window):
    # Window Config
    tk_window.title('Texture Splitting Utility v ' + VERSION)

    if HORRIBLE_BACKGROUND:
        tk_window.geometry('1047x785')
        back_img = ImageTk.PhotoImage(Image.open('imgs/back.jpg'))
        back = Label(tk_window, image=back_img)
        back.place(x=0, y=0, relwidth=1, relheight=1)
        back.image = back_img
    else:
        tk_window.geometry('820x100')

    # Labels
    label_folder_origin = Label(tk_window, text='Enter the texture origin folder with all the maps')
    label_folder_origin.grid(column=0, row=0)
    label_resolution = Label(tk_window, text='Texture name')
    label_resolution.grid(column=3, row=0)
    label_name = Label(tk_window, text='Number of splits')
    label_name.grid(column=5, row=0)
    label_1resolution = Label(tk_window, text='Result texture location')
    label_1resolution.grid(column=6, row=0)

    # Text Input
    txt_direction_input = Entry(tk_window, width=25)
    txt_direction_input.grid(column=0, row=1)
    txt_name_input = Entry(tk_window, width=10)
    txt_name_input.grid(column=3, row=1)
    txt_name_input.insert(0,'stone')
    txt_split_input = Entry(tk_window, width=4)
    txt_split_input.grid(column=5, row=1)
    txt_split_input.insert(0,'4')
    txt_result_input = Entry(tk_window, width=30)
    txt_result_input.grid(column=6, row=1)
    txt_result_input.insert(0,'')

    # Button Events
    def launch_item_search():
        selected_folder = filedialog.askdirectory()
        txt_direction_input.delete(0, END)
        txt_direction_input.insert(0,selected_folder)
    
    def launch_item_search2():
        selected_folder = filedialog.askdirectory()
        txt_result_input.delete(0, END)
        txt_result_input.insert(0,selected_folder)

    def split():
        button_split_1.configure(state='disabled', text='Splitting....')
        tk_window.update()
        seperator = '/'
        if os.name == 'nt':
            seperator = '\\'
        split_text(txt_direction_input.get() + seperator + txt_name_input.get(), int(txt_split_input.get()), txt_result_input.get() + seperator)
        messagebox.showinfo('Texture Splitting Utility', 'Finished splitting!')

        button_split_1.configure(state='normal', text='Split')
        tk_window.update()

    # Buttons
    button_search_1 = Button(tk_window, text='Search', command=launch_item_search)
    button_search_1.grid(column=1, row=1)
    button_search_1 = Button(tk_window, text='Search', command=launch_item_search2)
    button_search_1.grid(column=7, row=1)
    button_split_1 = Button(tk_window, text='Split', command=split)
    button_split_1.grid(column=5, row=2)


'''
    Launch the GUI
'''
if __name__ == '__main__':
    window = Tk()
    splitter_GUI(window)
    window.mainloop()
