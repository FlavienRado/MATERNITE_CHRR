from tkinter import *
from tkinter import ttk,messagebox
import pymysql


class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("500x200+500+250")
        self.root.resizable(width='False',height='False')
        self.root.focus_force()
        
        
        frame_login = Frame(self.root,bg='#7a1f5c')
        frame_login.place(x=0,y=0,width=500,height=200)
        
        title_login = Label(frame_login,text="Connexion",font=("Courrier", 20), bg='#7a1f5c',fg='white').place(x=30,y=10)

        utilisateur = Label(frame_login,text="Utilisateur",font=("Courrier", 10),bg='#7a1f5c',fg='white').place(x=90,y=40)
        self.champ_utilisateur = Entry(frame_login,font=("Courrier", 10))
        self.champ_utilisateur.place(x=90,y=60)
        
        passe = Label(frame_login,text="Mot de Passe",font=("Courrier", 10),bg='#7a1f5c',fg='white').place(x=90,y=80)
        self.champ_passe = Entry(frame_login,font=("Courrier", 10),show="*")
        self.champ_passe.place(x=90,y=100)
        
        valider = Button(frame_login,text="valider ",cursor='hand2',command=self.connexion, font=("Courrier", 15),bg='#009900',bd=0,fg='white').place(x=340,y=60)
        conn_creer = Button(frame_login,text="Créer un compte ",cursor='hand2',command=self.fenetre_registre_login,font=("Courrier", 10),bg='#7a1f5c',bd=0,fg='black').place(x=340,y=120)

    
    def connexion(self):
        if self.champ_utilisateur.get()=="" or self.champ_passe.get()=="":
            messagebox.showerror("Erreur","Veillez remplir les champs",parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost",user="root",password="",database="magesti")
                cur = con.cursor()
                cur.execute("select * from utilisateur where user=%s and passe=%s",(self.champ_utilisateur.get(), self.champ_passe.get()))
                row = cur.fetchone()
                
                if row == None:
                    messagebox.showerror("Erreur","Utilisateur ou mot de passe invalide",parent=self.root)
                else:
                    messagebox.showinfo("Success","Bienvenue sur MAGESTI",parent=self.root)
                    self.reiniti_champ_login()
                    self.root.destroy()
                    import patiente  
                    con.close()             
            except Exception as es:
                messagebox.showerror("Erreur",f"Erreur de connexion: {str(es)}",parent=self.root)    
    
    
    def reiniti_champ_login(self):
        self.champ_utilisateur.delete(0,END)
        self.champ_passe.delete(0,END) 
        
    
    def fenetre_registre_login(self):
        self.root.destroy()
        import registre_login
               







#affichage -----------------------
root = Tk()
obj = Login(root) 
root.mainloop()       