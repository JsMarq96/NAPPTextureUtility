from tkinter import Label, Entry, Button, Tk, filedialog, messagebox, END
from tkinter import Listbox, OptionMenu, StringVar, Toplevel, Variable
from PIL import Image, ImageTk
from os import path
import time
from Napp_Gen import generate_resourcepacks
from Splitter_GUI import splitter_GUI

'''
    GUI with tkinter for easier use without the command line
    by Juan S. Marquerie
'''

VERSION = '0.50'

HORRIBLE_BACKGROUND = True

COMP_OPTIONS = ['None', 'Light', 'Hard', 'Light w/Hard Speculars']
compr_result = 'None'
pack_res = 1024

def define_popup_GUI(tk_window):
    tk_window.geometry('350x197')

    # Labels
    label_txt1 = Label(tk_window, text='Destination pack resolution')
    label_txt1.grid(column=0, row=0)
    label_txt2 = Label(tk_window, text='Compression Levels')
    label_txt2.grid(column=2, row=0)

    # Option menu stuff
    comp_opt_var = StringVar(tk_window)
    comp_opt_var.set(COMP_OPTIONS[0])
    compress_menu = OptionMenu(tk_window, comp_opt_var, *COMP_OPTIONS)
    compress_menu.grid(column=2, row=1)

    # Text input
    txt_direction_input = Entry(tk_window, width=15)
    txt_direction_input.grid(column=0, row=1)

    def butt_press():
        global compr_result, pack_res
        compr_result = comp_opt_var.get()
        pack_res = int(txt_direction_input.get())

        tk_window.destroy()

    exit_button = Button(tk_window, text='Ok', command=butt_press)
    exit_button.grid(column=1, row=3)


def define_GUI(tk_window):
    # Window Config
    tk_window.title('TexturePack Resizer Utility v ' + VERSION)
    tk_window.geometry('750x420')

    if HORRIBLE_BACKGROUND:
        back_img = ImageTk.PhotoImage(Image.open('imgs/back_or.jpeg'))
        back = Label(tk_window, image=back_img)
        back.place(x=0, y=0, relwidth=1, relheight=1)
        back.image = back_img

    # Labels
    label_folder_origin = Label(tk_window, text='Enter the texture pack/origin folder')
    label_folder_origin.grid(column=0, row=0)
    label_resolution = Label(tk_window, text='Enter the resulting texture direction')
    label_resolution.grid(column=7, row=0)
    label_resolution = Label(tk_window, text='Enter the pack version')
    label_resolution.grid(column=0, row=3)

    # Text Input
    txt_direction_input = Entry(tk_window, width=25)
    txt_direction_input.grid(column=0, row=1)
    txt_result_direction_input = Entry(tk_window, width=25)
    txt_result_direction_input.grid(column=7, row=1)
    txt_version_input = Entry(tk_window, width=25)
    txt_version_input.grid(column=0, row=4)

    # List box
    pack_var = Variable()
    pack_list = Listbox(tk_window, listvariable=pack_var)
    pack_list.grid(column=9, row=2)

    # Button Events
    def add_pack_output():
        top = Toplevel(tk_window)
        define_popup_GUI(top)
        tk_window.wait_window(top)
        pack_list.insert(END, str(pack_res) + '-' + compr_result)

    def launch_splitter():
        top = Toplevel(tk_window)
        splitter_GUI(top)

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

        pack_list = pack_var.get()

        generate_resourcepacks(txt_direction_input.get(), pack_list, txt_result_direction_input.get(), txt_version_input.get())
        #resize_util.resize_directory(txt_direction_input.get(), txt_result_direction_input.get(), extensions)

        messagebox.showinfo('TexturePack Resizing Utility', 'Finished resizing!')
        button_resize.configure(state='normal', text='Resize')
        tk_window.update()

    def resize_n_zip():
        button_resize.configure(state='disabled', text='Resizing...')
        tk_window.update()

        pack_list = pack_var.get()

        generate_resourcepacks(txt_direction_input.get(), pack_list, txt_result_direction_input.get(), txt_version_input.get(),True)
        #resize_util.resize_directory(txt_direction_input.get(), txt_result_direction_input.get(), extensions)

        messagebox.showinfo('TexturePack Resizing Utility', 'Finished resizing!')
        button_resize.configure(state='normal', text='Resize')
        tk_window.update()

    # Buttons
    button_search = Button(tk_window, text='Search', command=launch_item_search)
    button_search.grid(column=1, row=1)
    button_search_2 = Button(tk_window, text='Search', command=launch_search_result_folder)
    button_search_2.grid(column=8, row=1)
    button_add_resize_pack = Button(tk_window, text='Add output pack', command=add_pack_output)
    button_add_resize_pack.grid(column=9, row=1)
    button_resize = Button(tk_window, text='Resize', command=resize)
    button_resize.grid(column=9, row=3)
    button_resize_zip = Button(tk_window, text='Resize & Zip', command=resize_n_zip)
    button_resize_zip.grid(column=9, row=4)
    button_launch_splitter = Button(tk_window, text='Texture Splitter Launcher', command=launch_splitter)
    button_launch_splitter.grid(column=9, row=5)

'''
    Launch the GUI
'''
if __name__ == '__main__':
    window = Tk()
    define_GUI(window)
    #define_popup_GUI(window)
    window.mainloop()
