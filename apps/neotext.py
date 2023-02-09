def main():

    import tkinter as tk
    from tkinter.filedialog import askopenfilename, asksaveasfilename
    from tkinter import messagebox

    def open_file():
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("All Files", "*.*"),("Text Files","*.txt*"),("Python Files","*.py*")]
        )
        if not filepath:
            return
        txt_edit.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window.title(f"NeoText - {filepath}")

    def save_file():
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"),("Text Files","*.txt*"),("Python Files","*.py*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
        window.title(f"NeoText - {filepath}")

    window = tk.Tk()
    window.title("NeoText")
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)

    def showinfo():
      tk.messagebox.showinfo(title="Info", message="NeoText is a simple, easy, text editor developed by NeoCryptix.\n\nThis version was edited by WaterHydraMC.")

    txt_edit = tk.Text(window)
    fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
    btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
    btn_info = tk.Button(fr_buttons, text="Info", command=showinfo)
    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
    btn_info.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

    window.mainloop()

