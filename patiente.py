from tkinter import *
from tkinter import ttk,messagebox
import pymysql
from pymysql import cursors
import os



class Patiente:
    def __init__(self,root):
        self.root = root
        self.root.title("Patiente")
        self.root.geometry("1220x690+50+10")
        self.root.resizable(width='False',height='False')
        
        
        
        #bar de menu--------------------------------------------
        bar_menu = Menu(self.root)
        premier_menu = Menu(bar_menu,tearoff=0)
        deuxieme_menu = Menu(bar_menu,tearoff=0)
        deuxieme_menu.add_command(label="ajouter",command=self.fenetre_vb)
        troisieme_menu = Menu(bar_menu,tearoff=0)
        troisieme_menu.add_command(label="ajouter",command=self.fenetre_oc)
        quatrieme_menu = Menu(bar_menu,tearoff=0)
        quatrieme_menu.add_command(label="consulter",command=self.fenetre_liste)

        bar_menu.add_cascade(label="Enregistrement",menu=premier_menu)
        bar_menu.add_cascade(label="Protocole VB",menu=deuxieme_menu)
        bar_menu.add_cascade(label="Protocole OC",menu=troisieme_menu)
        bar_menu.add_cascade(label="Liste des patientes",menu=quatrieme_menu)


    #boucle affichage bar menu---------------------
        self.root.config(menu=bar_menu)
    #-----------------------------------------------------------    
        frame_patiente = Frame(self.root,bg='#7a1f5c')
        frame_patiente.place(x=0,y=0,width=1220,height=690)
    
        
        enregistrement = LabelFrame(frame_patiente,text="Enregistrement",labelanchor='nw',bg='#7a1f5c',font=("Arial",12),bd=0)
    
        numero_enregistrement = Label(enregistrement,text="N° enregistrement",font=("Arial",11),bg='#7a1f5c',fg='white')
        numero_enregistrement.grid(row=0,column=0)
        self.champ_numero_enregistrement = Entry(enregistrement)
        self.champ_numero_enregistrement.grid(row=0,column=1)
        numero_enregistrement_service = Label(enregistrement,text="N° enregistrement service",font=("Arial",11),bg='#7a1f5c',fg='white')
        numero_enregistrement_service.grid(row=0,column=2)
        self.champ_numero_enregistrement_service = Entry(enregistrement)
        self.champ_numero_enregistrement_service.grid(row=0,column=3)
        date_entree = Label(enregistrement,text="Date",font=("Arial",11),bg='#7a1f5c',fg='white')
        date_entree.grid(row=0,column=4)
        self.champ_date_entre = Entry(enregistrement)
        self.champ_date_entre.grid(row=0,column=5)
        heure = Label(enregistrement,text="Heure",font=("Arial",11),bg='#7a1f5c',fg='white')
        heure.grid(row=0,column=6)
        self.champ_heure = Entry(enregistrement)
        self.champ_heure.grid(row=0,column=7)
        numero_salle_lit = Label(enregistrement,text="N°salle/lit",font=("Arial",11),bg='#7a1f5c',fg='white')
        numero_salle_lit.grid(row=0,column=8)
        self.champ_numero_salle = Entry(enregistrement)
        self.champ_numero_salle.grid(row=0,column=9)
        examen_par = Label(enregistrement,text="Examen fait par",font=("Arial",11),bg='#7a1f5c',fg='white')
        examen_par.grid(row=2,column=0)
        self.champ_examen_par = Entry(enregistrement,width=40)
        self.champ_examen_par.grid(row=2,column=1)
        enregistrement.grid(sticky='nw')
        
        patiente = LabelFrame(frame_patiente,pady=10,text="Identités",labelanchor='nw',bg='#7a1f5c',font=("Arial",12),bd=0)
        
        nom_complet = Label(patiente,text="Nom et Prenom",font=("Arial",11),bg='#7a1f5c',fg='white')
        nom_complet.grid(row=0,column=0)
        self.champ_nom = Entry(patiente,width=30)
        self.champ_nom.grid(row=0 ,column=1)
        date_naissance = Label(patiente,text="Date de naissance",font=("Arial",11),bg='#7a1f5c',fg='white')
        date_naissance.grid(row=0 ,column=2)
        self.champ_daten = Entry(patiente)
        self.champ_daten.grid(row=0 ,column=3)
        age = Label(patiente,text="Age",font=("Arial",11),bg='#7a1f5c',fg='white')
        age.grid(row=0 ,column=4)
        self.champ_age = Entry(patiente)
        self.champ_age.grid(row=0 ,column=5)
        profession = Label(patiente,text="Profession",font=("Arial",11),bg='#7a1f5c',fg='white')
        profession.grid(row=0 ,column=6)
        self.champ_profession = Entry(patiente)
        self.champ_profession.grid(row=0 ,column=7)
        telephone = Label(patiente,text="Telephone",font=("Arial",11),bg='#7a1f5c',fg='white')
        telephone.grid(row=3,column=0)
        self.champ_telephone = Entry(patiente)
        self.champ_telephone.grid(row=3,column=1)
        adresse = Label(patiente,text="Adresse:lot",font=("Arial",11),bg='#7a1f5c',fg='white')
        adresse.grid(row=3,column=2)
        self.champ_adresse = Entry(patiente)
        self.champ_adresse.grid(row=3,column=3)
        fkt = Label(patiente,text="FKT",font=("Arial",11),bg='#7a1f5c',fg='white')
        fkt.grid(row=3,column=4)
        self.champ_fkt = Entry(patiente)
        self.champ_fkt.grid(row=3,column=5)
        cin = Label(patiente,text="piece d'identité",font=("Arial",11),bg='#7a1f5c',fg='white')
        cin.grid(row=5 ,column=0)
        self.champ_cin = ttk.Combobox(patiente,state='readonly')
        self.champ_cin["values"]=("CIN","Passeport","permis de conduire")
        self.champ_cin.current(0)
        self.champ_cin.grid(row=5 ,column=1)
        num_cin = Label(patiente,text="N° piece d'identité",font=("Arial",11),bg='#7a1f5c',fg='white')
        num_cin.grid(row=5,column=2)
        self.champ_num_cin = Entry(patiente)
        self.champ_num_cin.grid(row=5,column=3)
        situation = Label(patiente,text="Situation Matrimoniale",font=("Arial",11),bg='#7a1f5c',fg='white')
        situation.grid(row=5,column=4)
        self.champ_situation = ttk.Combobox(patiente,state='readonly')
        self.champ_situation["values"]=("Célibataire","Concubinage","Mariée")
        self.champ_situation.current(2)
        self.champ_situation.grid(row=5,column=5)
        prevenir = Label(patiente,text="Personne à prévenir",font=("Arial",11),bg='#7a1f5c',fg='white')
        prevenir.grid(row=7,column=0)
        self.champ_prevenir = Entry(patiente,width=30)
        self.champ_prevenir.grid(row=7,column=1)
        prevenir_phone = Label(patiente,text="Téléphone",font=("Arial",11),bg='#7a1f5c',fg='white')
        prevenir_phone.grid(row=7,column=2)
        self.champ_prevenir_phone = Entry(patiente)
        self.champ_prevenir_phone.grid(row=7,column=3)
        patiente.grid(sticky='nw')
        
        admission = LabelFrame(frame_patiente,pady=10,text="Admission",labelanchor='nw',bg='#7a1f5c',font=("Arial",12),bd=0)
        
        admis = Label(admission,text="Admission",font=("Arial",11),bg='#7a1f5c',fg='white')
        admis.grid(row=0, column=0)
        self.champ_admis = ttk.Combobox(admission,state='readonly')
        self.champ_admis["values"]=("Auto Référée","Référée","Transférée")
        self.champ_admis.current(0)
        self.champ_admis.grid(row=0,column=1)
        motif_admis = Label(admission,text="Motif d'admission",font=("Arial",11),bg='#7a1f5c',fg='white')
        motif_admis.grid(row=0 ,column=2 )
        self.champ_motif_admis = Entry(admission,width=80)
        self.champ_motif_admis.grid(row=0,column=3)
        admission.grid(sticky='nw')
        
        bilan = LabelFrame(frame_patiente,pady=10,text="Bilan initial",labelanchor='nw',bg='#7a1f5c',font=("Arial",12),bd=0)
        
        glasgow = Label(bilan,text="Glasgow",font=("Arial",11),bg='#7a1f5c',fg='white')
        glasgow.grid(row=0 ,column=0 )
        self.champ_glasgow = Entry(bilan)
        self.champ_glasgow.grid(row=0,column=1)
        temperature = Label(bilan,text="Temperature",font=("Arial",11),bg='#7a1f5c',fg='white')
        temperature.grid(row=0 ,column=2 )
        self.champ_temperature = Entry(bilan)
        self.champ_temperature.grid(row=0,column=3)
        tad = Label(bilan,text="TAD",font=("Arial",11),bg='#7a1f5c',fg='white')
        tad.grid(row=0,column=4 )
        self.champ_tad = Entry(bilan)
        self.champ_tad.grid(row=0,column=5)
        tag = Label(bilan,text="TAG",font=("Arial",11),bg='#7a1f5c',fg='white')
        tag.grid(row=0,column=6 )
        self.champ_tag = Entry(bilan)
        self.champ_tag.grid(row=0,column=7)
        fc = Label(bilan,text="FC",font=("Arial",11),bg='#7a1f5c',fg='white')
        fc.grid(row=0 ,column=8)
        self.champ_fc = Entry(bilan)
        self.champ_fc.grid(row=0,column=9)
        fr = Label(bilan,text="FR",font=("Arial",11),bg='#7a1f5c',fg='white')
        fr.grid(row=3 ,column=0 )
        self.champ_fr = Entry(bilan)
        self.champ_fr.grid(row=3,column=1)
        poid = Label(bilan,text="Poids",font=("Arial",11),bg='#7a1f5c',fg='white')
        poid.grid(row=3,column=2 )
        self.champ_poid = Entry(bilan)
        self.champ_poid.grid(row=3,column=3)
        taille = Label(bilan,text="Taille",font=("Arial",11),bg='#7a1f5c',fg='white')
        taille.grid(row=3,column=4 )
        self.champ_taille = Entry(bilan)
        self.champ_taille.grid(row=3,column=5)
        ddr = Label(bilan,text="DDR",font=("Arial",11),bg='#7a1f5c',fg='white')
        ddr.grid(row=3 ,column=6 )
        self.champ_ddr = Entry(bilan)
        self.champ_ddr.grid(row=3,column=7)
        age_gesta = Label(bilan,text="Age gestationnel",font=("Arial",11),bg='#7a1f5c',fg='white')
        age_gesta.grid(row=3 ,column=8 )
        self.champ_age_gesta = Entry(bilan)
        self.champ_age_gesta.grid(row=3,column=9)
        nombre_cpn = Label(bilan,text="CPN Nombre",font=("Arial",11),bg='#7a1f5c',fg='white')
        nombre_cpn.grid(row=5 ,column=0 )
        self.champ_nombre_cpn = Entry(bilan)
        self.champ_nombre_cpn.grid(row=5,column=1)
        lieu_cpn = Label(bilan,text="Lieu",font=("Arial",11),bg='#7a1f5c',fg='white')
        lieu_cpn.grid(row=5 ,column=2)
        self.champ_lieu_cpn = Entry(bilan)
        self.champ_lieu_cpn.grid(row=5,column=3)
        vat = Label(bilan,text="VAT",font=("Arial",11),bg='#7a1f5c',fg='white')
        vat.grid(row=5,column=4)
        self.champ_vat = Entry(bilan)
        self.champ_vat.grid(row=5,column=5)
        serologie = Label(bilan,text="Sérologie",font=("Arial",11),bg='#7a1f5c',fg='white')
        serologie.grid(row=5,column=6)
        self.champ_serologie = ttk.Combobox(bilan,state='readonly')
        self.champ_serologie["values"]=("HIV Neg","Syphilis Neg","HIV et Syphilis Neg","HIV Neg et Syphilis Pos",
                                "HIV Pos et Syphilis Neg","HIV et Syphilis Pos","HIV Pos","Syphilis PosS")
        self.champ_serologie.current(2)
        self.champ_serologie.grid(row=5,column=7)
        
        bilan.grid(sticky='nw')
        
        hdmf = LabelFrame(frame_patiente,bg='#7a1f5c',font=("Arial",12),bd=0)
        hdm = Label(hdmf,text="Histoire de la maladie",font=("Arial",11),bg='#7a1f5c',fg='white')
        hdm.grid(row=0 ,column=0 )
        self.champ_hdm = Entry(hdmf,width=100)
        self.champ_hdm.grid(row=0,column=1)
        hdmf.grid(sticky='nw')
        
       
        
        antecedent = LabelFrame(frame_patiente,pady=10,text="Antecedent",labelanchor='nw',bg='#7a1f5c',font=("Arial",12),bd=0)
        
        gestite = Label(antecedent,text="Géstité",font=("Arial",11),bg='#7a1f5c',fg='white')
        gestite.grid(row=0 ,column=0 )
        self.champ_gestite = Entry(antecedent)
        self.champ_gestite.grid(row=0,column=1)
        parite = Label(antecedent,text="Parité",font=("Arial",11),bg='#7a1f5c',fg='white')
        parite.grid(row=0,column=2 )
        self.champ_parite = Entry(antecedent)
        self.champ_parite.grid(row=0,column=3)
        avortement = Label(antecedent,text="Avortement",font=("Arial",11),bg='#7a1f5c',fg='white')
        avortement.grid(row=0 ,column=4)
        self.champ_avortement = Entry(antecedent)
        self.champ_avortement.grid(row=0,column=5)
        date_acc = Label(antecedent,text="Dernier accouchement",font=("Arial",11),bg='#7a1f5c',fg='white')
        date_acc.grid(row=0 ,column=6 )
        self.champ_date_acc = Entry(antecedent)
        self.champ_date_acc.grid(row=0,column=7)
        oc_pour = Label(antecedent,text="OC pour",font=("Arial",11),bg='#7a1f5c',fg='white')
        oc_pour.grid(row=0 ,column=8 )
        self.champ_oc_pour = Entry(antecedent)
        self.champ_oc_pour.grid(row=0,column=9)
        atcd_med = Label(antecedent,text="ATCD méd",font=("Arial",11),bg='#7a1f5c',fg='white')
        atcd_med.grid(row=2,column=0 )
        self.champ_atcd_med= Entry(antecedent)
        self.champ_atcd_med.grid(row=2,column=1)
        atcd_chir = Label(antecedent,text="ATCD chir",font=("Arial",11),bg='#7a1f5c',fg='white')
        atcd_chir.grid(row=2,column=2 )
        self.champ_atcd_chir = Entry(antecedent)
        self.champ_atcd_chir.grid(row=2,column=3)
        allergie = Label(antecedent,text="Allergie",font=("Arial",11),bg='#7a1f5c',fg='white')
        allergie.grid(row=2 ,column=4 )
        self.champ_allergie = Entry(antecedent)
        self.champ_allergie.grid(row=2,column=5)
        contraception = Label(antecedent,text="Contraception",font=("Arial",11),bg='#7a1f5c',fg='white')
        contraception.grid(row=2 ,column=6 )
        self.champ_contraception = Entry(antecedent)
        self.champ_contraception.grid(row=2,column=7)
        atcd_toxi = Label(antecedent,text="ATCD Toxique",font=("Arial",11),bg='#7a1f5c',fg='white')
        atcd_toxi.grid(row=2,column=8)
        self.champ_atcd_toxi = ttk.Combobox(antecedent,state='readonly')
        self.champ_atcd_toxi["values"]=("tabac","alcool","tambavy","massage","tabac et alcool","tabac et tambavy","tabac et massage",
                                "alcool et tambavy","alcool et massage","tambavy et massage","aucun")
        self.champ_atcd_toxi.current(10)
        self.champ_atcd_toxi.grid(row=2,column=9)
        signe_fonc = Label(antecedent,text="Signes fonctionnels",font=("Arial",11),bg='#7a1f5c',fg='white')
        signe_fonc.grid(row=5 ,column=0 )
        self.champ_signe_fonc = Entry(antecedent)
        self.champ_signe_fonc.grid(row=5,column=1)
        abdo = Label(antecedent,text="Abdomen",font=("Arial",11),bg='#7a1f5c',fg='white')
        abdo.grid(row=5 ,column=2 )
        self.champ_abdo = Entry(antecedent)
        self.champ_abdo.grid(row=5,column=3)
        speculum = Label(antecedent,text="Spéculum",font=("Arial",11),bg='#7a1f5c',fg='white')
        speculum.grid(row=5 ,column=4)
        self.champ_speculum = Entry(antecedent)
        self.champ_speculum.grid(row=5,column=5)
        hu = Label(antecedent,text="HU",font=("Arial",11),bg='#7a1f5c',fg='white')
        hu.grid(row=5 ,column=6 )
        self.champ_hu = Entry(antecedent)
        self.champ_hu.grid(row=5,column=7)
        presentation = Label(antecedent,text="Présentation",font=("Arial",11),bg='#7a1f5c',fg='white')
        presentation.grid(row=5 ,column=8 )
        self.champ_presentation = Entry(antecedent)
        self.champ_presentation.grid(row=5,column=9)
        bdcf = Label(antecedent,text="BDCF",font=("Arial",11),bg='#7a1f5c',fg='white')
        bdcf.grid(row=7 ,column=0 )
        self.champ_bdcf = Entry(antecedent)
        self.champ_bdcf.grid(row=7,column=1)
        tv = Label(antecedent,text="Toucher vaginal",font=("Arial",11),bg='#7a1f5c',fg='white')
        tv.grid(row=7 ,column=2)
        self.champ_tv = Entry(antecedent)
        self.champ_tv.grid(row=7,column=3)
        autre_exam = Label(antecedent,text="Autre examen",font=("Arial",11),bg='#7a1f5c',fg='white')
        autre_exam.grid(row=7 ,column=4 )
        self.champ_autre_exam = Entry(antecedent)
        self.champ_autre_exam.grid(row=7,column=5)
        antecedent.grid(sticky='nw')
        
        diag = LabelFrame(frame_patiente,pady=10,text="Diagnostic",labelanchor='nw',bg='#7a1f5c',font=("Arial",12),bd=0)
        
        bleme = Label(diag,text="Diag ou Probleme",font=("Arial",11),bg='#7a1f5c',fg='white')
        bleme.grid(row=0 ,column=0 )
        self.champ_bleme = Entry(diag,width=40)
        self.champ_bleme.grid(row=0,column=1)
        exam_para = Label(diag,text="Examen paraclinique ",font=("Arial",11),bg='#7a1f5c',fg='white')
        exam_para.grid(row=0 ,column=2 )
        self.champ_exam_para = Entry(diag,width=40)
        self.champ_exam_para.grid(row=0,column=3)
        t3 = Label(diag,text="traitement de premier intention",font=("Arial",11),bg='#7a1f5c',fg='white')
        t3.grid(row=0 ,column=4 )
        self.champ_t3 = Entry(diag,width=40)
        self.champ_t3.grid(row=0,column=5)
        diag.grid(sticky='nw')
        
        
        
        valider_boutton = Button(frame_patiente,text="Enregistrer",command=self.ajout_patiente,font=("Arial",11),bg='white',fg='#7a1f5c')
        valider_boutton.grid(sticky='s')
        
    
    def fenetre_vb(self):
        import protocole_vb  
    
    def fenetre_oc(self):
        import protocole_oc
    
    def fenetre_liste(self):
        import liste_patientes           
    
    def ajout_patiente(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="magesti")
        cur = con.cursor()
        cur.execute("insert into patiente (num_enrg,num_service,date_entre,heure,num_salle,exam_par,nom,date_n,age,profession,phone,adresse,fkt,cin,num_cin,situation,prevenir,phone_prevenir,admission,motif,glasgow,temperature,tad,tag,fc,fr,poid,taille,ddr,age_gesta,num_cpn,cpn_lieu,vat,serologie,hdm,gestite,parite,avortement,d_acc,oc_pour,atcd_med,atcd_chir,allergie,contraception,atcd_toxi,signe_fonc,abdo,speculum,hu,presentation,bdcf,tv,autre_exam,bleme,para,t3) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.champ_numero_enregistrement.get(),
                        self.champ_numero_enregistrement_service.get(),
                        self.champ_date_entre.get(),
                        self.champ_heure.get(),
                        self.champ_numero_salle.get(),
                        self.champ_examen_par.get(),
                        self.champ_nom.get(),
                        self.champ_daten.get(),
                        self.champ_age.get(),
                        self.champ_profession.get(),
                        self.champ_telephone.get(),
                        self.champ_adresse.get(),
                        self.champ_fkt.get(),
                        self.champ_cin.get(),
                        self.champ_num_cin.get(),
                        self.champ_situation.get(),
                        self.champ_prevenir.get(),
                        self.champ_prevenir_phone.get(),
                        self.champ_admis.get(),
                        self.champ_motif_admis.get(),
                        self.champ_glasgow.get(),
                        self.champ_temperature.get(),
                        self.champ_tad.get(),
                        self.champ_tag.get(),
                        self.champ_fc.get(),
                        self.champ_fr.get(),
                        self.champ_poid.get(),
                        self.champ_taille.get(),
                        self.champ_ddr.get(),
                        self.champ_age_gesta.get(),
                        self.champ_nombre_cpn.get(),
                        self.champ_lieu_cpn.get(),
                        self.champ_vat.get(),
                        self.champ_serologie.get(),
                        self.champ_hdm.get(),
                        self.champ_gestite.get(),
                        self.champ_parite.get(),
                        self.champ_avortement.get(),
                        self.champ_date_acc.get(),
                        self.champ_oc_pour.get(),
                        self.champ_atcd_med.get(),
                        self.champ_atcd_chir.get(),
                        self.champ_allergie.get(),
                        self.champ_contraception.get(),
                        self.champ_atcd_toxi.get(),
                        self.champ_signe_fonc.get(),
                        self.champ_abdo.get(),
                        self.champ_speculum.get(),
                        self.champ_hu.get(),
                        self.champ_presentation.get(),
                        self.champ_bdcf.get(),
                        self.champ_tv.get(),
                        self.champ_autre_exam.get(),
                        self.champ_bleme.get(),
                        self.champ_exam_para.get(),
                        self.champ_t3.get()
                    ))
        con.commit()
        self.reinitialiser()
        con.close()  
        messagebox.showinfo("Succés","Patiente enregistrée avec succé")  
    
    
    def reinitialiser(self):
        self.champ_numero_enregistrement.delete(0,END),
        self.champ_numero_enregistrement_service.delete(0,END),
        self.champ_date_entre.delete(0,END),
        self.champ_heure.delete(0,END),
        self.champ_numero_salle.delete(0,END),
        self.champ_examen_par.delete(0,END),
        self.champ_nom.delete(0,END),
        self.champ_daten.delete(0,END),
        self.champ_age.delete(0,END),
        self.champ_profession.delete(0,END),
        self.champ_telephone.delete(0,END),
        self.champ_adresse.delete(0,END),
        self.champ_fkt.delete(0,END),
        self.champ_cin.delete(0,END),
        self.champ_num_cin.delete(0,END),
        self.champ_situation.delete(0,END),
        self.champ_prevenir.delete(0,END),
        self.champ_prevenir_phone.delete(0,END),
        self.champ_admis.delete(0,END),
        self.champ_motif_admis.delete(0,END),
        self.champ_glasgow.delete(0,END),
        self.champ_temperature.delete(0,END),
        self.champ_tad.delete(0,END),
        self.champ_tag.delete(0,END),
        self.champ_fc.delete(0,END),
        self.champ_fr.delete(0,END),
        self.champ_poid.delete(0,END),
        self.champ_taille.delete(0,END),
        self.champ_ddr.delete(0,END),
        self.champ_age_gesta.delete(0,END),
        self.champ_nombre_cpn.delete(0,END),
        self.champ_lieu_cpn.delete(0,END),
        self.champ_vat.delete(0,END),
        self.champ_serologie.delete(0,END),
        self.champ_hdm.delete(0,END),
        self.champ_gestite.delete(0,END),
        self.champ_parite.delete(0,END),
        self.champ_avortement.delete(0,END),
        self.champ_date_acc.delete(0,END),
        self.champ_oc_pour.delete(0,END),
        self.champ_atcd_med.delete(0,END),
        self.champ_atcd_chir.delete(0,END),
        self.champ_allergie.delete(0,END),
        self.champ_contraception.delete(0,END),
        self.champ_atcd_toxi.delete(0,END),
        self.champ_signe_fonc.delete(0,END),
        self.champ_abdo.delete(0,END),
        self.champ_speculum.delete(0,END),
        self.champ_hu.delete(0,END),
        self.champ_presentation.delete(0,END),
        self.champ_bdcf.delete(0,END),
        self.champ_tv.delete(0,END),
        self.champ_autre_exam.delete(0,END),
        self.champ_bleme.delete(0,END),
        self.champ_exam_para.delete(0,END),
        self.champ_t3.delete(0,END)
       
    



#affichage -----------------------
root = Tk()
obj = Patiente(root) 
root.mainloop()       

