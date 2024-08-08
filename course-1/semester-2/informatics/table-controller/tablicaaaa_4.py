import tkinter as tk
from tkinter import messagebox, filedialog, Scrollbar, ttk, Label, Frame, Entry, Button, END, NO, CENTER
import csv

def validate(new_value):
    return new_value == '' or new_value.isnumeric()


class TableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Программа для работы с таблицей")

        self.data = [[1,"Jack","gold"], [2,"Tom","Bronze"]]

        self.count=0

        self.table_frame = tk.Frame(root)
        self.table_frame.pack()



        self.scrollh = Scrollbar(self.table_frame)
        self.scrollh.pack(side='right', fill='y')

        self.scrollw = Scrollbar(self.table_frame,orient='horizontal')
        self.scrollw.pack(side='bottom',fill='x')

        self.table = ttk.Treeview(self.table_frame,yscrollcommand=self.scrollh.set, xscrollcommand=self.scrollw.set)
        self.table['columns']= ('id', 'full_Name','award')
        self.table.column("#0", width=0,  stretch=NO)
        self.table.column("id",anchor=CENTER, width=80)
        self.table.column("full_Name",anchor=CENTER, width=80)
        self.table.column("award",anchor=CENTER, width=80)

        self.table.heading("#0",text="",anchor=CENTER)
        self.table.heading("id",text="ID",anchor=CENTER)
        self.table.heading("full_Name",text="Full_Name",anchor=CENTER)
        self.table.heading("award",text="Award",anchor=CENTER)
        for record in self.data:

            self.table.insert(parent='',index='end',iid = self.count,text='',values=(record[0],record[1],record[2]))

            self.count += 1
        self.table.pack()

        self.scrollh.config(command=self.table.yview)
        self.scrollw.config(command=self.table.xview)

        '''
        add_row_button = tk.Button(root, text="Добавить строку", command=self.add_row)
        add_row_button.pack(side="top", padx=10, pady=5)

        add_column_button = tk.Button(root, text="Добавить столбец", command=self.add_column)
        add_column_button.pack(side="top", padx=10, pady=5)

        vcmd = (root.register(validate), '%P')

        remove_row_label = tk.Label(root, text="Удалить строку по номеру:")
        remove_row_label.pack(side="top", padx=10, pady=5)
        self.remove_row_entry = tk.Entry(root, width=10, validate='key', validatecommand=vcmd)
        self.remove_row_entry.pack(side="top", padx=10, pady=5)
        remove_row_button = tk.Button(root, text="Удалить строку", command=self.remove_row)
        remove_row_button.pack(side="top", padx=10, pady=5)


        remove_column_label = tk.Label(root, text="Удалить столбец по номеру:")
        remove_column_label.pack(side="top", padx=10, pady=5)
        self.remove_column_entry = tk.Entry(root, width=10, validate='key', validatecommand=vcmd)
        self.remove_column_entry.pack(side="top", padx=10, pady=5)
        remove_column_button = tk.Button(root, text="Удалить столбец", command=self.remove_column)
        remove_column_button.pack(side="top", padx=10, pady=5)


        sort_label = tk.Label(root, text="Сортировать таблицу по столбцу (номер):")
        sort_label.pack(side="top", padx=10, pady=5)
        self.sort_entry = tk.Entry(root, width=10, validate='key', validatecommand=vcmd)
        self.sort_entry.pack(side="top", padx=10, pady=5)
        sort_button = tk.Button(root, text="Сортировать", command=self.sort_table)
        sort_button.pack(side="top", padx=10, pady=5)

        load_button = tk.Button(root, text="Открыть файл", command=self.load_data)
        load_button.pack(side="top", padx=10, pady=5)

        save_button = tk.Button(root, text="Сохранить данные", command=self.save_data)
        save_button.pack(side="top", padx=10, pady=5)
        '''

        self.frame = Frame(root)
        self.frame.pack(pady=20)
        #labels
        self.playerid= Label(self.frame,text = "player_id")
        self.playerid.grid(row=0,column=0 )

        self.playername = Label(self.frame,text="player_name")
        self.playername.grid(row=0,column=1)

        self.playerrank = Label(self.frame,text="Player_rank")
        self.playerrank.grid(row=0,column=2)

        #Entry boxes
        self.playerid_entry= Entry(self.frame)
        self.playerid_entry.grid(row= 1, column=0)

        self.playername_entry = Entry(self.frame)
        self.playername_entry.grid(row=1,column=1)

        self.playerrank_entry = Entry(self.frame)
        self.playerrank_entry.grid(row=1,column=2)


        #Buttons
        self.select_button = Button(root,text="Select Record", command=self.select_record)
        self.select_button.pack(pady =10)

        self.refresh_button = Button(root,text="Refresh Record",command=self.update_record)
        self.refresh_button.pack(pady = 10)

        #button
        Input_button = Button(root,text = "Input Record",command=self.input_record)
        Input_button.pack()



        #Select Record
    def select_record(self):
        #clear entry boxes
        self.playerid_entry.delete(0,END)
        self.playername_entry.delete(0,END)
        self.playerrank_entry.delete(0,END)

        #grab record
        selected=self.table.focus()
        #grab record values
        values = self.table.item(selected,'values')
        #temp_label.config(text=selected)

        #output to entry boxes
        self.playerid_entry.insert(0,values[0])
        self.playername_entry.insert(0,values[1])
        self.playerrank_entry.insert(0,values[2])

    #save Record
    def update_record(self):
        selected=self.table.focus()
        #save new data
        self.table.item(selected,text="",values=(self.playerid_entry.get(),self.playername_entry.get(),self.playerrank_entry.get()))

        #clear entry boxes
        self.playerid_entry.delete(0,END)
        self.playername_entry.delete(0,END)
        self.playerrank_entry.delete(0,END)



    def input_record(self):

        self.table.insert(parent='',index='end',iid = self.count,text='',values=(self.playerid_entry.get(),self.playername_entry.get(),self.playerrank_entry.get()))
        self.count += 1


        #clear entry boxes
        self.playerid_entry.delete(0,END)
        self.playername_entry.delete(0,END)
        self.playerrank_entry.delete(0,END)








    def add_row(self):

        row_index = len(self.data)
        row = []
        for j in range(len(self.data[0])):
            entry = tk.Entry(self.table_frame, width=15)
            entry.grid(row=row_index, column=j, padx=5, pady=5)
            row.append(entry)
        self.data.append(row)
        self.update_table()

    def add_column(self):

        column_index = len(self.data[0])
        for i in range(len(self.data)):
            entry = tk.Entry(self.table_frame, width=15)
            entry.grid(row=i, column=column_index, padx=5, pady=5)
            self.data[i].append(entry)
        self.update_table()

    def remove_row(self):

        row_number = int(self.remove_row_entry.get())
        if (1 <= row_number) and (row_number <= len(self.data)):
            for entry in self.data[row_number - 1]:
                entry.grid_forget()
            self.data.pop(row_number - 1)
            self.update_table()
        else:
            messagebox.showerror("Ошибка", "Неверный номер строки")

    def remove_column(self):

        column_number = int(self.remove_column_entry.get())
        if (1 <= column_number) and (column_number <= len(self.data[0])):
            for i in range(len(self.data)):
                self.data[i][column_number - 1].grid_forget()
                self.data[i].pop(column_number - 1)
            self.update_table()
        else:
            messagebox.showerror("Ошибка", "Неверный номер столбца")

    def sort_table(self):

        column_number = int(self.sort_entry.get())
        if 1 <= column_number <= len(self.data[0]):
            temp_data = self.data[1:]
            temp_data.sort(key=lambda row: row[column_number - 1].get())
            temp_data.insert(0, self.data[0])
            self.data = temp_data
            self.update_table()
        else:
            messagebox.showerror("Ошибка", "Неверный номер столбца")

    def update_table(self):

        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self.data[i][j].grid(row=i, column=j, padx=5, pady=5)

    def save_data(self):

        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                for row in self.data:
                    row_data = [entry.get() for entry in row]
                    writer.writerow(row_data)
            messagebox.showinfo("Сохранение", "Данные успешно сохранены")

    def load_data(self):
        while (len(self.data) > 0):
            i = len(self.data) - 1
            for entry in self.data[i]:
                entry.grid_forget()
            self.data.pop(i)
            self.update_table()


        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if file_path:
            with open(file_path, newline="") as file:
                reader = csv.reader(file)
                self.data = []
                for row in reader:
                    row_entries = []
                    for value in row:
                        entry = tk.Entry(self.table_frame, width=15)
                        entry.insert(0, value)
                        row_entries.append(entry)
                    self.data.append(row_entries)
                self.update_table()
            messagebox.showinfo("Загрузка", "Данные успешно загружены")


root = tk.Tk()
app = TableApp(root)
root.mainloop()
