try:
    import tkinter as tk
except ImportError:
    print("please install tkinter")
    raise SystemExit
import initialise,process

root = tk.Tk()

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

class Main:
    
    def __init__(self,master):
        gameFrame = tk.Frame(master)
        gameFrame.pack(side=tk.LEFT)
        frame = tk.Frame(gameFrame)
        frame.pack()
        
        self.ruleButton = tk.Button(frame, text="Rules", command = self.showRules)
        self.ruleButton.pack(side=tk.LEFT)

        self.newGameButton = tk.Button(frame, text="New Game", command = lambda: self.newGame(gameFrame))
        self.newGameButton.pack(side=tk.LEFT)

        self.remAttemptLabel = tk.Label(frame)
        self.remAttemptLabel.pack(side=tk.RIGHT)

        self.historyFrame = tk.Frame(master)

    def showRules(self):
        ruleText = tk.Text(tk.Toplevel())
        ruleText.pack()
        ruleText.insert(tk.END, initialise.rules())

    def newGame(self,master):
        try:
            for widget in self.frame.winfo_children():
                widget.destroy()
        except AttributeError:
            self.frame = tk.Frame(master)
            self.frame.pack()
        self.n,self.maxChoice,self.colors = initialise.getColors("colors.txt")
        self.remAttemptLabel.configure(text=self.maxChoice)
        self.choice = [-1]*self.n
        self.counter,self.attempts = 0,0
        self.code = initialise.codeGen(self.colors,self.n)
        self.guessCanvas = tk.Canvas(self.frame,width=self.n*50,height=70)
        self.guessCanvas.pack()
        for n in range(self.n):
            self.guessCanvas.create_circle((n*50)+25,25,20,fill="#fff")
        
        colorFrame = tk.Frame(self.frame)
        colorFrame.pack()
        self.colorButtons = []
        for color in self.colors:
            b = tk.Button(colorFrame,bg=color,command = lambda color=color: self.choose(color))
            b.pack(side=tk.LEFT)
            self.colorButtons.append(b)

        self.historyCanvas = tk.Canvas(bg="#ffffff",width = 22*self.n, height = 12*self.maxChoice)
        self.historyFrame.pack()
        self.historyCanvas.pack()

    def choose(self,color):
        self.guessCanvas.create_circle((self.counter*50)+25,25,20,fill=color)
        self.choice[self.counter] = color
        if self.counter == self.n - 1:
            self.eval()
            self.counter = 0
            self.maxChoice -= 1
            self.remAttemptLabel.configure(text=str(self.maxChoice))
            self.attempts += 1
            for i,color in enumerate(self.choice):
                self.historyCanvas.create_circle((i*12)+8,12*self.attempts-4,5,fill=color)
        else: self.counter += 1
    def eval(self):
        white,red = process.check(self.choice,self.code)
        try: [self.guessCanvas.delete(box) for box in self.whiteRedBoxes]
        except AttributeError: pass
        self.whiteRedBoxes = []
        counter = 0        
        for w in range(white):
            box = self.guessCanvas.create_rectangle(5+(12*counter),55,15+(12*counter),65,fill="#fff")
            self.historyCanvas.create_rectangle((self.n-1)*12+15+((self.counter)*10),12*self.attempts-8,(self.n-1)*12+23+((self.counter)*10),12*self.attempts,fill="#fff")
            self.whiteRedBoxes.append(box)
            counter += 1
        for r in range(red):
            box = self.guessCanvas.create_rectangle(5+(12*counter),55,15+(12*counter),65,fill="#f00")
            self.historyCanvas.create_rectangle((self.n-1)*12+15+((self.counter)*10),12*self.attempts-8,(self.n-1)*12+23+((self.counter)*10),12*self.attempts,fill="#f00")
            self.whiteRedBoxes.append(box)
            counter += 1
        if red == self.n: 
            tk.Label(self.frame,text="YOU WIN!").pack()
        elif self.maxChoice == 1:
            tk.Label(self.frame,text="YOU LOSE!").pack()
            for button in self.colorButtons: button.configure(state = tk.DISABLED)

main = Main(root)
root.mainloop()