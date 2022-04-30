from tkinter import *
from tkinter import ttk,messagebox
import pymysql
import os

class Formulaire_log:
    def __init__(self,root):
        self.root = root
        self.root.title("Nouvelle Utilisateur")
        self.root.geometry("700x300+400+190")
        self.root.resizable(width='False',height='False')
        
        #champ du formulaire-----------------------------------
        
        frame_registre_formulaire = Frame(self.root,bg='#7a1f5c')
        frame_registre_formulaire.place(x=0,y=0,width=700,height=300)
        
        title_registre = Label(frame_registre_formulaire,text="Créer un compte",font=("Courrier", 20), bg='#7a1f5c',fg='white').place(x=50,y=30)

        utilisateur = Label(frame_registre_formulaire,text="Utilisateur",font=("Courrier", 10),bg='#7a1f5c',fg='white').place(x=120,y=90)
        self.champ_utilisateur = Entry(frame_registre_formulaire,font=("Courrier", 10))
        self.champ_utilisateur.place(x=120,y=110)
        
        passe = Label(frame_registre_formulaire,text="Mot de Passe",font=("Courrier", 10),bg='#7a1f5c',fg='white').place(x=120,y=130)
        self.champ_passe = Entry(frame_registre_formulaire,font=("Courrier", 10),show="*")
        self.champ_passe.place(x=120,y=150)
        
        confirm_passe = Label(frame_registre_formulaire,text="Confirmer mot de passe",font=("Courrier", 10),bg='#7a1f5c',fg='white').place(x=120,y=170)
        self.champ_confirm_passe = Entry(frame_registre_formulaire,font=("Courrier", 10),show="*")
        self.champ_confirm_passe.place(x=120,y=190)
        
        valider = Button(frame_registre_formulaire,text="Créer",cursor='hand2',command=self.creer,font=("Courrier", 15),bg='#d049a3',fg='white').place(x=480,y=90,width=140)
        conn = Button(frame_registre_formulaire,text="Se connecter",cursor='hand2',command=self.fenetre_login, font=("Courrier", 15),bg='#009900',fg='white').place(x=480,y=160,width=140)
        
        
    def creer(self):
        if self.champ_utilisateur.get()=="" or self.champ_passe.get()=="" or self.champ_confirm_passe.get()=="":
            messagebox.showerror("Erreur","Veillez remplir les champs",parent=self.root)
        elif self.champ_passe.get()!=self.champ_confirm_passe.get():
            messagebox.showerror("Erreur","Le mot de passe n'est pas identique",parent=self.root)   
        else:
            try:
                con = pymysql.connect(host="localhost",user="root",password="",database="magesti")
                cur = con.cursor()
                cur.execute("select * from utilisateur where user=%s",self.champ_utilisateur.get())
                row = cur.fetchone()
                
                if row!=None:
                    messagebox.showerror("Erreur","Utilisateur deja inscrit",parent=self.root)
                else:
                    cur.execute("insert into utilisateur (user, passe) values(%s,%s)",
                                    (
                                        self.champ_utilisateur.get(),
                                        self.champ_passe.get()
                                    )
                                ) 
                    messagebox.showinfo("Success","Votre compte a été bien crée",parent=self.root)  
            
                con.commit()
                self.reinitialiser()
                con.close()             
            except Exception as es:
                messagebox.showerror("Erreur",f"Erreur de connexion: {str(es)}",parent=self.root)
    def reinitialiser(self):
        self.champ_utilisateur.delete(0,END)
        self.champ_passe.delete(0,END)
        self.champ_confirm_passe.delete(0,END) 
        
        
    def fenetre_login(self):
        self.root.destroy()
        import login            
                
            



#affichage -----------------------
root = Tk()
obj = Formulaire_log(root) 
root.mainloop()   