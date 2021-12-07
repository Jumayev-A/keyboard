from tkinter import *
import time
import first_level
import third

class Level_2(Frame):
    def __init__(self, window, height, width):
        self.window = window
        self.window.resizable(width=False,height=False)
        self.height = height
        self.width = width

        self.time = time.strftime('%S')

        self.frame_2 = Frame(self.window,height=self.height, width=self.width)
        self.frame_2.grid(row=0)

        self.texts_on_board = StringVar()
        self.texts = StringVar()
        self.text = []
        
        with open('second_level.txt', 'r') as f:
            data = f.read()
        self.letters = data.split(',')
        for i in self.letters:
            for k in i.split():
                self.text.append(i.split())
        self.texts.set(self.text[0][0])

        self.page()
        # Oyunda dogrylary we yalnyslar
        self.true=0
        self.false=0
  
    def page(self):
        bg_img = PhotoImage(file='img/back.png')
        board_img = PhotoImage(file='img/board.png')
        frm_2 = Label(self.frame_2,compound='center', image=bg_img,font=['Times_New_Roman', 75])
        frm_2.image=bg_img
        board = Label(self.frame_2, image=board_img)
        board.image=board_img
        frm_2.grid(row=0)
        board.place(x=420, y=0)
        self.keyboard_and_board()

    def keyboard_and_board(self):
        ''' Command on keyboard '''
        self.window.bind('<grave>', lambda event, letter='ž': self.press(event, letter))
        self.window.bind('<zcaron>', lambda event, letter='ž': self.press(event, letter))
        self.window.bind('1', lambda event, letter='1': self.press(event, letter))
        self.window.bind('2', lambda event, letter='2': self.press(event, letter))
        self.window.bind('3', lambda event, letter='3': self.press(event, letter))
        self.window.bind('4', lambda event, letter='4': self.press(event, letter))
        self.window.bind('5', lambda event, letter='5': self.press(event, letter))
        self.window.bind('6', lambda event, letter='6': self.press(event, letter))
        self.window.bind('7', lambda event, letter='7': self.press(event, letter))
        self.window.bind('8', lambda event, letter='8': self.press(event, letter))
        self.window.bind('9', lambda event, letter='9': self.press(event, letter))
        self.window.bind('0', lambda event, letter='0': self.press(event, letter))
        self.window.bind('<minus>', lambda event, letter='-': self.press(event, letter))
        self.window.bind('<equal>', lambda event, letter='=': self.press(event, letter))
        self.window.bind('<BackSpace>', lambda event, letter='pozmak': self.press(event, letter))
        self.window.bind('q', lambda event, letter='ä': self.press(event, letter))
        self.window.bind('<adiaeresis>', lambda event, letter='ä': self.press(event, letter))
        self.window.bind('w', lambda event, letter='w': self.press(event, letter))
        self.window.bind('e', lambda event, letter='e': self.press(event, letter))
        self.window.bind('r', lambda event, letter='r': self.press(event, letter))
        self.window.bind('t', lambda event, letter='t': self.press(event, letter))
        self.window.bind('y', lambda event, letter='y': self.press(event, letter))
        self.window.bind('u', lambda event, letter='u': self.press(event, letter))
        self.window.bind('i', lambda event, letter='i': self.press(event, letter))
        self.window.bind('o', lambda event, letter='o': self.press(event, letter))
        self.window.bind('p', lambda event, letter='p': self.press(event, letter))
        self.window.bind('<bracketleft>', lambda event, letter='ň': self.press(event, letter))
        self.window.bind('<ncaron>', lambda event, letter='ň': self.press(event, letter))
        self.window.bind('<bracketright>', lambda event, letter='ö': self.press(event, letter))
        self.window.bind('<odiaeresis>', lambda event, letter='ö': self.press(event, letter))
        self.window.bind('a', lambda event, letter='a': self.press(event, letter))
        self.window.bind('s', lambda event, letter='s': self.press(event, letter))
        self.window.bind('d', lambda event, letter='d': self.press(event, letter))
        self.window.bind('f', lambda event, letter='f': self.press(event, letter))
        self.window.bind('g', lambda event, letter='g': self.press(event, letter))
        self.window.bind('h', lambda event, letter='h': self.press(event, letter))
        self.window.bind('j', lambda event, letter='j': self.press(event, letter))
        self.window.bind('k', lambda event, letter='k': self.press(event, letter))
        self.window.bind('l', lambda event, letter='l': self.press(event, letter))
        self.window.bind('<semicolon>', lambda event, letter=';': self.press(event, letter))
        self.window.bind('<apostrophe>', lambda event, letter='"': self.press(event, letter))
        self.window.bind('<backslash>', lambda event, letter='ş': self.press(event, letter))
        self.window.bind('z', lambda event, letter='z': self.press(event, letter))
        self.window.bind('<udiaeresis>', lambda event, letter='ü': self.press(event, letter))
        self.window.bind('x', lambda event, letter='ü': self.press(event, letter))
        self.window.bind('c', lambda event, letter='ç': self.press(event, letter))
        self.window.bind('<ccedilla>', lambda event, letter='ç': self.press(event, letter))
        self.window.bind('<yacute>', lambda event, letter='ý': self.press(event, letter))
        self.window.bind('v', lambda event, letter='ý': self.press(event, letter))
        self.window.bind('b', lambda event, letter='b': self.press(event, letter))
        self.window.bind('n', lambda event, letter='n': self.press(event, letter))
        self.window.bind('m', lambda event, letter='m': self.press(event, letter))
        self.window.bind('<comma>', lambda event, letter=',': self.press(event, letter))
        self.window.bind('<period>', lambda event, letter='.': self.press(event, letter))
        self.window.bind('<slash>', lambda event, letter='/': self.press(event, letter))
        self.window.bind('<space>', lambda event, letter=' ': self.press(event, letter))
        self.window.unbind_all('<<NextWindow>>')
        ''' Keyboard '''
        # first_line
        self.ž = Button(self.frame_2, bg='black',command=lambda: self.press('', 'ž'), activebackground='black',activeforeground='white',
        highlightthickness=0,fg='white',text='ž', border=2, width=2)
        self.ž.place(y=270, x=110, relheight=0.08)

        self.one = Button(self.frame_2, bg='black',command=lambda: self.press('', '1'), activebackground='black', activeforeground='white',
        highlightthickness=0,fg='white', text='1', border=2, width=2)
        self.one.place(y=270,x=160,relheight=0.08)

        self.two = Button(self.frame_2, bg='black',command=lambda: self.press('', '2'), activebackground='black',activeforeground='white',highlightthickness=0,fg='white',
        text='2', border=2, width=2)
        self.two.place(y=270,x=210, relheight=0.08)

        self.three = Button(self.frame_2, bg='black',command=lambda: self.press('', '3'), activebackground='black', activeforeground='white',highlightthickness=0,fg='white',
        text='3', border=2, width=2)
        self.three.place(y=270,x=260, relheight=0.08)

        self.four = Button(self.frame_2, bg='black',command=lambda: self.press('', '4'), activebackground='black', activeforeground='white',highlightthickness=0,fg='white',
        text='4', border=2, width=2)
        self.four.place(y=270,x=310, relheight=0.08)

        self.five = Button(self.frame_2, bg='black',command=lambda: self.press('', '5'), activebackground='black', activeforeground='white',highlightthickness=0,fg='white',
        text='5', border=2, width=2)
        self.five.place(y=270,x=360, relheight=0.08)

        self.six = Button(self.frame_2, bg='black',command=lambda: self.press('', '6'), activebackground='black', activeforeground='white',highlightthickness=0,fg='white',
        text='6', border=2, width=2)
        self.six.place(y=270,x=410, relheight=0.08)

        self.seven = Button(self.frame_2, bg='black',command=lambda: self.press('', '7'), activebackground='black', activeforeground='white',highlightthickness=0,fg='white',
        text='7', border=2, width=2)
        self.seven.place(y=270,x=460, relheight=0.08)

        self.eight = Button(self.frame_2, bg='black',command=lambda: self.press('', '8'), activebackground='black', activeforeground='white',highlightthickness=0,fg='white',
        text='8', border=2, width=2)
        self.eight.place(y=270,x=510, relheight=0.08)

        self.nine = Button(self.frame_2, bg='black',command=lambda: self.press('', '9'), activebackground='black', activeforeground='white',highlightthickness=0,fg='white',
        text='9', border=2, width=2)
        self.nine.place(y=270,x=560, relheight=0.08)

        self.zero = Button(self.frame_2, bg='black',command=lambda: self.press('', '0'), activebackground='black', activeforeground='white',highlightthickness=0,fg='white',
        text='0', border=2, width=2)
        self.zero.place(y=270,x=610, relheight=0.08)

        self.minus = Button(self.frame_2, bg='black',command=lambda: self.press('', '-'), activebackground='black', activeforeground='white',highlightthickness=0,fg='white',
        text='-', border=2, width=2)
        self.minus.place(y=270,x=660, relheight=0.08)

        self.plus = Button(self.frame_2, bg='black',command=lambda: self.press('', '='), activebackground='black', activeforeground='white',highlightthickness=0,fg='white',
        text='=', border=2, width=2)
        self.plus.place(y=270,x=710, relheight=0.08)

        self.backsapce = Button(self.frame_2, bg='black',command=lambda: self.press('', 'pozmak'), activebackground='black', activeforeground='white',highlightthickness=0,fg='white',
        text='pozmak', border=2, width=7)
        self.backsapce.place(y=270,x=760, relheight=0.08)

        # second_line
        self.ä = Button(self.frame_2, bg='black',command=lambda: self.press('', 'ä'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='ä', border=2, width=2)
        self.ä.place(y=315, x=190, relheight=0.08)

        self.w = Button(self.frame_2, bg='black',command=lambda: self.press('', 'w'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='w', border=2, width=2)
        self.w.place(y=315, x=240, relheight=0.08)

        self.e = Button(self.frame_2, bg='black',command=lambda: self.press('', 'e'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='e', border=2, width=2)
        self.e.place(y=315, x=290, relheight=0.08)

        self.r = Button(self.frame_2, bg='black',command=lambda: self.press('', 'r'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='r', border=2, width=2)
        self.r.place(y=315, x=340, relheight=0.08)

        self.t = Button(self.frame_2, bg='black',command=lambda: self.press('', 't'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='t', border=2, width=2)
        self.t.place(y=315, x=390, relheight=0.08)

        self.y = Button(self.frame_2, bg='black',command=lambda: self.press('', 'y'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='y', border=2, width=2)
        self.y.place(y=315, x=440, relheight=0.08)

        self.u = Button(self.frame_2, bg='black',command=lambda: self.press('', 'u'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='u', border=2, width=2)
        self.u.place(y=315, x=490, relheight=0.08)

        self.i = Button(self.frame_2, bg='black',command=lambda: self.press('', 'i'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='i', border=2, width=2)
        self.i.place(y=315, x=540, relheight=0.08)

        self.o = Button(self.frame_2, bg='black',command=lambda: self.press('', 'o'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='o', border=2, width=2)
        self.o.place(y=315, x=590, relheight=0.08)

        self.p = Button(self.frame_2, bg='black',command=lambda: self.press('', 'p'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='p', border=2, width=2)
        self.p.place(y=315, x=640, relheight=0.08)

        self.ň = Button(self.frame_2, bg='black',command=lambda: self.press('', 'ň'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='ň', border=2, width=2)
        self.ň.place(y=315, x=690, relheight=0.08)
        
        self.ö = Button(self.frame_2, bg='black',command=lambda: self.press('', 'ö'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='ö', border=2, width=2)
        self.ö.place(y=315, x=740, relheight=0.08)

        '''third_line'''
        self.a = Button(self.frame_2, bg='black',command=lambda: self.press('', 'a'), activebackground='black', activeforeground='white', highlightthickness=0,fg='white', text='a', border=2, width=2)
        self.a.place(y=360,x=205, relheight=0.08)

        self.s = Button(self.frame_2, bg='black',command=lambda: self.press('', 's'), activebackground='black', activeforeground='white', highlightthickness=0,fg='white', text='s', border=2, width=2)
        self.s.place(y=360,x=255, relheight=0.08)

        self.d = Button(self.frame_2, bg='black',command=lambda: self.press('', 'd'), activebackground='black', activeforeground='white', highlightthickness=0,fg='white', text='d', border=2, width=2)
        self.d.place(y=360,x=305, relheight=0.08)

        self.f = Button(self.frame_2, bg='black',command=lambda: self.press('', 'f'), activebackground='black', activeforeground='white', highlightthickness=0,fg='white', text='f', border=2, width=2)
        self.f.place(y=360,x=355, relheight=0.08)

        self.g = Button(self.frame_2, bg='black',command=lambda: self.press('', 'g'), activebackground='black', activeforeground='white', highlightthickness=0,fg='white', text='g', border=2, width=2)
        self.g.place(y=360,x=405, relheight=0.08)

        self.h = Button(self.frame_2, bg='black',command=lambda: self.press('', 'h'), activebackground='black', activeforeground='white', highlightthickness=0,fg='white', text='h', border=2, width=2)
        self.h.place(y=360,x=455, relheight=0.08)

        self.j = Button(self.frame_2, bg='black',command=lambda: self.press('', 'j'), activebackground='black', activeforeground='white', highlightthickness=0,fg='white', text='j', border=2, width=2)
        self.j.place(y=360,x=505, relheight=0.08)

        self.k = Button(self.frame_2, bg='black',command=lambda: self.press('', 'k'), activebackground='black', activeforeground='white', highlightthickness=0,fg='white', text='k', border=2, width=2)
        self.k.place(y=360,x=555, relheight=0.08)

        self.l = Button(self.frame_2, bg='black',command=lambda: self.press('', 'l'), activebackground='black', activeforeground='white', highlightthickness=0,fg='white', text='l', border=2, width=2)
        self.l.place(y=360,x=605, relheight=0.08)

        self.semicolon = Button(self.frame_2, bg='black',command=lambda: self.press('', ';'), activebackground='black', activeforeground='white', highlightthickness=0,fg='white', text=';', border=2, width=2)
        self.semicolon.place(y=360,x=655, relheight=0.08)

        self.apostrophe = Button(self.frame_2, bg='black',command=lambda: self.press('', '"'), activebackground='black', activeforeground='white', highlightthickness=0,fg='white', text='"', border=2, width=2)
        self.apostrophe.place(y=360,x=705, relheight=0.08)

        self.ş = Button(self.frame_2, bg='black',command=lambda: self.press('', "ş"), activebackground='black', activeforeground='white', highlightthickness=0,fg='white', text='ş', border=2, width=2)
        self.ş.place(y=360,x=755, relheight=0.08)

        # fourth_line
        self.z = Button(self.frame_2, bg='black',command=lambda: self.press('', ' z'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='z', border=2, width=2)
        self.z.place(y=405,x=230,relheight=0.08)

        self.ü = Button(self.frame_2, bg='black',command=lambda: self.press('', 'ü'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='ü', border=2, width=2)
        self.ü.place(y=405,x=280,relheight=0.08)

        self.ç = Button(self.frame_2, bg='black',command=lambda: self.press('', 'ç'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='ç', border=2, width=2)
        self.ç.place(y=405,x=330,relheight=0.08)

        self.ý = Button(self.frame_2, bg='black',command=lambda: self.press('', 'ý'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='ý', border=2, width=2)
        self.ý.place(y=405,x=380,relheight=0.08)

        self.b = Button(self.frame_2, bg='black',command=lambda: self.press('', 'b'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='b', border=2, width=2)
        self.b.place(y=405,x=430,relheight=0.08)

        self.n = Button(self.frame_2, bg='black',command=lambda: self.press('', 'n'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='n', border=2, width=2)
        self.n.place(y=405,x=480,relheight=0.08)

        self.m = Button(self.frame_2, bg='black',command=lambda: self.press('', 'm'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='m', border=2, width=2)
        self.m.place(y=405,x=530,relheight=0.08)

        self.comma = Button(self.frame_2, bg='black',command=lambda: self.press('', ','), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text=',', border=2, width=2)
        self.comma.place(y=405,x=580,relheight=0.08)

        self.period = Button(self.frame_2, bg='black',command=lambda: self.press('', '.'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='.', border=2, width=2)
        self.period.place(y=405,x=630,relheight=0.08)

        self.slash = Button(self.frame_2, bg='black',command=lambda: self.press('', '/'), activebackground='black', activeforeground='white', highlightthickness=0, fg='white', text='/', border=2, width=2)
        self.slash.place(y=405,x=680,relheight=0.08)

        self.bosluk = Button(self.frame_2,bg='black',command=lambda: self.press('', ' '),activebackground='black',activeforeground='white',highlightthickness=0,fg='white', text='boşluk',border=2,width=30)
        self.bosluk.place(y=450,x=325)
        ''' end '''
        ''' Board  '''
        self.brd = Label(self.frame_2, wraplength=495,textvariable=self.texts_on_board,padx=3.43,
                        justify=LEFT,fg='white',font='Times_New_Roman', bg='#1d7e41',anchor='nw',width=30)
        self.brd.place(y=13, x=441,relheight=0.264)
        ''' end  '''
        self.buttons = [
                    self.ž,self.one,self.two,self.three,self.four,self.five,
                    self.six,self.seven,self.eight,self.nine,self.zero,self.minus,self.plus,
                    self.backsapce,self.ä,self.w,self.e,self.r,self.t,self.y,
                    self.u,self.i,self.o,self.p,self.ň,self.ö,self.a,self.s,
                    self.d,self.f,self.g,self.h,self.j,self.k,self.l,
                    self.semicolon,self.apostrophe,self.ş,self.z,self.ü,self.ç,self.ý,
                    self.b,self.n,self.m,self.comma,self.period,self.slash,self.bosluk
                  ]
       
        self.show_letter()

    def press(self,event, letter):
        print(event, letter)
        print(self.true, self.false)
        if letter == 'pozmak':
            self.texts.set(self.texts.get()[:-1])
        else:
            for i in self.buttons:
                if i['text']==letter:
                    if len(self.texts.get())!=0:
                        if i['text']==self.letter_brd.cget('text')[0]:
                            i['bg']='green'
                            i['activebackground']='green'
                            self.texts_on_board.set(self.texts_on_board.get()+letter)
                            self.texts.set(self.texts.get()[1:])
                            print(self.texts.get(),len(self.texts.get()))
                            print(self.letter_brd.cget('text'))

                            if len(self.texts.get())==0:
                                if len(self.text)>1:
                                    for ltr in self.buttons:
                                        ltr['bg']='black'
                                        ltr['activebackground']='black'
                                    self.text.remove(self.text[0])
                                    self.texts_on_board.set('')
                                    self.texts.set(self.text[0][0])
                                    self.true+=1
                                else:
                                    self.close_page()
                        else:
                            from playsound import playsound
                            playsound('sound/error.wav')
                            i['bg']='red'
                            i['activebackground']='red'
                            self.false+=1

        self.show_letter()
    def show_letter(self):
        self.letter_brd = Label(self.frame_2,padx=5.85, textvariable=self.texts,wraplength=180,anchor='w',
                            font='Times_New_Roman',justify=LEFT,bg='#1d7e41', fg='white',width=18)
        self.letter_brd.place(y=13,x=745, relheight=0.264)
        
        self.title = Label(self.frame_2,bg='#1d7e41',fg='white', text='Aşakdaky sözi ýaz:', font=['Dyuthi',15])
        self.title.place(y=20,x=745)


  

    def close_page(self):
        if self.false<5 and self.true+1==len(self.letters):
            from tkinter import messagebox, Message
            from playsound import playsound
            playsound('sound/win.wav')
            msg = messagebox.showinfo(title="Berekella!",detail=f'Siz bu tapgyry {self.true+1} dogry we {self.false} yalnys bilen gecdiniz', message='Ikinji tapgyr ustunlikli gecildi!')
            self.frame_2.destroy()
            third.Level_3(self.window, 500, 960)
        else:
            from tkinter import messagebox
            from playsound import playsound
            playsound('sound/loser.wav')
            msg = messagebox.showerror(title="Sowsuz!",detail=f'Siz bu tapgyry {self.false} yalnys bilen gecdiniz! Tazeden birinji tapgyry gaytalan!', message='Ikinji tapgyr sowsuz boldy!')
            self.frame_2.destroy()
            first_level.Level_1(self.window, 500, 960)
        print('gutardy', self.true, len(self.letters))