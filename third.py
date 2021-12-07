from tkinter import *
import time
import second_level
class Level_3(Frame):
    def __init__(self, window, height, width):
        self.window = window
        self.window.resizable(width=False,height=False)
        self.height = height
        self.width = width

        self.time = time.strftime('%S')
        self.clock = 60

        self.frame_3 = Frame(self.window,height=self.height, width=self.width)
        self.frame_3.grid(row=0)

        self.texts = StringVar()

        self.text = []
        with open('third_level.txt', 'r') as f:
            data = f.read()
        self.words = data.split(',')
        for i in self.words:
            self.text.append(str(i))
        print(self.text)

        # Oyunda dogrylary we yalnyslar
        self.true=0
        self.false=0

        self.page()
        
    def page(self):
        bg_img = PhotoImage(file='img/bac4.png')
        frm_3 = Label(self.frame_3,compound='center', image=bg_img,font=['Times_New_Roman', 75])
        frm_3.image=bg_img
        frm_3.grid(row=0)
        
        self.change_time()

    def change_time(self):
        self.time = time.strftime('%S')
        self.clock-=1
        label_1 = Label(self.frame_3, text=f'00:{self.clock}',font=['Dyuthi',55],bg='#F0E2DA',borderwidth=10,relief="groove", fg='#594236',width=5)
        label_1.place(x=345,y=15)
        if self.clock>0:
           
            label_1.configure(text=f'00:{self.clock}')
            print(self.clock, type(self.time))
            if self.clock<=1:
                pass
            else:
                self.frame_3.after(1000, self.change_time)



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

        ''' Board  '''
        self.brd = Label(self.frame_3, wraplength=495,textvariable=self.texts,padx=3.43,
                        justify=LEFT,fg='black',font=['Times_New_Roman',14], bg='white',anchor='nw',width=52)
        self.brd.place(y=362, x=187,relheight=0.264)
        self.show_letter()
        ''' end  '''

    def press(self,event, letter):
        print(event, letter)
        if self.clock<=1:
                self.close_page()
        if letter == 'pozmak':
            self.texts.set(self.texts.get()[:-1])
        else:
            
            if letter == ' ':
                print('boşluk')
                if len(self.text)!=0:
                    if self.brd.cget('text')==self.text[0]:
                        if self.true:
                            print('dasjduiasjdioasjuidhasudhasduihasuidhasdas')
                        self.true+=1
                        self.texts.set('')
                        print(self.text)
                        self.text.remove(self.text[0])
                        print(self.text)
                    else:
                        self.false+=1

            else:
                self.texts.set(self.texts.get()+letter)
            
        self.show_letter()
    def show_letter(self):
        self.letter_brd = Label(self.frame_3,padx=5.85, text=self.text,wraplength=650,anchor='nw',
                            font=['Dyuthi',20],justify=LEFT,bg='white', fg='black')
        self.letter_brd.place(y=156,x=187, relheight=0.29, relwidth=0.63)
        
        title = Canvas(self.frame_3,bg='#594236', width=634, height=5)
        # self.title.create_line(5, 2, 200, 2)
        title.place(x=184,y=355)
        false_tabele = Label(self.frame_3, text=f'{self.false}',font=['Dyuthi',20],bg='red',borderwidth=5,relief="groove", fg='white',width=5)
        false_tabele.place(x=590,y=15,relheight=0.14)
        true_tabele = Label(self.frame_3, text=f'{self.true}',font=['Dyuthi',20],bg='green',borderwidth=5,relief="groove", fg='white',width=5)
        true_tabele.place(x=250,y=15,relheight=0.14)


    

    def close_page(self):
        from tkinter import messagebox, Message
        from playsound import playsound
        playsound('sound/win.wav')
        msg = messagebox.showinfo(title="Berekella!",detail=f'Siz bu tapgyry {self.true+1} dogry we {self.false} yalnys bilen gecdiniz', message='Ikinji tapgyr ustunlikli gecildi!')
        self.window.destroy()