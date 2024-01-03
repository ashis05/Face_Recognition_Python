from make import send
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage

CELL = 20
FCOLOR = "#8B5742"
COLOR1 = "#E9967A"
COLOR2 = "#006400"
COLORG = "#66CDAA"
THEME = "Snow"

class crossword:

    def __init__(self):
        self.game = tk.Frame(root)
        self.num_rows = 15
        self.num_cols = 15
        self.hints_used = 0
        self.box = [[None for _ in range(15)] for _ in range(15)]
        self.text = [None for _ in range(7)]
        self.entry = [None for _ in range(7)]
        self.hint = [None for _ in range(7)]
        self.hints = [0 for _ in range (7)]
        self.ans_num = [None for _ in range(7)]
        self.guess = [0 for _ in range(7)]
        [self.questions , self.answer , self.grid] = send()

        self.canvas = tk.Canvas(self.game, width=1280, height=720)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(-400,-200, image = cwbgz , anchor ="nw")
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.grid[row][col] != ' ':
                    
                    x1 = col * CELL + (1280 - 160 - 640)
                    y1 = row * CELL + (25)
                    x2 = x1 + CELL 
                    y2 = y1 + CELL 
                    center_x = (x1 + x2) // 2
                    center_y = (y1 + y2) // 2
                    self.box[row][col] = self.canvas.create_text(center_x, center_y, text=self.grid[row][col].upper(), font=("Helvetica", 10),state = tk.HIDDEN,fill=COLORG)
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline=COLOR1)
                

        i=1
        for ans in self.answer:
            [row , col , __] = self.find(ans)    
            x1 = col * CELL + (1280 - 160 - 640)
            y1 = row * CELL + (25)
            self.ans_num[i-1] = self.canvas.create_text(x1 + 4,y1 + 6, text=i, font=("Helvetica", 6),state = tk.NORMAL,fill=COLOR1)
            i+=1

        for index, question in enumerate(self.questions):
            
            self.text[index] = self.canvas.create_text(600,(350 + (index*50)),text = "{}. {}".format(index+1,question),font=("Comic Sans MC",8,'bold'),fill=COLOR1)
            
            self.entry[index] = tk.Entry(self.game)
            self.canvas.create_window(600,(370 + (index*50)), window=self.entry[index])
            self.entry[index].bind("<Return>", self.submit)

            self.hint[index] = tk.Button(self.game,text="Hint",background=COLOR2,
                  foreground=COLOR1,width=5,font=('Arial',8,'bold'),
                  command = lambda index=index: self.hintreveal(self.answer[index]))
            self.canvas.create_window(700,(370 + (index*50)), window=self.hint[index])
        


    def complete(self):
        flag = 0
        for all in self.guess:
            flag += all
            if flag == len(self.guess):
                self.canvas.pack_forget()
                self.end_canvas = tk.Canvas(self.game, width=1280, height=720)
                self.end_canvas.pack(fill="both", expand=True)
                self.end_canvas.create_image(-200,-200, image = cwbgz , anchor ="nw")
                self.end_canvas.create_text(650,150, text="Congratulations! You solved the crossword with {} hints!!".format(self.hints_used), font=("Helvetica",28,'bold'), fill=FCOLOR)
                button = tk.Button(self.game,
                  background=COLOR2,
                  foreground=COLOR1,
                  highlightthickness=10,
                  highlightbackground=COLOR2,
                  highlightcolor=COLOR1,
                  text = "Main Menu",
                  height=2,
                  width=12,
                  border=0,
                  font=('Arial',18,'bold'),command=lambda: [self.game.pack_forget(), mainmenu.pack()])
                self.end_canvas.create_window(550,230, anchor="nw", window=button)
        

    def check_word_right(self, word, row, col):
        if col + len(word) <= len(self.grid[row]):
            for i in range(len(word)):
                if self.grid[row][col + i] != word[i]:
                    return False
            return True
        return False

    def check_word_down(self, word, row, col):
        if row + len(word) <= len(self.grid):
            for i in range(len(word)):
                if self.grid[row + i][col] != word[i]:
                    return False
            return True
        return False

    def find(self, word):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.check_word_right(word, row, col):
                    return [row, col, 'right']
                
                if self.check_word_down(word, row, col):
                    return [row, col, 'down']
        return [-1,-1, '']
            
    def reveal(self, word):
        [row , col , dir] = self.find(word)
        for i in range(len(word)):
            if dir == 'down':
                self.canvas.itemconfig(self.box[row + i][col], state = tk.NORMAL)
            elif dir == 'right':
                self.canvas.itemconfig(self.box[row][col + i], state = tk.NORMAL)

    def hintreveal(self, word):
        [row , col , dir] = self.find(word)
        for index,ans in enumerate(self.answer):
            if word == ans:
                if self.hints[index] < len(word):
                    add_row , add_col = 0 , 0
                    if dir == 'down':
                        add_row = self.hints[index]
                    elif dir == 'right':
                        add_col = self.hints[index]
                    self.canvas.itemconfig(self.box[row + add_row][col + add_col], state = tk.NORMAL)
                    self.hints_used += 1
                    self.hints[index] += 1

    def submit(self, event):
        for i in range(len(self.entry)):
            try:
                test = self.entry[i].get().lower()
            except:
                continue
            else:
                if test == self.answer[i].lower():
                    self.canvas.itemconfig(self.ans_num[i], state = tk.HIDDEN)
                    self.reveal(self.entry[i].get().lower())
                    self.guess[i] = 1
                    self.entry[i].delete(0,'end')
                    self.entry[i].destroy()
                    self.hint[i].destroy()
                    self.canvas.itemconfig(self.text[i], fill = COLORG)
                    self.complete()

def create_crossword():
    new_game = crossword()
    mainmenu.pack_forget()
    new_game.game.pack()



root = tk.Tk()
icon = PhotoImage(file='cwicon.png')
root.iconphoto(False, icon)
root.title("Crossword")
root.geometry("1280x720")
root.resizable(False,False)

bgz = PhotoImage(file="bgz.png")
cwbgz = PhotoImage(file="cwbgz.png")

mainmenu = tk.Frame(root)
menu_canvas = tk.Canvas(mainmenu, width=1280, height=720)
menu_canvas.pack(fill="both", expand=True)
menu_canvas.create_image(-200,-200, image = bgz , anchor ="nw")
menu_canvas.create_text(650,150, text="The Crossword Puzzle", font=("Helvetica",36,'bold'), fill=FCOLOR)

start = tk.Button(mainmenu,
                  background=COLOR2,
                  foreground=COLOR1,
                  highlightthickness=10,
                  highlightbackground=COLOR2,
                  highlightcolor=COLOR1,
                  text = "Start",
                  height=2,
                  width=12,
                  border=0,
                  font=('Arial',18,'bold'),
                  command= create_crossword)
start_button = menu_canvas.create_window(550,230, anchor="nw", window=start)
mainmenu.pack()


root.mainloop()
