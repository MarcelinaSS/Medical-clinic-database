import sqlite3
from tkinter import *
from tkinter import scrolledtext
import tkinter as tk
import tkinter.ttk as ttk
import datetime
from tkinter import ttk

db = sqlite3.connect('BazaSellyOakley')
cur = db.cursor()





okno = tk.Tk()
okno.title("Baza Kliniki Selly Oakley")
okno.geometry('1000x500')
zakładki = ttk.Notebook(okno)
tab1 = ttk.Frame(zakładki)
tab2 = ttk.Frame(zakładki)
tab3 = ttk.Frame(zakładki)
tab4 = ttk.Frame(zakładki)
tab5 = ttk.Frame(zakładki)
tab6 = ttk.Frame(zakładki)
tab7 = ttk.Frame(zakładki)
tab8 = ttk.Frame(zakładki)
tab9 = ttk.Frame(zakładki)
tab10 = ttk.Frame(zakładki)
tab11 = ttk.Frame(zakładki)
tab12 = ttk.Frame(zakładki)
tab13 = ttk.Frame(zakładki)
tab14 = ttk.Frame(zakładki)
zakładki.add(tab1, text='Pracownicy')
zakładki.add(tab2, text='Lekarze')
zakładki.add(tab3, text='Łóżka')
zakładki.add(tab4, text='Wizyty')
zakładki.add(tab5, text='Pacjenci')
zakładki.add(tab6, text='Technicy')
zakładki.add(tab7, text='Zabiegi')
zakładki.add(tab8, text='Testy')
zakładki.add(tab9, text='Oddziały')
zakładki.add(tab10, text='Przedmioty')
zakładki.add(tab11, text='Rejestry godzin')
zakładki.add(tab12, text='Zużyte przedmioty')
zakładki.add(tab13, text='Pracownicy na oddziałach')
zakładki.add(tab14, text='Zapytania')

#treść1 = Label(tab1, text= 'opis 1') # może być taki prosty opis
"""treść1 = Label(tab1, text= 'opis 1', padx=25, pady=50)
treść1.grid(column=0, row=0)
treść2 = Label(tab2, text= 'opis 2', padx=65, pady=40)
treść2.grid(column=0, row=0)"""
zakładki.pack(expand=1, fill='both')


#----------------------Pracownicy-------------------------------
def create_pracownicy():
    with db:
        cur.execute("""CREATE TABLE if not exists pracownicy(
numer_pracownika INTEGER(10) PRIMARY KEY,
imie TEXT(20) NOT NULL,
nazwisko TEXT(30) NOT NULL,
adres_zamieszkania TEXT(40) NOT NULL,
etat TEXT(20) NOT NULL,
id_szefa INTEGER(10) NULL,
pensja_stała REAL(10) NULL,
pensja_godzinowa REAL(10) NULL,
FOREIGN KEY(id_szefa) REFERENCES pracownicy(numer_pracownika)
ON DELETE CASCADE ON UPDATE CASCADE
);""")

create_pracownicy()

def select_all_pracownicy():
    with db:
        cur.execute("select * from pracownicy")
        print(cur.fetchall())





frame_1 = ttk.LabelFrame(tab1, text="Dodaj pracownika")
frame_1.grid(row=1, column=0)
frame_2 = ttk.LabelFrame(tab1, text="Usuń pracownika")
frame_2.grid(row=2, column=0)
frame_3 = ttk.LabelFrame(tab1, text="Pokaż wszystkich pracowników")
frame_3.grid(row=0, column=1)
frame_4 = ttk.LabelFrame(tab1, text="Usuń wszystkich pracowników")
frame_4.grid(row=0, column=2)
frame_5 = ttk.LabelFrame(tab1, text="Wprowadź listę pracowników")
frame_5.grid(row=0, column=0)

# Ramka 1 - Dodaj pracownika
etykieta1 = tk.Label(frame_1, text="Wprowadż dane pracownika")
etykieta1.grid(row=0, columnspan=3)
label_11 = tk.Label(frame_1, text="Numer pracownika")
label_12 = tk.Label(frame_1, text="Imię")
label_13 = tk.Label(frame_1, text="Nazwisko")
label_14 = tk.Label(frame_1, text="Adres zamieszkania")
label_15 = tk.Label(frame_1, text="Etat")
label_16 = tk.Label(frame_1, text="Id szefa")
label_17 = tk.Label(frame_1, text="Pensja (stała)")
label_18 = tk.Label(frame_1, text="Pensja (godzinowa)")

inputNrPracownika = tk.Entry(frame_1)
inputImie = tk.Entry(frame_1)
inputNazwisko = tk.Entry(frame_1)
inputAdres = tk.Entry(frame_1)
inputEtat = tk.Entry(frame_1)
inputIdSzefa = tk.Entry(frame_1)
inputPensjaStała = tk.Entry(frame_1)
inputPensjaGodz = tk.Entry(frame_1)

label_11.grid(row=1, sticky='E')  # sticky alligns the text to right (E - east,
label_12.grid(row=2, sticky='E')  # W - west, N - north, S - south)
label_13.grid(row=3, sticky='E')
label_14.grid(row=4, sticky='E')
label_15.grid(row=5, sticky='E')
label_16.grid(row=6, sticky='E')
label_17.grid(row=7, sticky='E')
label_18.grid(row=8, sticky='E')

inputNrPracownika.grid(row=1, column=1)
inputImie.grid(row=2, column=1)
inputNazwisko.grid(row=3, column=1)
inputAdres.grid(row=4, column=1)
inputEtat.grid(row=5, column=1)
inputIdSzefa.grid(row=6, column=1)
inputPensjaStała.grid(row=7, column=1)
inputPensjaGodz.grid(row=8, column=1)


class Pracownicy:

    def __init__(self, numer_pracownika, imie, nazwisko,
                 adres_zamieszkania, etat, id_szefa, pensja_stała,
                 pensja_godzinowa):
        self.numer_pracownika = numer_pracownika
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres_zamieszkania = adres_zamieszkania
        self.etat = etat
        self.id_szefa = id_szefa
        self.pensja_stała = pensja_stała
        self.pensja_godzinowa = pensja_godzinowa


def insert_pracownika(prac):
    with db:
        cur.execute("""insert into pracownicy values (:numer_pracownika,
:imie, :nazwisko, :adres_zamieszkania, :etat, :id_szefa, :pensja_stała,
:pensja_godzinowa)""", {'numer_pracownika': prac.numer_pracownika,
                        'imie': prac.imie, 'nazwisko': prac.nazwisko,
                        'adres_zamieszkania': prac.adres_zamieszkania,
                        'etat': prac.etat, 'id_szefa': prac.id_szefa,
                        'pensja_stała': prac.pensja_stała,
                        'pensja_godzinowa': prac.pensja_godzinowa})


def dodaj_pracownika():
    nrPrac = inputNrPracownika.get()
    imie = inputImie.get()
    nazwisko = inputNazwisko.get()
    adres = inputAdres.get()
    etat = inputEtat.get()
    idSzefa = inputIdSzefa.get()
    pensjaStala = inputPensjaStała.get()
    pensjaGodz = inputPensjaGodz.get()

    pracownik = Pracownicy(nrPrac, imie, nazwisko, adres, etat, idSzefa,
                           pensjaStala, pensjaGodz)

    insert_pracownika(pracownik)


def on_select_dodaj(event=None):
    if event:
        dodaj_pracownika()
        db.commit()


b = tk.Button(frame_1, text="Dodaj")
b.grid(row=10, columnspan=3)
b.bind("<Button-1>", on_select_dodaj)

# Ramka 2 - Usuń pracownika
etykieta2 = tk.Label(frame_2, text="Wprowadż numer pracownika")
etykieta2.grid(row=0, columnspan=3)
label_21 = tk.Label(frame_2, text="Numer pracownika")
inputNrPracownika2 = tk.Entry(frame_2)

label_21.grid(row=1, sticky='E')
inputNrPracownika2.grid(row=1, column=1)


def delete_pracownika(prac):
    with db:
        cur.execute("""delete from pracownicy where
                    numer_pracownika = :numer_pracownika""",
                    {'numer_pracownika': prac})


def usun_pracownika():
    nrPrac = inputNrPracownika2.get()

    delete_pracownika(nrPrac)


def on_select_usun(event=None):
    if event:
        usun_pracownika()
        db.commit()


b2 = tk.Button(frame_2, text="Usuń")
b2.grid(row=10, columnspan=3)
b2.bind("<Button-1>", on_select_usun)


# Ramka 3 - Pokaż wszystkich pracowników
# from texttable import Texttable
def select_all_pracownicy():
    with db:
        cur.execute("select * from pracownicy")
        cur.fetchall()


def create_window():
    select = ('select * from pracownicy')
    window = Tk()
    window.title("Pracownicy - lista rekordów")
    window.geometry('900x500')
    txt = scrolledtext.ScrolledText(window, width=200, height=200)
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')

def pokaz_pracowników():
    create_window()


def on_select_pokaz(event=None):
    if event:
        pokaz_pracowników()


b3 = tk.Button(frame_3, text="Pokaż")
b3.pack()
b3.bind("<Button-1>", on_select_pokaz)


# Ramka 4 - Usuń wszystkich pracowników
def drop_pracownicy():
    with db:
        cur.execute("drop table if exists pracownicy")


def usunWszystkich():
    drop_pracownicy()
    create_pracownicy()


def on_select_usunWszystkich(event=None):
    if event:
        usunWszystkich()
        db.commit()


b4 = tk.Button(frame_4, text="Usuń")
b4.pack()
b4.bind("<Button-1>", on_select_usunWszystkich)





#Ramka 5 - Wprowadź listę pracowników

pracownicy = [(111,'Jan','Nowak','ul.Kwiatowa 2/1 Wroclaw',
               'Pielegniarka oddzialowa',168,3000,'null'),
              (100,'Zdzisław','Dyrektor','ul.Dyrekcyjna 33 Wroclaw',
               'Dyrektor',100,25000,'null'),
              (123,'Andrzej','Kowalski','ul.Czekoladowa 35 51-318',
               'Technik',189,4000,'null'),
              (134,'Janusz','Puzdro','ul.Prusa 48/15 50-316 Wroclaw',
               'Lekarz',168,3500,'null'),
              (167,'Alicja','Bachleda','ul.Sienkiewicza 18/22 50-317 Wroclaw',
               'Pielegniarka oddzialowa',465,3200,'null'),
              (189,'Marian','Gorecki','ul.Hubska 32/89 50-415 Wroclaw',
               'Ordynator',100,5000,'null'),
              (390,'Anna','Rogowska','ul.Ruska 34/9 51-321 Wroclaw',
               'Pielęgniarka oddzialowa',189,5000,'null'),
              (465,'Krzysztof','Krawczyk','ul.Parostatkowa 50-308 Wroclaw',
               'Ordynator',100,5500,'null'),
              (871,'Piotr','Adam','ul.Daszyńskiego 67 50-054 Wroclaw',
               'Lekarz',189,4500,'null'),
              (678,'Karolina','Kulińska','ul.Wielka 33/10 52-430 Wroclaw',
               'Pielegniarka oddzialowa',168,3200,'null'),
              (777,'Agnieszka','Markiewicz','ul.Owsiana 67/14 50-412 Wroclaw',
               'Technik',189,4000,'null'),
              (356,'Zbigniew','Stonoga','ul.Pomorska 45/89 50-012 Wroclaw',
               'Pielegniarka oddzialowa',190,4600,'null'),
              (156,'Patrycja','Krokiet','ul.Fiołkowa 69/39 50-561 Wroclaw',
               'Lekarz',465,2500,'null'),
              (364,'Dagmara','Panek','ul.Traugutta 47/22 50-314 Wroclaw',
               'Technik',465,'null',40),
              (122,'Krystian','Słowacki','ul.Kamienna 23/32 50-503 Wroclaw',
               'Lekarz',190,'null',45),
              (168,'Magdalena','Zapadka','ul.Promienna 14 51-230 Wroclaw',
               'Ordynator',100,'null',62),
              (449,'Wiktor','Orłowski','ul.Dworcowa 13/18 50-302 Wroclaw',
               'Technik',465,'null',41),
              (590,'Tomasz','Zatorski','ul.Malczewskiego 140/5 51-340 Wroclaw',
               'Lekarz',168,'null',42),
              (372,'Leokadia','Wróblewska','ul.Wesoła 45/1 50-550 Wroclaw',
               'Pielęgniarka oddziałowa',189,'null',38),
              (248,'Roman','Fujarski','ul.Świdnicka 37/15 50-308 Wroclaw',
               'Technik',189,'null',60),
              (190,'Sebastian','Darski','ul.Zachodnia 77 50-415 Wroclaw',
               'Ordynator',100,6800,'null'),
              (290,'Ryszard','Pająk','ul. Kminkowa 39/30 52-480 Wroclaw',
               'Lekarz',465,5000,'null'),
              (199,'Olaf','Gąska','ul. Słoneczna 13 50-140 Wroclaw','Lekarz',
               465,5000,'null'),
              (232,'Józef','Samuel','ul. Społeczna 23 51-90 Wroclaw','Lekarz',
               465,5000,'null'),
              (254,'Aleksandra','Kokot','ul.Wschodnia 70-415 Wroclaw',
               'Pielęgiarka oddziałowa',465,3500,'null'),
              (299,'Jan','Król', 'ul.Szmaragdowa 35 54-970 Wrocław','Lekarz',
               465,50,'null')]

def insert_wielu_pracow(lista_pracow):
    cur.executemany('''insert into pracownicy(numer_pracownika,imie,nazwisko,
adres_zamieszkania,etat,id_szefa,pensja_stała,pensja_godzinowa) values
(?,?,?,?,?,?,?,?)''', lista_pracow)


def on_select_wprowadzPracownicy(event=None):
    if event:
        insert_wielu_pracow(pracownicy)
        db.commit()



b5 = tk.Button(frame_5, text="Wprowadź")
b5.pack()
b5.bind("<Button-1>", on_select_wprowadzPracownicy)


#----------------------Lekarze-------------------------------

def create_lekarze():
    with db:
        cur.execute("""CREATE TABLE if not exists lekarze(
id_lekarza INTEGER(10) PRIMARY KEY,
imie TEXT(10) NOT NULL,
nazwisko TEXT(20) NOT NULL,
specjalnosc TEXT(20) NOT NULL,
numer_telefonu INTEGER(12) NOT NULL UNIQUE,
numer_pracownika INTEGER(10) NOT NULL,
id_ordynatora INTEGER(10) NULL,
FOREIGN KEY(numer_pracownika) REFERENCES pracownicy(numer_pracownika)
ON DELETE CASCADE ON UPDATE CASCADE
FOREIGN KEY(id_ordynatora) REFERENCES lekarze(id_lekarza)
ON DELETE CASCADE ON UPDATE CASCADE
);""")

create_lekarze()

def select_all_lekarze():
    with db:
        cur.execute("select * from lekarze")
        print(cur.fetchall())



frame_l1 = ttk.LabelFrame(tab2, text="Dodaj lekarza")
frame_l1.grid(row=1, column=0)
frame_l2 = ttk.LabelFrame(tab2, text="Usuń lekarza")
frame_l2.grid(row=2, column=0)
frame_l3 = ttk.LabelFrame(tab2, text="Pokaż wszystkich lekarzy")
frame_l3.grid(row=0, column=1)
frame_l4 = ttk.LabelFrame(tab2, text="Usuń wszystkich lekarzy")
frame_l4.grid(row=0, column=2)
frame_l5 = ttk.LabelFrame(tab2, text="Wprowadź listę lekarzy")
frame_l5.grid(row=0, column=0)

# Ramka 1 - Dodaj lekarza
etykietal1 = tk.Label(frame_l1, text="Wprowadż dane lekarza")
etykietal1.grid(row=0, columnspan=3)
label_l1 = tk.Label(frame_l1, text="Id lekarza")
label_l2 = tk.Label(frame_l1, text="Imię")
label_l3 = tk.Label(frame_l1, text="Nazwisko")
label_l4 = tk.Label(frame_l1, text="Specjalność")
label_l5 = tk.Label(frame_l1, text="Numer telefonu")
label_l6 = tk.Label(frame_l1, text="Numer Pracownika")
label_l7 = tk.Label(frame_l1, text="Id Ordynatora")

inputIdLekarzal1 = tk.Entry(frame_l1)
inputImiel1 = tk.Entry(frame_l1)
inputNazwiskol1 = tk.Entry(frame_l1)
inputSpecjalnosl1 = tk.Entry(frame_l1)
inputNumerTelefonul1 = tk.Entry(frame_l1)
inputNumerPracownikal1 = tk.Entry(frame_l1)
inputIdOrdynatoral1 = tk.Entry(frame_l1)

label_l1.grid(row=1, sticky='E')  # sticky alligns the text to right (E - east,
label_l2.grid(row=2, sticky='E')  # W - west, N - north, S - south)
label_l3.grid(row=3, sticky='E')
label_l4.grid(row=4, sticky='E')
label_l5.grid(row=5, sticky='E')
label_l6.grid(row=6, sticky='E')
label_l7.grid(row=7, sticky='E')

inputIdLekarzal1.grid(row=1, column=1)
inputImiel1.grid(row=2, column=1)
inputNazwiskol1.grid(row=3, column=1)
inputSpecjalnosl1.grid(row=4, column=1)
inputNumerTelefonul1.grid(row=5, column=1)
inputNumerPracownikal1.grid(row=6, column=1)
inputIdOrdynatoral1.grid(row=7, column=1)

class Lekarze:

    def __init__(self, id_lekarza, imie, nazwisko,
                 specjalnosc, numer_telefonu, numer_pracownika, id_ordynatora):
        self.id_lekarza = id_lekarza
        self.imie = imie
        self.nazwisko = nazwisko
        self.specjalnosc = specjalnosc
        self.numer_telefonu = numer_telefonu
        self.numer_pracownika = numer_pracownika
        self.id_ordynatora = id_ordynatora

def insert_lekarza(lekarz):
    with db:
        cur.execute("""insert into lekarze values (:id_lekarza,
:imie, :nazwisko,:specjalnosc, :numer_telefonu, :numer_pracownika,
:id_ordynatora)""",{'id_lekarza':lekarz.id_lekarza,
                    'imie':lekarz.imie,
                     'nazwisko':lekarz.nazwisko,
                    'specjalnosc':lekarz.specjalnosc,
                    'numer_telefonu':lekarz.numer_telefonu,
                    'numer_pracownika':lekarz.numer_pracownika,
                    'id_ordynatora':lekarz.id_ordynatora})


def dodaj_lekarza():
    nrLek = inputNumerPracownikal1.get()
    imie = inputImiel1.get()
    nazwisko = inputNazwiskol1.get()
    specjalnosc = inputSpecjalnosl1.get()
    NrTel = inputNumerTelefonul1.get()
    Nrprac = inputNumerPracownikal1.get()
    IdOrd = inputIdOrdynatoral1.get()

    lekarz = Lekarze(nrLek, imie, nazwisko, specjalnosc, NrTel, Nrprac, IdOrd)

    insert_lekarza(lekarz)


def on_select_dodaj_lekarza(event=None):
    if event:
        dodaj_lekarza()
        db.commit()


bl1 = tk.Button(frame_l1, text="Dodaj")
bl1.grid(row=10, columnspan=3)
bl1.bind("<Button-1>", on_select_dodaj_lekarza)

# Ramka 2 - Usuń lekarza
etykietal2 = tk.Label(frame_l2, text="Wprowadż Id lekarza")
etykietal2.grid(row=0, columnspan=3)
label_l9 = tk.Label(frame_l2, text="Id lekarza")
inputIdLekarzal2 = tk.Entry(frame_l2)

label_l9.grid(row=1, sticky='E')
inputIdLekarzal2.grid(row=1, column=1)

def delete_lekarza(lekarz):
    with db:
        cur.execute("delete from lekarze where id_lekarza = :id_lekarza",
        {'id_lekarza':lekarz})

def usun_lekarza():
    idLekarza = inputIdLekarzal2.get()

    delete_lekarza(idLekarza)

def on_select_usun_lekarza(event=None):
    if event:
        usun_lekarza()
        db.commit()

bl2 = tk.Button(frame_l2, text="Usuń")
bl2.grid(row=10, columnspan=3)
bl2.bind("<Button-1>", on_select_usun_lekarza)
#
# Ramka 3 - Pokaż wszystkich lekarzy
def select_all_lekarze():
    with db:
        cur.execute("select * from lekarze")
        print(cur.fetchall())

def create_windowl1():
    select = ('select * from lekarze')
    window = Tk()
    window.title("Lekarze - lista rekordów")
    window.geometry('700x300')
    txt = scrolledtext.ScrolledText(window, width=200, height=200)
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')

def pokaz_lekarzy():
    create_windowl1()

def on_select_pokaz_lekarzy(event=None):
    if event:
        pokaz_lekarzy()

etykietal3 = tk.Label(frame_l3)
bl3 = tk.Button(frame_l3, text="Pokaż")
bl3.pack()
bl3.bind("<Button-1>", on_select_pokaz_lekarzy)

# Ramka 4 - Usuń wszystkich lekarzy
def drop_lekarze():
    with db:
        cur.execute("drop table if exists lekarze")

def usun_wszystkich_lekarzy():
    drop_lekarze()
    create_lekarze()

def on_select_usun_wszystkich_lekarzy(event=None):
    if event:
        usun_wszystkich_lekarzy()
        db.commit()


bl4 = tk.Button(frame_l4, text="Usuń")
bl4.pack()
bl4.bind("<Button-1>", on_select_usun_wszystkich_lekarzy)


#Ramka 5

lekarze = [(555,'Marian','Górecki','Ordynator',586904356,189,189),
           (111,'Janusz','Puzdro','Onkolog',726458975,134,168),
           (112,'Piotr','Adam','Kardiolog',765120435,871,189),
           (113,'Patrycja','Krokiet','Pediatra',741963258,156,465),
           (114,'Krystian','Słowacki','Urolog',713647952,122,190),
           (115,'Tomasz','Zatorski','Kardiolog',741258963,590,189),
           (444,'Krzysztof','Krawczyk','Ordynator',790058093,465,465),
           (116,'Ryszard','Pająk','Internista',760430229,390,465),
           (117,'Olaf','Gąska','Internista',710104568,199,465),
           (118,'Józef','Samuel','Internista',792079451,232,465),
           (222,'Sebastian','Darski','Ordynator',678999056,190,190),
           (178,'Magdalena','Zapadka','Ordynator',573822901,168,168)]

def insert_wiele_lekarzy(lista_lekarzy):
    cur.executemany('''insert into lekarze(id_lekarza, imie,
nazwisko,specjalnosc,numer_telefonu,numer_pracownika,id_ordynatora) values
(?,?,?,?,?,?,?)''', lista_lekarzy)



def on_select_wprowadzLekarzy(event=None):
    if event:
        insert_wiele_lekarzy(lekarze)
        db.commit()

bl5 = tk.Button(frame_l5, text="Wprowadź")
bl5.pack()
bl5.bind("<Button-1>", on_select_wprowadzLekarzy)


#----------------------Lozka-------------------------------

def create_lozka():
    with db:
        cur.execute("""CREATE TABLE if not exists lozka(
numer_lozka INTEGER(3) PRIMARY KEY,
numer_pokoju INTEGER(3) NULL,
numer_oddzialu INTEGER(10) NOT NULL,
numer_pacjenta INTEGER(10) NULL,
FOREIGN KEY(numer_oddzialu) REFERENCES oddzialy(numer_oddzialu)
ON DELETE CASCADE ON UPDATE CASCADE
FOREIGN KEY(numer_pacjenta) REFERENCES pacjenci(numer_pacjenta)
ON DELETE CASCADE ON UPDATE CASCADE
);""")

create_lozka()

def select_all_lozka():
    with db:
        cur.execute("select * from lozka")
        print(cur.fetchall())



frame_loz1 = ttk.LabelFrame(tab3, text="Dodaj łóżko")
frame_loz1.grid(row=1, column=0)
frame_loz2 = ttk.LabelFrame(tab3, text="Usuń łóżko")
frame_loz2.grid(row=2, column=0)
frame_loz3 = ttk.LabelFrame(tab3, text="Pokaż wszystkie łóżka")
frame_loz3.grid(row=0, column=1)
frame_loz4 = ttk.LabelFrame(tab3, text="Usuń wszystkie łóżka")
frame_loz4.grid(row=0, column=2)
frame_loz5 = ttk.LabelFrame(tab3, text="Wprowadź listę łóżek")
frame_loz5.grid(row=0, column=0)

# Ramka 1 - Dodaj łóżko
etykietaloz1 = tk.Label(frame_loz1, text="Wprowadż dane łóżka")
etykietaloz1.grid(row=0, columnspan=3)
label_loz1 = tk.Label(frame_loz1, text="Numer łóżka")
label_loz2 = tk.Label(frame_loz1, text="Numer pokoju")
label_loz3 = tk.Label(frame_loz1, text="Numer oddziału")
label_loz4 = tk.Label(frame_loz1, text="Numer pacjenta")

inputNumerLozkaloz1 = tk.Entry(frame_loz1)
inputNumerPokojuloz1 = tk.Entry(frame_loz1)
inputNumerOddzialuloz1 = tk.Entry(frame_loz1)
inputNumerPacjentaloz1 = tk.Entry(frame_loz1)

label_loz1.grid(row=1, sticky='E')  # sticky alligns the text to right (E - east,
label_loz2.grid(row=2, sticky='E')  # W - west, N - north, S - south)
label_loz3.grid(row=3, sticky='E')
label_loz4.grid(row=4, sticky='E')

inputNumerLozkaloz1.grid(row=1, column=1)
inputNumerPokojuloz1.grid(row=2, column=1)
inputNumerOddzialuloz1.grid(row=3, column=1)
inputNumerPacjentaloz1.grid(row=4, column=1)

class Lozka:

    def __init__(self, numer_lozka, numer_pokoju, numer_oddzialu,
                 numer_pacjenta):
        self.numer_lozka = numer_lozka
        self.numer_pokoju = numer_pokoju
        self.numer_oddzialu = numer_oddzialu
        self.numer_pacjenta = numer_pacjenta

def insert_lozko(loz):
    with db:
        cur.execute("""insert into lozka values (:numer_lozka,
:numer_pokoju, :numer_oddzialu, :numer_pacjenta)""",
                    {'numer_lozka':loz.numer_lozka,
                     'numer_pokoju':loz.numer_pokoju,
                     'numer_oddzialu':loz.numer_oddzialu,
                     'numer_pacjenta':loz.numer_pacjenta})

def dodaj_lozko():
    nrLoz = inputNumerLozkaloz1.get()
    nrPok = inputNumerPokojuloz1.get()
    nrOdz = inputNumerOddzialuloz1.get()
    nrPac = inputNumerPacjentaloz1.get()

    lozko = Lozka(nrLoz, nrPok, nrOdz, nrPac)

    insert_lozko(lozko)

def on_select_dodaj_lozko(event=None):
    if event:
        dodaj_lozko()
        db.commit()

bloz1 = tk.Button(frame_loz1, text="Dodaj")
bloz1.grid(row=10, columnspan=3)
bloz1.bind("<Button-1>", on_select_dodaj_lozko)

# Ramka 2 - Usuń łóżka
etykietaloz2 = tk.Label(frame_loz2, text="Wprowadż numer łóżka")
etykietaloz2.grid(row=0, columnspan=3)
label_loz5 = tk.Label(frame_loz2, text="Numer łóżka")
inputNumerLozkaloz2 = tk.Entry(frame_loz2)

label_loz5.grid(row=1, sticky='E')
inputNumerLozkaloz2.grid(row=1, column=1)

def delete_lozko(loz):
    with db:
        cur.execute("delete from lozka where numer_lozka = :numer_lozka",
        {'numer_lozka':loz})

def usun_lozko():
    NumerLozka = inputNumerLozkaloz2.get()

    delete_lozko(NumerLozka)

def on_select_usun_lozko(event=None):
    if event:
        usun_lozko()
        db.commit()

bloz2 = tk.Button(frame_loz2, text="Usuń")
bloz2.grid(row=10, columnspan=3)
bloz2.bind("<Button-1>", on_select_usun_lozko)

# Ramka 3 - Pokaż wszystkie łóżka
def select_all_lozka():
    with db:
        cur.execute("select * from lozka")
        print(cur.fetchall())

def create_windowloz1():
    select = ('select * from lozka')
    window = Tk()
    window.title("Lista łóżek")
    window.geometry('500x600')
    txt = scrolledtext.ScrolledText(window, width=200, height=200)
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')

def pokaz_lozka():
    create_windowloz1()

def on_select_pokaz_lozka(event=None):
    if event:
        pokaz_lozka()

etykietaloz3 = tk.Label(frame_loz3)
bloz3 = tk.Button(frame_loz3, text="Pokaż")
bloz3.pack()
bloz3.bind("<Button-1>", on_select_pokaz_lozka)

# Ramka 4 - Usuń wszystkie lozka

def drop_lozka():
    with db:
        cur.execute("drop table if exists lozka")

def usun_wszystkie_lozka():
    drop_lozka()
    create_lozka()

def on_select_usun_wszystkie_lozka(event=None):
    if event:
        usun_wszystkie_lozka()
        db.commit()


bloz4 = tk.Button(frame_loz4, text="Usuń")
bloz4.pack()
bloz4.bind("<Button-1>", on_select_usun_wszystkie_lozka)


#Ramka 5

lozka = [(201,21,'02',2004),
         (112,14,'01',2020),
         (321,31,'03',2001),
         (123,11,'01',2012),
         (501,51,'05','null'),
         (100,10,'01','null'),
         (200,21,'02','null'),
         (203,21,'02','null'),
         (204,21,'02','null'),
         (209,21,'02','null'),
         (103,10,'01','null'),
         (104,10,'01','null'),
         (105,10,'01','null'),
         (111,10,'01','null'),
         (311,30,'03','null'),
         (313,30,'03','null'),
         (323,31,'03','null'),
         (324,31,'03','null'),
         (345,33,'03','null'),
         (346,33,'03','null'),
         (301,30,'03','null'),
         (302,30,'03','null'),
         (303,30,'03','null'),
         (304,30,'03','null'),
         (121,11,'01','null'),
         (126,11,'01','null'),
         (122,11,'01','null'),
         (124,11,'01','null'),
         (500,51,'05','null'),
         (502,51,'05','null'),
         (503,51,'05','null'),
         (504,51,'05','null'),
         (505,51,'05','null'),
         (506,51,'05','null')]

def insert_wiele_lozek(lista_lozek):
    cur.executemany('''insert into lozka(numer_lozka,
numer_pokoju, numer_oddzialu, numer_pacjenta) values
(?,?,?,?)''', lista_lozek)

def on_select_wprowadzLozka(event=None):
    if event:
        insert_wiele_lozek(lozka)
        db.commit()



bloz5 = tk.Button(frame_loz5, text="Wprowadź")
bloz5.pack()
bloz5.bind("<Button-1>", on_select_wprowadzLozka)

#----------------------Wizyty-------------------------------

def create_wizyty():
    with db:
        cur.execute("""CREATE TABLE if not exists wizyty(
numer_wizyty INTEGER(10) PRIMARY KEY,
data_wizyty TEXT NOT NULL,
id_lekarza INTEGER(10),
numer_pacjenta INTEGER(10),
FOREIGN KEY(id_lekarza) REFERENCES lekarze(id_lekarza)
ON DELETE NO ACTION ON UPDATE CASCADE
FOREIGN KEY(numer_pacjenta) REFERENCES pacjenci(numer_pacjenta)
ON DELETE NO ACTION ON UPDATE CASCADE
);""")


create_wizyty()


def select_all_wizyty():
    with db:
        cur.execute("select * from wizyty")
        print(cur.fetchall())



# Cztery ramki - Wizyty
frameWizyty_1 = ttk.LabelFrame(tab4, text="Dodaj Wizytę")
frameWizyty_1.grid(row=1, column=0)
frameWizyty_2 = ttk.LabelFrame(tab4, text="Usuń Wizytę")
frameWizyty_2.grid(row=2, column=0)
frameWizyty_3 = ttk.LabelFrame(tab4, text="Pokaż wszystkie wizyty")
frameWizyty_3.grid(row=0, column=1)
frameWizyty_4 = ttk.LabelFrame(tab4, text="Usuń wszystkie wizyty")
frameWizyty_4.grid(row=0, column=2)
frameWizyty_5 = ttk.LabelFrame(tab4, text="Wprowadź listę wizyt")
frameWizyty_5.grid(row=0, column=0)

# Ramka 1 - Dodaj wizytę
etykietaWizyty_1 = tk.Label(frameWizyty_1, text="Wprowadż dane wizyty")
etykietaWizyty_1.grid(row=0, columnspan=3)
labelWizyty_11 = tk.Label(frameWizyty_1, text="Numer wizyty")
labelWizyty_12 = tk.Label(frameWizyty_1, text="Data wizyty")
labelWizyty_13 = tk.Label(frameWizyty_1, text="Id lekarza")
labelWizyty_14 = tk.Label(frameWizyty_1, text="Numer pacjenta")

inputNrWizyty = tk.Entry(frameWizyty_1)
inputDataWizyty = tk.Entry(frameWizyty_1)
inputIdLekarza_Wizyty = tk.Entry(frameWizyty_1)
inputNrPacjenta_Wizyty = tk.Entry(frameWizyty_1)

labelWizyty_11.grid(row=1, sticky='E')  # sticky alligns the text to right (E - east,
labelWizyty_12.grid(row=2, sticky='E')  # W - west, N - north, S - south)
labelWizyty_13.grid(row=3, sticky='E')
labelWizyty_14.grid(row=4, sticky='E')

inputNrWizyty.grid(row=1, column=1)
inputDataWizyty.grid(row=2, column=1)
inputIdLekarza_Wizyty.grid(row=3, column=1)
inputNrPacjenta_Wizyty.grid(row=4, column=1)


class Wizyty:

    def __init__(self, numer_wizyty, data_wizyty, id_lekarza,
                 numer_pacjenta):
        self.numer_wizyty = numer_wizyty
        self.data_wizyty = data_wizyty
        self.id_lekarza = id_lekarza
        self.numer_pacjenta = numer_pacjenta


def insert_wizyte(wiz):
    with db:
        cur.execute("""insert into wizyty values (:numer_wizyty, :data_wizyty,
:id_lekarza, :numer_pacjenta)""", {'numer_wizyty': wiz.numer_wizyty,
                                   'data_wizyty': wiz.data_wizyty,
                                   'id_lekarza': wiz.id_lekarza,
                                   'numer_pacjenta': wiz.numer_pacjenta})


def dodaj_wizyte():
    nrWiz = inputNrWizyty.get()
    dataWiz = inputDataWizyty.get()
    idLekarz = inputIdLekarza_Wizyty.get()
    nrPacjenta = inputNrPacjenta_Wizyty.get()

    wizyta = Wizyty(nrWiz, dataWiz, idLekarz, nrPacjenta)

    insert_wizyte(wizyta)


def on_select_dodaj_wizyte(event=None):
    if event:
        dodaj_wizyte()
        db.commit()


b_Wizyty = tk.Button(frameWizyty_1, text="Dodaj")
b_Wizyty.grid(row=10, columnspan=3)
b_Wizyty.bind("<Button-1>", on_select_dodaj_wizyte)

# Ramka 2 - Usuń wizytę
etykietaWizyty_2 = tk.Label(frameWizyty_2, text="Wprowadż numer wizyty")
etykietaWizyty_2.grid(row=0, columnspan=3)
labelWizyty_21 = tk.Label(frameWizyty_2, text="Numer wizyty")
inputNrWizyty2 = tk.Entry(frameWizyty_2)

labelWizyty_21.grid(row=1, sticky='E')
inputNrWizyty2.grid(row=1, column=1)


def delete_wizyte(wiz):
    with db:
        cur.execute("delete from wizyty where numer_wizyty = :numer_wizyty",
                    {'numer_wizyty': wiz})


def usun_wizyte():
    nrWiz = inputNrWizyty2.get()

    delete_wizyte(nrWiz)


def on_select_usun_wizyte(event=None):
    if event:
        usun_wizyte()
        db.commit()


b_Wizyty2 = tk.Button(frameWizyty_2, text="Usuń")
b_Wizyty2.grid(row=10, columnspan=3)
b_Wizyty2.bind("<Button-1>", on_select_usun_wizyte)


# Ramka 3 - Pokaż wszystkie wizyty
def select_all_wizyty():
    with db:
        cur.execute("select * from wizyty")
        print(cur.fetchall())


def create_window_wizyt():
    select = ('select * from wizyty')
    window = Tk()
    window.title("Lista wizyt")
    window.geometry('500x700')
    txt = scrolledtext.ScrolledText(window, width=200, height=200)
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')


def pokaz_wizyty():
    create_window_wizyt()


def on_select_pokaz_wizyty(event=None):
    if event:
        pokaz_wizyty()


b_Wizyty3 = tk.Button(frameWizyty_3, text="Pokaż")
b_Wizyty3.pack()
b_Wizyty3.bind("<Button-1>", on_select_pokaz_wizyty)


# Ramka 4 - Usuń wszystkie wizyty
def drop_wizyty():
    with db:
        cur.execute("drop table if exists wizyty")


def usunWszystkieWizyty():
    drop_wizyty()
    create_wizyty()


def on_select_usunWszystkieWizyty(event=None):
    if event:
        usunWszystkieWizyty()
        db.commit()


b_Wizyty4 = tk.Button(frameWizyty_4, text="Usuń")
b_Wizyty4.pack()
b_Wizyty4.bind("<Button-1>", on_select_usunWszystkieWizyty)


#Ramka 5 - Wprowadź listę wizyt

wizyty = [(1, datetime.date(2018, 12, 13), 113, 2058),
          (2, datetime.date(2018, 11, 24), 113, 2059),
          (3, datetime.date(2018, 10, 30), 113, 2041),
          (4, datetime.date(2018, 9, 12), 113, 2099),
          (5, datetime.date(2018, 8, 9), 113, 2009),
          (6, datetime.date(2018, 7, 1), 113, 2021),
          (7, datetime.date(2015, 12, 11), 113, 2014),
          (8, datetime.date(2015, 11, 9), 114, 2025),
          (10, datetime.date(2015, 10, 24), 117, 2030),
          (11, datetime.date(2015, 9, 30), 117, 2063),
          (12, datetime.date(2015, 8, 14), 444, 2071),
          (13, datetime.date(2015, 7, 25), 116, 2033),
          (14, datetime.date(2015, 6, 15), 117, 2009),
          (15, datetime.date(2015, 5, 30), 118, 2031),
          (16, datetime.date(2015, 4, 12), 444, 2012),
          (17, datetime.date(2015, 3, 9), 444, 2039),
          (18, datetime.date(2015, 2, 1), 118, 2077),
          (19, datetime.date(2015, 1, 24), 116, 2050),
          (20, datetime.date(2017, 3, 13), 117, 2030),
          (21, datetime.date(2015, 12, 20), 117, 2030),
          (23, datetime.date(2016, 8, 21), 117, 2090),
          (24, datetime.date(2015, 11, 30), 117, 2090),
          (25, datetime.date(2015, 5, 30), 118, 2031),
          (26, datetime.date(2015, 2, 22), 118, 2077),
          (27, datetime.date(2018, 5, 13), 118, 2077),
          (28, datetime.date(2018, 11, 20), 116, 2033),
          (29, datetime.date(2015, 5, 18), 116, 2050),
          (30, datetime.date(2016, 9, 13), 116, 2050),
          (50, datetime.date(2015, 7, 13), 117, 2022),
          (31, datetime.date(2017, 2, 8), 117, 2022),
          (32, datetime.date(2018, 3, 1), 117, 2022),
          (33, datetime.date(2015, 10, 30), 117, 2023),
          (34, datetime.date(2017, 12, 17), 118, 2024),
          (35, datetime.date(2013, 1, 21), 118, 2024),
          (36, datetime.date(2017, 5, 24), 118, 2024),
          (37, datetime.date(2016, 12, 23), 118, 2024),
          (38, datetime.date(2018, 11, 30), 116, 2026),
          (39, datetime.date(2018, 3, 8), 116, 2026),
          (40, datetime.date(2016, 4, 9), 116, 2026),
          (41, datetime.date(2018, 6, 5), 117, 2027),
          (42, datetime.date(2015, 2, 11), 118, 2028),
          (43, datetime.date(2017, 11, 17), 118, 2028),
          (44, datetime.date(2018, 7, 23), 116, 2029),
          (45, datetime.date(2015, 8, 1), 116, 2029),
          (46, datetime.date(2017, 9, 20), 116, 2029),
          (47, datetime.date(2018, 11, 19), 117, 2050),
          (58, datetime.date(2018, 12, 13), 118, 2060),
          (59, datetime.date(2016, 9, 11), 118, 2060),
          (85, datetime.date(2015, 12, 13), 113, 2077),
          (91, datetime.date(2015, 10, 1), 113, 2100)]


def insert_wiele_wizyt(lista_wizyt):
    cur.executemany('''insert into wizyty(numer_wizyty,
data_wizyty, id_lekarza, numer_pacjenta) values
(?,?,?,?)''', lista_wizyt)




def on_select_wprowadzWizyty(event=None):
    if event:
        insert_wiele_wizyt(wizyty)
        db.commit()


b_Wizyty5 = tk.Button(frameWizyty_5, text="Wprowadź")
b_Wizyty5.pack()
b_Wizyty5.bind("<Button-1>", on_select_wprowadzWizyty)


#----------------------Pacjenci-------------------------------

def create_pacjenci():
    with db:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS pacjenci(
        numer_pacjenta INTEGER(10) PRIMARY KEY,
        nazwisko TEXT(20) NOT NULL,
        adres TEXT(40) NOT NULL,
        najblizszy_krewny TEXT(30) NULL,
        status TEXT(20) NOT NULL,
        numer_lozka INTEGER(3) NULL,
        id_lekarza INTEGER(10) NOT NULL,
        nazwa_zabiegu TEXT(50) NULL,
        numer_testu INTEGER(10) NULL,
        data_urodzenia TEXT NOT NULL,
        diagnoza TEXT(30) NOT NULL,
        FOREIGN KEY(numer_lozka) REFERENCES lozka(numer_lozka)
        ON DELETE CASCADE ON UPDATE CASCADE
        FOREIGN KEY(id_lekarza) REFERENCES lekarze(id_lekarza)
        ON DELETE CASCADE ON UPDATE CASCADE
        FOREIGN KEY(nazwa_zabiegu) REFERENCES zabiegi(nazwa_zabiegu)
        ON DELETE NO ACTION ON UPDATE CASCADE
        FOREIGN KEY(numer_testu) REFERENCES testy(numer_testu)
        ON DELETE NO ACTION ON UPDATE CASCADE)
        """)


create_pacjenci()


def select_all_pacjenci():
    with db:
        cur.execute("select * from pacjenci")
        print(cur.fetchall())



# Cztery ramki - Pacjenci
framePacjenci_1 = ttk.LabelFrame(tab5, text="Dodaj Pacjenta")
framePacjenci_1.grid(row=1, column=0)
framePacjenci_2 = ttk.LabelFrame(tab5, text="Usuń Pacjenta")
framePacjenci_2.grid(row=2, column=0)
framePacjenci_3 = ttk.LabelFrame(tab5, text="Pokaż wszystkich pacjentów")
framePacjenci_3.grid(row=0, column=1)
framePacjenci_4 = ttk.LabelFrame(tab5, text="Usuń wszystkich pacjentów")
framePacjenci_4.grid(row=0, column=2)
framePacjenci_5 = ttk.LabelFrame(tab5, text="Wprowadź listę pacjentów")
framePacjenci_5.grid(row=0, column=0)

# Ramka 1 - Dodaj pacjenta
etykietaPacjenci_1 = tk.Label(framePacjenci_1, text="Wprowadż dane pacjenta")
etykietaPacjenci_1.grid(row=0, columnspan=3)
labelPacjenci_11 = tk.Label(framePacjenci_1, text="Numer pacjenta")
labelPacjenci_12 = tk.Label(framePacjenci_1, text="Nazwisko")
labelPacjenci_13 = tk.Label(framePacjenci_1, text="Adres")
labelPacjenci_14 = tk.Label(framePacjenci_1, text="Najbliższy krewny")
labelPacjenci_15 = tk.Label(framePacjenci_1, text="Status")
labelPacjenci_16 = tk.Label(framePacjenci_1, text="Numer łóżka")
labelPacjenci_17 = tk.Label(framePacjenci_1, text="ID lekarza")
labelPacjenci_18 = tk.Label(framePacjenci_1, text="Zabieg")
labelPacjenci_19 = tk.Label(framePacjenci_1, text="Numer testu")
labelPacjenci_110 = tk.Label(framePacjenci_1, text="Data urodzenia")
labelPacjenci_111 = tk.Label(framePacjenci_1, text="Diagnoza")

inputNrPacjenta_Pacjenci = tk.Entry(framePacjenci_1)
inputNazwisko_Pacjenci = tk.Entry(framePacjenci_1)
inputAdres_Pacjenci = tk.Entry(framePacjenci_1)
inputKrewny_Pacjenci = tk.Entry(framePacjenci_1)
inputStatus_Pacjenci = tk.Entry(framePacjenci_1)
inputNrLozka_Pacjenci = tk.Entry(framePacjenci_1)
inputIdLekarza_Pacjenci = tk.Entry(framePacjenci_1)
inputZabieg_Pacjenci = tk.Entry(framePacjenci_1)
inputNrTestu_Pacjenci = tk.Entry(framePacjenci_1)
inputDataUr_Pacjenci = tk.Entry(framePacjenci_1)
inputDiagnoza_Pacjenci = tk.Entry(framePacjenci_1)

labelPacjenci_11.grid(row=1, sticky='E')
labelPacjenci_12.grid(row=2, sticky='E')
labelPacjenci_13.grid(row=3, sticky='E')
labelPacjenci_14.grid(row=4, sticky='E')
labelPacjenci_15.grid(row=5, sticky='E')
labelPacjenci_16.grid(row=6, sticky='E')
labelPacjenci_17.grid(row=7, sticky='E')
labelPacjenci_18.grid(row=8, sticky='E')
labelPacjenci_19.grid(row=9, sticky='E')
labelPacjenci_110.grid(row=10, sticky='E')
labelPacjenci_111.grid(row=11, sticky='E')

inputNrPacjenta_Pacjenci.grid(row=1, column=1)
inputNazwisko_Pacjenci.grid(row=2, column=1)
inputAdres_Pacjenci.grid(row=3, column=1)
inputKrewny_Pacjenci.grid(row=4, column=1)
inputStatus_Pacjenci.grid(row=5, column=1)
inputNrLozka_Pacjenci.grid(row=6, column=1)
inputIdLekarza_Pacjenci.grid(row=7, column=1)
inputZabieg_Pacjenci.grid(row=8, column=1)
inputNrTestu_Pacjenci.grid(row=9, column=1)
inputDataUr_Pacjenci.grid(row=10, column=1)
inputDiagnoza_Pacjenci.grid(row=11, column=1)


class Pacjenci:

    def __init__(self, numer_pacjenta, nazwisko, adres,
                 najblizszy_krewny, status, numer_lozka, id_lekarza,
                 nazwa_zabiegu, numer_testu, data_urodzenia, diagnoza):
        self.numer_pacjenta = numer_pacjenta
        self.nazwisko = nazwisko
        self.adres = adres
        self.najblizszy_krewny = najblizszy_krewny
        self.status = status
        self.numer_lozka = numer_lozka
        self.id_lekarza = id_lekarza
        self.nazwa_zabiegu = nazwa_zabiegu
        self.numer_testu = numer_testu
        self.ndata_urodzenia = data_urodzenia
        self.diagnoza = diagnoza


def insert_pacjenci(pacj):
    with db:
        cur.execute("""insert into pacjenci values (:numer_pacjenta,
                    :nazwisko, :adres, :najblizszy_krewny, :status,
                    :numer_lozka, :id_lekarza, :nazwa_zabiegu, :numer_testu,
                    :data_urodzenia, :diagnoza)""",
                    {'numer_pacjenta': pacj.numer_pacjenta,
                     'nazwisko': pacj.nazwisko,
                     'adres': pacj.adres,
                     'najblizszy_krewny': pacj.najblizszy_krewny,
                     'status': pacj.status,
                     'numer_lozka': pacj.numer_lozka,
                     'id_lekarza': pacj.id_lekarza,
                     'nazwa_zabiegu': pacj.nazwa_zabiegu,
                     'numer_testu': pacj.numer_testu,
                     'data_urodzenia': pacj.data_urodzenia,
                     'diagnoza': pacj.diagnoza})


def dodaj_pacjenta():
    nrPacjenta = inputNrPacjenta_Pacjenci.get()
    nazwisko = inputNazwisko_Pacjenci.get()
    adres = inputAdres_Pacjenci.get()
    krewny = inputKrewny_Pacjenci.get()
    status = inputStatus_Pacjenci.get()
    nrlozka = inputNrLozka_Pacjenci.get()
    idLekarza = inputIdLekarza_Pacjenci.get()
    zabieg = inputZabieg_Pacjenci.get()
    nrTestu = inputNrTestu_Pacjenci.get()
    dataUr = inputDataUr_Pacjenci.get()
    diag = inputDiagnoza_Pacjenci.get()

    pacjent = Pacjenci(nrPacjenta, nazwisko, adres, krewny, status, nrlozka,
                       idLekarza, zabieg, nrTestu, dataUr, diag)

    insert_pacjenci(pacjent)


def on_select_dodaj_pacjenta(event=None):
    if event:
        dodaj_pacjenta()
        db.commit()


b_Pacjenci = tk.Button(framePacjenci_1, text="Dodaj")
b_Pacjenci.grid(row=12, columnspan=3)
b_Pacjenci.bind("<Button-1>", on_select_dodaj_pacjenta)

# Ramka 2 - Usuń pacjenta
etykietaPacjenci_2 = tk.Label(framePacjenci_2, text="Wprowadż numer pacjenta")
etykietaPacjenci_2.grid(row=0, columnspan=3)
labelPacjenci_21 = tk.Label(framePacjenci_2, text="Numer pacjenta")
inputNrPacjenta_Pacjenci2 = tk.Entry(framePacjenci_2)

labelPacjenci_21.grid(row=1, sticky='E')
inputNrPacjenta_Pacjenci2.grid(row=1, column=1)


def delete_pacjenci(pacj):
    with db:
        cur.execute("""delete from pacjenci where
                    numer_pacjenta = :numer_pacjenta""",
                    {'numer_pacjenta': pacj})


def usun_pacjenta():
    nrPacjenta = inputNrPacjenta_Pacjenci2.get()

    delete_pacjenci(nrPacjenta)


def on_select_usun_pacjenta(event=None):
    if event:
        usun_pacjenta()
        db.commit()


b_Pacjenci2 = tk.Button(framePacjenci_2, text="Usuń")
b_Pacjenci2.grid(row=10, columnspan=3)
b_Pacjenci2.bind("<Button-1>", on_select_usun_pacjenta)


# Ramka 3 - Pokaż wszystkich pacjentów
def select_all_pacjenci():
    with db:
        cur.execute("select * from pacjenci")
        print(cur.fetchall())


def create_window_pacjenci():
    select = ('select * from pacjenci')
    window = Tk()
    window.title("Lista pacjentów")
    window.geometry('1200x500')
    txt = scrolledtext.ScrolledText(window, width=200, height=200)
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')

def pokaz_pacjenci():
    create_window_pacjenci()


def on_select_pokaz_pacjenci(event=None):
    if event:
        pokaz_pacjenci()


b_Pacjenci3 = tk.Button(framePacjenci_3, text="Pokaż")
b_Pacjenci3.pack()
b_Pacjenci3.bind("<Button-1>", on_select_pokaz_pacjenci)


# Ramka 4 - Usuń wszystkich pacjentów
def drop_pacjenci():
    with db:
        cur.execute("drop table if exists pacjenci")


def usunWszystkichPacjenci():
    drop_pacjenci()
    create_pacjenci()


def on_select_usunWszystkichPacjenci(event=None):
    if event:
        usunWszystkichPacjenci()
        db.commit()


b_Pacjenci4 = tk.Button(framePacjenci_4, text="Usuń")
b_Pacjenci4.pack()
b_Pacjenci4.bind("<Button-1>", on_select_usunWszystkichPacjenci)



#Ramka 5 - Wprowadź listę pacjentów

pacjent = [(
           2030, 'Krzewiński', 'ul. Krzywoustego 58/4 56-320 Wrocław', 'Anna Krzewińska-matka', 'pacjent przyjęty', 303,
           117, 'Usunięcie nerki', 5236, '1994-12-24', 'rak nerki'),
           (2014, 'Kaliciak', 'ul. Świętokrzyska 34/16 50-325 Wrocław', 'Mariola Kaliciak-matka', 'pacjent przyjęty',
            666, 113, 'Wycięcie wyrostka', 4125, '1990-11-13', 'zapelenie wyrostka'),
           (2025, 'Grzyb', 'ul. Kosmonautow 58/3 52-323 Wrocław', 'Antonina Grzyb-żona', 'pacjent przyjęty', 302, 114,
            'Usunięcie nerki', '', '2000-10-12', 'rak nerki'),
           (2063, 'Fasolka', 'ul. Działkowa 12 54-350 Wrocław', 'Jakub Fasolka-mąż', 'pacjent nieprzyjęty', '', 117, '',
            '', '1968-09-20', 'miażdżycowe zapalenie tętnic'),
           (2071, 'Żuraw', 'ul. Magnoliowa 34 57-380 Wrocław', 'Jagoda Żuraw-córka', 'pacjent nieprzyjęty', '', 444, '',
            '', '1994-08-06', 'alergia pokarmowa'),
           (
           2033, 'Stasiuk', 'ul. Studzienna 29/14 50-080 Wrocław', 'Marcin Stasiuk-syn', 'pacjent przyjęty', '501', 116,
           '', '7436', '1978-07-06', 'zapalenie żołądka'),
           (2090, 'Kownacki', 'ul. Klonowa 36/11 51-280 Wrocław', 'Laura Kownacka-żona', 'pacjent przyjęty', '146', 117,
            '', '4298', '1990-06-13', 'zwichnięcie barku'),
           (2031, 'Dzban', 'ul. Rycerska 15/19 50-377 Wrocław', 'Suzanna Colins -żona', 'pacjent przyjęty', '256', 118,
            '', '', '1978-05-10', 'zpalanie stawów'),
           (2012, 'Sokół', 'ul. Stylowa 13b 51-322 Wrocław', 'Konrad Sokół-syn', 'pacjent nieprzyjęty', '', 444, '', '',
            '1970-04-11', 'migrena'),
           (2039, 'Sumienna', 'ul. Potok 3 52-380 Wrocław', 'Marek Sumienny-córka', 'pacjent przyjęty', '434', 444, '',
            '6598', '1975-03-12', 'kolka'),
           (2077, 'Kamiński', 'ul. Matejki 24/12 53-318 Wrocław', 'Jagoda Kamińska-matka', 'pacjent przyjęty', '678',
            118, '', '8426', '1980-02-23', 'złamanie obojczyka'),
           (2058, 'Kliniec', 'ul. Świętokrzyska 47/1 54-098 Wrocław', 'Katarzyna Kliniec-matka', 'pacjent nieprzyjęty',
            '', 113, '', '', '2001-01-09', 'cukrzyca'),
           (2059, 'Gołaszewska', 'ul. Beskidzka 29/3 55-296 Wrocław', 'Patrycja Gołaszewska-matka',
            'pacjent nieprzyjęty', '', 113, '', '', '2002-02-04', 'cukrzyca'),
           (2041, 'Grządkowska', 'ul. Bieszczadzka 12/12 56-879 Wrocław', 'Paulina Grządkowska-matka',
            'pacjent nieprzyjęty', '', 113, '', '', '2005-03-01', 'cukrzyca'),
           (
           2099, 'Cuch', 'ul. Tatrzańska 34/11 57-643 Wrocław', 'Piotr Cuch-ojciec', 'pacjent nieprzyjęty', '', 113, '',
           '', '2006-04-21', 'cukrzyca'),
           (2009, 'Paluszczak', 'ul. Łowicka 11/65 58-234 Wrocław', 'Przemek Paluszczak-ojciec', 'pacjent nieprzyjęty',
            '', 113, '', '', '2004-05-23', 'cukrzyca'),
           (2021, 'Mański', 'ul. Liliowa 33/28 51-111 Wrocław', 'Paweł Mański-ojciec', 'pacjent nieprzyjęty', '', 113,
            '', '', '2006-06-11', 'cukrzyca'),
           (2022, 'Sokół', 'ul. Czarna 31 51-647 Wrocław', 'Karol Sokół-ojciec', 'pacjent nieprzyjęty', '', '118', '',
            '', '1995-06-11', 'zapalenie ucha środkowego'),
           (2023, 'Sobótka', 'ul. Krasickiego 11 52-253 Wrocław', 'Marian Sobótka-ojciec', 'pacjent nieprzyjęty', '',
            116, '', '', '1999-11-01', 'grypa'),
           (
           2024, 'Superson', 'ul. Kwiatowa 23 56-546 Wrocław', 'Mietek Superson-ojciec', 'pacjent nieprzyjęty', '', 117,
           '', '', '1979-03-17', 'zapalenie migdałków'),
           (2026, 'Seweryn', 'ul. Stolnicza 9 59-354 Wrocław', 'Tymon Seweryn-ojciec', 'pacjent nieprzyjęty', '', 118,
            '', '', '1983-12-16', 'zapelenie tchawicy'),
           (2027, 'Szal', 'ul. Strzegomska 33 56-164 Wrocław', 'Ewa Szal-matka', 'pacjent nieprzyjęty', '', 116, '', '',
            '2000-07-05', 'zapalenie spojówki'),
           (
           2028, 'Soczek', 'ul. Stara 10 51-546 Wrocław', 'Kamila Soczek-matka', 'pacjent nieprzyjęty', '', 117, '', '',
           '1991-01-21', 'zapalenie zatok'),
           (2029, 'Sanki', 'ul. Ukryta 22 53-758 Wrocław', 'Ksawery Sanki-syn', 'pacjent nieprzyjęty', '', 118, '', '',
            '1990-06-23', 'zatrucie pokarmowe'),
           (2050, 'Serwetka', 'ul. Cicha 44 53-869 Wrocław', 'Olga Serwetka-matka', 'pacjent nieprzyjęty', '', 116, '',
            '', '2001-04-03', 'grypa'),
           (
           2060, 'Skórka', 'ul. Słoneczna 20 53-756 Wrocław', 'Janina Słomka-matka', 'pacjent nieprzyjęty', '', 117, '',
           '', '1994-10-11', 'zapalenie gardła')]


def insert_wiele_pacjenci():
    with db:
        cur.executemany('INSERT INTO pacjenci VALUES(?,?,?,?,?,?,?,?,?,?,?)', pacjent)




def on_select_wprowadzPacjenci(event=None):
    if event:
        insert_wiele_pacjenci()
        db.commit()


b_Pacjenci5 = tk.Button(framePacjenci_5, text="Wprowadź")
b_Pacjenci5.pack()
b_Pacjenci5.bind("<Button-1>", on_select_wprowadzPacjenci)


#----------------------Technicy-------------------------------

def create_technik():
    with db:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS technik (
            numer_technika INTEGER(10) PRIMARY KEY,
            nazwisko TEXT(10) NOT NULL,
            imie TEXT(10) NOT NULL,
            numer_pracownika INTEGER(10) NOT NULL,
            FOREIGN KEY(numer_pracownika) REFERENCES pracownicy(numer_pracownika)
            ON DELETE CASCADE ON UPDATE CASCADE
            )""")


create_technik()


def select_all_technicy():
    with db:
        cur.execute("select * from technik")
        print(cur.fetchall())




# Cztery ramki - Technicy
frameTechnicy_1 = ttk.LabelFrame(tab6, text="Dodaj Technika")
frameTechnicy_1.grid(row=1, column=0)
frameTechnicy_2 = ttk.LabelFrame(tab6, text="Usuń Technika")
frameTechnicy_2.grid(row=2, column=0)
frameTechnicy_3 = ttk.LabelFrame(tab6, text="Pokaż wszystkich techników")
frameTechnicy_3.grid(row=0, column=1)
frameTechnicy_4 = ttk.LabelFrame(tab6, text="Usuń wszystkich techników")
frameTechnicy_4.grid(row=0, column=2)
frameTechnicy_5 = ttk.LabelFrame(tab6, text="Wprowadź listę techników")
frameTechnicy_5.grid(row=0, column=0)

# Ramka 1 - Dodaj technika
etykietaTechnicy_1 = tk.Label(frameTechnicy_1, text="Wprowadż dane pacjenta")
etykietaTechnicy_1.grid(row=0, columnspan=3)
labelTechnicy_11 = tk.Label(frameTechnicy_1, text="Numer technika")
labelTechnicy_12 = tk.Label(frameTechnicy_1, text="Nazwisko")
labelTechnicy_13 = tk.Label(frameTechnicy_1, text="Imię")
labelTechnicy_14 = tk.Label(frameTechnicy_1, text="Numer pracownika")

inputNrTechnika_Technicy = tk.Entry(frameTechnicy_1)
inputNazwisko_Technicy = tk.Entry(frameTechnicy_1)
inputImie_Technicy = tk.Entry(frameTechnicy_1)
inputNrPracownika_Technicy = tk.Entry(frameTechnicy_1)

labelTechnicy_11.grid(row=1, sticky='E')
labelTechnicy_12.grid(row=2, sticky='E')
labelTechnicy_13.grid(row=3, sticky='E')
labelTechnicy_14.grid(row=4, sticky='E')

inputNrTechnika_Technicy.grid(row=1, column=1)
inputNazwisko_Technicy.grid(row=2, column=1)
inputImie_Technicy.grid(row=3, column=1)
inputNrPracownika_Technicy.grid(row=4, column=1)


class Technicy:

    def __init__(self, numer_technika, nazwisko, imie, numer_pracownika):
        self.numer_technika = numer_technika
        self.nazwisko = nazwisko
        self.imie = imie
        self.numer_pracownika = numer_pracownika


def insert_technik(tech):
    with db:
        cur.execute("""insert into technik values (:numer_technika,
                    :nazwisko, :imie, :numer_pracownika)""",
                    {'numer_technika': tech.numer_technika,
                     'nazwisko': tech.nazwisko,
                     'imie': tech.imie,
                     'numer_pracownika': tech.numer_pracownika})


def dodaj_technika():
    nrTech = inputNrTechnika_Technicy.get()
    nazwisko = inputNazwisko_Technicy.get()
    imie = inputImie_Technicy.get()
    nrPracownika = inputNrPracownika_Technicy.get()

    technik = Technicy(nrTech, nazwisko, imie, nrPracownika)

    insert_technik(technik)


def on_select_dodaj_technika(event=None):
    if event:
        dodaj_technika()
        db.commit()


b_Technicy = tk.Button(frameTechnicy_1, text="Dodaj")
b_Technicy.grid(row=5, columnspan=3)
b_Technicy.bind("<Button-1>", on_select_dodaj_technika)

# Ramka 2 - Usuń technika
etykietaTechnicy__2 = tk.Label(frameTechnicy_2, text="Wprowadż numer technika")
etykietaTechnicy__2.grid(row=0, columnspan=3)
labelTechnicy_21 = tk.Label(frameTechnicy_2, text="Numer technika")
inputNrPracownika_Technicy2 = tk.Entry(frameTechnicy_2)

labelTechnicy_21.grid(row=1, sticky='E')
inputNrPracownika_Technicy2.grid(row=1, column=1)


def delete_technik(tech):
    with db:
        cur.execute("""delete from technik where
                    numer_technika = :numer_technika""",
                    {'numer_technika': tech})


def usun_technika():
    nrTech = inputNrPracownika_Technicy2.get()

    delete_technik(nrTech)


def on_select_usun_technika(event=None):
    if event:
        usun_technika()
        db.commit()


b_Technicy2 = tk.Button(frameTechnicy_2, text="Usuń")
b_Technicy2.grid(row=10, columnspan=3)
b_Technicy2.bind("<Button-1>", on_select_usun_technika)


# Ramka 3 - Pokaż wszystkich pacjentów
def select_all_technicy():
    with db:
        cur.execute("select * from technik")
        print(cur.fetchall())


def create_window_technicy():
    select = ('select * from technik')
    window = Tk()
    window.title("Lista techników")
    window.geometry('400x200')
    txt = scrolledtext.ScrolledText(window, width=200, height=200)
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')


def pokaz_technicy():
    create_window_technicy()


def on_select_pokaz_technicy(event=None):
    if event:
        pokaz_technicy()


b_Technicy3 = tk.Button(frameTechnicy_3, text="Pokaż")
b_Technicy3.pack()
b_Technicy3.bind("<Button-1>", on_select_pokaz_technicy)


# Ramka 4 - Usuń wszystkich techników
def drop_technik():
    with db:
        cur.execute("drop table if exists technik")


def usunWszystkichTechnicy():
    drop_technik()
    create_technik()


def on_select_usunWszystkichTechnicy(event=None):
    if event:
        usunWszystkichTechnicy()
        db.commit()


b_Technicy4 = tk.Button(frameTechnicy_4, text="Usuń")
b_Technicy4.pack()
b_Technicy4.bind("<Button-1>", on_select_usunWszystkichTechnicy)




#Ramka 5 - Wprowadź listę techników

technik = [(11, 'Kowalski', 'Andrzej', 123),
           (12, 'Agnieszka', 'Markiewicz', 777),
           (13, 'Dagmara', 'Panek', 364),
           (14, 'Roman', 'Fujarski', 248),
           (15, 'Orłowski', 'Wiktor', 449)]


def insert_wielu_technik():
    with db:
        cur.executemany('INSERT INTO technik (numer_technika,nazwisko,imie,numer_pracownika) VALUES (?,?,?,?)', technik)




def on_select_wprowadzTechnicy(event=None):
    if event:
        insert_wielu_technik()
        db.commit()


b_Technicy5 = tk.Button(frameTechnicy_5, text="Wprowadź")
b_Technicy5.pack()
b_Technicy5.bind("<Button-1>", on_select_wprowadzTechnicy)






#----------------------Zabiegi-------------------------------

def create_zabiegi():
    with db:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS zabiegi (
            nazwa_zabiegu TEXT(50) PRIMARY KEY,
            data TEXT NOT NULL,
            czas TEXT NOT NULL,
            wynik TEXT(200) NOT NULL,
            id_lekarza INTEGER(10) NOT NULL,
            numer_pacjenta INTEGER(10) NOT NULL,
            FOREIGN KEY(id_lekarza) REFERENCES lekarze(id_lekarza)
            ON DELETE NO ACTION ON UPDATE CASCADE
            FOREIGN KEY(numer_pacjenta) REFERENCES pacjenci(numer_pacjenta)
            ON DELETE NO ACTION ON UPDATE CASCADE)
            """)

create_zabiegi()

def select_all_zabiegi():
    with db:
        cur.execute("select * from zabiegi")
        print(cur.fetchall())


frame_z1 = ttk.LabelFrame(tab7, text="Dodaj zabieg")
frame_z1.grid(row=1, column=0)
frame_z2 = ttk.LabelFrame(tab7, text="Usuń zabieg")
frame_z2.grid(row=2, column=0)
frame_z3 = ttk.LabelFrame(tab7, text="Pokaż wszystkie zabiegi")
frame_z3.grid(row=0, column=1)
frame_z4 = ttk.LabelFrame(tab7, text="Usuń wszystkie zabiegi")
frame_z4.grid(row=0, column=2)
frame_z5 = ttk.LabelFrame(tab7, text="Wprowadź listę zabiegów")
frame_z5.grid(row=0, column=0)

# Ramka 1 - Dodaj zabieg
etykietaz1 = tk.Label(frame_z1, text="Wprowadż dane zabiegu")
etykietaz1.grid(row=0, columnspan=3)
label_z1 = tk.Label(frame_z1, text="Nazwa zabiegu")
label_z2 = tk.Label(frame_z1, text="Data")
label_z3 = tk.Label(frame_z1, text="Czas")
label_z4 = tk.Label(frame_z1, text="Wynik")
label_z5 = tk.Label(frame_z1, text="Id lekarza wykonującego zabieg")
label_z6 = tk.Label(frame_z1, text="Numer pacjenta")

inputNazwaZabieguz1 = tk.Entry(frame_z1)
inputDataz1 = tk.Entry(frame_z1)
inputCzasz1 = tk.Entry(frame_z1)
inputWinikz1 = tk.Entry(frame_z1)
inputIdLekarzaz1 = tk.Entry(frame_z1)
inputNumerPacjentaz1 = tk.Entry(frame_z1)

label_z1.grid(row=1, sticky='E')  # sticky alligns the text to right (E - east,
label_z2.grid(row=2, sticky='E')  # W - west, N - north, S - south)
label_z3.grid(row=3, sticky='E')
label_z4.grid(row=4, sticky='E')
label_z5.grid(row=5, sticky='E')
label_z6.grid(row=6, sticky='E')

inputNazwaZabieguz1.grid(row=1, column=1)
inputDataz1.grid(row=2, column=1)
inputCzasz1.grid(row=3, column=1)
inputWinikz1.grid(row=4, column=1)
inputIdLekarzaz1.grid(row=5, column=1)
inputNumerPacjentaz1.grid(row=6, column=1)

class Zabiegi:

    def __init__(self, nazwa_zabiegu, data, czas,
                 wynik, id_lekarza, numer_pacjenta):
        self.nazwa_zabiegu = nazwa_zabiegu
        self.data = data
        self.czas = czas
        self.wynik = wynik
        self.id_lekarza = id_lekarza
        self.numer_pacjenta = numer_pacjenta

def insert_zabiegi(zab):
    with db:
        cur.execute("""insert into zabiegi values (:nazwa_zabiegu,
                    :data, :czas, :wynik, :id_lekarza, :numer_pacjenta)""",
                    {'nazwa_zabiegu':zab.nazwa_zabiegu,
                    'data':zab.data,
                    'czas':zab.czas,
                    'wynik':zab.wynik,
                    'id_lekarza':zab.id_lekarza,
                    'numer_pacjenta':zab.numer_pacjenta})

def dodaj_zabieg():
    nazwaz1 = inputNazwaZabieguz1.get()
    dataz1 = inputDataz1.get()
    czasz1 = inputCzasz1.get()
    wynikz1 = inputWinikz1.get()
    IdLekz1 = inputIdLekarzaz1.get()
    NrPacz1 = inputNumerPacjentaz1.get()

    zabi = Zabiegi(nazwaz1, dataz1, czasz1, wynikz1, IdLekz1, NrPacz1)

    insert_zabiegi(zabi)

def on_select_dodaj_zabieg(event=None):
    if event:
        dodaj_zabieg()
        db.commit()

bz1 = tk.Button(frame_z1, text="Dodaj")
bz1.grid(row=10, columnspan=3)
bz1.bind("<Button-1>", on_select_dodaj_zabieg)

# Ramka 2 - Usuń zabiegi
etykietaz2 = tk.Label(frame_z2, text="Wprowadż nazwę zabiegu")
etykietaz2.grid(row=0, columnspan=3)
label_z7 = tk.Label(frame_z2, text="Nazwa zabiegu")
inputNazwaZabieguz2 = tk.Entry(frame_z2)

label_z7.grid(row=1, sticky='E')
inputNazwaZabieguz2.grid(row=1, column=1)

def delete_zabiegi(zab):
    with db:
        cur.execute("""delete from zabiegi where
                    nazwa_zabiegu = :nazwa_zabiegu""",
             {'nazwa_zabiegu':zab})

def usun_zabieg():
    NazwaZabiegu = inputNazwaZabieguz2.get()

    delete_zabiegi(NazwaZabiegu)

def on_select_usun_zabieg(event=None):
    if event:
        usun_zabieg()
        db.commit()

bz2 = tk.Button(frame_z2, text="Usuń")
bz2.grid(row=10, columnspan=3)
bz2.bind("<Button-1>", on_select_usun_zabieg)

# Ramka 3 - Pokaż wszystkie zabiegi

def select_all_zabiegi():
    with db:
        cur.execute("select * from zabiegi")
        print(cur.fetchall())

def create_windowz1():
    select = ('select * from zabiegi')
    window = Tk()
    window.title("Lista zabiegów")
    window.geometry('900x200')
    txt = scrolledtext.ScrolledText(window, width=200, height=200)
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')

def pokaz_zabiegi():
    create_windowz1()

def on_select_pokaz_zabiegi(event=None):
    if event:
        pokaz_zabiegi()

etykietaz3 = tk.Label(frame_z3)
bz3 = tk.Button(frame_z3, text="Pokaż")
bz3.pack()
bz3.bind("<Button-1>", on_select_pokaz_zabiegi)

 # Ramka 4 - Usuń wszystkie zabiegi

def drop_zabiegi():
    with db:
        cur.execute("drop table if exists zabiegi")

def usun_wszystkie_zabiegi():
    drop_zabiegi()
    create_zabiegi()

def on_select_usun_wszystkie_zabiegi(event=None):
    if event:
        usun_wszystkie_zabiegi()
        db.commit()


bz4 = tk.Button(frame_z4, text="Usuń")
bz4.pack()
bz4.bind("<Button-1>", on_select_usun_wszystkie_zabiegi)


#Ramka 5 - Wprowadź listę zabiegów

zabieg=[('Wycięcie wyrostka',datetime.date(2019,1,3),'12:30:00','wyrostek usunięty',113,2014),
('Wstawienie zastawki',datetime.date(2018,12,28),'14:00:00','zastawka wstawiona',112,2001),
('Bajpasy',datetime.date(2018,12,31),'17:00:00','zgon',115,2011),
('Biopsja pęcherza',datetime.date(2018,12,24),'19:00:00','wycinek pobrany',114,2025),
('Usunięcie nerki',datetime.date(2019,1,8),'13:00:00','usunięta lewa nerka',117,2030)]

def insert_wiele_zabiegi():
    with db:
        cur.executemany('INSERT INTO zabiegi (nazwa_zabiegu,data,czas,wynik,id_lekarza,numer_pacjenta) VALUES (?,?,?,?,?,?)', zabieg )




def on_select_wprowadxZabiegi(event=None):
    if event:
        insert_wiele_zabiegi()
        db.commit()


bz5 = tk.Button(frame_z5, text="Wprowadź")
bz5.pack()
bz5.bind("<Button-1>", on_select_wprowadxZabiegi)



#----------------------Testy-------------------------------

def create_testy():
    with db:
        cur.execute("""CREATE TABLE if not exists testy(
            id_testu INTEGER(10) PRIMARY KEY,
            data DATE NOT NULL,
            wynik TEXT(200) NOT NULL,
            numer_pacjenta INTEGER(10) NOT NULL,
            numer_technika INTEGER(10) NOT NULL,
            FOREIGN KEY(numer_pacjenta) REFERENCES pacjenci(numer_pacjenta)
            ON DELETE NO ACTION ON UPDATE CASCADE
            FOREIGN KEY(numer_technika) REFERENCES technik(numer_technika)
            ON DELETE NO ACTION ON UPDATE CASCADE)
            """)


create_testy()


def select_all_testy():
    with db:
        cur.execute("select * from testy")
        print(cur.fetchall())




# Pięć ramkek - Testy
frameTesty_1 = ttk.LabelFrame(tab8, text="Dodaj Test")
frameTesty_1.grid(row=1, column=0)
frameTesty_2 = ttk.LabelFrame(tab8, text="Usuń Test")
frameTesty_2.grid(row=2, column=0)
frameTesty_3 = ttk.LabelFrame(tab8, text="Pokaż wszystkie testy")
frameTesty_3.grid(row=0, column=1)
frameTesty_4 = ttk.LabelFrame(tab8, text="Usuń wszystkie testy")
frameTesty_4.grid(row=0, column=2)
frameTesty_5 = ttk.LabelFrame(tab8, text="Wprowadź listę testów")
frameTesty_5.grid(row=0, column=0)

# Ramka 1 - Dodaj Test
etykietaTesty_1 = tk.Label(frameTesty_1, text="Wprowadż dane testu")
etykietaTesty_1.grid(row=0, columnspan=3)
labelTesty_11 = tk.Label(frameTesty_1, text="Numer testu")
labelTesty_12 = tk.Label(frameTesty_1, text="Data wykonania")
labelTesty_13 = tk.Label(frameTesty_1, text="Wynik")
labelTesty_14 = tk.Label(frameTesty_1, text="Numer pacjenta")
labelTesty_15 = tk.Label(frameTesty_1, text="Numer technika")

inputIdtestu_Testy = tk.Entry(frameTesty_1)
inputData_Testy = tk.Entry(frameTesty_1)
inputWynik_Testy = tk.Entry(frameTesty_1)
inputNrPacjenta_Testy = tk.Entry(frameTesty_1)
inputNrTechnika_Testy = tk.Entry(frameTesty_1)

labelTesty_11.grid(row=1, sticky='E')
labelTesty_12.grid(row=2, sticky='E')
labelTesty_13.grid(row=3, sticky='E')
labelTesty_14.grid(row=4, sticky='E')
labelTesty_15.grid(row=5, sticky='E')

inputIdtestu_Testy.grid(row=1, column=1)
inputData_Testy.grid(row=2, column=1)
inputWynik_Testy.grid(row=3, column=1)
inputNrPacjenta_Testy.grid(row=4, column=1)
inputNrTechnika_Testy.grid(row=5, column=1)


class Testy:

    def __init__(self, id_testu, data, wynik,
                 numer_pacjenta, numer_technika):
        self.id_testu = id_testu
        self.data = data
        self.wynik = wynik
        self.numer_pacjenta = numer_pacjenta
        self.numer_technika = numer_technika


def insert_testy(testy):
    with db:
        cur.execute("""insert into testy values (:id_testu,
                    :data, :wynik, :numer_pacjenta, :numer_technika)""",
                    {'id_testu': testy.id_testu,
                     'data': testy.data,
                     'wynik': testy.wynik,
                     'numer_pacjenta': testy.numer_pacjenta,
                     'numer_technika': testy.numer_technika})


def dodaj_test():
    idTestu = inputIdtestu_Testy.get()
    data = inputData_Testy.get()
    wynik = inputWynik_Testy.get()
    nrPacjenta = inputNrPacjenta_Testy.get()
    nrTechnik = inputNrTechnika_Testy.get()

    test = Testy(idTestu, data, wynik, nrPacjenta, nrTechnik)

    insert_testy(test)


def on_select_dodaj_test(event=None):
    if event:
        dodaj_test()
        db.commit()


b_Testy = tk.Button(frameTesty_1, text="Dodaj")
b_Testy.grid(row=6, columnspan=3)
b_Testy.bind("<Button-1>", on_select_dodaj_test)

# Ramka 2 - Usuń test
etykietaTesty_2 = tk.Label(frameTesty_2, text="Wprowadż numer testu")
etykietaTesty_2.grid(row=0, columnspan=3)
labelTesty_21 = tk.Label(frameTesty_2, text="Numer testu")
inputIdTestu_Testy2 = tk.Entry(frameTesty_2)

labelTesty_21.grid(row=1, sticky='E')
inputIdTestu_Testy2.grid(row=1, column=1)


def delete_test(test):
    with db:
        cur.execute("""delete from testy where
                    id_testu = :id_testu""",
                    {'id_testu': test})


def usun_test():
    nrTestu = inputIdTestu_Testy2.get()

    delete_test(nrTestu)


def on_select_usun_test(event=None):
    if event:
        usun_test()
        db.commit()


b_Testy2 = tk.Button(frameTesty_2, text="Usuń")
b_Testy2.grid(row=10, columnspan=3)
b_Testy2.bind("<Button-1>", on_select_usun_test)


# Ramka 3 - Pokaż wszystkie testy
def select_all_testy():
    with db:
        cur.execute("select * from testy")
        print(cur.fetchall())


def create_window_testy():
    select = ('select * from testy')
    window = Tk()
    window.title("Lista wykonanych testów")
    window.geometry('600x200')
    txt = scrolledtext.ScrolledText(window, width=200, height=200)
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')


def pokaz_testy():
    create_window_testy()


def on_select_pokaz_testy(event=None):
    if event:
        pokaz_testy()



b_Testy3 = tk.Button(frameTesty_3, text="Pokaż")
b_Testy3.pack()
b_Testy3.bind("<Button-1>", on_select_pokaz_testy)


# Ramka 4 - Usuń wszystkie testy
def drop_testy():
    with db:
        cur.execute("drop table if exists testy")


def usunWszystkieTesty():
    drop_testy()
    create_testy()


def on_select_usunWszystkieTesty(event=None):
    if event:
        usunWszystkieTesty()
        db.commit()


b_Testy4 = tk.Button(frameTesty_4, text="Usuń")
b_Testy4.pack()
b_Testy4.bind("<Button-1>", on_select_usunWszystkieTesty)



#Ramka 5 - Wprowadź listę testów

test = [(6598, datetime.date(2019, 1, 3), 'negatywny', 2001, 15),
        (4298, datetime.date(2018, 12, 8),
         'posiew bakteriologiczny na Salmonelloze dodatni', 2013, 13),
        (7436, datetime.date(2018, 12, 15), 'test wenerologiczny na kiłę dodatni',
         2006, 11), (4162, datetime.date(2019, 1, 8), 'wyniki krwi w normie', 2020, 15),
        (8426, datetime.date(2018, 12, 31), 'pozytywny', 2005, 12)]


def insert_wiele_testy():
    with db:
        cur.executemany('INSERT INTO testy VALUES(?,?,?,?,?)', test)





def on_select_wprowadzTesty(event=None):
    if event:
        insert_wiele_testy()
        db.commit()


b_Testy5 = tk.Button(frameTesty_5, text="Wprowadź")
b_Testy5.pack()
b_Testy5.bind("<Button-1>", on_select_wprowadzTesty)



#----------------------Oddziały-------------------------------

def create_oddzialy():
    with db:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS oddzialy (
            numer_oddzialu INTEGER(10) PRIMARY KEY,
            nazwa_oddzialu TEXT(30) NOT NULL,
            numer_pielegniarki INTEGER(10) NOT NULL,
            FOREIGN KEY(numer_pielegniarki) REFERENCES pracownicy(numer_pracownika)
            ON DELETE CASCADE ON UPDATE CASCADE
            )""")


create_oddzialy()


def select_all_oddzialy():
    with db:
        cur.execute("select * from oddzialy")
        print(cur.fetchall())




# Pięć ramek - Odddziały
frameOddzialy_1 = ttk.LabelFrame(tab9, text="Dodaj Oddział")
frameOddzialy_1.grid(row=1, column=0)
frameOddzialy_2 = ttk.LabelFrame(tab9, text="Usuń Oddział")
frameOddzialy_2.grid(row=2, column=0)
frameOddzialy_3 = ttk.LabelFrame(tab9, text="Pokaż wszystkie oddziały")
frameOddzialy_3.grid(row=0, column=1)
frameOddzialy_4 = ttk.LabelFrame(tab9, text="Usuń wszystkie oddziały")
frameOddzialy_4.grid(row=0, column=2)
frameOddzialy_5 = ttk.LabelFrame(tab9, text="Wprowadź listę oddziałów")
frameOddzialy_5.grid(row=0, column=0)

# Ramka 1 - Dodaj oddział
etykietaOddzialy_1 = tk.Label(frameOddzialy_1, text="Wprowadż dane oddziału")
etykietaOddzialy_1.grid(row=0, columnspan=3)
labelOddzialy_11 = tk.Label(frameOddzialy_1, text="Numer oddziału")
labelOddzialy_12 = tk.Label(frameOddzialy_1, text="Nazwa oddziału")
labelOddzialy_13 = tk.Label(frameOddzialy_1, text="Numer pielęgniarki")

inputNrOddzialu_Oddzialy = tk.Entry(frameOddzialy_1)
inputNazwaOddzialu_Oddzialy = tk.Entry(frameOddzialy_1)
inputNrPiel_Oddzialy = tk.Entry(frameOddzialy_1)

labelOddzialy_11.grid(row=1, sticky='E')
labelOddzialy_12.grid(row=2, sticky='E')
labelOddzialy_13.grid(row=3, sticky='E')

inputNrOddzialu_Oddzialy.grid(row=1, column=1)
inputNazwaOddzialu_Oddzialy.grid(row=2, column=1)
inputNrPiel_Oddzialy.grid(row=3, column=1)


class Oddzialy:
    def __init__(self, numer_oddzialu, nazwa_oddzialu,
                 numer_pielegniarki):
        self.numer_oddzialu = numer_oddzialu
        self.nazwa_oddzialu = nazwa_oddzialu
        self.numer_pielegniarki = numer_pielegniarki


def insert_oddzialy(odz):
    with db:
        cur.execute("""insert into oddzialy values (:numer_oddzialu,
                    :nazwa_oddzialu, :numer_pielegniarki)""",
                    {'numer_oddzialu': odz.numer_oddzialu,
                     'nazwa_oddzialu': odz.nazwa_oddzialu,
                     'numer_pielegniarki': odz.numer_pielegniarki})


def dodaj_oddzial():
    nrOddzial = inputNrOddzialu_Oddzialy.get()
    nazwaOddzial = inputNazwaOddzialu_Oddzialy.get()
    nrPiel = inputNrPiel_Oddzialy.get()

    oddzial = Oddzialy(nrOddzial, nazwaOddzial, nrPiel)

    insert_oddzialy(oddzial)


def on_select_dodaj_oddzial(event=None):
    if event:
        dodaj_oddzial()
        db.commit()


b_Oddzialy = tk.Button(frameOddzialy_1, text="Dodaj")
b_Oddzialy.grid(row=4, columnspan=3)
b_Oddzialy.bind("<Button-1>", on_select_dodaj_oddzial)

# Ramka 2 - Usuń oddział
etykietaOddzialy_2 = tk.Label(frameOddzialy_2, text="Wprowadż numer oddziału")
etykietaOddzialy_2.grid(row=0, columnspan=3)
labelOddzialy_21 = tk.Label(frameOddzialy_2, text="Numer oddziału")
inputNrOddzialu_Oddzialy2 = tk.Entry(frameOddzialy_2)

labelOddzialy_21.grid(row=1, sticky='E')
inputNrOddzialu_Oddzialy2.grid(row=1, column=1)


def delete_oddzialy(odz):
    with db:
        cur.execute("""delete from oddzialy where
                    numer_oddzialu = :numer_oddzialu""",
                    {'numer_oddzialu': odz})


def usun_oddzial():
    nrOddzial = inputNrOddzialu_Oddzialy2.get()

    delete_oddzialy(nrOddzial)


def on_select_usun_oddzial(event=None):
    if event:
        usun_oddzial()
        db.commit()


b_Oddzialy2 = tk.Button(frameOddzialy_2, text="Usuń")
b_Oddzialy2.grid(row=2, columnspan=3)
b_Oddzialy2.bind("<Button-1>", on_select_usun_oddzial)


# Ramka 3 - Pokaż wszystkie oddziały
def select_all_oddzialy():
    with db:
        cur.execute("select * from oddzialy")
        print(cur.fetchall())


def create_window_oddzialy():
    select = ('select * from oddzialy')
    window = Tk()
    window.title("Lista oddziałow")
    window.geometry('400x200')
    txt = scrolledtext.ScrolledText(window, width=200, height=200)
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')


def pokaz_oddzialy():
    create_window_oddzialy()


def on_select_pokaz_oddzialy(event=None):
    if event:
        pokaz_oddzialy()


b_Oddzialy3 = tk.Button(frameOddzialy_3, text="Pokaż")
b_Oddzialy3.pack()
b_Oddzialy3.bind("<Button-1>", on_select_pokaz_oddzialy)


# Ramka 4 - Usuń wszystkie oddziały
def drop_oddzialy():
    with db:
        cur.execute("drop table if exists oddzialy")


def usunWszystkieOddzialy():
    drop_oddzialy()
    create_oddzialy()


def on_select_usunWszystkieOddzialy(event=None):
    if event:
        usunWszystkieOddzialy()
        db.commit()


b_Oddzialy4 = tk.Button(frameOddzialy_4, text="Usuń")
b_Oddzialy4.pack()
b_Oddzialy4.bind("<Button-1>", on_select_usunWszystkieOddzialy)




#Ramka 5 - Wprowadź listę oddziałów

oddzial = [('01', 'Oddział Położniczy', 372),
           ('02', 'Oddział Onkologiczny', 356),
           ('03', 'Oddział Urologiczny', 390),
           ('04', 'Oddział Chorób Wewnętrznych', 167),
           ('05', 'Oddział Kardiologiczny', 678),
           ('06', 'Oddział Chirurgii Ogólnej', 111),
           ('07', 'Oddzial Pediatryczny', 254)]


def insert_wiele_oddzialy():
    with db:
        cur.executemany('INSERT INTO oddzialy (numer_oddzialu, nazwa_oddzialu,numer_pielegniarki) VALUES (?,?,?)',
                        oddzial)




def on_select_wprowadzOddzialy(event=None):
    if event:
        insert_wiele_oddzialy()
        db.commit()


b_Oddzialy5 = tk.Button(frameOddzialy_5, text="Wprowadź")
b_Oddzialy5.pack()
b_Oddzialy5.bind("<Button-1>", on_select_wprowadzOddzialy)


#----------------------Przedmioty-------------------------------
def create_przedmioty():
    with db:
        cur.execute("""
         CREATE TABLE IF NOT EXISTS przedmioty (
            nazwa_przedmiotu TEXT(30) NOT NULL PRIMARY KEY,
            data_zuzycia DATE NOT NULL,
            godzina_zuzycia DATE NOT NULL,
            ilosc REAL(10) NOT NULL,
            koszt_jednostkowy REAL(10) NOT NULL
            )""")

create_przedmioty()

def select_all_przedmioty():
    with db:
        cur.execute("select * from przedmioty")
        print(cur.fetchall())



frame_p1 = ttk.LabelFrame(tab10, text="Dodaj Przedmiot")
frame_p1.grid(row=1, column=0)
frame_p2 = ttk.LabelFrame(tab10, text="Usuń Przedmiot")
frame_p2.grid(row=2, column=0)
frame_p3 = ttk.LabelFrame(tab10, text="Pokaż wszystkie Przedmioty")
frame_p3.grid(row=0, column=1)
frame_p4 = ttk.LabelFrame(tab10, text="Usuń wszystkie Przedmioty")
frame_p4.grid(row=0, column=2)
frame_p5 = ttk.LabelFrame(tab10, text="Wprowadź listę Przedmiotów")
frame_p5.grid(row=0, column=0)

# Ramka 1 - Dodaj przedmiot
etykietap1 = tk.Label(frame_p1, text="Wprowadż dane przedmiotu")
etykietap1.grid(row=0, columnspan=3)
label_p1 = tk.Label(frame_p1, text="Nazwa przedmiotu")
label_p2 = tk.Label(frame_p1, text="Data zużycia")
label_p3 = tk.Label(frame_p1, text="Godzina zużycia")
label_p4 = tk.Label(frame_p1, text="Ilość")
label_p5 = tk.Label(frame_p1, text="Koszt jednostkowy")

inputNazwaPrzedmiotup1 = tk.Entry(frame_p1)
inputDataZuzyciap1 = tk.Entry(frame_p1)
inputGodzinaZuzyciap1 = tk.Entry(frame_p1)
inputIloscp1 = tk.Entry(frame_p1)
inputKosztjednostkowyp1 = tk.Entry(frame_p1)


label_p1.grid(row=1, sticky='E')  # sticky alligns the text to right (E - east,
label_p2.grid(row=2, sticky='E')  # W - west, N - north, S - south)
label_p3.grid(row=3, sticky='E')
label_p4.grid(row=4, sticky='E')
label_p5.grid(row=5, sticky='E')

inputNazwaPrzedmiotup1.grid(row=1, column=1)
inputDataZuzyciap1.grid(row=2, column=1)
inputGodzinaZuzyciap1.grid(row=3, column=1)
inputIloscp1.grid(row=4, column=1)
inputKosztjednostkowyp1.grid(row=5, column=1)

class Przedmioty:

    def __init__(self, nazwa_przedmiotu, data_zuzycia, godzina_zuzycia,
                 ilosc, koszt_jednostkowy):
        self.nazwa_przedmiotu = nazwa_przedmiotu
        self.data_zuzycia = data_zuzycia
        self.godzina_zuzycia = godzina_zuzycia
        self.ilosc = ilosc
        self.koszt_jednostkowy = koszt_jednostkowy

def insert_przedmioty(przed):
    with db:
        cur.execute("""insert into przedmioty values (:nazwa_przedmiotu,
                    :data_zuzycia, :godzina_zuzycia, :ilosc, :koszt_jednostkowy)""",
                    {'nazwa_przedmiotu':przed.nazwa_przedmiotu,
                    'data_zuzycia':przed.data_zuzycia,
                    'godzina_zuzycia':przed.godzina_zuzycia,
                    'ilosc':przed.ilosc,
                    'koszt_jednostkowy':przed.koszt_jednostkowy})

def dodaj_przedmiot():
    nazwap1 = inputNazwaPrzedmiotup1.get()
    datazuzyciap1 = inputDataZuzyciap1.get()
    godzinazuzyciap11 = inputGodzinaZuzyciap1.get()
    iloscp1 = inputIloscp1.get()
    kosztjednostkowyp1 = inputKosztjednostkowyp1.get()

    przed = Przedmioty(nazwap1, datazuzyciap1, godzinazuzyciap11, iloscp1, kosztjednostkowyp1)

    insert_przedmioty(przed)

def on_select_dodaj_przedmiot(event=None):
    if event:
        dodaj_przedmiot()
        db.commit()

bp1 = tk.Button(frame_p1, text="Dodaj")
bp1.grid(row=10, columnspan=3)
bp1.bind("<Button-1>", on_select_dodaj_przedmiot)

# Ramka 2 - Usuń przedmiot
etykietap2 = tk.Label(frame_p2, text="Wprowadż nazwę przedmiotu")
etykietap2.grid(row=0, columnspan=3)
label_p7 = tk.Label(frame_p2, text="Nazwa przedmiotu")
inputNazwaPrzedmiotup2 = tk.Entry(frame_p2)

label_p7.grid(row=1, sticky='E')
inputNazwaPrzedmiotup2.grid(row=1, column=1)

def delete_przedmioty(przed):
    with db:
        cur.execute("""delete from przedmioty where
                    nazwa_przedmiotu = :nazwa_przedmiotu""",
        {'nazwa_przedmiotu':przed})

def usun_przedmiot():
    NazwaPrzedmiotu = inputNazwaPrzedmiotup2.get()

    delete_przedmioty(NazwaPrzedmiotu)

def on_select_usun_przedmiot(event=None):
    if event:
        usun_przedmiot()
        db.commit()

bp2 = tk.Button(frame_p2, text="Usuń")
bp2.grid(row=10, columnspan=3)
bp2.bind("<Button-1>", on_select_usun_przedmiot)

# Ramka 3 - Pokaż wszystkie przedmioty

def select_all_przedmioty():
    with db:
        cur.execute("select * from przedmioty")
        print(cur.fetchall())

def create_windowp1():
    select = ('select * from przedmioty')
    window = Tk()
    window.title("Zużyte przedmioty")
    window.geometry('700x400')
    txt = scrolledtext.ScrolledText(window, width=200, height=200)
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')

def pokaz_przedmioty():
    create_windowp1()

def on_select_pokaz_przedmioty(event=None):
    if event:
        pokaz_przedmioty()

etykietap3 = tk.Label(frame_p3)
bp3 = tk.Button(frame_p3, text="Pokaż")
bp3.pack()
bp3.bind("<Button-1>", on_select_pokaz_przedmioty)

 # Ramka 4 - Usuń wszystkie przedmioty

def drop_przedmioty():
    with db:
        cur.execute("drop table if exists przedmioty")

def usun_wszystkie_przedmioty():
    drop_przedmioty()
    create_przedmioty()

def on_select_usun_wszystkie_przedmioty(event=None):
    if event:
        usun_wszystkie_przedmioty()
        db.commit()


bp4 = tk.Button(frame_p4, text="Usuń")
bp4.pack()
bp4.bind("<Button-1>", on_select_usun_wszystkie_przedmioty)



#Ramka 5 - Wprowadź listę przedmiotów

przedmiociki =[('Lek dicoflor 50 mg','2014-03-02','14:00:00',1,1),
('stetoskop jednorazowy','2018-12-24','08:50:00',2,5),
('Cewnik pojemnośc 500 ml','2018-12-15','09:32:00',1,3),
('Lek zyrtec 200 mg','2018-12-12','10:12:00',1,2.5),
('Rękawiczki lateksowe','2018-12-20','09:30:00',100,0.5),
('Gaza jałowa - opakowanie','2018-12-09','15:00:00',50,10),
('Fartuch jednorazowy','2018-12-21','16:12:00',40,1),
('Plastry duze opakowanie','2018-12-30','19:42:00',50,5),
('Sól fizjologiczna','2018-12-17','18:22:00',3,12),
('Wenflon jednorazowy','2018-12-02','21:30:00',20,3),
('Kroplowka - glukoza 200 mg','2018-12-05','06:32:00',10,10),
('Lek Morfina 50 mg','2018-12-13','17:11:00',1,40),
('Lek propolis','2018-12-15','13:14:00',2,3),
('Pęseta metalowa duża','2018-12-11','17:12:00',5,20),
('Czepek jednorazowy','2018-12-08','21:51:00',50,0.5),
('Pyn dezynfekcyjny 500 ml','2018-12-28','23:13:00',10,30),
('Opatrunek uciskowy','2018-12-05','06:12:00',50,2),
('szwy samowchłaniające - opakowanie','2018-12-14','05:31:00',5,30),
('Plyn USG - opakowanie 50 ml','2018-12-10','12:45:00',5,25),
('Wymazowka bawalniana - opakowanie','2018-12-01','13:32:00',100,1),
('Cetol-2','2018-12-13','10:00:00',1,25)]


def insert_wiele_przedmioty():
    with db:
        cur.executemany('INSERT INTO przedmioty VALUES(?,?,?,?,?)', przedmiociki)




def on_select_wprowadzPrzedmioty(event=None):
    if event:
        insert_wiele_przedmioty()
        db.commit()


bp5 = tk.Button(frame_p5, text="Wprowadź")
bp5.pack()
bp5.bind("<Button-1>", on_select_wprowadzPrzedmioty)


#----------------------Rejestry godzin-------------------------------

def create_rejestry_godzin():
    with db:
        cur.execute("""CREATE TABLE if not exists rejestry_godzin(
            id_rejestru TEXT(10) PRIMARY KEY,
            ilosc_godzin REAL(3) NULL,
            numer_tygodnia INTEGER(2) NOT NULL,
            numer_oddzialu INTEGER(10) NOT NULL,
            numer_pracownika INTEGER NOT NULL,
            FOREIGN KEY(numer_pracownika) REFERENCES pracownicy(numer_pracownika)
            ON DELETE NO ACTION ON UPDATE CASCADE
            FOREIGN KEY(numer_oddzialu) REFERENCES oddzialy(numer_oddzialu)
            ON DELETE NO ACTION ON UPDATE CASCADE)
            """)


create_rejestry_godzin()


def select_all_rejestry_godzin():
    with db:
        cur.execute("select * from rejestry_godzin")
        print(cur.fetchall())



# Pięć ramek - Rejestr godzin
frameRejestr_1 = ttk.LabelFrame(tab11, text="Dodaj Rejestr")
frameRejestr_1.grid(row=1, column=0)
frameRejestr_2 = ttk.LabelFrame(tab11, text="Usuń Rejestr")
frameRejestr_2.grid(row=2, column=0)
frameRejestr_3 = ttk.LabelFrame(tab11, text="Pokaż wszystkie zarejestrowane godziny")
frameRejestr_3.grid(row=0, column=1)
frameRejestr_4 = ttk.LabelFrame(tab11, text="Usuń wszystkie zarejestrowane godziny")
frameRejestr_4.grid(row=0, column=2)
frameRejestr_5 = ttk.LabelFrame(tab11, text="Wprowadź listę zarejestrowanych godziny")
frameRejestr_5.grid(row=0, column=0)

# Ramka 1 - Dodaj rejestr
etykietaRejestr_1 = tk.Label(frameRejestr_1, text="Wprowadż dane rejestru")
etykietaRejestr_1.grid(row=0, columnspan=3)
labelRejestr_11 = tk.Label(frameRejestr_1, text="ID rejestru")
labelRejestr_12 = tk.Label(frameRejestr_1, text="Ilość godzin")
labelRejestr_13 = tk.Label(frameRejestr_1, text="Numer tygodnia")
labelRejestr_14 = tk.Label(frameRejestr_1, text="Nazwa oddziału")
labelRejestr_15 = tk.Label(frameRejestr_1, text="Numer pracownika")

inputIdRejestru_Rejestr = tk.Entry(frameRejestr_1)
inputIloscGodzin_Rejestr = tk.Entry(frameRejestr_1)
inputNrTyg_Rejestr = tk.Entry(frameRejestr_1)
inputNazwaOddzialu_Rejestr = tk.Entry(frameRejestr_1)
inputNrPracownika_Rejestr = tk.Entry(frameRejestr_1)

labelRejestr_11.grid(row=1, sticky='E')
labelRejestr_12.grid(row=2, sticky='E')
labelRejestr_13.grid(row=3, sticky='E')
labelRejestr_14.grid(row=4, sticky='E')
labelRejestr_15.grid(row=5, sticky='E')

inputIdRejestru_Rejestr.grid(row=1, column=1)
inputIloscGodzin_Rejestr.grid(row=2, column=1)
inputNrTyg_Rejestr.grid(row=3, column=1)
inputNazwaOddzialu_Rejestr.grid(row=4, column=1)
inputNrPracownika_Rejestr.grid(row=5, column=1)


class Rejestry_godzin:

    def __init__(self, id_rejestru, ilosc_godzin, numer_tygodnia,
                 numer_oddzialu, numer_pracownika):
        self.id_rejestru = id_rejestru
        self.ilosc_godzin = ilosc_godzin
        self.numer_tygodnia = numer_tygodnia
        self.numer_oddzialu = numer_oddzialu
        self.numer_pracownika = numer_pracownika


def insert_rejestry_godzin(rej):
    with db:
        cur.execute("""insert into rejestry_godzin values (:id_rejestru,
                    :ilosc_godzin, :numer_tygodnia, :numer_oddzialu, :numer_pracownika)""",
                    {'id_rejestru': rej.id_rejestru,
                     'ilosc_godzin': rej.ilosc_godzin,
                     'numer_tygodnia': rej.numer_tygodnia,
                     'numer_oddzialu': rej.numer_oddzialu,
                     'numer_pracownika': rej.numer_pracownika})


def dodaj_rejestr():
    idRejestr = inputIdRejestru_Rejestr.get()
    liczbaGodz = inputIloscGodzin_Rejestr.get()
    nrTyg = inputNrTyg_Rejestr.get()
    nazwaOddz = inputNazwaOddzialu_Rejestr.get()
    nrPrac = inputNrPracownika_Rejestr.get()

    rejestr = Rejestry_godzin(idRejestr, liczbaGodz, nrTyg, nazwaOddz, nrPrac)

    insert_rejestry_godzin(rejestr)


def on_select_dodaj_rejestr(event=None):
    if event:
        dodaj_rejestr()
        db.commit()


b_Rejestr = tk.Button(frameRejestr_1, text="Dodaj")
b_Rejestr.grid(row=6, columnspan=3)
b_Rejestr.bind("<Button-1>", on_select_dodaj_rejestr)

# Ramka 2 - Usuń rejestr
etykietaRejestr_2 = tk.Label(frameRejestr_2, text="Wprowadż ID rejestru")
etykietaOddzialy_2.grid(row=0, columnspan=3)
labelRejestr_21 = tk.Label(frameRejestr_2, text="ID rejestru")
inputIdRejestru_Rejestr2 = tk.Entry(frameRejestr_2)

labelRejestr_21.grid(row=1, sticky='E')
inputIdRejestru_Rejestr2.grid(row=1, column=1)


def delete_rejestry_godzin(rej):
    with db:
        cur.execute("""delete from rejestry_godzin where
                    id_rejestru = :id_rejestru""",
                    {'id_rejestru': rej})


def usun_rejestr():
    idRejestr = inputIdRejestru_Rejestr2.get()

    delete_rejestry_godzin(idRejestr)


def on_select_usun_rejestr(event=None):
    if event:
        usun_rejestr()
        db.commit()


b_Rejestr2 = tk.Button(frameRejestr_2, text="Usuń")
b_Rejestr2.grid(row=4, columnspan=3)
b_Rejestr2.bind("<Button-1>", on_select_usun_rejestr)


# Ramka 3 - Pokaż wszystkie rejestry
def select_all_rejestry_godzin():
    with db:
        cur.execute("select * from rejestry_godzin")
        print(cur.fetchall())


def create_window_rejestry():
    select = ('select * from rejestry_godzin')
    window = Tk()
    window.title("Rejestry godzin pracowników")
    window.geometry('600x200')
    txt = scrolledtext.ScrolledText(window, width=200, height=200)
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')


def pokaz_rejestry():
    create_window_rejestry()


def on_select_pokaz_rejestry(event=None):
    if event:
        pokaz_rejestry()


b_Rejestr3 = tk.Button(frameRejestr_3, text="Pokaż")
b_Rejestr3.pack()
b_Rejestr3.bind("<Button-1>", on_select_pokaz_rejestry)


# Ramka 4 - Usuń wszystkie rejestry
def drop_rejestry_godzin():
    with db:
        cur.execute("drop table if exists rejestry_godzin")


def usunWszystkieRejestry():
    drop_rejestry_godzin()
    create_rejestry_godzin()


def on_select_usunWszystkieRejestry(event=None):
    if event:
        usunWszystkieRejestry()
        db.commit()


b_Rejestr4 = tk.Button(frameRejestr_4, text="Usuń")
b_Rejestr4.pack()
b_Rejestr4.bind("<Button-1>", on_select_usunWszystkieRejestry)


#Ramka 5 - Wprowadź listę zarejestrowanych godzin

godzina = [('1-372-01', 96, 1, 1, 372),
           ('1-678-05', 120, 1, 5, 678),
           ('1-390-03', 111, 1, 3, 390),
           ('1-168-02', 89, 1, 2, 168),
           ('1-167-04', 86, 1, 4, 167)]


def insert_wiele_rejestry_godziny():
    with db:
        cur.executemany('INSERT INTO rejestry_godzin VALUES(?,?,?,?,?)', godzina)




def on_select_wprowadzRejestry(event=None):
    if event:
        insert_wiele_rejestry_godziny()
        db.commit()


b_Rejestr5 = tk.Button(frameRejestr_5, text="Wprowadź")
b_Rejestr5.pack()
b_Rejestr5.bind("<Button-1>", on_select_wprowadzRejestry)




#----------------------Zuzyte przedmioty-------------------------------

def create_pacjenci_przedmioty():
    with db:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS pacjenci_przedmioty (
            numer_pacjenta INTEGER(10),
            nazwa_przedmiotu TEXT(30) NOT NULL,
            PRIMARY KEY( numer_pacjenta,nazwa_przedmiotu),
            FOREIGN KEY(numer_pacjenta) REFERENCES pacjenci(numer_pacjenta)
            ON DELETE CASCADE ON UPDATE CASCADE
            FOREIGN KEY(nazwa_przedmiotu) REFERENCES przedmioty(nazwa_przedmiotu)
            ON DELETE CASCADE ON UPDATE CASCADE
            )""")

create_pacjenci_przedmioty()

def select_all_pacjenci_przedmioty():
    with db:
        cur.execute("select * from pacjenci_przedmioty")
        print(cur.fetchall())


frame_pp1 = ttk.LabelFrame(tab12, text="Przypisz zużyty przedmiot do pacjenta")
frame_pp1.grid(row=1, column=0)
frame_pp2 = ttk.LabelFrame(tab12, text="Usuń powiązanie pacjenta z przedmiotem")
frame_pp2.grid(row=2, column=0)
frame_pp3 = ttk.LabelFrame(tab12, text="Pokaż wszystkich Pacjentów z zużytymi przedmiotami")
frame_pp3.grid(row=0, column=1)
frame_pp4 = ttk.LabelFrame(tab12, text="Usuń wszystkie powiązania Pacjenta z przedmiotem")
frame_pp4.grid(row=0, column=2)
frame_pp5 = ttk.LabelFrame(tab12, text="Wprowadź listę powiązań Pacjentów z przedmiotami")
frame_pp5.grid(row=0, column=0)

# Ramka 1 - Dodaj przedmiot
etykietapp1 = tk.Label(frame_p1, text="Wprowadż przedmiot i pacjenta")
etykietapp1.grid(row=0, columnspan=3)
label_pp1 = tk.Label(frame_pp1, text="Numer pacjenta")
label_pp2 = tk.Label(frame_pp1, text="Nazwa przedmiotu")

inputNumerPacjentapp1 = tk.Entry(frame_pp1)
inputNazwaPrzedmiotupp1 = tk.Entry(frame_pp1)

label_pp1.grid(row=1, sticky='E')  # sticky alligns the text to right (E - east,
label_pp2.grid(row=2, sticky='E')  # W - west, N - north, S - south)

inputNumerPacjentapp1.grid(row=1, column=1)
inputNazwaPrzedmiotupp1.grid(row=2, column=1)

class Pacjenci_przedmioty:

    def __init__(self, numer_pacjenta, nazwa_przedmiotu):
        self.numer_pacjenta = numer_pacjenta
        self.nazwa_przedmiotu = nazwa_przedmiotu

def insert_pacjenci_przedmioty(pacp):
    with db:
        cur.execute("""insert into pacjenci_przedmioty values (:numer_pacjenta,
                    :nazwa_przedmiotu)""",
                    {'numer_pacjenta':pacp.numer_pacjenta,
                    'nazwa_przedmiotu':pacp.nazwa_przedmiotu})


def dodaj_pacp():
    pacjentpp1 = inputNumerPacjentapp1.get()
    przedmiotpp1 = inputNazwaPrzedmiotupp1.get()


    pacp = Przedmioty(pacjentpp1, przedmiotpp1)

    insert_pacjenci_przedmioty(pacp)

def on_select_dodaj_pacp(event=None):
    if event:
        dodaj_pacp()
        db.commit()

bpp1 = tk.Button(frame_pp1, text="Dodaj")
bpp1.grid(row=10, columnspan=3)
bpp1.bind("<Button-1>", on_select_dodaj_pacp)

# Ramka 2 - Usuń pacjenci_przedmioty
etykietapp2 = tk.Label(frame_pp2, text="Wprowadż numer pacjenta i nazwę przedmiotu")
etykietapp2.grid(row=0, columnspan=3)
label_pp7 = tk.Label(frame_pp2, text="Numer pacjenta")
inputNumerPacjentapp2 = tk.Entry(frame_pp2)
label_pp8 = tk.Label(frame_pp2, text="Nazwa przedmiotu")
inputNazwaPrzedmiotupp2 = tk.Entry(frame_pp2)

label_pp7.grid(row=1, sticky='E')
inputNumerPacjentapp2.grid(row=1, column=1)
label_pp8.grid(row=2, sticky='E')
inputNazwaPrzedmiotupp2.grid(row=2, column=1)

def delete_pacjenci_przedmioty(pacp):
    with db:
        cur.execute("""delete from pacjenci_przedmioty where
                    numer_pacjenta = :numer_pacjenta AND nazwa_przedmiotu = :nazwa_przedmiotu """,
        {'numer_pacjenta':pacp.numer_pacjenta,
         'nazwa_przedmiotu':pacp.nazwa_przedmiotu})

def usun_pacp():
    pacp1 = inputNumerPacjentapp2.get()
    pacp2 = inputNazwaPrzedmiotupp2.get()

    pacp = Pacjenci_przedmioty(pacp1, pacp2)

    delete_pacjenci_przedmioty(pacp)

def on_select_usun_pacp(event=None):
    if event:
        usun_pacp()
        db.commit()

bpp2 = tk.Button(frame_pp2, text="Usuń")
bpp2.grid(row=10, columnspan=3)
bpp2.bind("<Button-1>", on_select_usun_pacp)

# Ramka 3 - Pokaż wszystkie przedmioty

def select_all_pacjenci_przedmioty():
    with db:
        cur.execute("select * from pacjenci_przedmioty")
        print(cur.fetchall())

def create_windowpp2():
    select = ('select * from pacjenci_przedmioty')
    window = Tk()
    window.title("Pacjenci, którzy zużyli przedmioty:")
    window.geometry('700x300')
    txt = scrolledtext.ScrolledText(window, width=200, height=200)
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')

def pokaz_pacp():
    create_windowpp2()

def on_select_pokaz_pacp(event=None):
    if event:
        pokaz_pacp()

etykietapp3 = tk.Label(frame_pp3)
bpp3 = tk.Button(frame_pp3, text="Pokaż")
bpp3.pack()
bpp3.bind("<Button-1>", on_select_pokaz_pacp)

 # Ramka 4 - Usuń wszystkich pcjenci_przedmioty

def drop_pacp():
    with db:
        cur.execute("drop table if exists pacjenci_przedmioty")

def usun_wszystkie_pacp():
    drop_pacp()
    create_pacjenci_przedmioty()

def on_select_usun_wszystkie_pacp(event=None):
    if event:
        usun_wszystkie_pacp()
        db.commit()


bpp4 = tk.Button(frame_pp4, text="Usuń")
bpp4.pack()
bpp4.bind("<Button-1>", on_select_usun_wszystkie_pacp)




#Ramka 5 - Wprowadź listę powiązań pacjent-przedmiot

pacjent_przedmiot= [(2014,'stetoskop jednorazowy'),
(2001,'szwy samowchłaniające - opakowanie'),
(2071,'Fartuch jednorazowy'),
(2025,'Lek Morfina 50 mg'),
(2030,'Lek propolis'),
(2058,'Cetol-2'),
(2059,'Cetol-2'),
(2041,'Cetol-2'),
(2099,'Cetol-2'),
(2009,'Cetol-2'),
(2021,'Cetol-2')]

def insert_wiele_pacjenci_przedmioty():
    with db:
        cur.executemany('INSERT INTO pacjenci_przedmioty (numer_pacjenta, nazwa_przedmiotu) VALUES (?,?)', pacjent_przedmiot)





def on_select_wprowadzPacpPrzed(event=None):
    if event:
        insert_wiele_pacjenci_przedmioty()
        db.commit()


bpp5 = tk.Button(frame_pp5, text="Wprowadź")
bpp5.pack()
bpp5.bind("<Button-1>", on_select_wprowadzPacpPrzed)





#----------------------Pracownicy na oddziałach-------------------------------
def create_pracownicy_oddzialy():
    with db:
        cur.execute("""
            CREATE TABLE if not exists pracownicy_oddzialy(
            numer_oddzialu INTEGER(10),
            numer_pracownika INTEGER(10),
            PRIMARY KEY(numer_pracownika,numer_oddzialu),
            FOREIGN KEY(numer_oddzialu) REFERENCES oddzialy(numer_oddzialu)
            ON DELETE CASCADE ON UPDATE CASCADE
            FOREIGN KEY(numer_pracownika)REFERENCES pracownicy(numer_pracownika)
            ON DELETE CASCADE ON UPDATE CASCADE)
            """)


create_pracownicy_oddzialy()


def select_all_pracownicy_oddzialy():
    with db:
        cur.execute("select * from pracownicy_oddzialy")
        print(cur.fetchall())



# Pięć ramek - Pracownicy-Oddziały
framePracOddz_1 = ttk.LabelFrame(tab13, text="Dodaj Pracownika do Oddziału")
framePracOddz_1.grid(row=1, column=0)
framePracOddz_2 = ttk.LabelFrame(tab13, text="Usuń Pracownika z Oddziału")
framePracOddz_2.grid(row=2, column=0)
framePracOddz_3 = ttk.LabelFrame(tab13, text="Pokaż wszystkich pracowników na oddziałach")
framePracOddz_3.grid(row=0, column=1)
framePracOddz_4 = ttk.LabelFrame(tab13, text="Usuń wszystkich pracowników z oddziałach")
framePracOddz_4.grid(row=0, column=2)
framePracOddz_5 = ttk.LabelFrame(tab13, text="Wprowadź listę pracowników na oddziałach")
framePracOddz_5.grid(row=0, column=0)

# Ramka 1 - Dodaj pracownika na oddział
etykietaPracOddz_1 = tk.Label(framePracOddz_1, text="Wprowadż dane pracownika i oddziału")
etykietaPracOddz_1.grid(row=0, columnspan=3)
labelPracOddz_11 = tk.Label(framePracOddz_1, text="Numer oddziału")
labelPracOddz_12 = tk.Label(framePracOddz_1, text="Numer pracownika")

inputNrOddzialu_PracOddz = tk.Entry(framePracOddz_1)
inputNrPracownika_PracOddz = tk.Entry(framePracOddz_1)

labelPracOddz_11.grid(row=1, sticky='E')
labelPracOddz_12.grid(row=2, sticky='E')

inputNrOddzialu_PracOddz.grid(row=1, column=1)
inputNrPracownika_PracOddz.grid(row=2, column=1)


class Pracownicy_oddzialy:

    def __init__(self, numer_oddzialu, numer_pracownika):
        self.numer_oddzialu = numer_oddzialu
        self.numer_pracownika = numer_pracownika


def insert_pracownicy_oddzialy(pracod):
    with db:
        cur.execute("""insert into pracownicy_oddzialy values (:numer_oddzialu,
                    :numer_pracownika)""",
                    {'numer_oddzialu': pracod.numer_oddzialu,
                     'numer_pracownika': pracod.numer_pracownika})


def dodaj_PracOddz():
    nrOddz = inputNrOddzialu_PracOddz.get()
    nrPrac = inputNrPracownika_PracOddz.get()

    pracOddz = Pracownicy_oddzialy(nrOddz, nrPrac)

    insert_pracownicy_oddzialy(pracOddz)


def on_select_dodaj_PracOddz(event=None):
    if event:
        dodaj_PracOddz()
        db.commit()


b_PracOddz = tk.Button(framePracOddz_1, text="Dodaj")
b_PracOddz.grid(row=6, columnspan=3)
b_PracOddz.bind("<Button-1>", on_select_dodaj_PracOddz)

# Ramka 2 - Usuń pracownika z oddziału
etykietaPracOddz_2 = tk.Label(framePracOddz_2, text="Wprowadż dane numer pracownika i oddzialu")
etykietaPracOddz_2.grid(row=0, columnspan=3)
labelPracOddz_21 = tk.Label(framePracOddz_2, text="Numer pracownika")
inputNrPracownika_PracOddz2 = tk.Entry(framePracOddz_2)
labelPracOddz_22 = tk.Label(framePracOddz_2, text="Numer oddziału")
inputNrOddzialu_PracOddz2 = tk.Entry(framePracOddz_2)

labelPracOddz_21.grid(row=1, sticky='E')
labelPracOddz_22.grid(row=2, sticky='E')
inputNrPracownika_PracOddz2.grid(row=1, column=1)
inputNrOddzialu_PracOddz2.grid(row=2, column=1)


def delete_pracownicy_oddzialy(pracod):
    with db:
        cur.execute("""delete from pracownicy_oddzialy where
                    numer_pracownika = :numer_pracownika AND numer_oddzialu = :numer_oddzialu """,
                    {'numer_pracownika': pracod.numer_pracownika,
                     'numer_oddzialu': pracod.numer_oddzialu})


def usun_PracOddz():
    nrOddz = inputNrOddzialu_PracOddz2.get()
    nrPrac = inputNrPracownika_PracOddz2.get()

    pracOddz = Pracownicy_oddzialy(nrOddz, nrPrac)

    delete_pracownicy_oddzialy(pracOddz)


def on_select_usun_PracOddz(event=None):
    if event:
        usun_PracOddz()
        db.commit()


b_PracOddz2 = tk.Button(framePracOddz_2, text="Usuń")
b_PracOddz2.grid(row=3, columnspan=3)
b_PracOddz2.bind("<Button-1>", on_select_usun_PracOddz)


# Ramka 3 - Pokaż wszystkich pracowników na oddziałach
def select_all_pracownicy_oddzialy():
    with db:
        cur.execute("select * from pracownicy_oddzialy")
        print(cur.fetchall())


def create_window_PracOddz():
    select = ('select * from pracownicy_oddzialy')
    window = Tk()
    window.title("Pracownicy przypisanie do oddziałów")
    window.geometry('300x200')
    txt = scrolledtext.ScrolledText(window, width=200, height=200)
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')


def pokaz_PracOddz():
    create_window_PracOddz()


def on_select_pokaz_PracOddz(event=None):
    if event:
        pokaz_PracOddz()


b_PracOddz3 = tk.Button(framePracOddz_3, text="Pokaż")
b_PracOddz3.pack()
b_PracOddz3.bind("<Button-1>", on_select_pokaz_PracOddz)


# Ramka 4 - Usuń wszystkich pracowników z oddziałów
def drop_pracownicy_oddzialy():
    with db:
        cur.execute("drop table if exists pracownicy_oddzialy")


def usunWszystkichPracOddz():
    drop_pracownicy_oddzialy()
    create_pracownicy_oddzialy()


def on_select_usunWszystkichPracOddz(event=None):
    if event:
        usunWszystkichPracOddz()
        db.commit()


b_PracOddz4 = tk.Button(framePracOddz_4, text="Usuń")
b_PracOddz4.pack()
b_PracOddz4.bind("<Button-1>", on_select_usunWszystkichPracOddz)



#Ramka 5 - Wprowadź listę pracowników na oddziałach

pracownik_oddzial = [(1, 372), (2, 168), (3, 390), (4, 167), (5, 678), (7, 156), (4, 123),
                     (5, 134), (7, 189)]


def insert_wiele_pracownicy_oddzialy():
    with db:
        cur.executemany('INSERT INTO pracownicy_oddzialy VALUES(?,?)', pracownik_oddzial)




def on_select_wprowadzPracOddz(event=None):
    if event:
        insert_wiele_pracownicy_oddzialy()
        db.commit()


b_PracOddz5 = tk.Button(framePracOddz_5, text="Wprowadź")
b_PracOddz5.pack()
b_PracOddz5.bind("<Button-1>", on_select_wprowadzPracOddz)



#----------------------Zapytania-------------------------------

#Dziesięć ramek
frameZap_1 = ttk.LabelFrame(tab14, width=50, height=30, text = "Zapytanie 1")
frameZap_1.grid(row=0,column=0)
etykieta_Zap1 = tk.Label(frameZap_1, text="""Nazwiska i daty urodzeń pacjentów, którym przypisnao lek 'Cetol-2', cierpiących na cukrzycę,
którzy odbyli jedną lub więcej wizy u lekarza pracującego na oddziale pediatrycznym.""")
etykieta_Zap1.grid(row=1, column=0)

frameZap_2 = ttk.LabelFrame(tab14, width=50, height=30, text = "Zapytanie 2")
frameZap_2.grid(row=1, column=0)
etykieta_Zap2 = tk.Label(frameZap_2, text="""Lista pacjentów, którzy odwiedzili jednego lub więcej lekarzy ogólnych: 'Dr Pająk', 'Dr Samuel'
i 'Dr Gąska'. Wymień tylko nazwiska posortowane alfabetycznie - nie są
wymagane żadne inne szczegóły.""")
etykieta_Zap2.grid(row=1, column=0)

frameZap_3 = ttk.LabelFrame(tab14, width=50, height=30, text = "Zapytanie 3")
frameZap_3.grid(row=2, column=0)
etykieta_Zap3 = tk.Label(frameZap_3, text="""Łączna liczba pacjentów, których nazwisko zaczyna się na literę 'S', i którzy złożyli więcej niż
2 wizyty u lekarza ogólnego.""")
etykieta_Zap3.grid(row=1, column=0)

frameZap_4 = ttk.LabelFrame(tab14, width=50, height=30, text = "Zapytanie 4")
frameZap_4.grid(row=3, column=0)
etykieta_Zap4 = tk.Label(frameZap_4, text="""Nazwisko i imię lekarza, który miał najmniej wizyt pacjentów w 2015 roku.""")
etykieta_Zap4.grid(row=1, column=0)

frameZap_5 = ttk.LabelFrame(tab14, width=50, height=30, text = "Zapytanie 5")
frameZap_5.grid(row=4,column=0)
etykieta_Zap5 = tk.Label(frameZap_5, text="""Wyświetl nazwiska i stawki godzinowe powiększone o 15% dla wszystkich pracowników
z pensją naliczaną godzinowo i zaokrąglone do liczb całkowitych.""")
etykieta_Zap5.grid(row=1, column=0)

frameZap_6 = ttk.LabelFrame(tab14, width=50, height=30, text = "Zapytanie 6")
frameZap_6.grid(row=0, column=1)
etykieta_Zap6 = tk.Label(frameZap_6, text="""Dla każdego pracownika zatrudnionego na stałym etacie wyświetl wartość jego płacy
podstawowej, ale ukryj wartość płacy jeśli etat pracownika to 'Ordynator'.""")
etykieta_Zap6.grid(row=1, column=0)

frameZap_7 = ttk.LabelFrame(tab14, text = "Zapytanie 7")
frameZap_7.grid(row=1, column=1)
etykieta_Zap7 = tk.Label(frameZap_7, text="""Dla każdego oddziału wyświetl liczbę zatrudnionych w nim pracowników.""")
etykieta_Zap7.grid(row=1, column=0)

frameZap_8 = ttk.LabelFrame(tab14, width=50, height=30, text = "Zapytanie 8")
frameZap_8.grid(row=2, column=1)
etykieta_Zap8 = tk.Label(frameZap_8, text="""Wyświetl nazwiska i etaty pracowników, których rzeczywiste zarobki nie przekraczają
50% zarobków ich szefów.""")
etykieta_Zap8.grid(row=1, column=0)

frameZap_9 = ttk.LabelFrame(tab14, width=50, height=30, text = "Zapytanie 9")
frameZap_9.grid(row=3, column=1)
etykieta_Zap9 = tk.Label(frameZap_9, text="""Podaj nazwę oddziału oraz liczbę pacjentów, w których ilość pacjentów przekracza
średnią ilość pacjentów na oddział w szpitalu.""")
etykieta_Zap9.grid(row=1, column=0)

frameZap_10 = ttk.LabelFrame(tab14, width=50, height=30, text = "Zapytanie 10")
frameZap_10.grid(row=4, column=1)
etykieta_Zap10 = tk.Label(frameZap_10, text="""Wyświetl nazwę oddziału wypłacającego miesięcznie swoim pracownikom ze stałą
pensją najwięcej pieniędzy.""")
etykieta_Zap10.grid(row=1, column=0)


#Zapytanie 1
#def create_window_Zap1():
    #window = tk.Toplevel(frameZap_1)
    #window.title("Zapytanie 1")
    #window.geometry("800x500")
    #poleTekstowe = tk.Text(window, width=500, height=300, background="white")
    #poleTekstowe.pack()
    #u = cur.execute("""SELECT nazwisko, data_urodzenia FROM (pacjenci NATURAL JOIN
#pacjenci_przedmioty) NATURAL JOIN wizyty WHERE diagnoza='cukrzyca' AND wizyty.id_lekarza=113
#AND nazwa_przedmiotu='Cetol-2';""")
    #y = cur.fetchall()
    #poleTekstowe.insert(tk.END, y)

def create_window_Zap1():
    select = ("""SELECT nazwisko, data_urodzenia FROM (pacjenci NATURAL JOIN
pacjenci_przedmioty) NATURAL JOIN wizyty WHERE diagnoza='cukrzyca' AND wizyty.id_lekarza=113
AND nazwa_przedmiotu='Cetol-2';""")
    window = Tk()
    window.title("Zapytanie 1")
    window.geometry("500x300")
    txt = scrolledtext.ScrolledText(window, width=200, height=200, background="white")
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')


def on_select_Zap1(event=None):
    if event:
        create_window_Zap1()


b_Zap1 = tk.Button(frameZap_1, text="Pokaż")
b_Zap1.grid(row=2, columnspan=2)
b_Zap1.bind("<Button-1>", on_select_Zap1)


# Zapytanie 2
def create_window_Zap2():
    select = ("""SELECT pacjenci.nazwisko FROM pacjenci JOIN lekarze ON
pacjenci.id_lekarza=lekarze.id_lekarza WHERE lekarze.nazwisko='Samuel' OR
lekarze.nazwisko='Gąska' OR lekarze.nazwisko='Pająk' GROUP BY pacjenci.nazwisko;""")
    window = Tk()
    window.title("Zapytanie 2")
    window.geometry("500x300")
    txt = scrolledtext.ScrolledText(window, width=500, height=300, background="white")
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')


def on_select_Zap2(event=None):
    if event:
        create_window_Zap2()


b_Zap2 = tk.Button(frameZap_2, text="Pokaż")
b_Zap2.grid(row=2, columnspan=2)
b_Zap2.bind("<Button-1>", on_select_Zap2)


# Zapytanie 3
def create_window_Zap3():
    select = ("""SELECT count(*)
FROM (SELECT COUNT(pacjenci.numer_pacjenta) 
	FROM (pacjenci JOIN wizyty ON pacjenci.numer_pacjenta=wizyty.numer_pacjenta)
	JOIN lekarze ON wizyty.id_lekarza=lekarze.id_lekarza
	WHERE specjalnosc='Internista' AND pacjenci.nazwisko LIKE 'S%'
	GROUP BY pacjenci.nazwisko
	HAVING COUNT (*)>2);""")
    window = Tk()
    window.title("Zapytanie 2")
    window.geometry("500x300")
    txt = scrolledtext.ScrolledText(window, width=500, height=300, background="white")
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')


def on_select_Zap3(event=None):
    if event:
        create_window_Zap3()


b_Zap3 = tk.Button(frameZap_3, text="Pokaż")
b_Zap3.grid(row=2, columnspan=2)
b_Zap3.bind("<Button-1>", on_select_Zap3)


# Zapytanie 4
def create_window_Zap4():
    select = ("""SELECT MIN(mycount),imie,nazwisko
FROM    (SELECT imie,nazwisko,COUNT(wizyty.id_lekarza) mycount 
	FROM lekarze JOIN wizyty ON lekarze.id_lekarza=wizyty.id_lekarza
	WHERE data_wizyty between "2015-01-01" and "2015-12-31"
	GROUP BY wizyty.id_lekarza
	HAVING COUNT (*));""")
    window = Tk()
    window.title("Zapytanie 4")
    window.geometry("500x300")
    txt = scrolledtext.ScrolledText(window, width=500, height=300, background="white")
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')


def on_select_Zap4(event=None):
    if event:
        create_window_Zap4()


b_Zap4 = tk.Button(frameZap_4, text="Pokaż")
b_Zap4.grid(row=2, columnspan=2)
b_Zap4.bind("<Button-1>", on_select_Zap4)


# Zapytanie 5
def create_window_Zap5():
    select = ("""SELECT nazwisko,pensja_godzinowa,
round(pensja_godzinowa * 1.15, 0) FROM pracownicy
WHERE pensja_godzinowa<>'0';""")
    window = Tk()
    window.title("Zapytanie 5")
    window.geometry("500x450")
    txt = scrolledtext.ScrolledText(window, width=500, height=300, background="white")
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')


def on_select_Zap5(event=None):
    if event:
        create_window_Zap5()


b_Zap5 = tk.Button(frameZap_5, text="Pokaż")
b_Zap5.grid(row=2, columnspan=2)
b_Zap5.bind("<Button-1>", on_select_Zap5)






#Zapytanie 6
def create_window_Zap6():
    select = ("""SELECT nazwisko,
    CASE WHEN etat = 'Ordynator' THEN '***'
    ELSE cast(pensja_stała as character(10))
    END as pensja
    FROM pracownicy WHERE pensja_stała<>'null';""")
    window = Tk()
    window.title("Zapytanie6")
    window.geometry('500x500')
    txt = scrolledtext.ScrolledText(window, width=200, height=200)
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')

def on_select_Zap6(event=None):
    if event:
        create_window_Zap6()


b_Zap6 = tk.Button(frameZap_6, text="Pokaż")
b_Zap6.grid(row=2, columnspan=2)
b_Zap6.bind("<Button-1>", on_select_Zap6)


#Zapytanie 7
def create_window_Zap7():
    select = ("""select nazwa_oddzialu, count(*) as liczba_pracowników from oddzialy odd left join pracownicy_oddzialy pr_oddz where 
    odd.numer_oddzialu=pr_oddz.numer_oddzialu group by nazwa_oddzialu;""")
    window = Tk()
    window.title("Zapytanie 7")
    window.geometry('300x200')
    txt = scrolledtext.ScrolledText(window, width=200, height=200)
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')

def on_select_Zap7(event=None):
    if event:
        create_window_Zap7()


b_Zap7 = tk.Button(frameZap_7, text="Pokaż")
b_Zap7.grid(row=2, columnspan=2)
b_Zap7.bind("<Button-1>", on_select_Zap7)




#Zapytanie 8
def create_window_Zap8():
    select = ("""select nazwisko, etat from pracownicy where pensja_stała<(select 0.5*pensja_stała from pracownicy where 
    id_szefa is not null);""")
    window = Tk()
    window.title("Zapytanie 8")
    window.geometry('300x200')
    txt = scrolledtext.ScrolledText(window, width=200, height=200)
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')

def on_select_Zap8(event=None):
    if event:
        create_window_Zap8()

b_Zap8 = tk.Button(frameZap_8, text="Pokaż")
b_Zap8.grid(row=2, columnspan=2)
b_Zap8.bind("<Button-1>", on_select_Zap8)




#Zapytanie 9
def create_window_Zap9():
    select = ("""with Pancjenci_na_Oddział as (select oddz.nazwa_oddzialu, loz.numer_oddzialu, loz.numer_pacjenta, count(*) as 
    liczba_pacjentów from oddzialy oddz left join lozka loz on oddz.numer_oddzialu=loz.numer_oddzialu where 
    numer_pacjenta is not null group by oddz.nazwa_oddzialu) select * from Pancjenci_na_Oddział where 
    liczba_pacjentów>(select avg(liczba_pacjentów) from Pancjenci_na_Oddział);""")
    window = Tk()
    window.title("Zapytanie 9")
    window.geometry('500x200')
    txt = scrolledtext.ScrolledText(window, width=200, height=200)
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')

def on_select_Zap9(event=None):
    if event:
        create_window_Zap9()


b_Zap9 = tk.Button(frameZap_9, text="Pokaż")
b_Zap9.grid(row=2, columnspan=2)
b_Zap9.bind("<Button-1>", on_select_Zap9)




#Zapytanie 10
def create_window_Zap10():
    select = ("""select nazwa_oddzialu, max(sumy_pensji) from (select nazwa_oddzialu, sum(pensja_stała) as sumy_pensji from
    oddzialy oddz left join pracownicy_oddzialy pr_od on oddz.numer_oddzialu=pr_od.numer_oddzialu left join
    pracownicy prac on pr_od.numer_pracownika=prac.numer_pracownika group by nazwa_oddzialu);""")
    window = Tk()
    window.title("Zapytanie 10")
    window.geometry('400x200')
    txt = scrolledtext.ScrolledText(window, width=200, height=200)
    txt.grid(column=0, row=0)
    cur.execute(select)
    w = cur.fetchall()
    x = [tuple[0] for tuple in cur.description]
    txt.insert(INSERT, x)
    txt.insert(END, '\n')
    for row in w:
        print(row)
        txt.insert(INSERT, list(row))
        txt.insert(END, '\n')

def on_select_Zap10(event=None):
    if event:
        create_window_Zap10()


b_Zap10 = tk.Button(frameZap_10, text="Pokaż")
b_Zap10.grid(row=2, columnspan=2)
b_Zap10.bind("<Button-1>", on_select_Zap10)




okno.mainloop()












