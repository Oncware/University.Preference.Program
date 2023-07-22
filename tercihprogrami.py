import tkinter as tk
from tkinter import ttk, messagebox
import json
from tkcalendar import DateEntry
from tkinter import simpledialog

class UniversityApp:
    def __init__(self, master):
        self.master = master
        self.master.title("University Application")
        self.notebook = ttk.Notebook(master)
        self.notebook.pack()

        self.page1 = ttk.Frame(self.notebook)
        self.page2 = ttk.Frame(self.notebook)
        self.page3 = ttk.Frame(self.notebook)

        self.notebook.add(self.page1, text='Okullar')
        self.notebook.add(self.page2, text='İstek Listesi')
        self.notebook.add(self.page3, text='Tanıtım Günleri')

        self.load()

        self.create_widgets()

    def create_widgets(self):
        # Page 1: Okullar
        self.university_label = tk.Label(self.page1, text="Üniversite")
        self.university_label.grid(row=0, column=0)
        self.university_input = tk.Entry(self.page1)
        self.university_input.grid(row=0, column=1)
        self.score_label = tk.Label(self.page1, text="Eski Sıralama")
        self.score_label.grid(row=4, column=0)
        self.score_input = tk.Entry(self.page1)
        self.score_input.grid(row=4, column=1)
        self.city_label = tk.Label(self.page1, text="Şehir")
        self.city_label.grid(row=1, column=0)
        self.city_input = tk.Entry(self.page1)
        self.city_input.grid(row=1, column=1)



        self.department_label = tk.Label(self.page1, text="Bölüm")
        self.department_label.grid(row=2, column=0)
        self.department_input = tk.Entry(self.page1)
        self.department_input.grid(row=2, column=1)
        
        self.ranking_label = tk.Label(self.page1, text="Sıralama")
        self.ranking_label.grid(row=3, column=0)
        self.ranking_input = tk.Entry(self.page1)
        self.ranking_input.grid(row=3, column=1)

        self.note_label = tk.Label(self.page1, text="Not")
        self.note_label.grid(row=5, column=0)
        self.note_input = tk.Entry(self.page1)
        self.note_input.grid(row=5, column=1)

        self.add_button = tk.Button(self.page1, text="Okul Ekle", command=self.add_to_list)
        self.add_button.grid(row=6, column=1)

        self.delete_button = tk.Button(self.page1, text="Seçili Okulu Sil", command=self.delete)
        self.delete_button.grid(row=7, column=1)

        columns = ('#1', '#2', '#3', '#4', '#5', '#6')  # Add a new column
        self.school_list = ttk.Treeview(self.page1, columns=columns, show='headings')
        self.school_list.heading('#1', text='Üniversite')
        self.school_list.heading('#2', text='Şehir')
        self.school_list.heading('#3', text='Bölüm')
        self.school_list.heading('#4', text='Sıralama')
        self.school_list.heading('#5', text='Eski Sıralama')  # New column header
        self.school_list.heading('#6', text='Not')
        self.school_list.grid(row=8, column=0, columnspan=2)

        # Page 2: İstek Listesi
        self.add_wishlist_button = tk.Button(self.page1, text="İstek Listesine Ekle", command=self.add_to_wishlist)
        self.add_wishlist_button.grid(row=5, column=2)

        self.delete_wishlist_button = tk.Button(self.page2, text="Seçili İstek Listesi Öğesini Sil", command=self.delete_wishlist)
        self.delete_wishlist_button.pack()

        columns = ('#1', '#2', '#3', '#4', '#5', '#6')  # Add a new column
        self.wishlist_treeview = ttk.Treeview(self.page2, columns=columns, show='headings')
        self.wishlist_treeview.heading('#1', text='Üniversite')
        self.wishlist_treeview.heading('#2', text='Şehir')
        self.wishlist_treeview.heading('#3', text='Bölüm')
        self.wishlist_treeview.heading('#4', text='Sıralama')
        self.wishlist_treeview.heading('#5', text='Eski Sıralama')  # New column header
        self.wishlist_treeview.heading('#6', text='Not')
        self.wishlist_treeview.pack()
        self.city_label_page3 = tk.Label(self.page3, text="Şehir")
        self.city_label_page3.pack()
        self.city_input_page3 = tk.Entry(self.page3)
        self.city_input_page3.pack()
        self.school_list.bind("<Double-1>", self.on_double_click)

        self.university_label_page3 = tk.Label(self.page3, text="Üniversite")
        self.university_label_page3.pack()
        self.university_input_page3 = tk.Entry(self.page3)
        self.university_input_page3.pack()

        self.date_label_page3 = tk.Label(self.page3, text="Tarih")
        self.date_label_page3.pack()
        self.date_input_page3 = tk.Entry(self.page3)
        self.date_input_page3.pack()

        self.note_label_page3 = tk.Label(self.page3, text="Not")
        self.note_label_page3.pack()
        self.note_input_page3 = tk.Entry(self.page3)
        self.note_input_page3.pack()

        self.add_button_page3 = tk.Button(self.page3, text="Tanıtım Günü Ekle", command=self.add_to_presentation_days)
        self.add_button_page3.pack()

        columns = ('#1', '#2', '#3', '#4')
        self.presentation_days_list = ttk.Treeview(self.page3, columns=columns, show='headings')
        self.presentation_days_list.heading('#1', text='Şehir')
        self.presentation_days_list.heading('#2', text='Üniversite')
        self.presentation_days_list.heading('#3', text='Tarih')
        self.presentation_days_list.heading('#4', text='Not')
        self.presentation_days_list.pack()
        self.school_list.bind("<Double-1>", self.edit_score)
        self.load_listbox()
    def edit_score(self, event):
        selected_item = self.school_list.focus()
        item = self.school_list.item(selected_item)
        values = item['values']

        new_score = simpledialog.askstring("Input", "Yeni eski sıralama girin:",parent=self.master)

        # Input validation can be added here.

        for data_item in self.data:
            if (data_item['university'] == values[0] and
                data_item['city'] == values[1] and
                data_item['department'] == values[2]):
                data_item['score'] = new_score

        self.save_data()
        self.load_listbox()

    # Now bind this function to Treeview double click event.
        

    def add_to_list(self):
        university = self.university_input.get()
        city = self.city_input.get()
        department = self.department_input.get()
        ranking = self.ranking_input.get()
        note = self.note_input.get()
        score = self.score_input.get()
        for item in self.data:
            if item['university'] == university and item['city'] == city and item['department'] == department:
            # update the existing university
                item['ranking'] = ranking
                item['note'] = note
                item['score'] = score
                self.save_data()
                self.load_listbox()
                return
        item = {'university': university, 'city': city, 'department': department, 'ranking': ranking, 'score': score, 'note': note}
        self.data.append(item)
        self.save_data()
        self.load_listbox()
    def add_to_presentation_days(self):
        city = self.city_input_page3.get()
        university = self.university_input_page3.get()
        date = self.date_input_page3.get()
        note = self.note_input_page3.get()
    
        item = {'city': city, 'university': university, 'date': date, 'note': note}
        self.presentation_days.append(item)
        self.save_presentation_days()
        self.load_listbox()
    def on_double_click(self, event):
        selected_item = self.school_list.focus()  # get selected item
        item = self.school_list.item(selected_item)
        values = item['values']
    
    # Input validation can be added here.

        for data_item in self.data:
            if (data_item['university'] == values[0] and
                data_item['city'] == values[1] and
                data_item['department'] == values[2]):
            
            # updating the input fields with selected item
                self.university_input.delete(0, 'end')
                self.university_input.insert(0, data_item['university'])
                
                self.city_input.delete(0, 'end')
                self.city_input.insert(0, data_item['city'])
                
                self.department_input.delete(0, 'end')
                self.department_input.insert(0, data_item['department'])
                
                self.ranking_input.delete(0, 'end')
                self.ranking_input.insert(0, data_item['ranking'])
                
                self.score_input.delete(0, 'end')
                self.score_input.insert(0, data_item['score'])
                
                self.note_input.delete(0, 'end')
                self.note_input.insert(0, data_item['note'])

    def add_to_wishlist(self):
        university = self.university_input.get()
        city = self.city_input.get()
        department = self.department_input.get()
        ranking = self.ranking_input.get()
        score = self.score_input.get()  # Get the score from the input field
        note = self.note_input.get()

        item = {'university': university, 'city': city, 'department': department, 'ranking': ranking, 'score': score, 'note': note}
        self.wishlist.append(item)
        self.save_wishlist()
        self.load_listbox()

    def delete(self):
        selected_item = self.school_list.focus()  # get selected item
        item = self.school_list.item(selected_item)
        values = item['values']
        
        self.school_list.delete(selected_item)
        
        self.data = [item for item in self.data if not (item["university"] == values[0] and
                                                        item["city"] == values[1] and
                                                        item["department"] == values[2] and
                                                        item["ranking"] == values[3] and
                                                        item["score"] == values[4] and
                                                        item["note"] == values[5])]

        self.save_data()
        self.load_listbox()

    def delete_wishlist(self):
        selected_item = self.wishlist_treeview.focus()  # get selected item
        item = self.wishlist_treeview.item(selected_item)
        values = item['values']
        
        self.wishlist_treeview.delete(selected_item)
        
        self.wishlist = [item for item in self.wishlist if not (item["university"] == values[0] and
                                                                item["city"] == values[1] and
                                                                item["department"] == values[2] and
                                                                item["ranking"] == values[3] and
                                                                item["score"] == values[4] and
                                                                item["note"] == values[5])]
        
        self.save_wishlist()
        self.load_listbox()
    def load_listbox(self):
        self.presentation_days_list.delete(*self.presentation_days_list.get_children())
        for item in sorted(self.presentation_days, key=lambda item: item['date']):
            self.presentation_days_list.insert('', 'end', values=(item['city'], item['university'], item['date'], item['note']))
        self.school_list.delete(*self.school_list.get_children())
        for item in sorted(self.data, key=lambda item: item['department']):
            self.school_list.insert('', 'end', values=(item['university'], item['city'], item['department'], item['ranking'], item['score'], item['note']))


        self.wishlist_treeview.delete(*self.wishlist_treeview.get_children())
        for item in sorted(self.wishlist, key=lambda item: item['department']):
            self.wishlist_treeview.insert('', 'end', values=(item['university'], item['city'], item['department'], item['ranking'], item['score'], item['note']))  # Include score
    def save_presentation_days(self):
        with open('presentation_days.json', 'w') as f:
            json.dump(self.presentation_days, f)
    def save_data(self):
        with open('tercihdata.json', 'w') as f:
            json.dump(self.data, f)

    def save_wishlist(self):
        with open('tercihwishlist.json', 'w') as f:
            json.dump(self.wishlist, f)

    def load(self):
        try:
            with open('tercihdata.json', 'r') as f:
                self.data = json.load(f)
            for item in self.data:
                if 'score' not in item:
                    item['score'] = ''
        except FileNotFoundError:
            self.data = []

        try:
            with open('tercihwishlist.json', 'r') as f:
                self.wishlist = json.load(f)
            for item in self.wishlist:
                if 'score' not in item:
                    item['score'] = ''
        except FileNotFoundError:
            self.wishlist = []
        
        try:
            with open('presentation_days.json', 'r') as f:
                self.presentation_days = json.load(f)
        except FileNotFoundError:
            self.presentation_days = []


root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

width = int(screen_width * 0.9)
height = int(screen_height * 0.9)

root.geometry(f"{width}x{height}")
app = UniversityApp(root)
root.mainloop()
