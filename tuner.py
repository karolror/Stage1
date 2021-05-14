import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from intelhex import IntelHex
import pymongo
from database import Database


class Tuner(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        '#Background'
        self.bg = tk.PhotoImage(file="img/board.png")
        self.label1 = tk.Label(image=self.bg)
        self.label1.place(x=0, y=0, relheight=1, relwidth=1)
        '#Listboxes'
        self.listbox1 = tk.Listbox()
        self.listbox1.place(x=25, y=30)
        self.listbox1.insert('end', "Ford")
        self.listbox1.insert('end', "Renault")
        self.listbox2 = tk.Listbox(width=100)
        self.listbox2.place(x=170, y=30)
        self.scrollbar = tk.Scrollbar()
        self.scrollbar.place(x=775, y=30)
        self.listbox2.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox2.yview)
        '#Buttons'
        self.search_button = tk.Button(text="Search Models", command=lambda: self.get_model(self.get_value_listbox1()))
        self.search_button.place(x=26, y=220)
        self.generate_button = tk.Button(text="Click to generate Stage1!", height="2", width="105",
                                         activebackground="#72A56A", activeforeground="#ff3333", command=self.generate)
        self.generate_button.place(x=30, y=450)
        self.load_button = tk.Button(text="Load File", command=self.openfile)
        self.load_button.place(x=713, y=220)
        self.select_button = tk.Button(text="Select model:", command=lambda: self.select_model(self.get_value_listbox2()))
        self.select_button.place(x=500, y=220)
        '#Textboxes'
        self.textbox = tk.Text(height=1, width=10)
        self.textbox.place(x=600, y=223)
        '#DB'
        self.client = pymongo.MongoClient(
            "mongodb+srv://db_user1:useruser123@cluster0.qqmqr.mongodb.net/sample_training?retryWrites=true&w=majority")
        self.loaded_dir = None
        self.loaded_id = None
        self.injection = None
        self.turbo = None
        self.rail = None
        self.ih = IntelHex()
        self.data = Database(self.client)

    def get_value_listbox1(self):
        keykey = self.listbox1.get(tk.ACTIVE)
        return keykey

    def get_value_listbox2(self):
        keykey2 = self.listbox2.get(tk.ACTIVE)
        return keykey2

    def get_model(self, brand):
        self.listbox2.delete(0, tk.END)
        db = self.client["drivers"]
        collection = db["sizes"]
        desc = collection.find({"brand": brand})
        goto = []
        for i in desc:
            for x in i:
                ins_text = str(x) + " : " + str(i[x]) + " | "
                goto.append(ins_text)
            concentrate = " ".join(goto)
            self.listbox2.insert(tk.END, concentrate)
            del goto[:]

    def openfile(self):
        self.loaded_dir = filedialog.askopenfilename()
        print(self.loaded_dir)

    def select_model(self, key_listbox):
        try:
            self.textbox.delete("1.0", tk.END)
            pull_num = [int(s) for s in key_listbox.split() if s.isdigit()]
            self.loaded_id = pull_num[0]
            self.textbox.insert(tk.END, str(self.loaded_id))
        except IndexError:
            self.textbox.delete("1.0", tk.END)
            self.textbox.insert(tk.END, "Error")

    def generate(self):
        if self.loaded_id:
            print("id loaded")
            if self.loaded_dir:
                self.pattern()
            else:
                tk.messagebox.showerror(title="Error", message="Load ECU file!")
        else:
            tk.messagebox.showerror(title="Error", message="Select car model!")

    def pattern(self):
        self.ih_import_file()
        self.injection = self.data.get_injection(self.loaded_id)
        self.turbo = self.data.get_turbo(self.loaded_id)
        self.rail = self.data.get_rail(self.loaded_id)
        if self.injection:
            x_inj, y_inj = self.data.get_injection_pos(self.loaded_id)
            print("Inj tuning...")
            self.ih = self.tuning(self.injection, x_inj, y_inj)
        else:
            pass
        if self.turbo:
            x_trb, y_trb = self.data.get_turbo_pos(self.loaded_id)
            print("Turbo tuning...")
            self.ih = self.tuning(self.turbo, x_trb, y_trb)
        else:
            pass
        if self.rail:
            x_ril, y_ril = self.data.get_rail_pos(self.loaded_id)
            print("Rail tuning...")
            self.ih = self.tuning(self.rail, x_ril, y_ril)
        else:
            pass
        self.ih.tofile("mod.bin", format="bin")

    def ih_import_file(self):
        self.ih.loadbin(self.loaded_dir)

    def tuning(self, tune_hex, a, b, element="0x"):
        driver_to_list = tune_hex.split()
        count = 0
        for i in range(a, b+1):
            changer = element + driver_to_list[count]
            self.ih[i] = int(changer, base=16)
            count += 1
        return self.ih
