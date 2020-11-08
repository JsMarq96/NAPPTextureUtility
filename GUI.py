from tkinter import Label, Entry, Button, Tk, filedialog, messagebox, END
from PIL import Image, ImageTk
from TexPackResize import TexPackResize
from os import path
import time

'''
    GUI with tkinter for easier use without the command line
    by Juan S. Marquerie
'''

VERSION = '0.65'

'''
    This requeires a bit of an explanation... While I was doing
    my first Android App project, I added as a background a really no good,
    ugly green to orange gradient; and del_cieno critisized and mocked
    endlessly this choice...
    In hindshight, this was for the better, but I can still have some fun
    with this...
'''
HORRIBLE_BACKGROUND = True

def define_GUI(tk_window, resize_util):
    # Window Config
    tk_window.title('TexturePack Resizing Utility v ' + VERSION)
    tk_window.geometry('650x100')

    if HORRIBLE_BACKGROUND:
        back_img = ImageTk.PhotoImage(Image.open('imgs/background.jpg'))
        back = Label(tk_window, image=back_img)
        back.place(x=0, y=0, relwidth=1, relheight=1)
        back.image = back_img

    # Labels
    label_folder_origin = Label(tk_window, text='Enter the texture pack/origin folder')
    label_folder_origin.grid(column=0, row=0)
    label_resolution = Label(tk_window, text='Resolution')
    label_resolution.grid(column=3, row=0)
    label_resolution = Label(tk_window, text='Enter the resulting texture direction')
    label_resolution.grid(column=7, row=0)
    label_x = Label(tk_window, text='x ')
    label_x.grid(column=4, row=1)
    label_file_extensions = Label(tk_window, text='File extensions:')
    label_file_extensions.grid(column=1, row=2)

    # Text Input
    txt_direction_input = Entry(tk_window, width=25)
    txt_direction_input.grid(column=0, row=1)
    txt_width_input = Entry(tk_window, width=4)
    txt_width_input.grid(column=3, row=1)
    txt_width_input.insert(0,'512')
    txt_height_input = Entry(tk_window, width=4)
    txt_height_input.grid(column=5, row=1)
    txt_height_input.insert(0,'512')
    txt_result_direction_input = Entry(tk_window, width=25)
    txt_result_direction_input.grid(column=7, row=1)
    txt_file_extensions = Entry(tk_window, width=10)
    txt_file_extensions.grid(column=3, row=2)
    txt_file_extensions.insert(0,'.png')

    # Button Events
    def launch_item_search():
        selected_folder = filedialog.askdirectory()
        txt_direction_input.delete(0, END)
        txt_direction_input.insert(0,selected_folder)

    def launch_search_result_folder():
        selected_folder = filedialog.askdirectory()
        txt_result_direction_input.delete(0, END)
        txt_result_direction_input.insert(0,selected_folder)

    def resize():
        button_resize.configure(state='disabled', text='Resizing...')
        tk_window.update()

        extensions = txt_file_extensions.get()
        extensions = tuple(extensions.split(','))

        resize_util.scale = (int(txt_width_input.get()), int(txt_height_input.get()))
        resize_util.resize_directory(txt_direction_input.get(), txt_result_direction_input.get(), extensions)
        messagebox.showinfo('TexturePack Resizing Utility', 'Finished resizing!')
        button_resize.configure(state='normal', text='Resize')
        tk_window.update()


    # Buttons
    button_search = Button(tk_window, text='Search', command=launch_item_search)
    button_search.grid(column=1, row=1)
    button_search_2 = Button(tk_window, text='Search', command=launch_search_result_folder)
    button_search_2.grid(column=8, row=1)
    button_resize = Button(tk_window, text='Resize', command=resize)
    button_resize.grid(column=5, row=6)


'''
    Launch the GUI
'''
if __name__ == '__main__':
    window = Tk()
    define_GUI(window, TexPackResize((512, 512)))
    window.mainloop()