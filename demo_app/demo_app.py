import tkinter as tk
from tkinter import font as tkfont, messagebox, filedialog
from space_py import SpaceApi, Astronaut, Launch, Launcher
import json


class SpaceApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Arial', size=18, weight="bold")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Astro, Lnc, Lcr, Statistics, StatLauncher, StatLaunch, StatAstronaut):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    url = "http://127.0.0.1:4533"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Rocket Space Stuff !!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Astronaut page",
                            command=lambda: controller.show_frame("Astro"))
        button2 = tk.Button(self, text="Go to Launch page",
                            command=lambda: controller.show_frame("Lnc"))
        button3 = tk.Button(self, text="Go to Launcher page",
                            command=lambda: controller.show_frame("Lcr"))
        button4 = tk.Button(self, text="Go to Statistics page",
                            command=lambda: controller.show_frame("Statistics"))
        self.url_label = tk.Text(self, height=1, width=30)
        self.url_label.delete("1.0", "end")
        self.url_label.insert(tk.END, StartPage.url)
        button5 = tk.Button(self, text="Change Base Url",
                            command=lambda: self.change_url())
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        self.url_label.pack(side="top", fill="x")
        button5.pack()

    def change_url(self):
        StartPage.url = self.url_label.get(1.0, "end-1c")


class Astro(tk.Frame):
    placeholder_astro = Astronaut()
    astro_list = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.__temp_astro = Astronaut()
        self.saved_label = tk.Text(self, height=1, width=30)
        self.saved_label.insert(tk.END, str(Astro.placeholder_astro.name))
        label = tk.Label(self, text="This is the Astronaut page", font=controller.title_font)
        label.grid(row=0, columnspan=2, column=1, pady=10)
        label1 = tk.Label(self, text="Entities Saved In Temporary Memory:",
                          font=tkfont.Font(family='Arial', size=10, weight="bold"))
        label1.grid(row=6, columnspan=3)
        label2 = tk.Label(self, text="Last Saved Astronaut ->")
        label2.grid(row=7, column=0, columnspan=2)
        self.saved_len_list_label = tk.Label(self, text=f"Length of Saved Astronaut List: {len(Astro.astro_list)}")
        self.saved_len_list_label.grid(row=7, column=3)
        self.saved_label.grid(row=7, column=2)
        button1 = tk.Button(self, text="Clear Entire Temporary List",
                            command=lambda: self.remove_last(True))
        button1.grid(row=6, column=4)
        button2 = tk.Button(self, text="Remove Last Element",
                            command=lambda: self.remove_last(False))
        button2.grid(row=7, column=4)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=0, column=0)
        button3 = tk.Button(self, text="Go to the Statistics page",
                            command=lambda: controller.show_frame("StatAstronaut"))
        button3.grid(row=0, column=3)
        button4 = tk.Button(self, text="Get all entries of dataset",
                            command=lambda: self.search_astro(f_mode="all"))
        button4.grid(row=0, column=4)

        self.folder_label1 = tk.Label(self,
                                      text="If you want to Save a JSON file firstly add data to the Temporary List!!!",
                                      font=tkfont.Font(family='Arial', size=10, weight="bold"))
        self.folder_label = tk.Label(self, text="Save JSON file for Temporary List",
                                     font=tkfont.Font(family='Arial', size=10, weight="bold"))
        self.folder_btn = tk.Button(self, text="Download Folder", command=lambda: self.folder_diag())
        self.path = tk.StringVar()
        self.folder_path_label = tk.Label(self, text=self.path.get())
        self.folder_btn1 = tk.Button(self, text="Save List to File", command=lambda: self.save_json())
        self.after_idle(lambda: self.check_json_list())

        choices = ['id', 'name', 'date_of_birth', 'date_of_death', 'nationality', 'bio', 'twitter', 'instagram', 'wiki',
                   'profile_image', 'profile_image_thumbnail', 'flights_count', 'landings_count', 'last_flight',
                   'first_flight', 'status_name', 'type_name', 'agency_name', 'agency_type', 'agency_country_code',
                   'agency_abbrev', 'agency_logo_url']

        # Find options:
        label_find = tk.Label(self, text="Find Astronaut by (exact value):")
        variable_find = tk.StringVar(self)
        variable_find.set('id')
        find_choice = tk.OptionMenu(self, variable_find, *choices)
        input_find = tk.Text(self, width=30, height=1)
        button_find = tk.Button(self, text="Find",
                                command=lambda: self.find_astro(variable_find.get(), input_find.get(1.0, "end-1c")))
        label_find.grid(row=1, column=0)
        find_choice.grid(row=1, column=1)
        input_find.grid(row=1, column=2)
        button_find.grid(row=1, column=4)

        # Search options:
        label_search = tk.Label(self, text="Search Astronaut by:")
        variable_search = tk.StringVar(self)
        variable_search.set('id')
        search_choice = tk.OptionMenu(self, variable_search, *choices)
        input_search = tk.Text(self, width=30, height=1)
        button_search = tk.Button(self, text="Search",
                                  command=lambda: self.search_astro(variable=variable_search.get(),
                                                                    value=input_search.get(1.0, "end-1c")))
        label_search.grid(row=2, column=0)
        search_choice.grid(row=2, column=1)
        input_search.grid(row=2, column=2)
        button_search.grid(row=2, column=4)

        # Post options:
        label_post = tk.Label(self, text="Post Astronaut:")
        label1_post = tk.Label(self, text="Firstly:")
        label2_post = tk.Label(self, text="Then:")
        button_create_post = tk.Button(self, text="Insert Astronaut Data",
                                       command=lambda: self.create_astro())
        button_send_post = tk.Button(self, text="Post Data",
                                     command=lambda: self.post_astro())
        label_post.grid(row=3, column=0)
        label1_post.grid(row=3, column=1)
        button_create_post.grid(row=3, column=2)
        label2_post.grid(row=3, column=3)
        button_send_post.grid(row=3, column=4)

        # Delete options:
        label_delete = tk.Label(self, text="Delete Astronaut by (exact value):")
        variable_delete = tk.StringVar(self)
        variable_delete.set('id')
        delete_choice = tk.OptionMenu(self, variable_delete, *choices)
        input_delete = tk.Text(self, width=30, height=1)
        button_delete = tk.Button(self, text="Find and Delete",
                                  command=lambda: self.delete_astro(variable_delete.get(),
                                                                    input_delete.get(1.0, "end-1c")))
        label_delete.grid(row=4, column=0)
        delete_choice.grid(row=4, column=1)
        input_delete.grid(row=4, column=2)
        button_delete.grid(row=4, column=4)

        # Update options:
        label_update = tk.Label(self, text="Update Astronaut by:")
        variable_update = tk.StringVar(self)
        variable_update.set('id')
        update_choice = tk.OptionMenu(self, variable_update, *choices)
        input_update = tk.Text(self, width=30, height=1)
        button_create_update = tk.Button(self, text="Insert Astronaut Data",
                                         command=lambda: self.create_astro())
        button_send_update = tk.Button(self, text="Update Data",
                                       command=lambda: self.update_astro(variable_update.get(),
                                                                         input_update.get(1.0, "end-1c")))
        label_update.grid(row=5, column=0)
        update_choice.grid(row=5, column=1)
        input_update.grid(row=5, column=2)
        button_create_update.grid(row=5, column=3)
        button_send_update.grid(row=5, column=4)

    def save_json(self):
        temp_dict = {}
        for i in range(len(Astro.astro_list)):
            temp_dict[i] = Astro.astro_list[i].jsonify
        with open(f'{self.path.get()}/astronaut_{str(len(Astro.astro_list))}.json', 'w') as fp:
            json.dump(temp_dict, fp)
        messagebox.showinfo(title="Success", message=f"File astronaut_{str(len(Astro.astro_list))}.json saved!")

    def check_json_list(self):
        if len(Astro.astro_list) == 0:

            self.folder_label1.grid(row=8, columnspan=4)
            self.folder_label.grid_remove()
            self.folder_path_label.grid_remove()
            self.folder_btn.grid_remove()
            self.folder_btn1.grid_remove()
        else:
            self.folder_label1.grid_remove()
            self.folder_label.grid(row=8, column=0)
            self.path.set("C:/Users/Public/Downloads")
            self.folder_path_label.grid(row=8, column=2)
            self.folder_btn.grid(row=8, column=1)
            self.folder_btn1.grid(row=8, column=3)

    def folder_diag(self):
        folder_path = str(filedialog.askdirectory(initialdir="C:/Users/Public/Downloads"))
        self.path.set(f"{folder_path}")
        self.folder_path_label.configure(text=self.path.get())

    def remove_last(self, value=True):
        if value:
            Astro.astro_list = []
            self.saved_label.delete("1.0", "end")
            self.saved_label.insert(tk.END, "None")
            self.saved_len_list_label.configure(text=f"Length of Saved Astronaut List: {len(Astro.astro_list)}")
            self.check_json_list()
            return
        if len(Astro.astro_list) <= 1:
            Astro.astro_list = []
            self.saved_label.delete("1.0", "end")
            self.saved_label.insert(tk.END, "None")
            self.saved_len_list_label.configure(text=f"Length of Saved Astronaut List: 0")
            self.check_json_list()
        else:
            Astro.astro_list.pop()
            self.saved_len_list_label.configure(text=f"Length of Saved Astronaut List: {len(Astro.astro_list)}")
            self.saved_label.delete("1.0", "end")
            self.saved_label.insert(tk.END, Astro.astro_list[-1].name)
            self.check_json_list()

    def update_astro(self, variable, value):
        if not self.check_astro(self.__temp_astro):
            messagebox.showinfo(title="Error", message="Insert data correctly!")
            return
        else:
            finder = SpaceApi()
            finder.url = StartPage.url
            finder.update_astro_by(variable, value, self.__temp_astro)
            messagebox.showinfo(title="Success", message="Entry added to database!")

    @staticmethod
    def delete_astro(variable, value):
        root = tk.Tk()
        finder = SpaceApi()
        finder.url = StartPage.url
        root.title("you searched for:")
        text = tk.Text(root)
        text.pack(side="top", fill="x", pady=10)
        text.insert(tk.END, finder.delete_astro_by(variable, value))
        B1 = tk.Button(root, text="Close Delete Message", command=root.destroy)
        B1.pack()
        root.mainloop()

    def find_astro(self, variable, value):
        root = tk.Tk()
        finder = SpaceApi()
        finder.url = StartPage.url
        root.title("you searched for:")
        ast = finder.find_astro_by(variable, value)
        text = tk.Text(root)
        text.pack(side="top", fill="x", pady=10)
        text.insert(tk.END, ast)
        B1 = tk.Button(root, text="Close Search", command=root.destroy)
        B1.pack()

        if type(ast) == Astronaut:
            def save_astronaut():
                Astro.placeholder_astro = ast
                self.saved_label.delete("1.0", "end")
                self.saved_label.insert(tk.END, Astro.placeholder_astro.name)
                Astro.astro_list.append(Astro.placeholder_astro)
                self.saved_len_list_label.configure(text=f"Length of Saved Astronaut List: {len(Astro.astro_list)}")
                self.check_json_list()
                root.destroy()

            B2 = tk.Button(root, text="Save current Astronaut into memory for later statistics",
                           command=lambda: save_astronaut())
            B2.pack()

        root.mainloop()

    def search_astro(self, variable="id", value="", f_mode="single"):
        root = tk.Tk()
        finder = SpaceApi()
        finder.url = StartPage.url
        if f_mode == "all":
            diction = finder.find_all_astro()
        else:
            diction = finder.search_astro_by(variable, value)
        count = tk.IntVar(root, 0)
        key_list = list(diction.keys())

        def slider(n):
            count.set(count.get() + n)
            if count.get() >= len(key_list) or count.get() <= -len(key_list):
                count.set(0)
            text.delete("1.0", "end")
            text.insert(tk.END, diction[key_list[count.get()]])

        root.title("you searched for:")
        text = tk.Text(root, width=200)
        text.insert(tk.END, diction[key_list[count.get()]])
        text.grid(column=0, columnspan=5, row=0, rowspan=15, pady=10)
        B1 = tk.Button(root, text="Close Search", command=root.destroy)
        B1.grid(row=15, column=2)
        B2 = tk.Button(root, text="<- Previous", command=lambda: slider(-1))
        B1.grid(row=15, column=2)
        B3 = tk.Button(root, text="Next ->", command=lambda: slider(1))
        B1.grid(row=15, column=2)
        B2.grid(row=15, column=1)
        B3.grid(row=15, column=3)

        if type(diction[key_list[count.get()]]) == Astronaut:
            def save_astronaut(mode="single"):
                if mode == "single":
                    Astro.placeholder_astro = diction[key_list[count.get()]]
                    self.saved_label.delete("1.0", "end")
                    self.saved_label.insert(tk.END, Astro.placeholder_astro.name)
                    Astro.astro_list.append(Astro.placeholder_astro)
                    self.saved_len_list_label.configure(text=f"Length of Saved Astronaut List: {len(Astro.astro_list)}")
                    slider(1)
                    self.check_json_list()
                else:
                    for i in range(len(key_list)):
                        Astro.placeholder_astro = diction[key_list[i]]
                        Astro.astro_list.append(Astro.placeholder_astro)
                    self.saved_label.delete("1.0", "end")
                    self.saved_label.insert(tk.END, Astro.placeholder_astro.name)
                    self.saved_len_list_label.configure(text=f"Length of Saved Astronaut List: {len(Astro.astro_list)}")
                    self.check_json_list()
                    root.destroy()

            B5 = tk.Button(root, text="Save all Astronauts into memory for later statistics and go Close",
                           command=lambda: save_astronaut("all"))
            B5.grid(row=17, column=1, columnspan=3)

            B4 = tk.Button(root, text="Save current Astronaut into memory for later statistics and go to Next",
                           command=lambda: save_astronaut())
            B4.grid(row=16, column=1, columnspan=3)

        root.mainloop()

    @staticmethod
    def none_converter(st: str):
        if st == "":
            return "None"
        else:
            return st

    def check_astro(self, ast: Astronaut):
        if ast.name == "None" or ast.nationality == "None" or ast.bio == "None" or ast.flights_count == "None" or ast.landings_count == "None" or ast.agency_abbrev == "None":
            messagebox.showinfo(title="Error",
                                message="Insert at least: Name, Nationality, Bio, Flights count, Landings count, Agency abbrev.")
            return False
        else:
            self.__temp_astro = ast
            messagebox.showinfo(title="Success", message="Data was saved correctly!")
            return True

    def create_astro(self):
        root = tk.Tk()
        root.title("Astro settings:")
        a = Astronaut()

        label_name = tk.Label(root, text="1. Insert name")
        txt_name = tk.Text(root, width=30, height=1)
        label_name.grid(row=1, column=0, sticky=tk.W)
        txt_name.grid(row=1, column=1)

        label_birth_date = tk.Label(root, text="2. Insert birth_date")
        txt_birth_date = tk.Text(root, width=30, height=1)
        label_birth_date.grid(row=2, column=0, sticky=tk.W)
        txt_birth_date.grid(row=2, column=1)

        label_death_date = tk.Label(root, text="3. Insert death_date")
        txt_death_date = tk.Text(root, width=30, height=1)
        label_death_date.grid(row=3, column=0, sticky=tk.W)
        txt_death_date.grid(row=3, column=1)

        label_nationality = tk.Label(root, text="4. Insert nationality")
        txt_nationality = tk.Text(root, width=30, height=1)
        label_nationality.grid(row=4, column=0, sticky=tk.W)
        txt_nationality.grid(row=4, column=1)

        label_bio = tk.Label(root, text="5. Insert bio")
        txt_bio = tk.Text(root, width=30, height=1)
        label_bio.grid(row=5, column=0, sticky=tk.W)
        txt_bio.grid(row=5, column=1)

        label_twitter = tk.Label(root, text="6. Insert twitter")
        txt_twitter = tk.Text(root, width=30, height=1)
        label_twitter.grid(row=6, column=0, sticky=tk.W)
        txt_twitter.grid(row=6, column=1)

        label_instagram = tk.Label(root, text="7. Insert instagram")
        txt_instagram = tk.Text(root, width=30, height=1)
        label_instagram.grid(row=7, column=0, sticky=tk.W)
        txt_instagram.grid(row=7, column=1)

        label_wiki = tk.Label(root, text="8. Insert wiki")
        txt_wiki = tk.Text(root, width=30, height=1)
        label_wiki.grid(row=8, column=0, sticky=tk.W)
        txt_wiki.grid(row=8, column=1)

        label_profile_image = tk.Label(root, text="9. Insert profile_image")
        txt_profile_image = tk.Text(root, width=30, height=1)
        label_profile_image.grid(row=9, column=0, sticky=tk.W)
        txt_profile_image.grid(row=9, column=1)

        label_profile_image_thumbnail = tk.Label(root, text="10. Insert profile_image_thumbnail")
        txt_profile_image_thumbnail = tk.Text(root, width=30, height=1)
        label_profile_image_thumbnail.grid(row=10, column=0, sticky=tk.W)
        txt_profile_image_thumbnail.grid(row=10, column=1)

        label_flights_count = tk.Label(root, text="11. Insert flights_count")
        txt_flights_count = tk.Text(root, width=30, height=1)
        label_flights_count.grid(row=11, column=0, sticky=tk.W)
        txt_flights_count.grid(row=11, column=1)

        label_landings_count = tk.Label(root, text="12. Insert landings_count")
        txt_landings_count = tk.Text(root, width=30, height=1)
        label_landings_count.grid(row=12, column=0, sticky=tk.W)
        txt_landings_count.grid(row=12, column=1)

        label_last_flight = tk.Label(root, text="13. Insert last_flight")
        txt_last_flight = tk.Text(root, width=30, height=1)
        label_last_flight.grid(row=13, column=0, sticky=tk.W)
        txt_last_flight.grid(row=13, column=1)

        label_first_flight = tk.Label(root, text="14. Insert first_flight")
        txt_first_flight = tk.Text(root, width=30, height=1)
        label_first_flight.grid(row=14, column=0, sticky=tk.W)
        txt_first_flight.grid(row=14, column=1)

        label_status_name = tk.Label(root, text="15. Insert status_name")
        txt_status_name = tk.Text(root, width=30, height=1)
        label_status_name.grid(row=15, column=0, sticky=tk.W)
        txt_status_name.grid(row=15, column=1)

        label_type_name = tk.Label(root, text="16. Insert type_name")
        txt_type_name = tk.Text(root, width=30, height=1)
        label_type_name.grid(row=16, column=0, sticky=tk.W)
        txt_type_name.grid(row=16, column=1)

        label_agency_name = tk.Label(root, text="17. Insert agency_name")
        txt_agency_name = tk.Text(root, width=30, height=1)
        label_agency_name.grid(row=17, column=0, sticky=tk.W)
        txt_agency_name.grid(row=17, column=1)

        label_agency_type = tk.Label(root, text="18. Insert agency_type")
        txt_agency_type = tk.Text(root, width=30, height=1)
        label_agency_type.grid(row=18, column=0, sticky=tk.W)
        txt_agency_type.grid(row=18, column=1)

        label_agency_country_code = tk.Label(root, text="19. Insert agency_country_code")
        txt_agency_country_code = tk.Text(root, width=30, height=1)
        label_agency_country_code.grid(row=19, column=0, sticky=tk.W)
        txt_agency_country_code.grid(row=19, column=1)

        label_agency_abbrev = tk.Label(root, text="20. Insert agency_abbrev")
        txt_agency_abbrev = tk.Text(root, width=30, height=1)
        label_agency_abbrev.grid(row=20, column=0, sticky=tk.W)
        txt_agency_abbrev.grid(row=20, column=1)

        label_agency_logo_url = tk.Label(root, text="21. Insert agency_logo_url")
        txt_agency_logo_url = tk.Text(root, width=30, height=1)
        label_agency_logo_url.grid(row=21, column=0, sticky=tk.W)
        txt_agency_logo_url.grid(row=21, column=1)

        def get_values():
            a.name = self.none_converter(txt_name.get(1.0, "end-1c"))
            a.birth_date = self.none_converter(txt_birth_date.get(1.0, "end-1c"))
            a.death_date = self.none_converter(txt_death_date.get(1.0, "end-1c"))
            a.nationality = self.none_converter(txt_nationality.get(1.0, "end-1c"))
            a.bio = self.none_converter(txt_bio.get(1.0, "end-1c"))
            a.twitter = self.none_converter(txt_twitter.get(1.0, "end-1c"))
            a.instagram = self.none_converter(txt_instagram.get(1.0, "end-1c"))
            a.wiki = self.none_converter(txt_wiki.get(1.0, "end-1c"))
            a.profile_image = self.none_converter(txt_profile_image.get(1.0, "end-1c"))
            a.profile_image_thumbnail = self.none_converter(txt_profile_image_thumbnail.get(1.0, "end-1c"))
            a.flights_count = self.none_converter(txt_flights_count.get(1.0, "end-1c"))
            a.landings_count = self.none_converter(txt_landings_count.get(1.0, "end-1c"))
            a.last_flight = self.none_converter(txt_last_flight.get(1.0, "end-1c"))
            a.first_flight = self.none_converter(txt_first_flight.get(1.0, "end-1c"))
            a.status_name = self.none_converter(txt_status_name.get(1.0, "end-1c"))
            a.type_name = self.none_converter(txt_type_name.get(1.0, "end-1c"))
            a.agency_name = self.none_converter(txt_agency_name.get(1.0, "end-1c"))
            a.agency_type = self.none_converter(txt_agency_type.get(1.0, "end-1c"))
            a.agency_country_code = self.none_converter(txt_agency_country_code.get(1.0, "end-1c"))
            a.agency_abbrev = self.none_converter(txt_agency_abbrev.get(1.0, "end-1c"))
            a.agency_logo_url = self.none_converter(txt_agency_logo_url.get(1.0, "end-1c"))
            self.check_astro(a)

        text = tk.Label(root, height=1, font=tkfont.Font(family='Arial', size=10, weight="bold"), text="Insert Data:")
        B1 = tk.Button(root, text="Save Data", command=lambda: get_values())

        text.grid(row=0, column=0, pady=10)
        B1.grid(row=0, column=1)
        root.mainloop()

    def post_astro(self):
        if not self.check_astro(self.__temp_astro):
            messagebox.showinfo(title="Error", message="Insert data correctly!")
            return
        else:
            finder = SpaceApi()
            finder.url = StartPage.url
            finder.add_astro(self.__temp_astro)
            messagebox.showinfo(title="Success", message="Entry added to database!")
            self.__temp_astro = Astronaut()


class Lcr(tk.Frame):
    placeholder_launcher = Launcher()
    launcher_list = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.__temp_launcher = Launcher()
        self.saved_label = tk.Text(self, height=1, width=30)
        self.saved_label.insert(tk.END, str(Lcr.placeholder_launcher.full_name))
        label = tk.Label(self, text="This is the Launcher page", font=controller.title_font)
        label.grid(row=0, columnspan=2, column=1, pady=10)
        label1 = tk.Label(self, text="Entities Saved In Temporary Memory:",
                          font=tkfont.Font(family='Arial', size=10, weight="bold"))
        label1.grid(row=6, columnspan=3)
        label2 = tk.Label(self, text="Last Saved Launcher ->")
        label2.grid(row=7, column=0, columnspan=2)
        self.saved_len_list_label = tk.Label(self, text=f"Length of Saved Launcher List: {len(Lcr.launcher_list)}")
        self.saved_len_list_label.grid(row=7, column=3)
        self.saved_label.grid(row=7, column=2)
        button1 = tk.Button(self, text="Clear Entire Temporary List",
                            command=lambda: self.remove_last(True))
        button1.grid(row=6, column=4)
        button2 = tk.Button(self, text="Remove Last Element",
                            command=lambda: self.remove_last(False))
        button2.grid(row=7, column=4)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=0, column=0)
        button3 = tk.Button(self, text="Go to the Statistics page",
                            command=lambda: controller.show_frame("StatLauncher"))
        button3.grid(row=0, column=3)
        button4 = tk.Button(self, text="Get all entries of dataset",
                            command=lambda: self.search_launcher(f_mode="all"))
        button4.grid(row=0, column=4)

        self.folder_label1 = tk.Label(self,
                                      text="If you want to Save a JSON file firstly add data to the Temporary List!!!",
                                      font=tkfont.Font(family='Arial', size=10, weight="bold"))
        self.folder_label = tk.Label(self, text="Save JSON file for Temporary List",
                                     font=tkfont.Font(family='Arial', size=10, weight="bold"))
        self.folder_btn = tk.Button(self, text="Download Folder", command=lambda: self.folder_diag())
        self.path = tk.StringVar()
        self.folder_path_label = tk.Label(self, text=self.path.get())
        self.folder_btn1 = tk.Button(self, text="Save List to File", command=lambda: self.save_json())
        self.after_idle(lambda: self.check_json_list())

        choices = ['id',
                   'flight_proven',
                   'serial_number',
                   'status',
                   'details',
                   'image_url',
                   'flights',
                   'last_launch_date',
                   'first_launch_date',
                   'launcher_config_full_name']

        # Find options:
        label_find = tk.Label(self, text="Find Launcher by (exact value):")
        variable_find = tk.StringVar(self)
        variable_find.set('id')
        find_choice = tk.OptionMenu(self, variable_find, *choices)
        input_find = tk.Text(self, width=30, height=1)
        button_find = tk.Button(self, text="Find",
                                command=lambda: self.find_launcher(variable_find.get(), input_find.get(1.0, "end-1c")))
        label_find.grid(row=1, column=0)
        find_choice.grid(row=1, column=1)
        input_find.grid(row=1, column=2)
        button_find.grid(row=1, column=4)

        # Search options:
        label_search = tk.Label(self, text="Search Launcher by:")
        variable_search = tk.StringVar(self)
        variable_search.set('id')
        search_choice = tk.OptionMenu(self, variable_search, *choices)
        input_search = tk.Text(self, width=30, height=1)
        button_search = tk.Button(self, text="Search",
                                  command=lambda: self.search_launcher(variable=variable_search.get(),
                                                                       value=input_search.get(1.0, "end-1c")))
        label_search.grid(row=2, column=0)
        search_choice.grid(row=2, column=1)
        input_search.grid(row=2, column=2)
        button_search.grid(row=2, column=4)

        # Post options:
        label_post = tk.Label(self, text="Post Launcher:")
        label1_post = tk.Label(self, text="Firstly:")
        label2_post = tk.Label(self, text="Then:")
        button_create_post = tk.Button(self, text="Insert Launcher Data",
                                       command=lambda: self.create_launcher())
        button_send_post = tk.Button(self, text="Post Data",
                                     command=lambda: self.post_launcher())
        label_post.grid(row=3, column=0)
        label1_post.grid(row=3, column=1)
        button_create_post.grid(row=3, column=2)
        label2_post.grid(row=3, column=3)
        button_send_post.grid(row=3, column=4)

        # Delete options:
        label_delete = tk.Label(self, text="Delete Launcher by (exact value):")
        variable_delete = tk.StringVar(self)
        variable_delete.set('id')
        delete_choice = tk.OptionMenu(self, variable_delete, *choices)
        input_delete = tk.Text(self, width=30, height=1)
        button_delete = tk.Button(self, text="Find and Delete",
                                  command=lambda: self.delete_launcher(variable_delete.get(),
                                                                       input_delete.get(1.0, "end-1c")))
        label_delete.grid(row=4, column=0)
        delete_choice.grid(row=4, column=1)
        input_delete.grid(row=4, column=2)
        button_delete.grid(row=4, column=4)

        # Update options:
        label_update = tk.Label(self, text="Update Launcher by:")
        variable_update = tk.StringVar(self)
        variable_update.set('id')
        update_choice = tk.OptionMenu(self, variable_update, *choices)
        input_update = tk.Text(self, width=30, height=1)
        button_create_update = tk.Button(self, text="Insert Launcher Data",
                                         command=lambda: self.create_launcher())
        button_send_update = tk.Button(self, text="Update Data",
                                       command=lambda: self.update_launcher(variable_update.get(),
                                                                            input_update.get(1.0, "end-1c")))
        label_update.grid(row=5, column=0)
        update_choice.grid(row=5, column=1)
        input_update.grid(row=5, column=2)
        button_create_update.grid(row=5, column=3)
        button_send_update.grid(row=5, column=4)

    def save_json(self):
        temp_dict = {}
        for i in range(len(Lcr.launcher_list)):
            temp_dict[i] = Lcr.launcher_list[i].jsonify
        with open(f'{self.path.get()}/launcher_{str(len(Lcr.launcher_list))}.json', 'w') as fp:
            json.dump(temp_dict, fp)
        messagebox.showinfo(title="Success", message=f"File launcher_{str(len(Lcr.launcher_list))}.json saved!")

    def check_json_list(self):
        if len(Lcr.launcher_list) == 0:

            self.folder_label1.grid(row=8, columnspan=4)
            self.folder_label.grid_remove()
            self.folder_path_label.grid_remove()
            self.folder_btn.grid_remove()
            self.folder_btn1.grid_remove()
        else:
            self.folder_label1.grid_remove()
            self.folder_label.grid(row=8, column=0)
            self.path.set("C:/Users/Public/Downloads")
            self.folder_path_label.grid(row=8, column=2)
            self.folder_btn.grid(row=8, column=1)
            self.folder_btn1.grid(row=8, column=3)

    def folder_diag(self):
        folder_path = str(filedialog.askdirectory(initialdir="C:/Users/Public/Downloads"))
        self.path.set(f"{folder_path}")
        self.folder_path_label.configure(text=self.path.get())

    def remove_last(self, value=True):
        if value:
            Lcr.launcher_list = []
            self.saved_label.delete("1.0", "end")
            self.saved_label.insert(tk.END, "None")
            self.saved_len_list_label.configure(text=f"Length of Saved Launcher List: {len(Lcr.launcher_list)}")
            self.check_json_list()
            return
        if len(Lcr.launcher_list) <= 1:
            Lcr.launcher_list = []
            self.saved_label.delete("1.0", "end")
            self.saved_label.insert(tk.END, "None")
            self.saved_len_list_label.configure(text=f"Length of Saved Launcher List: 0")
            self.check_json_list()
        else:
            Lcr.launcher_list.pop()
            self.saved_len_list_label.configure(text=f"Length of Saved Launcher List: {len(Lcr.launcher_list)}")
            self.saved_label.delete("1.0", "end")
            self.saved_label.insert(tk.END, Lcr.launcher_list[-1].full_name)
            self.check_json_list()

    def update_launcher(self, variable, value):
        if not self.check_launcher(self.__temp_launcher):
            messagebox.showinfo(title="Error", message="Insert data correctly!")
            return
        else:
            finder = SpaceApi()
            finder.url = StartPage.url
            finder.update_launcher_by(variable, value, self.__temp_launcher)
            messagebox.showinfo(title="Success", message="Entry added to database!")

    @staticmethod
    def delete_launcher(variable, value):
        root = tk.Tk()
        finder = SpaceApi()
        finder.url = StartPage.url
        root.title("you searched for:")
        text = tk.Text(root)
        text.pack(side="top", fill="x", pady=10)
        text.insert(tk.END, finder.delete_launcher_by(variable, value))
        B1 = tk.Button(root, text="Close Delete Message", command=root.destroy)
        B1.pack()
        root.mainloop()

    def find_launcher(self, variable, value):
        root = tk.Tk()
        finder = SpaceApi()
        finder.url = StartPage.url
        root.title("you searched for:")
        lcr = finder.find_launcher_by(variable, value)
        text = tk.Text(root)
        text.pack(side="top", fill="x", pady=10)
        text.insert(tk.END, lcr)
        B1 = tk.Button(root, text="Close Search", command=root.destroy)
        B1.pack()

        if type(lcr) == Launcher:
            def save_launcher():
                Lcr.placeholder_launcher = lcr
                self.saved_label.delete("1.0", "end")
                self.saved_label.insert(tk.END, Lcr.placeholder_launcher.full_name)
                Lcr.launcher_list.append(Lcr.placeholder_launcher)
                self.saved_len_list_label.configure(text=f"Length of Saved Launcher List: {len(Lcr.launcher_list)}")
                self.check_json_list()
                root.destroy()

            B2 = tk.Button(root, text="Save current Launcher into memory for later statistics",
                           command=lambda: save_launcher())
            B2.pack()

        root.mainloop()

    def search_launcher(self, variable="id", value="", f_mode="single"):
        root = tk.Tk()
        finder = SpaceApi()
        finder.url = StartPage.url
        if f_mode == "all":
            diction = finder.find_all_launcher()
        else:
            diction = finder.search_launcher_by(variable, value)
        count = tk.IntVar(root, 0)
        key_list = list(diction.keys())

        def slider(n):
            count.set(count.get() + n)
            if count.get() >= len(key_list) or count.get() <= -len(key_list):
                count.set(0)
            text.delete("1.0", "end")
            text.insert(tk.END, diction[key_list[count.get()]])

        root.title("you searched for:")
        text = tk.Text(root, width=200)
        text.insert(tk.END, diction[key_list[count.get()]])
        text.grid(column=0, columnspan=5, row=0, rowspan=15, pady=10)
        B1 = tk.Button(root, text="Close Search", command=root.destroy)
        B1.grid(row=15, column=2)
        B2 = tk.Button(root, text="<- Previous", command=lambda: slider(-1))
        B1.grid(row=15, column=2)
        B3 = tk.Button(root, text="Next ->", command=lambda: slider(1))
        B1.grid(row=15, column=2)
        B2.grid(row=15, column=1)
        B3.grid(row=15, column=3)

        if type(diction[key_list[count.get()]]) == Launcher:
            def save_launcher(mode="single"):
                if mode == "single":
                    Lcr.placeholder_launcher = diction[key_list[count.get()]]
                    self.saved_label.delete("1.0", "end")
                    self.saved_label.insert(tk.END, Lcr.placeholder_launcher.full_name)
                    Lcr.launcher_list.append(Lcr.placeholder_launcher)
                    self.saved_len_list_label.configure(text=f"Length of Saved Launcher List: {len(Lcr.launcher_list)}")
                    slider(1)
                    self.check_json_list()
                else:
                    for i in range(len(key_list)):
                        Lcr.placeholder_launcher = diction[key_list[i]]
                        Lcr.launcher_list.append(Lcr.placeholder_launcher)
                    self.saved_label.delete("1.0", "end")
                    self.saved_label.insert(tk.END, Lcr.placeholder_launcher.full_name)
                    self.saved_len_list_label.configure(text=f"Length of Saved Launcher List: {len(Lcr.launcher_list)}")
                    self.check_json_list()
                    root.destroy()

            B5 = tk.Button(root, text="Save all Launchers into memory for later statistics and go Close",
                           command=lambda: save_launcher("all"))
            B5.grid(row=17, column=1, columnspan=3)

            B4 = tk.Button(root, text="Save current Launcher into memory for later statistics and go to Next",
                           command=lambda: save_launcher())
            B4.grid(row=16, column=1, columnspan=3)

        root.mainloop()

    @staticmethod
    def none_converter(st: str):
        if st == "":
            return "None"
        else:
            return st

    def check_launcher(self, lcr: Launcher):
        if lcr.full_name == "None" or lcr.serial_n == "None" or lcr.status == "None" or lcr.description == "None" or lcr.flights_count == "None":
            messagebox.showinfo(title="Error",
                                message="Insert at least: Full Name, Serial N, Description, Flights count, Status.")
            return False
        else:
            self.__temp_launcher = lcr
            messagebox.showinfo(title="Success", message="Data was saved correctly!")

            return True

    def create_launcher(self):
        root = tk.Tk()
        root.title("Launcher settings:")
        lcc = Launcher()

        label_full_name = tk.Label(root, text="1. Insert full_name")
        txt_full_name = tk.Text(root, width=30, height=1)
        label_full_name.grid(row=1, column=0, sticky=tk.W)
        txt_full_name.grid(row=1, column=1)

        label_serial_n = tk.Label(root, text="2. Insert serial_n")
        txt_serial_n = tk.Text(root, width=30, height=1)
        label_serial_n.grid(row=2, column=0, sticky=tk.W)
        txt_serial_n.grid(row=2, column=1)

        label_status = tk.Label(root, text="3. Insert status")
        txt_status = tk.Text(root, width=30, height=1)
        label_status.grid(row=3, column=0, sticky=tk.W)
        txt_status.grid(row=3, column=1)

        label_description = tk.Label(root, text="4. Insert description")
        txt_description = tk.Text(root, width=30, height=1)
        label_description.grid(row=4, column=0, sticky=tk.W)
        txt_description.grid(row=4, column=1)

        label_launcher_image = tk.Label(root, text="5. Insert launcher_image")
        txt_launcher_image = tk.Text(root, width=30, height=1)
        label_launcher_image.grid(row=5, column=0, sticky=tk.W)
        txt_launcher_image.grid(row=5, column=1)

        label_flights_count = tk.Label(root, text="6. Insert flights_count")
        txt_flights_count = tk.Text(root, width=30, height=1)
        label_flights_count.grid(row=6, column=0, sticky=tk.W)
        txt_flights_count.grid(row=6, column=1)

        label_is_flight_proven = tk.Label(root, text="7. Insert is_flight_proven")
        txt_is_flight_proven = tk.Text(root, width=30, height=1)
        label_is_flight_proven.grid(row=7, column=0, sticky=tk.W)
        txt_is_flight_proven.grid(row=7, column=1)

        label_last_launch = tk.Label(root, text="8. Insert last_launch")
        txt_last_launch = tk.Text(root, width=30, height=1)
        label_last_launch.grid(row=8, column=0, sticky=tk.W)
        txt_last_launch.grid(row=8, column=1)

        label_first_launch = tk.Label(root, text="9. Insert first_launch")
        txt_first_launch = tk.Text(root, width=30, height=1)
        label_first_launch.grid(row=9, column=0, sticky=tk.W)
        txt_first_launch.grid(row=9, column=1)

        def get_values():
            lcc.full_name = self.none_converter(txt_full_name.get(1.0, "end-1c"))
            lcc.serial_n = self.none_converter(txt_serial_n.get(1.0, "end-1c"))
            lcc.status = self.none_converter(txt_status.get(1.0, "end-1c"))
            lcc.description = self.none_converter(txt_description.get(1.0, "end-1c"))
            lcc.launcher_image = self.none_converter(txt_launcher_image.get(1.0, "end-1c"))
            lcc.flights_count = self.none_converter(txt_flights_count.get(1.0, "end-1c"))
            lcc.is_flight_proven = self.none_converter(txt_is_flight_proven.get(1.0, "end-1c"))
            lcc.last_launch = self.none_converter(txt_last_launch.get(1.0, "end-1c"))
            lcc.first_launch = self.none_converter(txt_first_launch.get(1.0, "end-1c"))
            self.check_launcher(lcc)

        text = tk.Label(root, height=1, font=tkfont.Font(family='Arial', size=10, weight="bold"), text="Insert Data:")
        B1 = tk.Button(root, text="Save Data", command=lambda: get_values())

        text.grid(row=0, column=0, pady=10)
        B1.grid(row=0, column=1)
        root.mainloop()

    def post_launcher(self):
        if not self.check_launcher(self.__temp_launcher):
            messagebox.showinfo(title="Error", message="Insert data correctly!")
            return
        else:
            finder = SpaceApi()
            finder.url = StartPage.url
            finder.add_launcher(self.__temp_launcher)
            messagebox.showinfo(title="Success", message="Entry added to database!")
            self.__temp_launcher = Launcher()


class Lnc(tk.Frame):
    placeholder_launch = Launch()
    launch_list = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.__temp_launch = Launch()
        self.saved_label = tk.Text(self, height=1, width=30)
        self.saved_label.insert(tk.END, str(Lnc.placeholder_launch.name))
        label = tk.Label(self, text="This is the Launch page", font=controller.title_font)
        label.grid(row=0, columnspan=2, column=1, pady=10)
        label1 = tk.Label(self, text="Entities Saved In Temporary Memory:",
                          font=tkfont.Font(family='Arial', size=10, weight="bold"))
        label1.grid(row=6, columnspan=3)
        label2 = tk.Label(self, text="Last Saved Launch ->")
        label2.grid(row=7, column=0, columnspan=2)
        self.saved_len_list_label = tk.Label(self, text=f"Length of Saved Launch List: {len(Lnc.launch_list)}")
        self.saved_len_list_label.grid(row=7, column=3)
        self.saved_label.grid(row=7, column=2)
        button1 = tk.Button(self, text="Clear Entire Temporary List",
                            command=lambda: self.remove_last(True))
        button1.grid(row=6, column=4)
        button2 = tk.Button(self, text="Remove Last Element",
                            command=lambda: self.remove_last(False))
        button2.grid(row=7, column=4)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=0, column=0)
        button3 = tk.Button(self, text="Go to the Statistics page",
                            command=lambda: controller.show_frame("StatLaunch"))
        button3.grid(row=0, column=3)
        button4 = tk.Button(self, text="Get all entries of dataset",
                            command=lambda: self.search_launch(f_mode="all"))
        button4.grid(row=0, column=4)

        self.folder_label1 = tk.Label(self,
                                      text="If you want to Save a JSON file firstly add data to the Temporary List!!!",
                                      font=tkfont.Font(family='Arial', size=10, weight="bold"))
        self.folder_label = tk.Label(self, text="Save JSON file for Temporary List",
                                     font=tkfont.Font(family='Arial', size=10, weight="bold"))
        self.folder_btn = tk.Button(self, text="Download Folder", command=lambda: self.folder_diag())
        self.path = tk.StringVar()
        self.folder_path_label = tk.Label(self, text=self.path.get())
        self.folder_btn1 = tk.Button(self, text="Save List to File", command=lambda: self.save_json())
        self.after_idle(lambda: self.check_json_list())

        choices = ['id',
                   'name',
                   'net',
                   'window_end',
                   'window_start',
                   'failreason',
                   'image',
                   'infographic',
                   'orbital_launch_attempt_count',
                   'location_launch_attempt_count',
                   'pad_launch_attempt_count',
                   'agency_launch_attempt_count',
                   'orbital_launch_attempt_count_year',
                   'location_launch_attempt_count_year',
                   'pad_launch_attempt_count_year',
                   'agency_launch_attempt_count_year',
                   'status_name',
                   'launch_service_provider_name',
                   'launch_service_provider_type',
                   'rocket_id',
                   'rocket_configuration_full_name',
                   'mission_name',
                   'mission_description',
                   'mission_type',
                   'mission_orbit_name',
                   'pad_wiki_url',
                   'pad_latitude',
                   'pad_longitude',
                   'pad_location_name',
                   'pad_location_country_code']

        # Find options:
        label_find = tk.Label(self, text="Find Launch by (exact value):")
        variable_find = tk.StringVar(self)
        variable_find.set('id')
        find_choice = tk.OptionMenu(self, variable_find, *choices)
        input_find = tk.Text(self, width=30, height=1)
        button_find = tk.Button(self, text="Find",
                                command=lambda: self.find_launch(variable_find.get(), input_find.get(1.0, "end-1c")))
        label_find.grid(row=1, column=0)
        find_choice.grid(row=1, column=1)
        input_find.grid(row=1, column=2)
        button_find.grid(row=1, column=4)

        # Search options:
        label_search = tk.Label(self, text="Search Launch by:")
        variable_search = tk.StringVar(self)
        variable_search.set('id')
        search_choice = tk.OptionMenu(self, variable_search, *choices)
        input_search = tk.Text(self, width=30, height=1)
        button_search = tk.Button(self, text="Search",
                                  command=lambda: self.search_launch(variable=variable_search.get(),
                                                                     value=input_search.get(1.0, "end-1c")))
        label_search.grid(row=2, column=0)
        search_choice.grid(row=2, column=1)
        input_search.grid(row=2, column=2)
        button_search.grid(row=2, column=4)

        # Post options:
        label_post = tk.Label(self, text="Post Launch:")
        label1_post = tk.Label(self, text="Firstly:")
        label2_post = tk.Label(self, text="Then:")
        button_create_post = tk.Button(self, text="Insert Launch Data",
                                       command=lambda: self.create_launch())
        button_send_post = tk.Button(self, text="Post Data",
                                     command=lambda: self.post_launch())
        label_post.grid(row=3, column=0)
        label1_post.grid(row=3, column=1)
        button_create_post.grid(row=3, column=2)
        label2_post.grid(row=3, column=3)
        button_send_post.grid(row=3, column=4)

        # Delete options:
        label_delete = tk.Label(self, text="Delete Launch by (exact value):")
        variable_delete = tk.StringVar(self)
        variable_delete.set('id')
        delete_choice = tk.OptionMenu(self, variable_delete, *choices)
        input_delete = tk.Text(self, width=30, height=1)
        button_delete = tk.Button(self, text="Find and Delete",
                                  command=lambda: self.delete_launch(variable_delete.get(),
                                                                     input_delete.get(1.0, "end-1c")))
        label_delete.grid(row=4, column=0)
        delete_choice.grid(row=4, column=1)
        input_delete.grid(row=4, column=2)
        button_delete.grid(row=4, column=4)

        # Update options:
        label_update = tk.Label(self, text="Update Launch by:")
        variable_update = tk.StringVar(self)
        variable_update.set('id')
        update_choice = tk.OptionMenu(self, variable_update, *choices)
        input_update = tk.Text(self, width=30, height=1)
        button_create_update = tk.Button(self, text="Insert Launch Data",
                                         command=lambda: self.create_launch())
        button_send_update = tk.Button(self, text="Update Data",
                                       command=lambda: self.update_launch(variable_update.get(),
                                                                          input_update.get(1.0, "end-1c")))
        label_update.grid(row=5, column=0)
        update_choice.grid(row=5, column=1)
        input_update.grid(row=5, column=2)
        button_create_update.grid(row=5, column=3)
        button_send_update.grid(row=5, column=4)

    def save_json(self):
        temp_dict = {}
        for i in range(len(Lnc.launch_list)):
            temp_dict[i] = Lnc.launch_list[i].jsonify
        with open(f'{self.path.get()}/launch_{str(len(Lnc.launch_list))}.json', 'w') as fp:
            json.dump(temp_dict, fp)
        messagebox.showinfo(title="Success", message=f"File launch_{str(len(Lnc.launch_list))}.json saved!")

    def check_json_list(self):
        if len(Lnc.launch_list) == 0:

            self.folder_label1.grid(row=8, columnspan=4)
            self.folder_label.grid_remove()
            self.folder_path_label.grid_remove()
            self.folder_btn.grid_remove()
            self.folder_btn1.grid_remove()
        else:
            self.folder_label1.grid_remove()
            self.folder_label.grid(row=8, column=0)
            self.path.set("C:/Users/Public/Downloads")
            self.folder_path_label.grid(row=8, column=2)
            self.folder_btn.grid(row=8, column=1)
            self.folder_btn1.grid(row=8, column=3)

    def folder_diag(self):
        folder_path = str(filedialog.askdirectory(initialdir="C:/Users/Public/Downloads"))
        self.path.set(f"{folder_path}")
        self.folder_path_label.configure(text=self.path.get())

    def remove_last(self, value=True):
        if value:
            Lnc.launch_list = []
            self.saved_label.delete("1.0", "end")
            self.saved_label.insert(tk.END, "None")
            self.saved_len_list_label.configure(text=f"Length of Saved Launch List: {len(Lnc.launch_list)}")
            self.check_json_list()
            return
        if len(Lnc.launch_list) <= 1:
            Lnc.launch_list = []
            self.saved_label.delete("1.0", "end")
            self.saved_label.insert(tk.END, "None")
            self.saved_len_list_label.configure(text=f"Length of Saved Launch List: 0")
            self.check_json_list()
        else:
            Lnc.launch_list.pop()
            self.saved_len_list_label.configure(text=f"Length of Saved Launch List: {len(Lnc.launch_list)}")
            self.saved_label.delete("1.0", "end")
            self.saved_label.insert(tk.END, Lnc.launch_list[-1].name)
            self.check_json_list()

    def update_launch(self, variable, value):
        if not self.check_launch(self.__temp_launch):
            messagebox.showinfo(title="Error", message="Insert data correctly!")
            return
        else:
            finder = SpaceApi()
            finder.url = StartPage.url
            finder.update_launch_by(variable, value, self.__temp_launch)
            messagebox.showinfo(title="Success", message="Entry added to database!")

    @staticmethod
    def delete_launch(variable, value):
        root = tk.Tk()
        finder = SpaceApi()
        finder.url = StartPage.url
        root.title("you searched for:")
        text = tk.Text(root)
        text.pack(side="top", fill="x", pady=10)
        text.insert(tk.END, finder.delete_launch_by(variable, value))
        B1 = tk.Button(root, text="Close Delete Message", command=root.destroy)
        B1.pack()
        root.mainloop()

    def find_launch(self, variable, value):
        root = tk.Tk()
        finder = SpaceApi()
        finder.url = StartPage.url
        root.title("you searched for:")
        lnc = finder.find_launch_by(variable, value)
        text = tk.Text(root)
        text.pack(side="top", fill="x", pady=10)
        text.insert(tk.END, lnc)
        B1 = tk.Button(root, text="Close Search", command=root.destroy)
        B1.pack()

        if type(lnc) == Launch:
            def save_launch():
                Lnc.placeholder_launch = lnc
                self.saved_label.delete("1.0", "end")
                self.saved_label.insert(tk.END, Lnc.placeholder_launch.name)
                Lnc.launch_list.append(Lnc.placeholder_launch)
                self.saved_len_list_label.configure(text=f"Length of Saved Launch List: {len(Lnc.launch_list)}")
                self.check_json_list()
                root.destroy()

            B2 = tk.Button(root, text="Save current Launch into memory for later statistics",
                           command=lambda: save_launch())
            B2.pack()

        root.mainloop()

    def search_launch(self, variable="id", value="", f_mode="single"):
        root = tk.Tk()
        finder = SpaceApi()
        finder.url = StartPage.url
        if f_mode == "all":
            diction = finder.find_all_launch()
        else:
            diction = finder.search_launch_by(variable, value)
        count = tk.IntVar(root, 0)
        key_list = list(diction.keys())

        def slider(n):
            count.set(count.get() + n)
            if count.get() >= len(key_list) or count.get() <= -len(key_list):
                count.set(0)
            text.delete("1.0", "end")
            text.insert(tk.END, diction[key_list[count.get()]])

        root.title("you searched for:")
        text = tk.Text(root, width=200)
        text.insert(tk.END, diction[key_list[count.get()]])
        text.grid(column=0, columnspan=5, row=0, rowspan=15, pady=10)
        B1 = tk.Button(root, text="Close Search", command=root.destroy)
        B1.grid(row=15, column=2)
        B2 = tk.Button(root, text="<- Previous", command=lambda: slider(-1))
        B1.grid(row=15, column=2)
        B3 = tk.Button(root, text="Next ->", command=lambda: slider(1))
        B1.grid(row=15, column=2)
        B2.grid(row=15, column=1)
        B3.grid(row=15, column=3)

        if type(diction[key_list[count.get()]]) == Launch:
            def save_launch(mode="single"):
                if mode == "single":
                    Lnc.placeholder_launch = diction[key_list[count.get()]]
                    self.saved_label.delete("1.0", "end")
                    self.saved_label.insert(tk.END, Lnc.placeholder_launch.name)
                    Lnc.launch_list.append(Lnc.placeholder_launch)
                    self.saved_len_list_label.configure(text=f"Length of Saved Launch List: {len(Lnc.launch_list)}")
                    slider(1)
                    self.check_json_list()
                else:
                    for i in range(len(key_list)):
                        Lnc.placeholder_launch = diction[key_list[i]]
                        Lnc.launch_list.append(Lnc.placeholder_launch)
                    self.saved_label.delete("1.0", "end")
                    self.saved_label.insert(tk.END, Lnc.placeholder_launch.name)
                    self.saved_len_list_label.configure(text=f"Length of Saved Launch List: {len(Lnc.launch_list)}")
                    self.check_json_list()
                    root.destroy()

            B5 = tk.Button(root, text="Save all Launches into memory for later statistics and go Close",
                           command=lambda: save_launch("all"))
            B5.grid(row=17, column=1, columnspan=3)

            B4 = tk.Button(root, text="Save current Launch into memory for later statistics and go to Next",
                           command=lambda: save_launch())
            B4.grid(row=16, column=1, columnspan=3)

        root.mainloop()

    @staticmethod
    def none_converter(st: str):
        if st == "":
            return "None"
        else:
            return st

    def check_launch(self, launch: Launch):
        if launch.name == "None" or launch.net == "None" or launch.status_name == "None" or launch.launch_service_provider_name == "None" or launch.rocket_config_full_name == "None" or launch.mission_description == "None" or launch.pad_location_name == "None":
            messagebox.showinfo(title="Error",
                                message="Insert at least: Name, Net launch time, Status name, Launch service provider name, Rocket full configuration, Mission description, Pad location name.")
            return False
        else:
            self.__temp_launch = launch
            messagebox.showinfo(title="Success", message="Data was saved correctly!")
            return True

    def create_launch(self):
        root = tk.Tk()
        root.title("Launch settings:")
        lccn = Launch()

        label_name = tk.Label(root, text="1. Insert name")
        txt_name = tk.Text(root, width=30, height=1)
        label_name.grid(row=1, column=0, sticky=tk.W)
        txt_name.grid(row=1, column=1)

        label_net = tk.Label(root, text="2. Insert Net time of launch")
        txt_net = tk.Text(root, width=30, height=1)
        label_net.grid(row=2, column=0, sticky=tk.W)
        txt_net.grid(row=2, column=1)

        label_window_end = tk.Label(root, text="3. Insert window_end")
        txt_window_end = tk.Text(root, width=30, height=1)
        label_window_end.grid(row=3, column=0, sticky=tk.W)
        txt_window_end.grid(row=3, column=1)

        label_window_start = tk.Label(root, text="4. Insert window_start")
        txt_window_start = tk.Text(root, width=30, height=1)
        label_window_start.grid(row=4, column=0, sticky=tk.W)
        txt_window_start.grid(row=4, column=1)

        label_fail_reason = tk.Label(root, text="5. Insert fail_reason")
        txt_fail_reason = tk.Text(root, width=30, height=1)
        label_fail_reason.grid(row=5, column=0, sticky=tk.W)
        txt_fail_reason.grid(row=5, column=1)

        label_image = tk.Label(root, text="6. Insert image")
        txt_image = tk.Text(root, width=30, height=1)
        label_image.grid(row=6, column=0, sticky=tk.W)
        txt_image.grid(row=6, column=1)

        label_infographic = tk.Label(root, text="7. Insert infographic")
        txt_infographic = tk.Text(root, width=30, height=1)
        label_infographic.grid(row=7, column=0, sticky=tk.W)
        txt_infographic.grid(row=7, column=1)

        label_orbital_launch_attempt_count = tk.Label(root, text="8. Insert orbital_launch_attempt_count")
        txt_orbital_launch_attempt_count = tk.Text(root, width=30, height=1)
        label_orbital_launch_attempt_count.grid(row=8, column=0, sticky=tk.W)
        txt_orbital_launch_attempt_count.grid(row=8, column=1)

        label_location_launch_attempt_count = tk.Label(root, text="9. Insert location_launch_attempt_count")
        txt_location_launch_attempt_count = tk.Text(root, width=30, height=1)
        label_location_launch_attempt_count.grid(row=9, column=0, sticky=tk.W)
        txt_location_launch_attempt_count.grid(row=9, column=1)

        label_pad_launch_attempt_count = tk.Label(root, text="10. Insert pad_launch_attempt_count")
        txt_pad_launch_attempt_count = tk.Text(root, width=30, height=1)
        label_pad_launch_attempt_count.grid(row=10, column=0, sticky=tk.W)
        txt_pad_launch_attempt_count.grid(row=10, column=1)

        label_agency_launch_attempt_count = tk.Label(root, text="11. Insert agency_launch_attempt_count")
        txt_agency_launch_attempt_count = tk.Text(root, width=30, height=1)
        label_agency_launch_attempt_count.grid(row=11, column=0, sticky=tk.W)
        txt_agency_launch_attempt_count.grid(row=11, column=1)

        label_orbital_launch_attempt_count_year = tk.Label(root, text="12. Insert orbital_launch_attempt_count_year")
        txt_orbital_launch_attempt_count_year = tk.Text(root, width=30, height=1)
        label_orbital_launch_attempt_count_year.grid(row=12, column=0, sticky=tk.W)
        txt_orbital_launch_attempt_count_year.grid(row=12, column=1)

        label_location_launch_attempt_count_year = tk.Label(root, text="13. Insert location_launch_attempt_count_year")
        txt_location_launch_attempt_count_year = tk.Text(root, width=30, height=1)
        label_location_launch_attempt_count_year.grid(row=13, column=0, sticky=tk.W)
        txt_location_launch_attempt_count_year.grid(row=13, column=1)

        label_pad_launch_attempt_count_year = tk.Label(root, text="14. Insert pad_launch_attempt_count_year")
        txt_pad_launch_attempt_count_year = tk.Text(root, width=30, height=1)
        label_pad_launch_attempt_count_year.grid(row=14, column=0, sticky=tk.W)
        txt_pad_launch_attempt_count_year.grid(row=14, column=1)

        label_agency_launch_attempt_count_year = tk.Label(root, text="15. Insert agency_launch_attempt_count_year")
        txt_agency_launch_attempt_count_year = tk.Text(root, width=30, height=1)
        label_agency_launch_attempt_count_year.grid(row=15, column=0, sticky=tk.W)
        txt_agency_launch_attempt_count_year.grid(row=15, column=1)

        label_launch_service_provider_name = tk.Label(root, text="16. Insert launch_service_provider_name")
        txt_launch_service_provider_name = tk.Text(root, width=30, height=1)
        label_launch_service_provider_name.grid(row=16, column=0, sticky=tk.W)
        txt_launch_service_provider_name.grid(row=16, column=1)

        label_status_name = tk.Label(root, text="17. Insert status_name")
        txt_status_name = tk.Text(root, width=30, height=1)
        label_status_name.grid(row=17, column=0, sticky=tk.W)
        txt_status_name.grid(row=17, column=1)

        label_launch_service_provider_type = tk.Label(root, text="18. Insert launch_service_provider_type")
        txt_launch_service_provider_type = tk.Text(root, width=30, height=1)
        label_launch_service_provider_type.grid(row=18, column=0, sticky=tk.W)
        txt_launch_service_provider_type.grid(row=18, column=1)

        label_rocket_id = tk.Label(root, text="19. Insert rocket_id")
        txt_rocket_id = tk.Text(root, width=30, height=1)
        label_rocket_id.grid(row=19, column=0, sticky=tk.W)
        txt_rocket_id.grid(row=19, column=1)

        label_rocket_config_full_name = tk.Label(root, text="20. Insert rocket_config_full_name")
        txt_rocket_config_full_name = tk.Text(root, width=30, height=1)
        label_rocket_config_full_name.grid(row=20, column=0, sticky=tk.W)
        txt_rocket_config_full_name.grid(row=20, column=1)

        label_mission_name = tk.Label(root, text="21. Insert mission_name")
        txt_mission_name = tk.Text(root, width=30, height=1)
        label_mission_name.grid(row=21, column=0, sticky=tk.W)
        txt_mission_name.grid(row=21, column=1)

        label_mission_description = tk.Label(root, text="22. Insert mission_description")
        txt_mission_description = tk.Text(root, width=30, height=1)
        label_mission_description.grid(row=22, column=0, sticky=tk.W)
        txt_mission_description.grid(row=22, column=1)

        label_mission_type = tk.Label(root, text="23. Insert mission_type")
        txt_mission_type = tk.Text(root, width=30, height=1)
        label_mission_type.grid(row=23, column=0, sticky=tk.W)
        txt_mission_type.grid(row=23, column=1)

        label_mission_orbit_name = tk.Label(root, text="24. Insert mission_orbit_name")
        txt_mission_orbit_name = tk.Text(root, width=30, height=1)
        label_mission_orbit_name.grid(row=24, column=0, sticky=tk.W)
        txt_mission_orbit_name.grid(row=24, column=1)

        label_pad_wiki_url = tk.Label(root, text="25. Insert pad_wiki_url")
        txt_pad_wiki_url = tk.Text(root, width=30, height=1)
        label_pad_wiki_url.grid(row=25, column=0, sticky=tk.W)
        txt_pad_wiki_url.grid(row=25, column=1)

        label_pad_latitude = tk.Label(root, text="26. Insert pad_latitude")
        txt_pad_latitude = tk.Text(root, width=30, height=1)
        label_pad_latitude.grid(row=26, column=0, sticky=tk.W)
        txt_pad_latitude.grid(row=26, column=1)

        label_pad_longitude = tk.Label(root, text="27. Insert pad_longitude")
        txt_pad_longitude = tk.Text(root, width=30, height=1)
        label_pad_longitude.grid(row=27, column=0, sticky=tk.W)
        txt_pad_longitude.grid(row=27, column=1)

        label_pad_location_name = tk.Label(root, text="28. Insert pad_location_name")
        txt_pad_location_name = tk.Text(root, width=30, height=1)
        label_pad_location_name.grid(row=28, column=0, sticky=tk.W)
        txt_pad_location_name.grid(row=28, column=1)

        label_pad_location_country_code = tk.Label(root, text="29. Insert pad_location_country_code")
        txt_pad_location_country_code = tk.Text(root, width=30, height=1)
        label_pad_location_country_code.grid(row=29, column=0, sticky=tk.W)
        txt_pad_location_country_code.grid(row=29, column=1)

        def get_values():
            lccn.name = self.none_converter(txt_name.get(1.0, "end-1c"))
            lccn.net = self.none_converter(txt_net.get(1.0, "end-1c"))
            lccn.window_end = self.none_converter(txt_window_end.get(1.0, "end-1c"))
            lccn.window_start = self.none_converter(txt_window_start.get(1.0, "end-1c"))
            lccn.fail_reason = self.none_converter(txt_fail_reason.get(1.0, "end-1c"))
            lccn.image = self.none_converter(txt_image.get(1.0, "end-1c"))
            lccn.infographic = self.none_converter(txt_infographic.get(1.0, "end-1c"))
            lccn.orbital_launch_attempt_count = self.none_converter(txt_orbital_launch_attempt_count.get(1.0, "end-1c"))
            lccn.location_launch_attempt_count = self.none_converter(
                txt_location_launch_attempt_count.get(1.0, "end-1c"))
            lccn.pad_launch_attempt_count = self.none_converter(txt_pad_launch_attempt_count.get(1.0, "end-1c"))
            lccn.agency_launch_attempt_count = self.none_converter(txt_agency_launch_attempt_count.get(1.0, "end-1c"))
            lccn.orbital_launch_attempt_count_year = self.none_converter(
                txt_orbital_launch_attempt_count_year.get(1.0, "end-1c"))
            lccn.location_launch_attempt_count_year = self.none_converter(
                txt_location_launch_attempt_count_year.get(1.0, "end-1c"))
            lccn.pad_launch_attempt_count_year = self.none_converter(
                txt_pad_launch_attempt_count_year.get(1.0, "end-1c"))
            lccn.agency_launch_attempt_count_year = self.none_converter(
                txt_agency_launch_attempt_count_year.get(1.0, "end-1c"))
            lccn.launch_service_provider_name = self.none_converter(txt_launch_service_provider_name.get(1.0, "end-1c"))
            lccn.status_name = self.none_converter(txt_status_name.get(1.0, "end-1c"))
            lccn.launch_service_provider_type = self.none_converter(txt_launch_service_provider_type.get(1.0, "end-1c"))
            lccn.rocket_id = self.none_converter(txt_rocket_id.get(1.0, "end-1c"))
            lccn.rocket_config_full_name = self.none_converter(txt_rocket_config_full_name.get(1.0, "end-1c"))
            lccn.mission_name = self.none_converter(txt_mission_name.get(1.0, "end-1c"))
            lccn.mission_description = self.none_converter(txt_mission_description.get(1.0, "end-1c"))
            lccn.mission_type = self.none_converter(txt_mission_type.get(1.0, "end-1c"))
            lccn.mission_orbit_name = self.none_converter(txt_mission_orbit_name.get(1.0, "end-1c"))
            lccn.pad_wiki_url = self.none_converter(txt_pad_wiki_url.get(1.0, "end-1c"))
            lccn.pad_latitude = self.none_converter(txt_pad_latitude.get(1.0, "end-1c"))
            lccn.pad_longitude = self.none_converter(txt_pad_longitude.get(1.0, "end-1c"))
            lccn.pad_location_name = self.none_converter(txt_pad_location_name.get(1.0, "end-1c"))
            lccn.pad_location_country_code = self.none_converter(txt_pad_location_country_code.get(1.0, "end-1c"))
            self.check_launch(lccn)

        text = tk.Label(root, height=1, font=tkfont.Font(family='Arial', size=10, weight="bold"), text="Insert Data:")
        B1 = tk.Button(root, text="Save Data", command=lambda: get_values())

        text.grid(row=0, column=0, pady=10)
        B1.grid(row=0, column=1)
        root.mainloop()

    def post_launch(self):
        if not self.check_launch(self.__temp_launch):
            messagebox.showinfo(title="Error", message="Insert data correctly!")
            return
        else:
            finder = SpaceApi()
            finder.url = StartPage.url
            finder.add_launch(self.__temp_launch)
            messagebox.showinfo(title="Success", message="Entry added to database!")
            self.__temp_launch = Launch()


class Statistics(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Statistics Tools For:",
                         font=controller.title_font)
        label.grid(columnspan=3, row=0, pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=4, column=1)
        button1 = tk.Button(self, text="Go to the Statistics page for Astronaut",
                            command=lambda: controller.show_frame("StatAstronaut"))
        button1.grid(row=1, column=0)
        button2 = tk.Button(self, text="Go to the Statistics page for Launcher",
                            command=lambda: controller.show_frame("StatLauncher"))
        button2.grid(row=1, column=1)
        button3 = tk.Button(self, text="Go to the Statistics page for Launch",
                            command=lambda: controller.show_frame("StatLaunch"))
        button3.grid(row=1, column=2)


class StatAstronaut(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Astronauts Statistics:",
                         font=controller.title_font)
        label.grid(columnspan=3, row=0, pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=0, column=3)
        choices = ["Sum", "Average", "Maximum", "Minimum", "Standard Deviation"]

        label_age = tk.Label(self, text="Age:")
        variable_age = tk.StringVar(self)
        variable_age.set('Sum')
        age_choice = tk.OptionMenu(self, variable_age, *choices)
        button_age = tk.Button(self, text="Calculate",
                               command=lambda: self.calculate_age(variable_age.get()))
        self.result_age = tk.Label(self, text="Result = 0")
        label_age.grid(row=1, column=0)
        age_choice.grid(row=1, column=1)
        button_age.grid(row=1, column=2)
        self.result_age.grid(row=1, column=3)

        label_flights_count = tk.Label(self, text="Flights Count:")
        variable_flights_count = tk.StringVar(self)
        variable_flights_count.set('Sum')
        flights_count_choice = tk.OptionMenu(self, variable_flights_count, *choices)
        button_flights_count = tk.Button(self, text="Calculate",
                                         command=lambda: self.calculate_flights_count(variable_flights_count.get()))
        self.result_flights_count = tk.Label(self, text="Result = 0")
        label_flights_count.grid(row=2, column=0)
        flights_count_choice.grid(row=2, column=1)
        button_flights_count.grid(row=2, column=2)
        self.result_flights_count.grid(row=2, column=3)

        label_landings_count = tk.Label(self, text="Landings Count:")
        variable_landings_count = tk.StringVar(self)
        variable_landings_count.set('Sum')
        landings_count_choice = tk.OptionMenu(self, variable_landings_count, *choices)
        button_landings_count = tk.Button(self, text="Calculate",
                                          command=lambda: self.calculate_landings_count(variable_landings_count.get()))
        self.result_landings_count = tk.Label(self, text="Result = 0")
        label_landings_count.grid(row=3, column=0)
        landings_count_choice.grid(row=3, column=1)
        button_landings_count.grid(row=3, column=2)
        self.result_landings_count.grid(row=3, column=3)

    def calculate_age(self, mode):
        if len(Astro.astro_list) == 0:
            messagebox.showinfo(title="Error",
                                message="You must first add some Astronauts to your list")
            self.controller.show_frame("Astro")
            return
        value_list = []
        for ast in Astro.astro_list:
            try:
                v = int(ast.age)
            except ValueError:
                v = 0
            value_list.append(v)
        if mode == "Sum":
            self.result_age.configure(text=f"Result = {sum(value_list)}")
        elif mode == "Average":
            self.result_age.configure(text=f"Result = {round(sum(value_list) / len(value_list), 4)}")
        elif mode == "Maximum":
            self.result_age.configure(text=f"Result = {max(value_list)}")
        elif mode == "Minimum":
            self.result_age.configure(text=f"Result = {min(value_list)}")
        else:
            mean = sum(value_list) / len(value_list)
            variance = sum([((x - mean) ** 2) for x in value_list]) / len(value_list)
            res = variance ** 0.5
            self.result_age.configure(text=f"Result = {round(res, 4)}")

    def calculate_flights_count(self, mode):
        if len(Astro.astro_list) == 0:
            messagebox.showinfo(title="Error",
                                message="You must first add some Astronauts to your list")
            self.controller.show_frame("Astro")
            return
        value_list = []
        for ast in Astro.astro_list:
            try:
                v = int(ast.flights_count)
            except ValueError:
                v = 0
            value_list.append(v)
        if mode == "Sum":
            self.result_flights_count.configure(text=f"Result = {sum(value_list)}")
        elif mode == "Average":
            self.result_flights_count.configure(text=f"Result = {round(sum(value_list) / len(value_list), 4)}")
        elif mode == "Maximum":
            self.result_flights_count.configure(text=f"Result = {max(value_list)}")
        elif mode == "Minimum":
            self.result_flights_count.configure(text=f"Result = {min(value_list)}")
        else:
            mean = sum(value_list) / len(value_list)
            variance = sum([((x - mean) ** 2) for x in value_list]) / len(value_list)
            res = variance ** 0.5
            self.result_flights_count.configure(text=f"Result = {round(res, 4)}")

    def calculate_landings_count(self, mode):
        if len(Astro.astro_list) == 0:
            messagebox.showinfo(title="Error",
                                message="You must first add some Astronauts to your list")
            self.controller.show_frame("Astro")
            return
        value_list = []
        for ast in Astro.astro_list:
            try:
                v = int(ast.landings_count)
            except ValueError:
                v = 0
            value_list.append(v)
        if mode == "Sum":
            self.result_landings_count.configure(text=f"Result = {sum(value_list)}")
        elif mode == "Average":
            self.result_landings_count.configure(text=f"Result = {round(sum(value_list) / len(value_list), 4)}")
        elif mode == "Maximum":
            self.result_landings_count.configure(text=f"Result = {max(value_list)}")
        elif mode == "Minimum":
            self.result_landings_count.configure(text=f"Result = {min(value_list)}")
        else:
            mean = sum(value_list) / len(value_list)
            variance = sum([((x - mean) ** 2) for x in value_list]) / len(value_list)
            res = variance ** 0.5
            self.result_landings_count.configure(text=f"Result = {round(res, 4)}")


class StatLauncher(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Launcher Statistics:",
                         font=controller.title_font)
        label.grid(columnspan=3, row=0, pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=0, column=3)
        choices = ["Sum", "Average", "Maximum", "Minimum", "Standard Deviation"]

        label_flights_count = tk.Label(self, text="Flights Count:")
        variable_flights_count = tk.StringVar(self)
        variable_flights_count.set('Sum')
        flights_count_choice = tk.OptionMenu(self, variable_flights_count, *choices)
        button_flights_count = tk.Button(self, text="Calculate",
                                         command=lambda: self.calculate_flights_count(variable_flights_count.get()))
        self.result_flights_count = tk.Label(self, text="Result = 0")
        label_flights_count.grid(row=1, column=0)
        flights_count_choice.grid(row=1, column=1)
        button_flights_count.grid(row=1, column=2)
        self.result_flights_count.grid(row=1, column=3)

    def calculate_flights_count(self, mode):
        if len(Lcr.launcher_list) == 0:
            messagebox.showinfo(title="Error",
                                message="You must first add some Launchers to your list")
            self.controller.show_frame("Lcr")
            return
        value_list = []
        for ast in Lcr.launcher_list:
            try:
                v = int(ast.flights_count)
            except ValueError:
                v = 0
            value_list.append(v)
        if mode == "Sum":
            self.result_flights_count.configure(text=f"Result = {sum(value_list)}")
        elif mode == "Average":
            self.result_flights_count.configure(text=f"Result = {round(sum(value_list) / len(value_list), 4)}")
        elif mode == "Maximum":
            self.result_flights_count.configure(text=f"Result = {max(value_list)}")
        elif mode == "Minimum":
            self.result_flights_count.configure(text=f"Result = {min(value_list)}")
        else:
            mean = sum(value_list) / len(value_list)
            variance = sum([((x - mean) ** 2) for x in value_list]) / len(value_list)
            res = variance ** 0.5
            self.result_flights_count.configure(text=f"Result = {round(res, 4)}")


class StatLaunch(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Launch Statistics:",
                         font=controller.title_font)
        label.grid(columnspan=3, row=0, pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=0, column=3)
        choices = ["Sum", "Average", "Maximum", "Minimum", "Standard Deviation"]

        label_orbital_launch_attempt_count_year = tk.Label(self, text="Yearly Orbital Launch Attempt Count:")
        variable_orbital_launch_attempt_count_year = tk.StringVar(self)
        variable_orbital_launch_attempt_count_year.set('Sum')
        orbital_launch_attempt_count_year_choice = tk.OptionMenu(self, variable_orbital_launch_attempt_count_year,
                                                                 *choices)
        button_orbital_launch_attempt_count_year = tk.Button(self, text="Calculate",
                                                             command=lambda: self.calculate_orbital_launch_attempt_count_year(
                                                                 variable_orbital_launch_attempt_count_year.get()))
        self.result_orbital_launch_attempt_count_year = tk.Label(self, text="Result = 0")
        label_orbital_launch_attempt_count_year.grid(row=1, column=0)
        orbital_launch_attempt_count_year_choice.grid(row=1, column=1)
        button_orbital_launch_attempt_count_year.grid(row=1, column=2)
        self.result_orbital_launch_attempt_count_year.grid(row=1, column=3)

        label_location_launch_attempt_count_year = tk.Label(self, text="Yearly Location Launch Attempt Count:")
        variable_location_launch_attempt_count_year = tk.StringVar(self)
        variable_location_launch_attempt_count_year.set('Sum')
        location_launch_attempt_count_year_choice = tk.OptionMenu(self, variable_location_launch_attempt_count_year,
                                                                  *choices)
        button_location_launch_attempt_count_year = tk.Button(self, text="Calculate",
                                                              command=lambda: self.calculate_location_launch_attempt_count_year(
                                                                  variable_location_launch_attempt_count_year.get()))
        self.result_location_launch_attempt_count_year = tk.Label(self, text="Result = 0")
        label_location_launch_attempt_count_year.grid(row=2, column=0)
        location_launch_attempt_count_year_choice.grid(row=2, column=1)
        button_location_launch_attempt_count_year.grid(row=2, column=2)
        self.result_location_launch_attempt_count_year.grid(row=2, column=3)

        label_pad_launch_attempt_count_year = tk.Label(self, text="Yearly Pad Launch Attempt Count:")
        variable_pad_launch_attempt_count_year = tk.StringVar(self)
        variable_pad_launch_attempt_count_year.set('Sum')
        pad_launch_attempt_count_year_choice = tk.OptionMenu(self, variable_pad_launch_attempt_count_year,
                                                             *choices)
        button_pad_launch_attempt_count_year = tk.Button(self, text="Calculate",
                                                         command=lambda: self.calculate_pad_launch_attempt_count_year(
                                                             variable_pad_launch_attempt_count_year.get()))
        self.result_pad_launch_attempt_count_year = tk.Label(self, text="Result = 0")
        label_pad_launch_attempt_count_year.grid(row=3, column=0)
        pad_launch_attempt_count_year_choice.grid(row=3, column=1)
        button_pad_launch_attempt_count_year.grid(row=3, column=2)
        self.result_pad_launch_attempt_count_year.grid(row=3, column=3)

        label_agency_launch_attempt_count_year = tk.Label(self, text="Yearly Agency Launch Attempt Count:")
        variable_agency_launch_attempt_count_year = tk.StringVar(self)
        variable_agency_launch_attempt_count_year.set('Sum')
        agency_launch_attempt_count_year_choice = tk.OptionMenu(self, variable_agency_launch_attempt_count_year,
                                                                *choices)
        button_agency_launch_attempt_count_year = tk.Button(self, text="Calculate",
                                                            command=lambda: self.calculate_agency_launch_attempt_count_year(
                                                                variable_agency_launch_attempt_count_year.get()))
        self.result_agency_launch_attempt_count_year = tk.Label(self, text="Result = 0")
        label_agency_launch_attempt_count_year.grid(row=4, column=0)
        agency_launch_attempt_count_year_choice.grid(row=4, column=1)
        button_agency_launch_attempt_count_year.grid(row=4, column=2)
        self.result_agency_launch_attempt_count_year.grid(row=4, column=3)

    def calculate_orbital_launch_attempt_count_year(self, mode):
        if len(Lnc.launch_list) == 0:
            messagebox.showinfo(title="Error",
                                message="You must first add some Launches to your list")
            self.controller.show_frame("Lnc")
            return
        value_list = []
        for ast in Lnc.launch_list:
            try:
                v = int(ast.orbital_launch_attempt_count_year)
            except ValueError:
                v = 0
            value_list.append(v)
        if mode == "Sum":
            self.result_orbital_launch_attempt_count_year.configure(text=f"Result = {sum(value_list)}")
        elif mode == "Average":
            self.result_orbital_launch_attempt_count_year.configure(
                text=f"Result = {round(sum(value_list) / len(value_list), 4)}")
        elif mode == "Maximum":
            self.result_orbital_launch_attempt_count_year.configure(text=f"Result = {max(value_list)}")
        elif mode == "Minimum":
            self.result_orbital_launch_attempt_count_year.configure(text=f"Result = {min(value_list)}")
        else:
            mean = sum(value_list) / len(value_list)
            variance = sum([((x - mean) ** 2) for x in value_list]) / len(value_list)
            res = variance ** 0.5
            self.result_orbital_launch_attempt_count_year.configure(text=f"Result = {round(res, 4)}")

    def calculate_location_launch_attempt_count_year(self, mode):
        if len(Lnc.launch_list) == 0:
            messagebox.showinfo(title="Error",
                                message="You must first add some Launches to your list")
            self.controller.show_frame("Lnc")
            return
        value_list = []
        for ast in Lnc.launch_list:
            try:
                v = int(ast.location_launch_attempt_count_year)
            except ValueError:
                v = 0
            value_list.append(v)
        if mode == "Sum":
            self.result_location_launch_attempt_count_year.configure(text=f"Result = {sum(value_list)}")
        elif mode == "Average":
            self.result_location_launch_attempt_count_year.configure(
                text=f"Result = {round(sum(value_list) / len(value_list), 4)}")
        elif mode == "Maximum":
            self.result_location_launch_attempt_count_year.configure(text=f"Result = {max(value_list)}")
        elif mode == "Minimum":
            self.result_location_launch_attempt_count_year.configure(text=f"Result = {min(value_list)}")
        else:
            mean = sum(value_list) / len(value_list)
            variance = sum([((x - mean) ** 2) for x in value_list]) / len(value_list)
            res = variance ** 0.5
            self.result_location_launch_attempt_count_year.configure(text=f"Result = {round(res, 4)}")

    def calculate_pad_launch_attempt_count_year(self, mode):
        if len(Lnc.launch_list) == 0:
            messagebox.showinfo(title="Error",
                                message="You must first add some Launches to your list")
            self.controller.show_frame("Lnc")
            return
        value_list = []
        for ast in Lnc.launch_list:
            try:
                v = int(ast.pad_launch_attempt_count_year)
            except ValueError:
                v = 0
            value_list.append(v)
        if mode == "Sum":
            self.result_pad_launch_attempt_count_year.configure(text=f"Result = {sum(value_list)}")
        elif mode == "Average":
            self.result_pad_launch_attempt_count_year.configure(
                text=f"Result = {round(sum(value_list) / len(value_list), 4)}")
        elif mode == "Maximum":
            self.result_pad_launch_attempt_count_year.configure(text=f"Result = {max(value_list)}")
        elif mode == "Minimum":
            self.result_pad_launch_attempt_count_year.configure(text=f"Result = {min(value_list)}")
        else:
            mean = sum(value_list) / len(value_list)
            variance = sum([((x - mean) ** 2) for x in value_list]) / len(value_list)
            res = variance ** 0.5
            self.result_pad_launch_attempt_count_year.configure(text=f"Result = {round(res, 4)}")

    def calculate_agency_launch_attempt_count_year(self, mode):
        if len(Lnc.launch_list) == 0:
            messagebox.showinfo(title="Error",
                                message="You must first add some Launches to your list")
            self.controller.show_frame("Lnc")
            return
        value_list = []
        for ast in Lnc.launch_list:
            try:
                v = int(ast.agency_launch_attempt_count_year)
            except ValueError:
                v = 0
            value_list.append(v)
        if mode == "Sum":
            self.result_agency_launch_attempt_count_year.configure(text=f"Result = {sum(value_list)}")
        elif mode == "Average":
            self.result_agency_launch_attempt_count_year.configure(
                text=f"Result = {round(sum(value_list) / len(value_list), 4)}")
        elif mode == "Maximum":
            self.result_agency_launch_attempt_count_year.configure(text=f"Result = {max(value_list)}")
        elif mode == "Minimum":
            self.result_agency_launch_attempt_count_year.configure(text=f"Result = {min(value_list)}")
        else:
            mean = sum(value_list) / len(value_list)
            variance = sum([((x - mean) ** 2) for x in value_list]) / len(value_list)
            res = variance ** 0.5
            self.result_agency_launch_attempt_count_year.configure(text=f"Result = {round(res, 4)}")


if __name__ == "__main__":
    app = SpaceApp()
    app.mainloop()
