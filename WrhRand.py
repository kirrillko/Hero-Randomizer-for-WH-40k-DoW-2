from tkinter import *
import random
from PIL import Image, ImageTk

class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(False, False)):
        self.root=Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+280+150')
        self.root.resizable(resizable[0], resizable[1])

        #ИКОНКА ПРИЛОЖЕНИЯ
        icon = "venv/images/ico.ico"
        self.root.iconbitmap(default=icon)

        #МАССИВЫ ЧЕКБОКСОВ И ИХ СОСТОЯНИЙ, ПЕРЕМЕННЫЕ ГЕРОЕВ
        chk = []
        chk_state = []
        hero1='герой 1'
        hero2='герой 2'

        #СПИСОК ГЕРОЕВ В ИГРЕ
        heroes=[]
        heroes.append('Командор')
        heroes.append('Апотекарий')
        heroes.append('Технодесантник')
        heroes.append('Лорд Хаоса')
        heroes.append('Чемпион Чумы')
        heroes.append('Колдун Хаоса')
        heroes.append('Варлок')
        heroes.append('Экзарх пауков варпа')
        heroes.append('Видящая')
        heroes.append('Босс')
        heroes.append('Ноб-Коммандо')
        heroes.append('Мек')
        heroes.append('Тиран Улья')
        heroes.append('Альфа-Пожиратель')
        heroes.append('Альфа-Ликтор')
        heroes.append('Инквизитор')
        heroes.append('Лорд-Комиссар')
        heroes.append('Лорд-Генерал')
        heroes.append('Brother-Captain')
        heroes.append('2-й серый рыцарь')
        heroes.append('3-й серый рыцарь')

        # ГЕРОИ ИГРОКА 1
        lblpl1 = Label(self.root, text="Герои игрока 1", font=("Arial Bold", 14))
        lblpl1.grid(column=0, row=0)
        lblh1 = Label(self.root, text=hero1, font=("Arial Bold", 14))
        lblh1.grid(column=5, row=0)

        for i in range(0,21):
            chk_state.append(BooleanVar())
            chk_state[i].set(True)
            chk.append(Checkbutton(self.root, text=heroes[i], var=chk_state[i]))
            chk[i].grid(column=i%3, row=i//3+1)

        # ГЕРОИ ИГРОКА 2
        lblpl2 = Label(self.root, text="Герои игрока 2", font=("Arial Bold", 14))
        lblpl2.grid(column=0, row=8)
        lblh2 = Label(self.root, text=hero2, font=("Arial Bold", 14))
        lblh2.grid(column=5, row=9)

        for i in range(21,42):
            chk_state.append(BooleanVar())
            chk_state[i].set(True)
            chk.append(Checkbutton(self.root, text=heroes[i-21], var=chk_state[i]))
            chk[i].grid(column=i%3, row=i//3+2)

        #ВЫКЛЮЧЕНИЕ СЕРЫХ РЫЦАРЕЙ ПО УМОЛЧАНИЮ
        chk_state[18].set(False)
        chk_state[19].set(False)
        chk_state[20].set(False)
        chk_state[39].set(False)
        chk_state[40].set(False)
        chk_state[41].set(False)

        # ПИК ГЕРОЕВ
        def Clicked():
            h1 = random.randint(0, 20)
            h2 = random.randint(0, 20)
            if chk_state[h1].get() == 1 and chk_state[h2+21].get() == 1:
                lblh1.config(text=heroes[h1])
                lblh2.config(text=heroes[h2])
            else:
                Clicked()

            #ПОРТРЕТЫ ГЕРОЕВ
            img1 = Image.open("venv/images/hero_" + str(h1) + ".png")
            img2 = Image.open("venv/images/hero_" + str(h2) + ".png")
            img1 = img1.resize((180, 180), Image.ANTIALIAS)
            img2 = img2.resize((180, 180), Image.ANTIALIAS)
            img1.save("venv/images/hero_" + str(h1) + ".png")
            img2.save("venv/images/hero_" + str(h2) + ".png")

            photo1 = ImageTk.PhotoImage(img1)
            photo2 = ImageTk.PhotoImage(img2)
            lab1 = Label(self.root, image=photo1).place(x=470, y=30)
            lab2 = Label(self.root, image=photo2).place(x=470, y=270)
            lab1.image=photo1
            lab1.pack()
            lab2.image = photo2
            lab2.pack()

        #КНОПКА
        btn = Button(self.root, text="PICK!", font=("Arial Bold", 18), command=Clicked)
        btn.grid(column=1, row=44)

    def run(self):
        self.root.mainloop()

window = Window(680, 470, 'Warhammer Random Picker')
window.run()
