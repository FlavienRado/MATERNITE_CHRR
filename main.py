from tkinter import *



class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("MAGESTI")
        self.screen_x = self.window.winfo_screenwidth()
        self.screen_y = self.window.winfo_screenheight()
        self.window_x = 700
        self.window_y = 300
        self.pos_x = (self.screen_x//2)-(self.window_x//2)
        self.pos_y = (self.screen_y//2)-(self.window_y//2)
        geo=f"{self.window_x}x{self.window_y}+{self.pos_x//2}+{self.pos_y//2}"
        self.window.geometry(geo)
        self.window.resizable(width='False', height='False')
        self.window.iconbitmap("")
        self.window.config(background='#7a1f5c')

        # initialization des composants
        self.frame = Frame(self.window, bg='#7a1f5c')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.create_button()

    def create_title(self):
        label_title = Label(self.frame, text="Bienvenue sur l'application MAGESTI", font=("Courrier", 30), bg='#7a1f5c',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, text="c'est une application pour gérer les dossiers des patientes;dévélopper par RAKOTONDRANIVO R Flavien", font=("Courrier", 10), bg='#7a1f5c',
                               fg='white')
        label_subtitle.pack()

    def create_button(self):
        start_button = Button(self.frame, text="Demarrer", font=("Courrier", 20), bg='white', fg='#7a1f5c',
                           command=self.page_login)
        start_button.pack(pady=25, fill=X)

    def page_login(self):
        self.window.destroy()
        import registre_login
    


# afficher
app = MyApp()
app.window.mainloop()
