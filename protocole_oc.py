from tkinter import *
from tkinter import ttk,messagebox
import pymysql
from pymysql import cursors





class Oc:
    def __init__(self,root):
        self.root = root
        self.root.title("Protocole accouchement OC")
        self.root.geometry("1220x690+50+10")
        self.root.resizable(width='False',height='False')
        
        
        frame_oc = Frame(self.root,bg='#7a1f5c')
        frame_oc.place(x=0,y=0,width=1220,height=690)
        
        #formulaire oc ------------------------------------------
        identite = LabelFrame(frame_oc,bg='#7a1f5c',font=("Arial",12),bd=0)
        dateoc = Label(identite,text="Date",font=("Arial",11),bg='#7a1f5c',fg='white')
        dateoc.grid(row=0,column=0)
        self.champ_dateoc = Entry(identite)
        self.champ_dateoc.grid(row=0,column=1)
        heureoc = Label(identite,text="Heure",font=("Arial",11),bg='#7a1f5c',fg='white')
        heureoc.grid(row=0,column=2)
        self.champ_heureoc = Entry(identite)
        self.champ_heureoc.grid(row=0,column=3)
        nom = Label(identite,text="Nom et Prenom",font=("Arial",11),bg='#7a1f5c',fg='white')
        nom.grid(row=2,column=0)
        self.champ_nom = Entry(identite)
        self.champ_nom.grid(row=2,column=1)
        age = Label(identite,text="Age",font=("Arial",11),bg='#7a1f5c',fg='white')
        age.grid(row=2,column=2)
        self.champ_age = Entry(identite)
        self.champ_age.grid(row=2,column=3)
        indication = Label(identite,text="Indication et diagnostic",font=("Arial",11),bg='#7a1f5c',fg='white')
        indication.grid(row=2,column=4)
        self.champ_indication = Entry(identite,width=100)
        self.champ_indication.grid(row=2,column=5)
        anesthesie = Label(identite,text="Type d'anesthesie",font=("Arial",11),bg='#7a1f5c',fg='white')
        anesthesie.grid(row=4,column=0)
        self.champ_anesthesie = ttk.Combobox(identite)
        self.champ_anesthesie["values"]=("ag","alr","l")
        self.champ_anesthesie.current(0)
        self.champ_anesthesie.grid(row=4,column=1)
        identite.grid(sticky='nw',padx=20,pady=10)
        
        intervention = LabelFrame(frame_oc,text="Intervention",labelanchor='nw',bg='#7a1f5c',font=("Arial",12),bd=0)
        self.champ_intervention = Entry(intervention,width=190)
        self.champ_intervention.grid(row=0)
        intervention.grid(sticky='wn',padx=20,pady=20,ipadx=20,ipady=10)
        
        parametre = LabelFrame(frame_oc,bg='#7a1f5c',font=("Arial",12),bd=0)
        ta = Label(parametre,text="TA",font=("Arial",11),bg='#7a1f5c',fg='white')
        ta.grid(row=0,column=0)
        self.champ_ta = Entry(parametre)
        self.champ_ta.grid(row=0,column=1)
        fc = Label(parametre,text="FC",font=("Arial",11),bg='#7a1f5c',fg='white')
        fc.grid(row=0,column=2)
        self.champ_fc = Entry(parametre)
        self.champ_fc.grid(row=0,column=3)
        diurese = Label(parametre,text="Diiurese",font=("Arial",11),bg='#7a1f5c',fg='white')
        diurese.grid(row=0,column=4)
        self.champ_diurese = Entry(parametre)
        self.champ_diurese.grid(row=0,column=5)
        saignement = Label(parametre,text="Saignement",font=("Arial",11),bg='#7a1f5c',fg='white')
        saignement.grid(row=0,column=6)
        self.champ_saignement = Entry(parametre)
        self.champ_saignement.grid(row=0,column=7)
        drain = Label(parametre,text="Drain",font=("Arial",11),bg='#7a1f5c',fg='white')
        drain.grid(row=0,column=8)
        self.champ_drain = Entry(parametre)
        self.champ_drain.grid(row=0,column=9)
        check_list = Label(parametre,text="Check list",font=("Arial",11),bg='#7a1f5c',fg='white')
        check_list.grid(row=0,column=10)
        self.champ_check_list = ttk.Combobox(parametre,state='readonly')
        self.champ_check_list["values"]=("oui","non")
        self.champ_check_list.current(0)
        self.champ_check_list.grid(row=0,column=11)
        parametre.grid(sticky='w',padx=20,pady=10)
        
        cat = LabelFrame(frame_oc,text="CAT post operatoire",labelanchor='nw',bg='#7a1f5c',font=("Arial",12),bd=0)
        self.champ_cat = Entry(cat,width=190)
        self.champ_cat.grid()
        cat.grid(sticky='ws',padx=20,pady=10,ipadx=10,ipady=5)
        
        operateur = LabelFrame(frame_oc,bg='#7a1f5c',font=("Arial",12),bd=0)
        nom_operateur = Label(operateur,text="Nom de l'operateur/Aide",font=("Arial",11),bg='#7a1f5c',fg='white')
        nom_operateur.grid(row=0,column=0)
        self.champ_nom_operateur = Entry(operateur,width=100)
        self.champ_nom_operateur.grid(row=0,column=1)
        nom_anesth_inf = Label(operateur,text="Nom de l'Anesthesiste/infirmier de bloc",font=("Arial",11),bg='#7a1f5c',fg='white')
        nom_anesth_inf.grid(row=2,column=0)
        self.champ_anesth_inf = Entry(operateur,width=100)
        self.champ_anesth_inf.grid(row=2,column=1)
        operateur.grid(sticky='sw',padx=20,pady=10)
        
        valider_boutton = Button(frame_oc,text="Enregistrer",command=self.ajout_oc,font=("Arial",11),bg='white',fg='#7a1f5c')
        valider_boutton.grid(sticky='s',padx=20,pady=10)



    def ajout_oc(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="magesti")
        cur = con.cursor() 
        cur.execute("insert into oc (date_oc,heure,nom,age,indication,anesthesie,intervention,ta,fc,diurese,saignement,drain,lists,cat,operateur,infirmier) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.champ_dateoc.get(),
                        self.champ_heureoc.get(),
                        self.champ_nom.get(),
                        self.champ_age.get(),
                        self.champ_indication.get(),
                        self.champ_anesthesie.get(),
                        self.champ_intervention.get(),
                        self.champ_ta.get(),
                        self.champ_fc.get(),
                        self.champ_diurese.get(),
                        self.champ_saignement.get(),
                        self.champ_drain.get(),
                        self.champ_check_list.get(),
                        self.champ_cat.get(),
                        self.champ_nom_operateur.get(),
                        self.champ_anesth_inf.get()
                     ))   
        con.commit()
        self.reinitialiser()
        con.close()  
        messagebox.showinfo("Succés","enregistrée avec succé")


    def reinitialiser(self):
        self.champ_dateoc.delete(0,END),
        self.champ_heureoc.delete(0,END),
        self.champ_nom.delete(0,END),
        self.champ_age.delete(0,END),
        self.champ_indication.delete(0,END),
        self.champ_anesthesie.delete(0,END),
        self.champ_intervention.delete(0,END),
        self.champ_ta.delete(0,END),
        self.champ_fc.delete(0,END),
        self.champ_diurese.delete(0,END),
        self.champ_saignement.delete(0,END),
        self.champ_drain.delete(0,END),
        self.champ_check_list.delete(0,END),
        self.champ_cat.delete(0,END),
        self.champ_nom_operateur.delete(0,END),
        self.champ_anesth_inf.delete(0,END)   


#affichage -----------------------
root = Tk()
obj = Oc(root) 
root.mainloop()           