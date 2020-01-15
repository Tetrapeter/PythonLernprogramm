import tkinter as tk
from tkinter import messagebox, StringVar
import json

color_background = '#e6ddde'
color_background_textbox = '#e6ddde'
color_background_listbox = '#e6ddde'
color_frame_background = 'white'
color_font = '#443235'
font_standard = 'Courier New'              #'Monospaced Font !Wichtig!
color_button = '#BC8F8F'
color_button_font = 'white'

entry_max_chars = 20                       #Maximale Zeichen im Entryfeld für Begriffsdefinition
max_character_textbox = 400                #Wird praktisch noch nicht verwendet -> siehe BAUSTELLE

class FancyButtonDeluxe(tk.Button):
    """Default Button Design"""
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw,
                           relief="solid", borderwidth=0, activebackground=color_font,
                           activeforeground=color_frame_background, font=(font_standard, 10, 'bold'),
                           background=color_button, foreground=color_font)

        tk.Button.grid(self, ipady=2.5, ipadx=10)

class Popup_Entry_Window():
    """Dialogfenster mit Eingabefeld Parameter: output_instance, outputliste"""

    def __init__(self, outputliste, x, y):
        self.size_n_position = "245x90+"+str(x+100)+"+"+str(y+180)

        self.root = tk.Tk(className=' Eingabe')
        self.root.geometry(self.size_n_position)

        self.canvas1 = tk.Canvas(self.root, bg=color_frame_background)
        self.canvas1.pack()

        self.frame1 = tk.Frame(self.canvas1, bg=color_frame_background)
        self.frame1.grid()

        self.label_name = tk.Label(self.frame1, text='Namen für neue Quizestsammlung eingeben',
                                   bg=color_frame_background)
        self.label_name.grid()

        self.entry_field = tk.Entry(self.frame1, width=30)
        self.entry_field.grid(padx=5, pady=5)

        """Anmerkung: edit_object ist das instanzierte Objekt"""
        self.button_ok = FancyButtonDeluxe(self.frame1, text="Speichern",
                                           command=lambda: self.returnfunc(outputliste))
        self.button_ok.grid(padx=5, pady=5)

    def returnfunc(self, outputliste):
        """returnfunc(self, insert_list_object) nimmt Wert aus Entryfeld. Speichert Wert in global out.
        Parameter: Ziel Output listbox"""
        global out
        out = str(self.entry_field.get())
        # if len(out)
        self.root.destroy()
        outputliste.insert('end', out)





class Create_New_Window():
    """Standardfenster Grundlayout"""

    def __init__(self, windowname):
        self.gap_marker_left = str(">")
        self.gap_marker_right = str("<")
        self.aktive_testsammlung = str("")
        self.name_quizsammlung = ""  # Anfangswert für aktuell ausgewählte Testsammlung
        self.root = tk.Tk(className=' Definiquestion')
        self.root.geometry("800x650")
        self.root.maxsize(800, 650)
        self.root.minsize(800, 650)


        self.canvas = tk.Canvas(self.root, width=800, height=650, bg=color_background, borderwidth = 0)
        self.canvas.pack()

        self.frame_upper = tk.Frame(self.canvas, bg=color_font, borderwidth=0, relief='solid')
        self.frame_upper.place(relx=0.075, rely=0.05, relwidth=0.85, relheight=0.1)

        self.frame_center = tk.Frame(self.canvas, bg=color_frame_background)
        self.frame_center.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.25)

        self.frame_stripe = tk.Frame(self.canvas, bg=color_font)
        self.frame_stripe.place(relx=0.075, rely=0.4725, relwidth=0.85, relheight=0.005)

        self.frame_lower = tk.Frame(self.canvas, bg=color_frame_background, bd=10)
        self.frame_lower.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.45)

        self.frame_stripe1 = tk.Frame(self.canvas, bg=color_font)
        self.frame_stripe1.place(relx=0.075, rely=0.97, relwidth=0.85, relheight=0.005)

        self.label = tk.Label(self.frame_upper, bg=color_background, text=windowname, font=(font_standard, '18'),
                              fg=color_font)

        self.label.place(relx=0.5, rely=0.5, relwidth=1, relheight=0.85, anchor ='center')

    def go_to_window(self, ziel):
        """Gehe zu Fenster x. Parameter: Fenster x"""
        pos_x = self.root.winfo_x()
        pos_y = self.root.winfo_y()
        pos_string = "800x650+"+str(pos_x)+"+"+str(pos_y)
        self.root.destroy()
        destination_instance = ziel
        destination_instance.root.geometry(pos_string)





class Quiz_Edit_Window(Create_New_Window, FancyButtonDeluxe):
    """Bearbeitungstool für die Quizfragen und Quizfragensammlung"""

    def __init__(self):
        Create_New_Window.__init__(self, "Quiz Editor")

        """Quizsammlungsliste"""

        self.master_listbox_frame = tk.Frame(self.frame_center, height=100)
        self.scrollbar_quizsammlung_listbox = tk.Scrollbar(self.master_listbox_frame, orient='vertical')
        self.quizsammlung_listbox = tk.Listbox(self.master_listbox_frame, font=(font_standard, 8), fg=color_font,
                                               bg=color_background_listbox, selectbackground=color_font, height=7,
                                               yscrollcommand=self.scrollbar_quizsammlung_listbox.set, borderwidth=0)

        #self.quizsammlung_listbox2 = tk.Listbox(self.master_listbox_frame, bg=color_background_listbox, fg=color_font,
        #  Plan: zweite Listbox für             selectbackground=color_font, height=7, font=(font_standard, 8),
        #        extra Werte (zB Datum)         yscrollcommand=self.scrollbar_quizsammlung_listbox.set, borderwidth=0)

        self.scrollbar_quizsammlung_listbox.config(command=self.quizsammlung_listbox.yview)
        self.master_listbox_frame.grid(row=0, column=1, padx=40, pady=15, rowspan=4)
        self.scrollbar_quizsammlung_listbox.pack(side='right', fill='y')
        self.quizsammlung_listbox.pack(side='left', fill='both')
        #self.quizsammlung_listbox2.pack(side='left', fill='both') #siehe Plan


        """Parent Frame für 3 Buttons"""
        self.parent_button_quizsammlung = tk.Frame(self.frame_center, bg=color_frame_background)
        self.parent_button_quizsammlung.grid(row=0, column=0, padx=35,pady=20)

        """Button: neue Quizsammlung erstellen und in Quizsammlungsliste einfügen"""
        self.button_new_quizsammlung = FancyButtonDeluxe(self.parent_button_quizsammlung, text="Neue Quizsammlung erstellen",
                                                         width=25, command=lambda: self.create_new_testsammlung())
        self.button_new_quizsammlung.grid(row=0, column=0, pady=5)

        """Button: Lade ausgewählte Quizsammlung"""
        self.button_load_testsammlung = FancyButtonDeluxe(self.parent_button_quizsammlung, text="Quizsammlung laden",
                                                          width=25, command=lambda: self.load_quizsammlung())
        self.button_load_testsammlung.grid(row=1, column=0, pady=5)

        """Button: ausgewählte Quizsammlung löschen"""
        self.button_delete_quizsammlung = FancyButtonDeluxe(self.parent_button_quizsammlung, text="Quizsammlung löschen",
                                                            width=25, command=lambda: self.delete_quizsammlung())
        self.button_delete_quizsammlung.grid(row=2, column=0, pady=5)

        """___________Neuer Frame___________________________________________________________________"""

        """pragmatischer Leerer Frame für Lückenbildung"""

        self.frame_aestetic_gap1 = tk.Frame(self.frame_lower)
        self.frame_aestetic_gap1.grid(row=0, column=0, padx=15)


        """Label akuelle aktive Quizsammlung"""

        self.parent_frame = tk.Frame(self.frame_lower, bg=color_font)
        self.parent_frame.grid(row=1, column=1, columnspan=6)

        self.label_aktive_quizsammlung = tk.Label(self.parent_frame, text="Aktive Quizsammlung:", foreground=color_font,
                                                  bg=color_frame_background, font=(font_standard, 14), bd=2)
        self.label_aktive_quizsammlung.grid(row=1, column=0, columnspan=2)
        self.label_name_aktive_quizsammlung = tk.Label(self.parent_frame, text=self.name_quizsammlung,
                                                       foreground=color_font, bg=color_frame_background,
                                                       font=(font_standard, 14))
        self.label_name_aktive_quizsammlung.grid(row=1, column=2)


        """Label Begriffeingabe"""

        self.label_definition = tk.Label(self.frame_lower, text="Begriff:", bg=color_frame_background,
                                         font=(font_standard, 12))
        self.label_definition.grid(row=3, column=1, padx=5, sticky='e')

        """Texteingabe für Begriff"""

        self.text_input_trace = StringVar()
        self.input_definition = tk.Entry(self.frame_lower, bg=color_background, borderwidth=0, font=(font_standard, 12),
                                         foreground=color_font, textvariable=self.text_input_trace)
        self.input_definition.grid(row=3, column=2, padx=5, pady=20, ipady=2, sticky='w')
        self.text_input_trace.trace("w", lambda *args: self.character_limit(self.text_input_trace, entry_max_chars))

        """leerer Frame für Lückenbildung"""
        self.frame_aestetic_gap2 = tk.Frame(self.frame_lower)
        self.frame_aestetic_gap2.grid(row=3, column=4, padx=15)

        """Button Quiz laden"""
        self.load_quiz_button = FancyButtonDeluxe(self.frame_lower, text='Laden', command=lambda: self.load_test_from_listbox())
        self.load_quiz_button.grid(row=3, column=5)

        """Button: Eintrag Löschen aus Listbox UND aus Json,datei"""
        self.delete_button = FancyButtonDeluxe(self.frame_lower, text='Eintrag löschen', command=lambda: self.delete_test())
        self.delete_button.grid(row=3, column=6, sticky='w', padx=5)

        """Texteingabe für Begriffdefinition"""
        self.master_textframe = tk.Frame(self.frame_lower)
        self.scrollbar_input_field = tk.Scrollbar(self.master_textframe)
        self.input_field = tk.Text(self.master_textframe, bg=color_background_textbox, width=35, height=7,
                                   borderwidth=0, selectbackground=color_font, foreground=color_font,
                                   yscrollcommand=self.scrollbar_input_field.set, wrap='word', font=(font_standard, 10))

        self.scrollbar_input_field.config(command=self.input_field.yview)
        self.input_field.bind('<Key>', lambda *args:self.character_limit_text(self.input_field, max_character_textbox))
        self.master_textframe.grid(row=4, column=1, columnspan=3, sticky='e', padx=3)
        self.input_field.pack(side='left')
        self.scrollbar_input_field.pack(side='right', fill='y')

        #self.char_count_label = tk.Label(self.frame_lower, text='0/400', font=(font_standard, 7), bg=color_frame_background)
        #self.char_count_label.grid(row=3, column=1, sticky='s') # Das soll mal die Anzeige für die Anzahl der Zeichen in
                                                                 # der Textbox werden



        """Listbox mit den gespeicherten Quizfragen"""
        self.list_master_frame = tk.Frame(self.frame_lower)
        self.list_master_frame.grid(row=4, column=5, columnspan=2, sticky='w')
        self.scrollbar_test_listbox = tk.Scrollbar(self.list_master_frame, orient='vertical')
        self.test_listbox = tk.Listbox(self.list_master_frame, yscrollcommand=self.scrollbar_test_listbox.set,
                                       borderwidth=0, bg=color_background_listbox, selectbackground=color_font,
                                       height=9, width=28, font=(font_standard, 8), fg=color_font)


        self.scrollbar_test_listbox.config(command=self.test_listbox.yview)
        self.test_listbox.pack(side="left", fill='x')
        self.scrollbar_test_listbox.pack(side='right', fill='y')

        """Button: Lücke definieren"""
        self.gap_marker_button = FancyButtonDeluxe(self.frame_lower, text='Lücke definieren', width=14,
                                                   command=lambda: self.gap_marker())
        self.gap_marker_button.grid(row=5, column=1, sticky="w",  columnspan=2)

        """Button: Text und Begriff speichern"""
        self.save_button = FancyButtonDeluxe(self.frame_lower, width=15, text='Speichern', command=lambda: self.save_text())
        self.save_button.grid(row=5, column=2, columnspan=2, pady=5, sticky='e')

        """Button: Zurück zum Hauptbildschirm"""
        self.backtomain_button = FancyButtonDeluxe(self.frame_lower, width=25, text='Zurück zum Hauptbildschirm',
                                                   command=lambda:self.go_to_window(Index_Main_Window("Willkommen")))
        self.backtomain_button.grid(row=5, column=5, columnspan=2, pady=5, sticky='w')

        self.update_list_quizsammlung()



    def character_limit(self, entry_text, max):
        """definiert eine maximale Eingabezahl. Wenn Limit erreicht wird, kann man nichts mehr eintippen"""
        if len(entry_text.get()) > max:
            entry_text.set(entry_text.get()[0:max])



    """_BAUSTELLE BAUSTELLE BAUSTELLE _____________________Das läuft nicht___________________________________________"""

    def character_limit_text(self, input_textwidget, max_char):
        """Zeichenlimit im Textfeldwidget"""
        print("Es kommt was an in character_limit_text()")
        input = input_textwidget.get('1.0', 'end')
        len1 = len(input)
        print(len1)

        """_BAUSTELLE BAUSTELLE BAUSTELLE ___________________________________________________________________________"""




    def save_text(self):
        """Text aus Textfeldern auslesen. Definitionswort und Definitionstext """

        get_input_definition = self.input_definition.get()  # get für Definitionswort
        get_input_field = self.input_field.get('1.0', 'end-1c')  # get für Definitionstext

        root = tk.Tk()
        root.withdraw()

        with open("test_list.json") as infile:  # Aktuelle Testsammlung auslesen
            json_scan_now = json.load(infile)

        if get_input_definition not in json_scan_now[self.name_quizsammlung]:
            """Prüfen ob Begriff schon in Sammlung vorhanden ist"""
            messagebox._show(title='Gespeichert!', message='Test zur Sammlung hinzugefügt!')
        else:
            messagebox._show(title='Aktualisiert!', message='Bestehenden Test aktualisiert!')

        json_scan_now[self.name_quizsammlung][get_input_definition] = get_input_field
        # Den Neuen Test in die Testsammlung hinzufügen. Also den Ausgelesenen Shit.

        with open("test_list.json", "w") as outfile:  # Aktualisierter Shit wieder als test_list.json abspeichern
            json.dump(json_scan_now, outfile)

        self.update_test_listbox()

        self.input_definition.delete(0, 'end')
        self.input_field.delete('1.0', 'end')



    def update_test_listbox(self):  # Insert alle Keys aus test_list.json in Listbox
        """Aktualisierung der Listbox mit einzelnen Testfragen"""
        self.test_listbox.delete(0, 'end')  # Delete, weil sonst doppelte Einträge entstehen

        with open("test_list.json") as infile:  # Aktuelle Testsammlung auslesen
            json_scan_now = json.load(infile)

        for key in json_scan_now[self.name_quizsammlung]:
            self.test_listbox.insert('end', key)

    def delete_test(self):
        "Löschen eines Eintrages aus Listbox UND aus Json Datei"
        selected = self.test_listbox.get('active')

        self.test_listbox.delete('active')
        self.input_definition.delete(0, 'end')
        self.input_field.delete('1.0', 'end')

        with open("test_list.json") as infile:
            json_scan_now = json.load(infile)

        del json_scan_now[self.name_quizsammlung][selected]

        with open("test_list.json", "w") as outfile:
            json.dump(json_scan_now, outfile)

    def gap_marker(self):
        """Markieren von Wörtern mit den Zeichen > und < am Anfang und Ende der Markierung"""

        index_sel_first = self.input_field.index("sel.first")
        sel_word = self.gap_marker_left + self.input_field.selection_get() + self.gap_marker_right

        self.input_field.delete('sel.first', 'sel.last')
        self.input_field.insert(index_sel_first, sel_word)

    def load_test_from_listbox(self):
        """Ausgewählten Test aus Listbox in die Textfelder laden"""
        dictKey = self.test_listbox.get('active')

        with open("test_list.json") as outfile:
            json_scan_now = json.load(outfile)

        dictValue = json_scan_now[self.name_quizsammlung][dictKey]

        self.input_definition.delete(0, 'end')
        self.input_field.delete('1.0', 'end')

        self.input_definition.insert(1, dictKey)
        self.input_field.insert('1.0', dictValue)



    def create_new_testsammlung(self):

        self.input_definition.delete(0, 'end')
        self.input_field.delete('1.0', 'end')
        self.test_listbox.delete(1, 'end')

        pos_x = self.root.winfo_x()
        pos_y = self.root.winfo_y()

        TestsammlungDialog = Popup_Entry_Window(self.quizsammlung_listbox, pos_x, pos_y)
        TestsammlungDialog.root.mainloop(1)
        self.name_quizsammlung = str(out)

        with open("test_list.json") as infile:
            json_scan_now = json.load(infile)

        json_scan_now[self.name_quizsammlung] = {}

        with open("test_list.json", 'w') as outfile:
            json.dump(json_scan_now, outfile)

        self.load_quizsammlung('end')    #letzten Eintrag laden. Also der, der eben erstellt wurde


    def load_quizsammlung(self, getter='active'):
        """Lade den Inhalt der ausgewählten Testsammlung in test_listbox und text_field im unteren Frame"""
        self.input_definition.delete(0, 'end')
        self.input_field.delete('1.0', 'end')
        self.name_quizsammlung = self.quizsammlung_listbox.get(getter)
        self.label_name_aktive_quizsammlung.config(text=self.name_quizsammlung)
        self.update_test_listbox()

    def update_list_quizsammlung(self):

        with open("test_list.json") as infile:
            json_scan_now = json.load(infile)

        for key in json_scan_now:
            self.quizsammlung_listbox.insert('end', key)

    def delete_quizsammlung(self, getter='active'):

        marked_quizsammlung = self.quizsammlung_listbox.get(getter)
        self.quizsammlung_listbox.delete(getter)

        with open("test_list.json") as infile:
            json_scan_now = json.load(infile)

        del json_scan_now[marked_quizsammlung]

        with open("test_list.json","w") as outfile:
            json.dump(json_scan_now, outfile)

        if marked_quizsammlung == self.name_quizsammlung:
            self.test_listbox.delete(0,'end')
            self.input_definition.delete(0,'end')
            self.input_field.delete('1.0','end')
            self.name_quizsammlung = ""
            self.label_name_aktive_quizsammlung.config(text=self.name_quizsammlung)


class Quizfenster(Create_New_Window):

    def __init__(self, input_quiz_text):
        Create_New_Window.__init__(self, "Quiz")

        self.string_split_dict = {}
        self.quiz_counter = 0
        self.begriff_quiz_list = []
        self.text_quiz_list = []
        self.font_text = font_standard


        self.width_entry= 12             #Entspricht in Courier 10 Zeichen. Wird für Tkinter gebraucht.
        self.entry_char_length = 12      #Benötigt die größe des Entryfeldes um den Zeilenumbruch zu berechnen
        self.max_char_linelength = 52    #Maximale Zeilenlänge in Buchstaben
        self.max_char_textlength = "400" #Maximale Textlänge

        self.button_check_quiz = FancyButtonDeluxe(self.frame_center, bg=color_frame_background,
                                                   command=lambda: self.check_if_correct(), text='Kontrolliere Quiz')
        self.button_check_quiz.grid(column=0, row=1, padx=6, pady=28, ipady=10)

        self.button_previous_quiz = FancyButtonDeluxe(self.frame_center, bg=color_frame_background, text='Vorheriges Quiz',
                                                      command=lambda: self.open_previous_quiz())
        self.button_previous_quiz.grid(column=1, row=1, padx=6, pady=28, ipady=10)

        self.button_next_quiz = FancyButtonDeluxe(self.frame_center, bg=color_frame_background, text='Nächstes Quiz',
                                        command=lambda: self.open_quiz_task())
        self.button_next_quiz.grid(column=2, row=1, padx=6, pady=28, ipady=10)
        self.button_home = FancyButtonDeluxe(self.frame_center, bg=color_frame_background, text='Hauptbildschirm',
                                                  command=lambda: self.go_to_window(Index_Main_Window('Willkommen')))
        self.button_home.grid(column=3, row=1, padx=6, pady=28, ipady=10)

        #self.begriffVar = ""
        self.begriff_main_frame = tk.LabelFrame(self.canvas, bg=color_frame_background, borderwidth=0, relief='solid')
        self.begriff_main_frame.place(relx=0.15, rely=0.35, relwidth=0.6, relheight=0.05)
        self.begriff_label1 = tk.Label(self.begriff_main_frame, text='Begriff: ', font=(font_standard, 16),
                                       bg=color_frame_background)
        self.begriff_label1.pack(side='left')
        self.begriff_label2 = tk.Label(self.begriff_main_frame, text="", font=(font_standard, 16, 'bold'),
                                       bg=color_frame_background, width=200)
        self.begriff_label2.pack(side='left')

        """Main Frame als Basis für das generierte Quiz"""
        self.main_frame = tk.Frame(self.frame_lower, bg=color_frame_background)
        self.main_frame.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)




        with open("test_list.json") as infile:
            json_dict_now = json.load(infile)

        for text in json_dict_now[input_quiz_text]:
            self.text_quiz_list.append(json_dict_now[input_quiz_text][text])

        for begriff in json_dict_now[input_quiz_text]:
            self.begriff_quiz_list.append(begriff)



        self.open_quiz_task(True)

    def open_quiz_task(self, first_time=False):
        """Funktion, die den aktuellen Quiztext-Frame mit dem nächsten Quiztext überschreibt
        Also einfach nur den nächsten Quiztext aufruft. Das ist für den Weiter-Button gedacht"""
        self.string_split_dict = {}
        self.clear_quiz()

        try:
            if first_time:
                self.quiz_counter -= 1
            self.quiz_counter += 1
            inputtext = self.text_quiz_list[self.quiz_counter]
            inputbegriff = self.begriff_quiz_list[self.quiz_counter]
            self.create_quiz_with_entry(inputtext, inputbegriff)

        except IndexError:
            self.quiz_counter -= 1
            inputtext = self.text_quiz_list[self.quiz_counter]
            inputbegriff = self.begriff_quiz_list[self.quiz_counter]
            self.create_quiz_with_entry(inputtext, inputbegriff)


            root = tk.Tk()
            root.geometry("300x75+{}+{}".format(self.root.winfo_x(), self.root.winfo_y()))
            root.withdraw()
            messagebox.showinfo(title="Ende!", message="Ende der Quizsammlung.")

    def open_previous_quiz(self):

        self.string_split_dict = {}
        self.clear_quiz()

        self.quiz_counter -= 1

        if self.quiz_counter > 0:
            inputtext = self.text_quiz_list[self.quiz_counter]
            inputbegriff = self.begriff_quiz_list[self.quiz_counter]
            self.begriffVar = inputbegriff
            self.create_quiz_with_entry(inputtext, inputbegriff)

        else:
            self.quiz_counter = 0
            inputtext = self.text_quiz_list[self.quiz_counter]
            inputbegriff = self.begriff_quiz_list[self.quiz_counter]
            self.create_quiz_with_entry(inputtext, inputbegriff)
            root = tk.Tk()
            root.geometry("300x75+{}+{}".format(self.root.winfo_x(), self.root.winfo_y()))
            root.withdraw()
            messagebox.showinfo(title="Ende!", message="Stop! Weiter zurück kannst du nicht")


    def check_if_correct(self):

        for key in self.string_split_dict:  # Erzeuge jedes einzelne Objekt. Entry und Label

            if key[3:8] == "entry":
                check = self.string_split_dict[key]
                if self.__dict__[key].get() == check[1:-1]:
                    self.__dict__[key].configure(background='#2EFE64')

                else:
                    self.__dict__[key].configure(background='#FA5858')
            else:
                pass

    def clear_quiz(self):   # Inhalt vom main_frame löschen
        list = self.main_frame.grid_slaves()
        for l in list:
            l.destroy()



    def create_quiz_with_entry(self, input_quiz_text, input_quiz_begriff):

        self.begriff_label2.config(text=input_quiz_begriff)


        """Erstellt aus einem Quiztext mit definierten Lücken, einzelne Objekte als Dict und als Tkinter Entry
         und Label. Das ist die Seite, in der man die Aufgaben/Quizfragen/Lückentexte löst"""
        position_x = 0
        position_y = 0
        position_string = 0
        count_object = 0


        while position_string < len(input_quiz_text):   # position_string -> Buchstabenposition an der man insgesamt
                                                        # befindet im Text.
            """Die Schleife speichert alle einzelnen Label mit den dazugehörigen Bezeichnungen in einem Dict ab. Daraus
            wird ein Grid System für tkinter erzeugt 
            Beispiel :
                f3_entry_Obj9 :  f3 steht für dritte Zeile. Das Programm packt immer soviele Elemente in die Zeile wie
                                durch self.max_char_linelength definiert werden. Der Int steht für Zeichenanzahl 
                                Obj9 steht für das x-te generierte Objekt(Entry und Label).                                
            """
            temp_split_label = ""
            temp_split_entry = ""
            """___Abfangen_von allen Zeichen, die keine Lückenmarkierer sind________________________________________ """
            if input_quiz_text[position_string] != self.gap_marker_left:

                while input_quiz_text[position_string] != self.gap_marker_left \
                        and position_x < self.max_char_linelength:
                    temp_split_label = temp_split_label + input_quiz_text[position_string]
                    #solange kein Lückentext Marker ">" auftaucht und 52chars nicht überschritten werden
                    #werden chars in temp_split_label gesammelt.
                    position_x += 1
                    position_string += 1
                    if position_string == len(input_quiz_text):
                        break

                if position_x < self.max_char_linelength:
                    #Wenn Zeilenlimit (52chars) nicht überschritten wird
                        self.string_split_dict["f" + str(position_y) +"_label_Obj"+ str(count_object)] = temp_split_label
                        count_object += 1


                elif position_x >= self.max_char_linelength:


                    if position_string == len(input_quiz_text):
                        self.string_split_dict["f" + str(position_y) + "_label_Obj" + str(count_object)] = temp_split_label
                                                                                      #wenn Zeichenlimit überschritten wird
                    elif input_quiz_text[position_string] == " "\
                            or input_quiz_text[position_string-1] == " ":

                        self.string_split_dict["f" + str(position_y) + "_label_Obj" + str(count_object)] = temp_split_label
                        count_object += 1
                        position_y += 1
                        position_x = 0

                    else:

                        z = 0
                        position_string_temp = position_string

                        while input_quiz_text[position_string_temp-1] != " " \
                                and input_quiz_text[position_string-1] != self.gap_marker_right \
                                and z*(-1) <= self.max_char_linelength:
                            position_string_temp -= 1
                            z -= 1

                        if z*-1 >= self.max_char_linelength:
                            self.string_split_dict[
                                "f" + str(position_y) + "_label_Obj" + str(count_object)] = temp_split_label
                            count_object += 1
                            position_y += 1
                            position_x = 0
                            print("temp_split_label in der while z>= maxchar: "+temp_split_label)

                        else:
                            self.string_split_dict["f" + str(position_y) + "_label_Obj" + str(count_object)]\
                                              = temp_split_label[0:z]
                            position_string = position_string_temp
                            count_object += 1
                            position_y += 1
                            position_x = 0



                """Wenn der String mit Lückenword (Entry) anfängt___________________________________________________"""

            elif input_quiz_text[position_string] == self.gap_marker_left:

                while input_quiz_text[position_string] != self.gap_marker_right \
                        or input_quiz_text[position_string] == self.gap_marker_left:

                    temp_split_entry = temp_split_entry + input_quiz_text[position_string]
                    position_string += 1

                temp_split_entry = temp_split_entry + input_quiz_text[position_string]
                position_string += 1
                position_x += self.entry_char_length  #Entry Felder haben immer die gleiche Breite.

                if position_x >= self.max_char_linelength:
                    position_y += 1
                    self.string_split_dict["f"+str(position_y)+"_entry_Obj"+str(count_object)] = temp_split_entry
                    count_object += 1
                    position_x = 9

                else:
                    self.string_split_dict["f" + str(position_y) + "_entry_Obj" + str(count_object)] = temp_split_entry
                    count_object += 1

            """_____________________________________________________________________________________________________"""


        """_ Erzeuge_alle Objekte in Self.main_frame__________________________________________________________________"""

        set_frames = set()
        for key in self.string_split_dict:       #Erzeuge set für alle Frames für die einzelnen Zeilen
            set_frames.add(key[0:2])

        dict_object_position = {}
        for key in set_frames:
            self.__dict__[key] = tk.Frame(self.main_frame, bg=color_frame_background)
            self.__dict__[key].grid(row=key[1], column=0, sticky='w')
            dict_object_position[key] = 0      # Erzeugt dict mit den Namen für die Framezeilen und Startwert 0




        for key in self.string_split_dict:       #Erzeuge jedes einzelne Objekt. Entry und Label

            if key[3:8] == "label":
                dict_object_position[key[0:2]] += 1
                content = self.string_split_dict[key]
                self.__dict__[key] = tk.Label(self.__dict__[key[0:2]],font=(self.font_text,12), text=content,
                                              bg=color_frame_background, justify='left')
                self.__dict__[key].grid(row=key[1], column=dict_object_position[key[0:2]], sticky='w')

            else:
                dict_object_position[key[0:2]] += 1
                self.__dict__[key] = tk.Entry(self.__dict__[key[0:2]], width=self.width_entry, font=(self.font_text,12),
                                              bg=color_background, justify='left', borderwidth=0, foreground=color_font)

                self.__dict__[key].grid(row=key[1], column=dict_object_position[key[0:2]], sticky='w')




class Index_Main_Window(Create_New_Window):
    """Das Hauptfenster. Wird angezeigt, wenn das Programm gestartet wird."""
    def __init__(self, windowname):
        Create_New_Window.__init__(self, windowname)

        self.frame_lower.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.25)
        self.frame_stripe1.place(relx=0.075, rely=0.78, relwidth=0.85, relheight=0.005)


        self.main_index_frame_center = tk.Frame(self.frame_center, bg=color_frame_background)
        self.main_index_frame_center.pack(anchor='center')
        self.button_editor_window = FancyButtonDeluxe(self.main_index_frame_center, text='Quiz Editor',
                                                      command=lambda: self.go_to_window(Quiz_Edit_Window()))
        self.button_editor_window.grid(row=0, column=0, ipadx=50, ipady=20, pady=45)


        self.main_index_frame_lower = tk.Frame(self.frame_lower, bg=color_frame_background)
        self.main_index_frame_lower.pack(anchor='center')

        self.main_empty_frame = tk.Frame(self.main_index_frame_lower, bg=color_frame_background)
        self.main_empty_frame.grid(row=0, column=1, columnspan=2, pady=8)

        self.main_list_frame = tk.Frame(self.main_index_frame_lower, bg=color_frame_background)
        self.main_list_frame.grid(row=1, column=1, rowspan=2, padx=20)


        """Listbox mit gespeicherten Quizsammlungen"""
        self.main_scrollbar = tk.Scrollbar(self.main_list_frame, orient='vertical')
        self.listbox_main_quizsammlung = tk.Listbox(self.main_list_frame, yscrollcommand=self.main_scrollbar.set,
                                                    font=(font_standard, 8), fg=color_font, bg=color_background_listbox,
                                                    selectbackground=color_font, height=7, borderwidth=0)
        self.main_scrollbar.config(command=self.listbox_main_quizsammlung.yview)
        self.listbox_main_quizsammlung.pack(side='left')
        self.main_scrollbar.pack(side='right', fill='y')

        """Button zum Quiz starten"""
        self.button_start_quiz = FancyButtonDeluxe(self.main_index_frame_lower, text='Starte Quiz Session',
                                                   width=30, height=2, command=lambda:self.start_quiz_session_get())
        self.button_start_quiz.grid(row=1, column=2, sticky='nw')

        """Button zum Einstellen des Ablaufs der Session.  Noch keine Funktion implementiert"""
        self.button_setting_quiz = FancyButtonDeluxe(self.main_index_frame_lower, text='Session Einstellungen',
                                                     width=30, height=2)
        self.button_setting_quiz.grid(row=2, column=2, sticky='nw')

        self.update_main_listbox()   #Quizsammlung in Listbox Laden


    def start_quiz_session_get(self):
        self.input_quizsammlung = self.listbox_main_quizsammlung.selection_get()
        self.go_to_window(Quizfenster(self.input_quizsammlung))


    def update_main_listbox(self):

        with open('test_list.json') as infile:
            json_dict_now = json.load(infile)

        for key in json_dict_now:
            self.listbox_main_quizsammlung.insert('end', key)



main_window = Index_Main_Window("Willkommen")
main_window.root.mainloop()






"""Testfunktionen________________und Notizen________________________________________________________________
string = ""
for key, values in string_split_dict.items():
    print(key, values)
testfile = ""
for key in string_split_dict:
    testfile += string_split_dict[key]
    string += string_split_dict[key]

if testfile == input_quiz_text:
    print("Ich glaubs nicht, es hat geklappt!")
else:
    print("-.- Nope.")

with open('outputyeah.json', 'w') as outfile:
    json.dump(testfile, outfile)
__________________________________________________________________________________________________________"""

'''
        """Masterframe in der die untergeordneten Zeilen_Frames kommen"""
        self.main_frame = tk.Frame(self.frame_center, bg="Dark Cyan")
        self.main_frame.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
        """___________________________________________________________"""

        """ZEILE__1___________________________________________________________"""
        self.f1_frame = tk.Frame(self.main_frame, bg="Dark Cyan")
        self.f1_label_name_1 = tk.Label(self.f1_frame, text="12345678901234567890", bg="Dark Cyan", font=self.font_text)
        self.f1_entryfield_1 = tk.Entry(self.f1_frame, width=15, borderwidth=0, bg='Cadet Blue')
        self.f1_label_name_2 = tk.Label(self.f1_frame, text="1234567890123456", bg="Dark Cyan", font=self.font_text)
        self.f1_entryfield_2 = tk.Entry(self.f1_frame, width=15, borderwidth=0, bg='Cadet Blue',)

        self.f1_frame.grid(row=0, column=0, sticky='w')
        self.f1_label_name_1.grid(row=0, column=0, sticky='w')
        self.f1_entryfield_1.grid(row=0, column=1, sticky='w')
        self.f1_label_name_2.grid(row=0, column=2, sticky='w')
        self.f1_entryfield_2.grid(row=0, column=3, sticky='w')
        """____________________________________________________________________"""

        """ZEILE__2____________________________________________________________"""
        self.f2_frame = tk.Frame(self.main_frame, bg="Dark Cyan")
        self.f2_label_name_1 = tk.Label(self.f2_frame, text="1234567890123456789", bg="Dark Cyan", font=self.font_text)
        self.f2_entryfield_1 = tk.Entry(self.f2_frame, width=15, borderwidth=0, bg='Cadet Blue')
        self.f2_label_name_2 = tk.Label(self.f2_frame, text="1234567890123456", bg="Dark Cyan", font=self.font_text)
        self.f2_entryfield_2 = tk.Entry(self.f2_frame, width=15, borderwidth=0, bg='Cadet Blue')

        self.f2_frame.grid(row=1, column=0, sticky='w')
        self.f2_label_name_1.grid(row=0, column=0, sticky='w')
        self.f2_entryfield_1.grid(row=0, column=1, sticky='w')
        self.f2_label_name_2.grid(row=0, column=2, sticky='w')
        self.f2_entryfield_2.grid(row=0, column=3, sticky='w')

        """____________________________________________________________________"""


        """Zeile__3____________________________________________________________"""

        self.f3_frame = tk.Frame(self.main_frame, bg="Dark Cyan")
        self.f3_label_name_1 = tk.Label(self.f3_frame, text="123456789Z123456789Z123456789Z123456789Z123456789Z123456789Z", bg="Dark Cyan", font=self.font_text,
                                        anchor='w')

        self.f3_frame.grid(row=2, column=0)
        self.f3_label_name_1.grid(row=0, column=0, sticky='w')
        """____________________________________________________________________"""



'''


"""
with open("test_list.json") as infile:  # Aktuelle Testsammlung auslesen
    json_scan_now = json.load(infile)


i=1
while i < 101:
    p=1
    MasterKey = "Sammlung"+str(i)
    key_value = {}
    while p <= 20:
        key = "Eintrag:"+str(p**2+i*2)
        value = "Das ist der >Kram< Nummer"+str(i*p+2)
        key_value.update({key:value}) #Den Neuen Test in die Testsammlung hinzufügen. Also den Ausgelesenen Shit
        p += 1
    json_scan_now[MasterKey]=key_value
    i+=1

with open("test_list.json", "w") as outfile:  # Aktualisierter Shit wieder als test_list.json abspeichern
    json.dump(json_scan_now, outfile)



"""



