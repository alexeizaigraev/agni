from tkinter import *
import tkinter
from typing import Any
from db.actual_refresh_otbor import ActualRefreshOtbor
from doc.act_peredachi import ActPeredachi
from doc.activaciya import Activqaciya
from modules import *
import os
import sys
import subprocess
from papa_pg import get_partners, get_terminals_list

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


from people.priem import *
from people.otpusk import *
from people.perevod import *
from people.postall import *
from some.pg_term import *
from some.pg_site import *
from some.pg_summury_otbor import *
from some.pg_summury import *
from some.pg_summury_ab import *
from some.natasha import *
from some.activ_term import *
from db.add_otbor_hard import *
from db.add_otbor import *
from db.add_otbor_hard_dep import *
from db.refresh_all import *
from monitor.walker import *
from monitor.monitor import *
from monitor.get_rp import *
from monitor.get_rp_all import *
from monitor.gnetz import *
from monitor.gdrive_backup_comon import *
from monitor.gdrive_backup_date import *
from kabinet.rro import *
from kabinet.pereezd import *
from kabinet.otmena import *
from kabinet.prro import *
from kabinet.knigi import *
from db.actual_refresh_all import *
from db.del_actual_all import *
from db.del_actual_otbor import *
from db.analis import *




def clear_me():
    text_box.delete(1.0, END)

def people_priem():
    clear_me()
    try:
        u = Priem()
        u.priem_main()
        text_box.insert(1.0, u.info)
    except Exception as ex:
        text_box.insert(1.0, str(ex))
   
def people_otpusk():
    clear_me()
    try:
        u = Otpusk()
        u.otpusk_main()
        text_box.insert(1.0, u.info)
    except Exception as ex:
        text_box.insert(1.0, str(ex))
 
def people_perevod():
    clear_me()
    try:
        u = Perevod()
        u.perevod_main()
        text_box.insert(1.0, u.info)
    except Exception as ex:
        text_box.insert(1.0, str(ex))
    

def people_postall():
    clear_me()
    try:
        u = Postall()
        u.postall_main()
        text_box.insert(1.0, u.info)
    except Exception as ex:
        text_box.insert(1.0, str(ex))


def some_term():
    text = ''
    clear_me()
    try:
        u = Term()
        u.main_term()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)
    



def some_site():
    text = ''
    clear_me()
    try:
        u = Site()
        u.main_site()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)
    

def some_summury_otbor():
    clear_me()
    text = ''
    try:
        u = SummuryOtbor()
        u.main_summury_otbor()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)


def some_summury():
    clear_me()
    selected_items  = box_partners.curselection()
    partner_choise = partners[selected_items[0]]
    text = ''
    try:
        get_terminals_list_partner(partner_choise)
        u = Summury(partner_choise)
        u.main_summury()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)
    
    

def some_summury_ab():
    text = ''
    clear_me()
    try:
        u = SummuryAb()
        u.main_summury_ab()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)
    



def some_natasha():
    text = ''
    clear_me()
    try:
        u = Natasha()
        u.main_natasha()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)

def some_activ_term():
    text = ''
    clear_me()
    try:
        u = ActivTerm()
        u.main_activ_term()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)
    


def otbor_text():
    mytext = str(text_box.get(1.0, END)).strip()
    text = ''
    
    try:
        u = Otbor(mytext)
        u.otbor_main()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    clear_me()    
    text_box.insert(1.0, text)
    
def otbor_text_list():
    mytext = str(text_box.get(1.0, END)).strip()
    text = ''
    
    try:
        u = OtborHardDep(mytext)
        u.main_otbor_hard_dep()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    clear_me()    
    text_box.insert(1.0, text)

    
def otbor_otbor():
    clear_me()
    term_list = []
    selected  = box_terminals.curselection()
    values = [box_terminals.get(idx) for idx in box_terminals.curselection()]
    text_box.insert(1.0, str(values))
    
    try:
        u = OtborHard(values)
        u.main_otbor_hard()
        text_box.insert(1.0, u.info)
    except Exception as ex:
        text_box.insert(1.0, str(ex))
    

def refresh_refresh():
    text = ''
    clear_me()
    try:
        u = RefreshAll()
        u.main_refresh()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)
    


def monitor_rasklad():
    clear_me()
    try:
        u = Walker()
        u.walker_main()
        text_box.insert(1.0, u.info)
    except Exception as ex:
        text_box.insert(1.0, str(ex))

def monitor_monitor():
    clear_me()
    try:
        u = Monitor()
        u.monitor_main()
        text_box.insert(1.0, u.info)
    except Exception as ex:
        text_box.insert(1.0, str(ex))



def monitor_get_rp():
    text = ''
    clear_me()
    try:
        u = GetRp()
        u.get_rp_main()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)
    
def monitor_get_rp_all():
    clear_me()
    selected_items  = box_folders.curselection()
    choise = folders[selected_items[0]]
    text = ''
    try:
        u = GetRpAll(choise)
        u.get_rp_all_main()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
        #text = '123'
    text_box.insert(1.0, text)
 
def monitor_gnetz_copy():
    kind = 'copy'
    text = ''
    clear_me()
    try:
        u = Gnetz(kind)
        u.gnetz_main()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)

def monitor_gnetz_move():
    kind = 'move'
    text = ''
    clear_me()
    try:
        u = Gnetz(kind)
        u.gnetz_main()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)  

def monitor_gdrive_backup_comon():
    text = ''
    clear_me()
    try:
        u = GdriveBackComon()
        u.gdriveback_comon_main()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)  

def monitor_gdrive_backup_date():
    kind = 'move'
    text = ''
    clear_me()
    try:
        u = GdriveBackDate()
        u.gdrive_back_date_main()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)  

def kabinet_rro():
    text = ''
    clear_me()
    try:
        u = Rro()
        u.main_rro()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)
    


def kabinet_pereezd():
    text = ''
    clear_me()
    try:
        u = Pereezd()
        u.main_pereezd()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)
    


def kabinet_otmena():
    text = ''
    clear_me()
    try:
        u = Otmena()
        u.main_otmena()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)
    


def kabinet_prro():
    text = ''
    clear_me()
    try:
        u = Prro()
        u.main_prro()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)
    
def kabinet_knigi():
    text = ''
    clear_me()
    try:
        u = Knigi()
        u.knigi_main()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)


def actual_all():
    text = ''
    clear_me()
    try:
        u = ActualAll()
        u.main_actual_all()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)


def actual_otbor():
    text = ''
    clear_me()
    try:
        u = ActualRefreshOtbor()
        u.main_actual_refresh_otbor()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)



def actual_del_otbor():
    text = ''
    clear_me()
    try:
        u = DelActualOtbor()
        u.main_del_actual_otbor()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)

def actual_del_all():
    text = ''
    clear_me()
    try:
        u = DelActualAll()
        u.main_del_actual_all()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)
 

def actual_analis():
    text = ''
    clear_me()
    try:
        u = Analis()
        u.main_analis()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)


def doc_activaciya():
    text = ''
    clear_me()
    try:
        u = Activqaciya()
        u.main_activaciya()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)

def doc_act_peredachi():
    text = ''
    clear_me()
    try:
        u = ActPeredachi()
        u.main_act_peredachi()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)




def clear_lb_term():
    #terms = get_terminals_list()
    box_terminals.delete(0, END)

def clear_lb_partners():
    box_partners.delete(0, END)

def clear_lb_folders():
    box_folders.delete(0, END)

def mk_partners():
    clear_lb_partners()
    partners = get_partners()
    for partner in partners:
        box_partners.insert(END, partner)


def mk_terminals():
    clear_lb_term()
    terminals = get_terminals_list()
    for terminal in terminals:
        box_terminals.insert(END, terminal)

def mk_folders():
    clear_lb_folders()
    items = comon_data_list(3)
    for item in items:
        box_folders.insert(END, item)
 


def refresh_lb_term():
    global terminals
    try:
        clear_lb_term()
    except:
        pass
    try:
        partner_choise  = partners[box_partners.curselection()[0]]
        if partner_choise:
            terminals = get_terminals_list_partner(partner_choise)
            for item in terminals:
                box_terminals.insert(END, item)
        else:
            mk_terminals()
    except:
        mk_terminals()
    
def refresh_me():
    app_path = file_to_vec('Config/app_path.txt')[0]
    try:
        subprocess.run(app_path)
    except:
        pass
    u = RefreshAll()
    u.main_refresh()

    mk_partners()
    mk_terminals() 
    mk_folders()


 
root = Tk()

mainmenu = Menu(root) 

font_size = 18
font_style = "Verdana"
root.config(menu=mainmenu)

people_memu = Menu(mainmenu, tearoff=0)
people_memu.add_command(label="??????????", command=people_priem, font=(font_style, font_size))
people_memu.add_command(label="????????????", command=people_otpusk, font=(font_style, font_size))
people_memu.add_command(label="??????????????", command=people_perevod, font=(font_style, font_size))
people_memu.add_command(label="????????????????", command=people_postall, font=(font_style, font_size))
 
some_memu = Menu(mainmenu, tearoff=0)
some_memu.add_command(label="??????????????????", command=some_term, font=(font_style, font_size))
some_memu.add_command(label="????????", command=some_site, font=(font_style, font_size))
some_memu.add_command(label="?????????? ??????????", command=some_summury_otbor, font=(font_style, font_size))
some_memu.add_command(label="??????????", command=some_summury, font=(font_style, font_size))
some_memu.add_command(label="???????????? ????", command=some_summury_ab, font=(font_style, font_size))
some_memu.add_command(label="????????????", command=some_natasha, font=(font_style, font_size))
some_memu.add_command(label="???????????????? ??????????", command=some_activ_term, font=(font_style, font_size))


otbor_memu = Menu(mainmenu, tearoff=0)
otbor_memu.add_command(label="??????????", command=otbor_otbor, font=(font_style, font_size))
otbor_memu.add_command(label="?????????????????? ???? ????", command=otbor_text, font=(font_style, font_size))
otbor_memu.add_command(label="???????????? ??????????????????", command=otbor_text_list, font=(font_style, font_size))


refresh_memu = Menu(mainmenu, tearoff=0)
refresh_memu.add_command(label="????????????????", command=refresh_refresh, font=(font_style, font_size))


monitor_memu = Menu(mainmenu, tearoff=0)
monitor_memu.add_command(label="??????????????", command=monitor_rasklad, font=(font_style, font_size))
monitor_memu.add_command(label="??????????????", command=monitor_monitor, font=(font_style, font_size))
monitor_memu.add_command(label="???? ??????????", command=monitor_get_rp, font=(font_style, font_size))
monitor_memu.add_command(label="???? ??????????????", command=monitor_get_rp_all, font=(font_style, font_size))
monitor_memu.add_command(label="???????? ????????", command=monitor_gnetz_copy, font=(font_style, font_size))
monitor_memu.add_command(label="???????? ????????", command=monitor_gnetz_move, font=(font_style, font_size))
monitor_memu.add_command(label="???????? ?????????? ??????????", command=monitor_gdrive_backup_comon, font=(font_style, font_size))
monitor_memu.add_command(label="???????? ?????????? ????????", command=monitor_gdrive_backup_date, font=(font_style, font_size))


kabinet_memu = Menu(mainmenu, tearoff=0)
kabinet_memu.add_command(label="??????", command=kabinet_rro, font=(font_style, font_size))
kabinet_memu.add_command(label="??????????????", command=kabinet_pereezd, font=(font_style, font_size))
kabinet_memu.add_command(label="????????????", command=kabinet_otmena, font=(font_style, font_size))
kabinet_memu.add_command(label="????????", command=kabinet_prro, font=(font_style, font_size))
kabinet_memu.add_command(label="??????????", command=kabinet_knigi, font=(font_style, font_size))

lb_memu = Menu(mainmenu, tearoff=0)
lb_memu.add_command(label="clearTerm", command=clear_lb_term, font=(font_style, font_size))
lb_memu.add_command(label="?????????????????? ????????????", command=refresh_lb_term, font=(font_style, font_size))


clear_memu = Menu(mainmenu, tearoff=0)
clear_memu.add_command(label="??????????????", command=clear_me, font=(font_style, font_size))

actual_memu = Menu(mainmenu, tearoff=0)
actual_memu.add_command(label="???????????? ??????", command=actual_all, font=(font_style, font_size))
actual_memu.add_command(label="???????????? ??????????", command=actual_otbor, font=(font_style, font_size))
actual_memu.add_command(label="?????????? ??????????", command=actual_del_otbor, font=(font_style, font_size))
actual_memu.add_command(label="?????????? ??????", command=actual_del_all, font=(font_style, font_size))
actual_memu.add_command(label="????????????", command=actual_analis, font=(font_style, font_size))

doc_memu = Menu(mainmenu, tearoff=0)
doc_memu.add_command(label="??????????????????", command=doc_activaciya, font=(font_style, font_size))
doc_memu.add_command(label="?????? ????????????????", command=doc_act_peredachi, font=(font_style, font_size))




refresh_memu = Menu(mainmenu, tearoff=0)
refresh_memu.add_command(label="????????????", command=refresh_me, font=(font_style, font_size))





mainmenu.add_cascade(label="????????",
                     menu=people_memu)
mainmenu.add_cascade(label="??????????????",
                     menu=some_memu)
mainmenu.add_cascade(label="??????????????",
                     menu=monitor_memu)
mainmenu.add_cascade(label="??????????????",
                     menu=kabinet_memu)
mainmenu.add_cascade(label="??????????????????",
                     menu=lb_memu)
mainmenu.add_cascade(label="??????????????",
                     menu=clear_memu)
mainmenu.add_cascade(label="??????????????",
                     menu=actual_memu)
mainmenu.add_cascade(label="????????",
                     menu=doc_memu)
mainmenu.add_cascade(label="??????????",
                     menu=otbor_memu)                
mainmenu.add_cascade(label="????????????",
                     menu=refresh_memu)
#mainmenu.add_command(label="??????????????", font=("Verdana", 30))




#root = Tk()
font_size = 18
font_style = "Verdana"
BOX_WIDH = 10

Button(text="????????", command=otbor_text, background = 'cyan').grid(row=0, column=10, sticky=W)
Button(text="????????????", command=refresh_me, background = 'cyan').grid(row=0, column=10)
Button(text="????????????", command=clear_me, background = 'cyan').grid(row=0, column=10, sticky=E)
Button(text="??????????????", command=refresh_lb_term, background = 'cyan').grid(row=0, column=1, sticky=W+E)
Button(text="????????????????", command=otbor_otbor, background = 'cyan').grid(row=0, column=4, sticky=W+E)
Button(text="", background = 'cyan').grid(row=0, column=6, sticky=W+E)
Button(text="???????? ????", command=monitor_get_rp_all, background = 'cyan').grid(row=0, column=7, sticky=W+E)
Button(text="", background = 'cyan').grid(row=3, column=9)

Button(text="", background = 'cyan').grid(row=3, column=0)
Button(text="", background = 'cyan').grid(row=3, column=11)


text_box = Text(font=(font_style, font_size), width=50, foreground='darkblue', background='cyan')
#text_box.grid(row=1, column=10)
text_box.grid(row=1, column=10, sticky=E+W)



box_partners = Listbox(selectmode=EXTENDED, font=(font_style, font_size), foreground='blue', background='cyan', width=BOX_WIDH)
box_partners.grid(row=1, column=1, rowspan=2, sticky=N+S)
scroll_partners = Scrollbar(command=box_partners.yview)
scroll_partners.grid(row=1, column=2, rowspan=3, sticky=N+S)
box_partners.config(yscrollcommand=scroll_partners.set)

box_terminals = Listbox(selectmode=EXTENDED, font=(font_style, font_size), foreground='blue', background='cyan', width=BOX_WIDH)
box_terminals.grid(row=1, column=4, rowspan=2, sticky=N+S)
scroll_terminals = Scrollbar(command=box_terminals.yview)
scroll_terminals.grid(row=1, column=5, rowspan=3, sticky=N+S)
box_terminals.config(yscrollcommand=scroll_terminals.set)

box_folders = Listbox(selectmode=EXTENDED, font=(font_style, font_size), foreground='blue', background='cyan', width=BOX_WIDH)
box_folders.grid(row=1, column=7, rowspan=2, sticky=N+S)
scroll_folders = Scrollbar(command=box_folders.yview)
scroll_folders.grid(row=1, column=8, rowspan=3, sticky=N+S)
box_folders.config(yscrollcommand=scroll_folders.set)


partners = get_partners()
folders = comon_data_list(3)

terminals = get_terminals_list()




root["bg"] = "cyan"
root.mainloop()