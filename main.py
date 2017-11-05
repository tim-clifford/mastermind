try:
    import tkinter as tk
except ImportError:
    print("please install tkinter")
    raise SystemExit
import initialise,process

root = tk.Tk()

# Add functionality to tkinter.Canvas
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

class Main:
    def __init__(self,master):
        '''
        Create initial frames and buttons and assign commands to the buttons
        '''
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
        self.historyFrame.pack()

    def showRules(self):
        '''
        Display the rules of the game in a new window

        Set as the command of ruleButton
        '''
        ruleText = tk.Text(tk.Toplevel())
        ruleText.pack()
        ruleText.insert(tk.END, initialise.rules())

    def newGame(self,master):
        '''
        Reset everything and start a new game

        Set as the command of newGameButton 
        '''
        self.n,self.maxChoice,self.colors = initialise.getInfo("colors.txt")
        try:
            # delete widgets from last game
            for widget in self.frame.winfo_children():
                widget.destroy()
            # clear history canvas
            self.historyCanvas.delete("all")
        except AttributeError:
            # unless it is the first game
            self.frame = tk.Frame(master)
            self.frame.pack()
            self.historyCanvas = tk.Canvas(bg="#fff",width = 22*self.n+4, height = 12*self.maxChoice+4)
            self.historyCanvas.pack()

        ### Initialise Widgets
        self.remAttemptLabel.configure(text=self.maxChoice)
        self.choice = [-1]*self.n
        self.counter,self.attempts = 0,0
        self.code = initialise.codeGen(self.colors,self.n)
        self.guessCanvas = tk.Canvas(self.frame,width=self.n*50,height=70)
        self.guessCanvas.pack()

        # Create blank choice circles
        for n in range(self.n):
            self.guessCanvas.create_circle((n*50)+25,25,20,fill="#fff")

        # Create choice buttons
        colorFrame = tk.Frame(self.frame)
        colorFrame.pack()
        self.colorButtons = []
        for color in self.colors:
            # the lambda default argument `color=color` is necessary as `color` is reassigned in the loop 
            b = tk.Button(colorFrame,bg=color,command = lambda color=color: self.choose(color))
            b.pack(side=tk.LEFT)
            self.colorButtons.append(b)

    def choose(self,color):
        '''
        choose a color as the next place; draw the choice; if it is the last place call self.eval() and reset

        Set as the command of each color button with the relevant color as the argument

        An attribute to the main class `counter` is used to represent the current progress of guessing. 
        Whilst this makes the code harder to reason about and more prone to error, it is necessary as 
        there can be no return value from `tk.Button` and no arguments
        '''
        #reset cirles
        if self.counter == 0:
            self.guessCanvas.delete("all")
            for n in range(self.n):
                self.guessCanvas.create_circle((n*50)+25,25,20,fill="#fff")

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
        '''
        Evaluate the current state and display red/white boxes; determine if the game is over

        Call when a full guess has been placed
        '''
        white,red = process.check(self.choice,self.code)
        try: [self.guessCanvas.delete(box) for box in self.whiteRedBoxes] # delete boxes from last guess
        except AttributeError: pass # unless this is the first guess
        self.whiteRedBoxes = []

        # a counter is used as we need something positionally and white and red are variable
        counter = 0

        # Display output in the guess canvas and history canvas
        for num, color in [(white,"#fff"),(red,"#f00")]:
            for n in range(num):
                box = self.guessCanvas.create_rectangle(5+(12*counter),55,15+(12*counter),65,fill=color)
                self.whiteRedBoxes.append(box)

                x1,y1,x2,y2 = (self.n)*12+((counter)*10)+4,12*self.attempts+4,(self.n)*12+8+((counter)*10)+4,12*self.attempts+12
                self.historyCanvas.create_rectangle(x1,y1,x2,y2,fill=color)

                counter += 1

        # Check if game is over- if so display message; disable buttons
        if red == self.n:
            tk.Label(self.frame,text="YOU WIN!").pack()
            for button in self.colorButtons: button.configure(state = tk.DISABLED)
        elif self.maxChoice == 1:
            tk.Label(self.frame,text="YOU LOSE!").pack()
            for button in self.colorButtons: button.configure(state = tk.DISABLED)

# Start the tkinter main loop with the Main class
main = Main(root)
root.mainloop()
