from tkinter import Tk, Entry, Label, Button,Canvas,Scrollbar, StringVar, Frame, Radiobutton
from tkinter.ttk import Combobox
#import telebot
import os
#import threading
#import json

import random

NAMES = [
    "Иванов Иван Иванович",
    "Смирнова Елена Петровна",
    "Кузнецова Ольга Александровна",
    "Попов Дмитрий Сергеевич",
    "Васильев Андрей Иванович",
    "Петрова Александра Дмитриевна",
    "Соколов Владимир Сергеевич",
    "Михайлова Екатерина Алексеевна",
    "Федоров Сергей Игоревич",
    "Морозова Мария Павловна",
    "Волков Алексей Александрович",
    "Алексеева Ирина Сергеевна",
    "Лебедев Игорь Анатольевич",
    "Семенова Татьяна Викторовна",
    "Егоров Денис Дмитриевич",
    "Павлова Елена Сергеевна",
    "Козлов Андрей Игоревич",
    "Степанова Анастасия Владимировна",
    "Николаев Илья Александрович",
    "Орлова Марина Викторовна",
    "Андреев Олег Владимирович",
    "Макарова Алина Павловна",
    "Захаров Максим Анатольевич",
    "Ефимова Валерия Дмитриевна",
    "Никитин Даниил Сергеевич",
    "Соловьева Елизавета Алексеевна",
    "Тимофеев Иван Викторович",
    "Осипова Дарья Егоровна",
    "Белов Александр Дмитриевич",
    "Калинина Ольга Сергеевна",
    "Медведев Дмитрий Иванович"
]
GROUPS = {
    "Group1":None,
    "Group2":None,
    "Group3":None,
    "Group4":None,
    "Group5":None,
    "Group6":None}

StatusNameList = [
    "ТЕХ",
    "РУЧНОЙ",
    "НА ЛИНИИ",
    "ОБЗВОН",
    "ОБУЧЕНИЕ"
]
DISTRIBUTION = {}
namesTemp = NAMES.copy()
for group in GROUPS:
    DISTRIBUTION[group] = []
    for i in range(3):
        name = random.choice(namesTemp)
        DISTRIBUTION[group].append(name)
        namesTemp.remove(name)
        


SELECTION = []
CWD = os.path.realpath(os.path.dirname(__name__))

MAIN = "#25252f"

window = Tk()
window.title("R.A.C.H.E.L. User Interface")
window.geometry("")

MainFrame = Frame(window)
MainFrame.pack(fill="both",expand=1,padx=3,pady=3)
TopFrame = Frame(MainFrame,relief="solid",borderwidth=2)
TopFrame.pack(side="top",fill="both",expand=1)
UtilitiesFrame = Frame(MainFrame,relief="solid",borderwidth=2)
UtilitiesFrame.pack(side="bottom",anchor="n",fill="x",pady=(2,0))

LeftFrame = Frame(TopFrame)
RButtonsFrame = Frame(LeftFrame,relief="solid",borderwidth=2)


StatusFrame = Frame(TopFrame,relief="solid",borderwidth=2)

RBLabel = Label(StatusFrame,text="Выберите статус в меню слева")

MuteButtonFrame = Frame(UtilitiesFrame,relief="solid",borderwidth=1)
MuteButtonFrame.pack(side="right",anchor="s")
MuteButton = Button(MuteButtonFrame,text="Выключить уведомления")
MuteButton.pack(side="right",anchor="s",padx=2,pady=2)

NameLabel = Label(TopFrame,text="Имя оператора в чате")
NameEntry = Entry(TopFrame,width=50)
GroupLabel = Label(TopFrame, text="Группа оператора")
GroupCombobox = Combobox(TopFrame,width=15)
GroupCombobox["values"] = GROUPS
GroupCombobox['state'] = 'readonly'

def ClearUI(Frame): # make universal clean
    for widget in Frame.winfo_children():
        widget.pack_forget()
def StatusPicked():
    ClearUI(StatusFrame)
    
    StatusSendFrame.pack(side="top",anchor="w",fill="x")
    StatusSend.pack(side="top",anchor="w",padx=2,pady=2,fill="x")
    
    GroupSelSaveButtonFrame = Frame(LeftFrame,relief="solid",borderwidth=2)
    GroupSelSaveButtonFrame.pack(side="bottom",anchor="w",fill="x")
    GroupSelSaveButton = Button(GroupSelSaveButtonFrame,text="Сохранить тек.группу",command=SaveSelection)
    GroupSelSaveButton.pack(side="bottom",anchor="w",fill="x")

    canvas = Canvas(StatusFrame)
    canvas.pack(side="left",fill="both",expand=1)
    scrollbar = Scrollbar(StatusFrame,orient="vertical",command=canvas.yview)
    scrollbar.pack(side="right",fill="y")
    def _bound_to_mousewheel(event):
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
    def _unbound_to_mousewheel(event):
        canvas.unbind_all("<MouseWheel>")
    canvas.bind('<Enter>', _bound_to_mousewheel)
    canvas.bind('<Leave>', _unbound_to_mousewheel)
    def _on_mousewheel(event):
        canvas.yview_scroll(-1*(event.delta//120), "units")
    window.bind_all("<MouseWheel>", _on_mousewheel)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>",lambda e: canvas.config(scrollregion=canvas.bbox("all")))
    StatusWindow = Frame(canvas)
    canvas.create_window((0,0),window=StatusWindow,anchor="nw")
    for group in GROUPS:
        GroupSelFrame = Frame(LeftFrame,relief="solid",borderwidth=2)
        GroupSelFrame.pack(side="top",anchor="w",fill="x")
        GroupSelButton = Button(GroupSelFrame, text=group, command=lambda i=DISTRIBUTION[group]:Select(i))
        GroupSelButton.pack(side="top",anchor="w",padx=2,pady=2,fill="x")
        
        GroupFrame = Frame(StatusWindow)
        GROUPS[group] = GroupFrame
        GroupFrame.pack(side="top",anchor="w",fill="both",expand=1)
        GroupLeftFrame = Frame(GroupFrame,relief="solid",borderwidth=2,name="group_"+str(random.randint(100,999))+"_"+group)
        GroupLeftFrame.pack(side="left",anchor="n",fill="y")
        GroupRightFrame = Frame(GroupFrame,relief="solid",borderwidth=2)
        GroupRightFrame.pack(side="left",anchor="n",fill="both",expand=1)
        GroupNameLabel = Label(GroupLeftFrame,text=group)
        GroupNameLabel.pack(side="top",anchor="w",fill="x")
        for name in DISTRIBUTION[group]:
            GroupOperatorFrame = Frame(GroupRightFrame,relief="solid",borderwidth=1,name="frame_"+name)
            GroupOperatorFrame.pack(side="top",anchor="w",padx=(0,2),fill="x")
            GroupOperatorNameLabel = Label(GroupOperatorFrame,text=name)
            GroupOperatorNameLabel.pack(side="left",anchor="n",pady=2)
            GroupOperatorSelButton = Button(GroupOperatorFrame,text="Выбрать")
            GroupOperatorSelButton.configure(command=lambda i=name: Select(i))
            GroupOperatorSelButton.pack(side="right",anchor="n",pady=2)



def Send():
    raise NotImplementedError

Statuses = [StatusNameList[i] for i in range(len(StatusNameList))]
Status = StringVar()
StatusSendFrame = Frame(LeftFrame,relief="solid",borderwidth=2)
StatusSend = Button(StatusSendFrame,text="Отправить статус",command=Send)

def Select(names):
    #print("names type: {};names len:{};Sel len:{} ".format(type(names),len(names),len(SELECTION)),end="-> ")
    if(type(names)==list):
        groupKey = list(DISTRIBUTION.keys())[list(DISTRIBUTION.values()).index(names)]
        if(groupKey in SELECTION):
            color = "white" 
            func = SELECTION.remove
        else:
            color = "lightblue" 
            func = SELECTION.append
        for widget in GROUPS[groupKey].winfo_children()[1].winfo_children():
            if(widget.winfo_name()[:5]=="frame"):
                try:func(widget.winfo_name()[6:])
                except ValueError:pass
                widget.configure(bg=color)
        for widget in GROUPS[groupKey].winfo_children():
            if(widget.winfo_name()[:5]=="group"):
                try:func(groupKey)
                except ValueError:pass
                widget.configure(bg=color)
    else:
        if (names in SELECTION):
            color = "white" 
            func = SELECTION.remove
        else:
            color = "lightblue" 
            func = SELECTION.append
        for key in list(DISTRIBUTION.keys()):
            if(names in DISTRIBUTION[key]):
                groupKey=key
                break
        for widget in GROUPS[groupKey].winfo_children()[1].winfo_children():
            if(names in widget.winfo_name()):
                func(names)
                widget.configure(bg=color)
                break
    #print("Sel len:{}".format(len(SELECTION)))

def SaveSelection():
    pass


def PageSetupUI():
    NameLabel.pack(side="top",anchor="w",padx=2,pady=2)
    NameEntry.pack(side="top",anchor="w",padx=2,pady=2)
    GroupLabel.pack(side="top",anchor="w",padx=2,pady=2)
    GroupCombobox.pack(side="top",anchor="w",padx=2,pady=2)
    OperationButton.pack(side="top",anchor="w",padx=2,pady=2)
def PageOperationRBUI():
    LeftFrame.pack(side="left",anchor="n",fill="both")
    RButtonsFrame.pack(side="top",fill="x")
    for RButton in Statuses:
        StatusRadiobutton = Radiobutton(RButtonsFrame, text=RButton,value=RButton,variable=Status)
        StatusRadiobutton.pack(side="top",anchor="w",padx=(5,2))
    RBLabel.pack(side="top",anchor="w")
    StatusFrame.pack(side="left",anchor="n",fill="both",expand=1)
    StatusPicked()
    
def OperationUI():
    ClearUI(TopFrame)
    PageOperationRBUI()
OperationButton = Button(TopFrame,text="Начать",command=OperationUI)
PageOperationRBUI()
window.mainloop()