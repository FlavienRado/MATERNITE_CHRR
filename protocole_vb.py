from tkinter import *
from tkinter import ttk,messagebox
from token import VBAR
import pymysql
from pymysql import cursors



class Vb:
    def __init__(self,root):
        self.root = root
        self.root.title("Protocole accouchement VB")
        self.root.geometry("1220x690+50+10")
        self.root.resizable(width='False',height='False')
        
        
        
        frame_vb = Frame(self.root,bg='#7a1f5c')
        frame_vb.place(x=0,y=0,width=1220,height=690)
        
        
        #creation formulaire-----------------------------------------
        enregistrement = LabelFrame(frame_vb,bg='#7a1f5c',font=("Arial",12),bd=0)
        num_enregistrement = Label(enregistrement,text="N° enregistrement",font=("Arial",11),bg='#7a1f5c',fg='white')
        num_enregistrement.grid(row=0,column=0)
        self.champ_num_enregistrement = Entry(enregistrement)
        self.champ_num_enregistrement.grid(row=0,column=1)
        nom_mere = Label(enregistrement,text="Nom de la mere",font=("Arial",11),bg='#7a1f5c',fg='white')
        nom_mere.grid(row=0,column=2)
        self.champ_nom_mere = Entry(enregistrement,width=40)
        self.champ_nom_mere.grid(row=0,column=3)
        dateacc = Label(enregistrement,text="Date",font=("Arial",11),bg='#7a1f5c',fg='white')
        dateacc.grid(row=0,column=4)
        self.champ_dateacc = Entry(enregistrement)
        self.champ_dateacc.grid(row=0,column=5)
        heureacc = Label(enregistrement,text="Heure",font=("Arial",11),bg='#7a1f5c',fg='white')
        heureacc.grid(row=0,column=6)
        self.champ_heureacc = Entry(enregistrement)
        self.champ_heureacc.grid(row=0,column=7)
        avb = Label(enregistrement,text="AVB",font=("Arial",11),bg='#7a1f5c',fg='white')
        avb.grid(row=3,column=0)
        self.champ_avb = Entry(enregistrement)
        self.champ_avb.grid(row=3,column=1)
        enregistrement.grid(sticky='sw',padx=20,pady=10)
        
        bb = LabelFrame(frame_vb,bg='#7a1f5c',font=("Arial",12),bd=0)
        presentation = Label(bb,text="Présentation",font=("Arial",11),bg='#7a1f5c',fg='white')
        presentation.grid(row=0,column=0)
        self.champ_presentation = ttk.Combobox(bb)
        self.champ_presentation["values"]=("céphalique","siege")
        self.champ_presentation.current(0)
        self.champ_presentation.grid(row=0,column=1)
        aide = Label(bb,text="Aidé par:",font=("Arial",11),bg='#7a1f5c',fg='white')
        aide.grid(row=0,column=2)
        self.champ_aide = ttk.Combobox(bb)
        self.champ_aide["values"]=("forceps","vaccum","spatule","")
        self.champ_aide.current(3)
        self.champ_aide.grid(row=0,column=3)
        degagement = Label(bb,text="Dégagement en",font=("Arial",11),bg='#7a1f5c',fg='white')
        degagement.grid(row=0,column=4)
        self.champ_degagement = ttk.Combobox(bb)
        self.champ_degagement["values"]=("OP","OS","SC","SI")
        self.champ_degagement.current(0)
        self.champ_degagement.grid(row=0,column=5)
        enfant = Label(bb,text="enfant",font=("Arial",11),bg='#7a1f5c',fg='white')
        enfant.grid(row=0,column=6)
        self.champ_enfant = ttk.Combobox(bb,state='readonly')
        self.champ_enfant["values"]=("vivant","mort")
        self.champ_enfant.current(0)
        self.champ_enfant.grid(row=0,column=7)
        sexe = Label(bb,text="sexe",font=("Arial",11),bg='#7a1f5c',fg='white')
        sexe.grid(row=0,column=8)
        self.champ_sexe = ttk.Combobox(bb,state='readonly')
        self.champ_sexe["values"]=("masculin","feminin")
        self.champ_sexe.current(0)
        self.champ_sexe.grid(row=0,column=9)
        m1 = Label(bb,text=" APGAR M1",font=("Arial",11),bg='#7a1f5c',fg='white')
        m1.grid(row=2,column=0)
        self.champ_m1 = Entry(bb)
        self.champ_m1.grid(row=2,column=1)
        m5 = Label(bb,text="M5",font=("Arial",11),bg='#7a1f5c',fg='white')
        m5.grid(row=2,column=2)
        self.champ_m5 = Entry(bb)
        self.champ_m5.grid(row=2,column=3)
        m10 = Label(bb,text="M 10",font=("Arial",11),bg='#7a1f5c',fg='white')
        m10.grid(row=2,column=4)
        self.champ_m10 = Entry(bb)
        self.champ_m10.grid(row=2,column=5)
        poid = Label(bb,text="Poids",font=("Arial",11),bg='#7a1f5c',fg='white')
        poid.grid(row=2,column=6)
        self.champ_poid = Entry(bb)
        self.champ_poid.grid(row=2,column=7)
        pc = Label(bb,text="PC",font=("Arial",11),bg='#7a1f5c',fg='white')
        pc.grid(row=4,column=0)
        self.champ_pc = Entry(bb)
        self.champ_pc.grid(row=4,column=1)
        pt = Label(bb,text="PT",font=("Arial",11),bg='#7a1f5c',fg='white')
        pt.grid(row=4,column=2)
        self.champ_pt = Entry(bb)
        self.champ_pt.grid(row=4,column=3)
        taille = Label(bb,text="Taille",font=("Arial",11),bg='#7a1f5c',fg='white')
        taille.grid(row=4,column=4)
        self.champ_taille = Entry(bb)
        self.champ_taille.grid(row=4,column=5)
        neonate = Label(bb,text="Transfert néonatale",font=("Arial",11),bg='#7a1f5c',fg='white')
        neonate.grid(row=4,column=6)
        self.champ_neonate = ttk.Combobox(bb,state='readonly')
        self.champ_neonate["values"]=("oui","non")
        self.champ_neonate.current(0)
        self.champ_neonate.grid(row=4,column=7)
        bb.grid(sticky='sw',padx=20,pady=20)
        
        mama = LabelFrame(frame_vb,bg='#7a1f5c',font=("Arial",12),bd=0)
        amniotique = Label(mama,text="Liquide amniotique",font=("Arial",11),bg='#7a1f5c',fg='white')
        amniotique.grid(row = 0,column=0)
        self.champ_amniotique = ttk.Combobox(mama,state='readonly')
        self.champ_amniotique["values"]=("clair","teinté")
        self.champ_amniotique.current(0)
        self.champ_amniotique.grid(row = 0,column=1)
        meconial = Label(mama,text="Méconial",font=("Arial",11),bg='#7a1f5c',fg='white')
        meconial.grid(row = 0,column=2)
        self.champ_meconiale = ttk.Combobox(mama,state='readonly')
        self.champ_meconiale["values"]=("+","++","+++")
        self.champ_meconiale.current(0)
        self.champ_meconiale.grid(row = 0,column=3)
        purep = Label(mama,text="Puré de pois",font=("Arial",11),bg='#7a1f5c',fg='white')
        purep.grid(row = 0,column=4)
        self.champ_purep = ttk.Combobox(mama,state='readonly')
        self.champ_purep["values"]=("excés","absent")
        self.champ_purep.current(0)
        self.champ_purep.grid(row = 0,column=5)
        delivrance = Label(mama,text="Délivrance",font=("Arial",11),bg='#7a1f5c',fg='white')
        delivrance.grid(row=0,column=6)
        self.champ_delivrance = ttk.Combobox(mama,state='readonly')
        self.champ_delivrance["values"]=("normal","assistée GATPA","manuelle")
        self.champ_delivrance.current(0)
        self.champ_delivrance.grid(row=0,column=7)
        cotyledons = Label(mama,text="Cotyledons",font=("Arial",11),bg='#7a1f5c',fg='white')
        cotyledons.grid(row=1,column=0)
        self.champ_cotyledons = ttk.Combobox(mama,state='readonly')
        self.champ_cotyledons["values"]=("complets","incomplets")
        self.champ_cotyledons.current(0)
        self.champ_cotyledons.grid(row=1,column=1)
        membrane = Label(mama,text="Membranes",font=("Arial",11),bg='#7a1f5c',fg='white')
        membrane.grid(row=2,column=0)
        self.champ_membrane = ttk.Combobox(mama,state='readonly')
        self.champ_membrane["values"]=("complets","incomplets")
        self.champ_membrane.current(0)
        self.champ_membrane.grid(row=2,column=1)
        hematome = Label(mama,text="Hématome",font=("Arial",11),bg='#7a1f5c',fg='white')
        hematome.grid(row = 2,column=2)
        self.champ_hematome = ttk.Combobox(mama,state='readonly')
        self.champ_hematome["values"]=("non","oui")
        self.champ_hematome.current(0)
        self.champ_hematome.grid(row = 2,column=3)
        cordon = Label(mama,text="Cordon",font=("Arial",11),bg='#7a1f5c',fg='white')
        cordon.grid(row = 2,column=4)
        self.champ_cordon = Entry(mama)
        self.champ_cordon.grid(row = 2,column=5)
        vaisseau= Label(mama,text="Nombre vaisseaux",font=("Arial",11),bg='#7a1f5c',fg='white')
        vaisseau.grid(row = 2,column=6)
        self.champ_vaisseau = Entry(mama)
        self.champ_vaisseau.grid(row = 2,column=7)
        rv = Label(mama,text="Revision uterine",font=("Arial",11),bg='#7a1f5c',fg='white')
        rv.grid(row = 4,column=0)
        self.champ_rv = ttk.Combobox(mama,state='readonly')
        self.champ_rv["values"]=("oui","non")
        self.champ_rv.current(0)
        self.champ_rv.grid(row = 4,column=1)
        col = Label(mama,text="Col",font=("Arial",11),bg='#7a1f5c',fg='white')
        col.grid(row = 4,column=2)
        self.champ_col = ttk.Combobox(mama,state='readonly')
        self.champ_col["values"]=("intact","dechire")
        self.champ_col.current(0)
        self.champ_col.grid(row = 4,column=3)
        vagin = Label(mama,text="Vagin",font=("Arial",11),bg='#7a1f5c',fg='white')
        vagin.grid(row = 4,column=4)
        self.champ_vagin = ttk.Combobox(mama,state='readonly')
        self.champ_vagin["values"]=("intact","dechire")
        self.champ_vagin.current(0)
        self.champ_vagin.grid(row = 4,column=5)
        perine = Label(mama,text="Périné",font=("Arial",11),bg='#7a1f5c',fg='white')
        perine.grid(row=4,column=6)
        self.champ_perine = ttk.Combobox(mama,state='readonly')
        self.champ_perine["values"]=("intact","dechire 1","dechire 2","dechire 3")
        self.champ_perine.current(0)
        self.champ_perine.grid(row=4,column=7)
        episiotomie = Label(mama,text="Episiotomie",font=("Arial",11),bg='#7a1f5c',fg='white')
        episiotomie.grid(row = 6,column=0)
        self.champ_episiotomie = ttk.Combobox(mama,state='readonly')
        self.champ_episiotomie["values"]=("non","oui")
        self.champ_episiotomie.current(0)
        self.champ_episiotomie.grid(row = 6,column=1)
        type_epi = Label(mama,text="Type",font=("Arial",11),bg='#7a1f5c',fg='white')
        type_epi.grid(row = 6,column=2)
        self.champ_type_epi = ttk.Combobox(mama,state='readonly')
        self.champ_type_epi["values"]=("laterale d","laterale g","mediane")
        self.champ_type_epi.current(0)
        self.champ_type_epi.grid(row = 6,column=3)
        rtu = Label(mama,text="Retraction de l'uterus",font=("Arial",11),bg='#7a1f5c',fg='white')
        rtu.grid(row = 6,column=4)
        self.champ_rtu = ttk.Combobox(mama,state='readonly')
        self.champ_rtu["values"]=("oui","non")
        self.champ_rtu.current(0)
        self.champ_rtu.grid(row = 6,column=5)
        hemorragie = Label(mama,text="Hémorragie",font=("Arial",11),bg='#7a1f5c',fg='white')
        hemorragie.grid(row = 6,column=6)
        self.champ_hemorragie = ttk.Combobox(mama,state='readonly')
        self.champ_hemorragie["values"]=("oui","non")
        self.champ_hemorragie.current(0)
        self.champ_hemorragie.grid(row = 6,column=7)
        mama.grid(sticky='sw',padx=20,pady=20)
        
        operateur = LabelFrame(frame_vb,bg='#7a1f5c',font=("Arial",12),bd=0)
        nombb = Label(operateur,text="Nom du Bebe",font=("Arial",11),bg='#7a1f5c',fg='white')
        nombb.grid(row = 0,column=0)
        self.champ_nombb = Entry(operateur,width=60)
        self.champ_nombb.grid(row = 0,column=1)
        accoucheur = Label(operateur,text="Accoucheur",font=("Arial",11),bg='#7a1f5c',fg='white')
        accoucheur.grid(row = 0,column=2)
        self.champ_accoucheur = Entry(operateur,width=60)
        self.champ_accoucheur.grid(row = 0,column=3)
        operateur.grid(sticky='sw',padx=20,pady=10)
        
        valider_boutton = Button(frame_vb,text="Enregistrer",command=self.ajout_vb, font=("Arial",11),bg='white',fg='#7a1f5c')
        valider_boutton.grid(sticky='nw')



    def  ajout_vb(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="magesti")
        cur = con.cursor()
        cur.execute("insert into vb (num_enrg,nom,date_vb,heure,avb,presentation,aide_par,degagement,enfant,sexe,m1,m5,m10,poids,pc,pt,taille,neonat,amniotique,meconial,pois,delivrance,cotyledon,membrane,hematome,cordon,num_vaisseau,ru,col,vagin,perine,episio,type,retract,hemorragie,nom_bb,accoucheur) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.champ_num_enregistrement.get(),
                        self.champ_nom_mere.get(),
                        self.champ_dateacc.get(),
                        self.champ_heureacc.get(),
                        self.champ_avb.get(),
                        self.champ_presentation.get(),
                        self.champ_aide.get(),
                        self.champ_degagement.get(),
                        self.champ_enfant.get(),
                        self.champ_sexe.get(),
                        self.champ_m1.get(),
                        self.champ_m5.get(),
                        self.champ_m10.get(),
                        self.champ_poid.get(),
                        self.champ_pc.get(),
                        self.champ_pt.get(),
                        self.champ_taille.get(),
                        self.champ_neonate.get(),
                        self.champ_amniotique.get(),
                        self.champ_meconiale.get(),
                        self.champ_purep.get(),
                        self.champ_delivrance.get(),
                        self.champ_cotyledons.get(),
                        self.champ_membrane.get(),
                        self.champ_hematome.get(),
                        self.champ_cordon.get(),
                        self.champ_vaisseau.get(),
                        self.champ_rv.get(),
                        self.champ_col.get(),
                        self.champ_vagin.get(),
                        self.champ_perine.get(),
                        self.champ_episiotomie.get(),
                        self.champ_type_epi.get(),
                        self.champ_rtu.get(),
                        self.champ_hemorragie.get(),
                        self.champ_nombb.get(),
                        self.champ_accoucheur.get()
                    )) 
        con.commit()
        self.reinitialiser()
        con.close()  
        messagebox.showinfo("Succés","enregistrée avec succé") 

    def reinitialiser(self):
        self.champ_num_enregistrement.delete(0,END),
        self.champ_nom_mere.delete(0,END),
        self.champ_dateacc.delete(0,END),
        self.champ_heureacc.delete(0,END),
        self.champ_avb.delete(0,END),
        self.champ_presentation.delete(0,END),
        self.champ_aide.delete(0,END),
        self.champ_degagement.delete(0,END),
        self.champ_enfant.delete(0,END),
        self.champ_sexe.delete(0,END),
        self.champ_m1.delete(0,END),
        self.champ_m5.delete(0,END),
        self.champ_m10.delete(0,END),
        self.champ_poid.delete(0,END),
        self.champ_pc.delete(0,END),
        self.champ_pt.delete(0,END),
        self.champ_taille.delete(0,END),
        self.champ_neonate.delete(0,END),
        self.champ_amniotique.delete(0,END),
        self.champ_meconiale.delete(0,END),
        self.champ_purep.delete(0,END),
        self.champ_delivrance.delete(0,END),
        self.champ_cotyledons.delete(0,END),
        self.champ_membrane.delete(0,END),
        self.champ_hematome.delete(0,END),
        self.champ_cordon.delete(0,END),
        self.champ_vaisseau.delete(0,END),
        self.champ_rv.delete(0,END),
        self.champ_col.delete(0,END),
        self.champ_vagin.delete(0,END),
        self.champ_perine.delete(0,END),
        self.champ_episiotomie.delete(0,END),
        self.champ_type_epi.delete(0,END),
        self.champ_rtu.delete(0,END),
        self.champ_hemorragie.delete(0,END),
        self.champ_nombb.delete(0,END),
        self.champ_accoucheur.delete(0,END)



#affichage -----------------------
root = Tk()
obj = Vb(root) 
root.mainloop()           