number = 0
def main():

    import tkinter as tk
    from tkinter import messagebox
    from tkinter.simpledialog import askstring

    number = 0

    class counter:
        def __init__(self):
            # self.master = master
            self.root = tk.Tk()
            self.root.geometry("250x215")
            self.root.title("GUI Counter")
            self.text = tk.StringVar()

            self.text.set(f"Value: {number}")
            self.label = tk.Label(self.root, textvariable=self.text, height=2, width=25)

            self.button1 = tk.Button(self.root,
                                     text="Add 1",
                                     command=self.add, height=3, width=20)

            self.button2 = tk.Button(self.root, text="Subtract 1", command=self.sub, width=20, height=3)

            self.button3 = tk.Button(self.root, text="Set Value", command=self.set, width=20)

            self.button4 = tk.Button(self.root, text="Save", command=self.write_save, width=20)

            self.label_null = tk.Label(self.root, text="")

            self.label.pack()
            self.button1.pack()
            self.button2.pack()
            self.button3.pack()
            self.button4.pack()
            # self.bindings()
            self.root.mainloop()

        def add(self):
            global number
            number = int(number)
            number += 1
            self.text.set(f"Value: {number}")

        def sub(self):
            global number
            number = int(number)
            number -= 1
            self.text.set(f"Value: {number}")

        def write_save(self):
            global number
            number = str(number)
            write = open('apps/tkcounter/save.txt', 'a')
            reset_count = [f'\n{number}']
            write.writelines(reset_count)
            write.close()

            messagebox.showinfo("Save Successful", "Your counter value was saved in \"save.txt\"."
                                                   "\nIt may take a few seconds to display.")

        def set(self):
            global number
            new_entry = ""

            while new_entry == "":
                inp = askstring("Set Value", "Enter set value below.\n"
                                             "If you clicked this by mistake, just enter the current counter value.")
                try:
                    new_entry = int(inp)

                except Exception:
                    new_entry = ""

            number = new_entry
            self.text.set(f"Value: {number}")

        # def bindings(self):
        # self.master.bind('a', lambda event: self.add())

        # self.master.bind('s', lambda event: self.sub())

        # self.master.bind('z', lambda event: self.set())

        # self.master.bind('x', lambda event: self.write_save())

    app = counter()

