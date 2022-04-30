from tkinter import *
from tkinter import ttk,messagebox
import pymysql
from pymysql import cursors







class Listes:
    def __init__(self,root):
        self.root = root
        self.root.title("LIste des Patientes")
        self.root.geometry("1220x690+50+10")
        self.root.resizable(width='False',height='False')
        
        
        frame_liste = Frame(self.root,bg='#7a1f5c')
        frame_liste.place(x=0,y=0,width=1220,height=690)

        
        #recherche dans listes---------------------------------------------------------------------------------
        
        liste_table = Frame(frame_liste,bg='#da71b7',relief=GROOVE)
        liste_table.place(x=10,y=10,width=1200,height=500)
        
        recherche_resultat = Label(liste_table,text="rechercher par:",font=("Arial",11,"bold"),bg='#da71b7')
        recherche_resultat.place(x=0,y=0)
        self.rech = ttk.Combobox(liste_table,state='readonly')
        self.rech["values"]=("nom","age","date_entre")
        self.rech.place(x=120,y=2,width=100,height=20)
        
        self.rech_text = Entry(liste_table,font=("Arial",11,))
        self.rech_text.place(x=230,y=2,width=220,height=20)
        
        rech_btn = Button(liste_table,text="Rechercher",cursor='hand2',command=self.rech_par,font=("Courrier", 7,"bold"),bg='#99e600',fg='black',bd=5,relief=RAISED).place(x=460,y=2,width=90)
        affiche_btn = Button(liste_table,text="Afficher Tous",cursor='hand2',command="",font=("Courrier", 7,"bold"),bg='#c4ff4d',fg='black',bd=5).place(x=560,y=2,width=110)
        
        
        #affichage du listes----------------------------------------------------------------------------------------
        result_frame = Frame(liste_table,bd=6,relief=GROOVE,bg='#e59acc')
        result_frame.place(x=0,y=50,width=1200,height=450)
        
        scroll_y = Scrollbar(result_frame,orient=VERTICAL)
        self.table_result = ttk.Treeview(result_frame,columns=("num_enrg","num_service","date_entre","heure","num_salle","nom"),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        self.table_result.heading("num_enrg",text="numero d'enregistrement")
        self.table_result.heading("num_service",text="numero dans service")
        self.table_result.heading("date_entre",text="date entrée")
        self.table_result.heading("heure",text="heure")
        self.table_result.heading("num_salle",text="numero salle/lit")
        self.table_result.heading("nom",text="nom")
        
        
        self.table_result.column("num_enrg",width=160)
        self.table_result.column("num_service",width=160)
        self.table_result.column("date_entre",width=150)
        self.table_result.column("heure",width=150)
        self.table_result.column("num_salle",width=140)
        self.table_result.column("nom",width=400)
        
        self.table_result["show"]="headings"
        self.table_result.pack()
        self.table_result.bind("<ButtonRelease-1")
        #-------------------------------------------------affichage resultat----------------------
        self.affiche_result()
        
    def affiche_result(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="magesti")
        cur = con.cursor()
        cur.execute("select num_enrg,num_service,date_entre,heure,num_salle,nom from patiente")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.table_result.delete(*self.table_result.get_children()) 
            for row in rows:
                self.table_result.insert('',END,values=row) 
        con.commit()  
        con.close()  

    def rech_par(self) :
        con = pymysql.connect(host="localhost",user="root",password="",database="magesti")
        cur = con.cursor()
        cur.execute("select num_enrg,num_service,date_entre,heure,num_salle,nom from patiente where"+str(self.rech.get())+"LIKE'%"+str(self.rech_text.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.table_result.delete(*self.table_result.get_children())
            for row in rows:
                self.table_result.insert('',END,values=row)
        con.commit()
        con.close()

        
#affichage -----------------------
root = Tk()
obj = Listes(root) 
root.mainloop()           