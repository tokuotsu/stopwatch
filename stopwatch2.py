import time
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        master.geometry("300x650")
        master.title("Stop Watch")
        master.config(bg="black")
        
        self.startTime = time.time()
        self.stopTime=0.0
        self.elapsedTime=0.0
        self.playTime=False
        self.spl=[]
        self.splitTime=0.0

        self.canvas = tk.Canvas(master, width=290, height=80, bg="skyblue")
        self.canvas.place(x=3, y=10)
        self.canvas2 = tk.Canvas(master, width=290, height=400)
        self.canvas2.place(x=3, y=110)
        self.canvas2.create_text(50,40,text="ラップ",font=("Helvetica",5,"bold"),fill="black")
        self.canvas2.create_text(130,40,text="ラップタイム",font=("Helvetica",5,"bold"),fill="black")
        self.canvas2.create_text(230,40,text="スプリットタイム",font=("Helvetica",5,"bold"),fill="black")

        width=15
        tk.Button(master,text="リセット",command=self.resetButtonClick,width=width).place(x=160, y=590)
        tk.Button(master,text="スタート",command=self.startButtonClick,width=width).place(x=20, y=540)
        tk.Button(master,text="ラップ",command=self.lapButtonClick,width=width).place(x=160, y=540)
        tk.Button(master,text="ストップ",command=self.stopButtonClick,width=width).place(x=20, y=590)


        master.after(5,self.update)
    
    def lapButtonClick(self):
        if self.playTime:
            self.splitTime = time.time() - self.startTime
            self.spl.append(self.splitTime)
            self.playTime=True

    def startButtonClick(self):
        if not self.playTime:
            self.startTime=time.time()-self.elapsedTime
            self.playTime=True

    def stopButtonClick(self):
        if self.playTime:
            self.stopTime=time.time()-self.startTime
            self.playTime=False

    def resetButtonClick(self):
        self.startTime = time.time()
        self.stopTime = 0.0
        self.elapsedTime = 0.0
        self.splitTime = 0.0
        self.spl = []
        self.playTime = False
    
    def update(self):
        self.canvas.delete("Time")
        self.canvas2.delete("Time")
        if len(self.spl)>0:
        #self.laps.append(self.lap[-1]-self.lap[-2])       
            for i in range(len(self.spl)):
                font=15
                self.canvas2.create_text(250,60+30*i,text='{:.3f}'.format(round(self.spl[i],3)),font=("Helvetica",font,"bold"),fill="black",tag="Time",anchor="e")
                #number
                self.canvas2.create_text(60,60+30*i,text=round(i+1),font=("Helvetica",font,"bold"),fill="black",tag="Time",anchor="e")
                if i == 0: #laptime
                    self.canvas2.create_text(150,60+30*i,text='{:.3f}'.format(round(self.spl[0],3),font=("Helvetica",font,"bold")),fill="black",tag="Time",anchor="e")
                else:
                    self.canvas2.create_text(150,60+30*i,text='{:.3f}'.format(round(self.spl[i]-self.spl[i-1],3)),font=("Helvetica",font,"bold"),fill="black",tag="Time",anchor="e")
        if self.playTime:
            self.elapsedTime=time.time()-self.startTime
            self.canvas.create_text(280,40,text='{:.3f}'.format(round(self.elapsedTime,3)),font=("Helvetica",40,"bold"),fill="black",tag="Time",anchor="e")
        else:
            self.canvas.create_text(280,40,text='{:.3f}'.format(round(self.stopTime,3)),font=("Helvetica",40,"bold"),fill="black",tag="Time",anchor="e")

        self.master.after(5,self.update)

def main():
        win = tk.Tk()
        app = Application(master=win)
        app.mainloop()

if __name__ == "__main__":
        main()
