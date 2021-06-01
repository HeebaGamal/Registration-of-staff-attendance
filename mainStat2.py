# import numpy as np; np.random.seed(13)
import matplotlib.pyplot as plt
import math
from tkinter import *
from tkinter.constants import *
import statistics
from scipy.stats import linregress
import tkinter.messagebox
import matplotlib.pylab as pylab
from PIL import Image, ImageTk
import time
from datetime import date
from datetime import datetime
import pydoc


strdata=""
values = []
str=""
mean=0
median=0
mode=0
slope=0
intercept=0
r_value=0
p_value=0
std_err=0
variance=0
standardDivition=0
x=[]
y=[]
temp=[]
currentHour=0
def getCurrentTimeOfRegestration():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_hour=now.strftime("%H")
    currentHour=current_hour
    tkinter.messagebox.showinfo("Your Regestration at ", current_time)
    # if currentHour>12:
    #     currentHour=currentHour-12
    temp.append(currentHour)
    temp.append(' ')
def corrletion_regression():
    def calcoorelation(eslope, eIntercept, eR_value, eStandard):
        try:
            strx = eX.get().split()
            for i in strx:
                x.append(int(i))
                print(i + "\n")

            stry = eY.get().split()
            for i in stry:
                y.append(int(i))

            if len(x)==len(y):
                slope, intercept, r_value, p_value, std_err = linregress(x, y)
                eslope.delete(0, END)
                eslope.insert(0, slope)
                eIntercept.delete(0, END)
                eIntercept.insert(0, intercept)
                eR_value.delete(0, END)
                eR_value.insert(0, r_value)
                eStandard.delete(0, END)
                eStandard.insert(0, std_err)
                if r_value<0:
                    r_value=r_value*-1
                if r_value == 1:
                    valueOfR="Correlation is perfect  "
                elif r_value >=0.7 and r_value<=0.9:
                    valueOfR="Correlation is Strong   "
                elif r_value >=0.4 and r_value<=0.6:
                    valueOfR = "Correlation is Moderate   "
                elif r_value >=0.1 and r_value<=0.3:
                    valueOfR = "Correlation is Weak   "
                else:
                    valueOfR="No Correlation  "

                tkinter.messagebox.showinfo("Correlation ",valueOfR)
            else:
                tkinter.messagebox.showinfo("Correlation ", "x and y Must be in the same size ")
                x.clear()
                y.clear()
        except:
            tkinter.messagebox.showinfo("Invalid Data ","Enter valid Data")

    def ResetFields():
        eX.delete(0, END)
        eY.delete(0, END)
        eslope.delete(0,END)
        eslope.insert(0, 0)
        eIntercept.delete(0,END)
        eIntercept.insert(0,0)
        eR_value.delete(0, END)
        eR_value.insert(0, 0)
        eStandard.delete(0, END)
        eStandard.insert(0, 0)
        x.clear()
        y.clear()

    def help():
        tkinter.messagebox.showinfo("!", "The Entered Data should be Integer and separated by space ")
    corrletion_regressionWindow = tkinter.Tk()
    corrletion_regressionWindow.geometry("250x250")
    lblTitleX = tkinter.Label(corrletion_regressionWindow, text="X = ")
    lblTitleX.place(x=0, y=0)

    eX = tkinter.Entry(corrletion_regressionWindow)
    eX.place(x=100, y=0)

    lblTitleY = tkinter.Label(corrletion_regressionWindow, text="Y = ")
    lblTitleY.place(x=0, y=25)

    b1lhelp = tkinter.Button(corrletion_regressionWindow, text='!', command=help)
    b1lhelp.place(x=235, y=10)

    eY = tkinter.Entry(corrletion_regressionWindow)
    eY.place(x=100, y = 25)

    lblslope = tkinter.Label(corrletion_regressionWindow, text=" Slope            = ")
    lblslope.place(x=0, y=75)

    eslope = tkinter.Entry(corrletion_regressionWindow)
    eslope.place(x=100, y=75)

    lblIntercept = tkinter.Label(corrletion_regressionWindow, text=" Intercept        = ")
    lblIntercept.place(x=0, y=100)

    eIntercept = tkinter.Entry(corrletion_regressionWindow)
    eIntercept.place(x=100, y=100)

    lblR_value = tkinter.Label(corrletion_regressionWindow, text=" R value          = ")
    lblR_value.place(x=0, y=125)

    eR_value = tkinter.Entry(corrletion_regressionWindow)
    eR_value.place(x=100, y=125)

    lblStandard = tkinter.Label(corrletion_regressionWindow, text=" standard Error   = ")
    lblStandard.place(x=0, y=150)

    eStandard = tkinter.Entry(corrletion_regressionWindow)
    eStandard.place(x=100, y=150)

    bttn = tkinter.Button(corrletion_regressionWindow, text='Calculate', width=25,command=lambda: calcoorelation(eslope, eIntercept, eR_value, eStandard))
    bttn.place(x=25, y=47)

    btttnRset = tkinter.Button(corrletion_regressionWindow, text='Reset', width=25, command=ResetFields)
    btttnRset.place(x=25, y=175)

    btttnQuit = tkinter.Button(corrletion_regressionWindow, text='Quit', width=25, command=corrletion_regressionWindow.quit)
    btttnQuit.place(x=25, y=200)

    corrletion_regressionWindow.title("corrletion regressionWindow")
    corrletion_regressionWindow.mainloop()

def Central_Tendency_Variability():
    # Caclulate k
    def calNumOfIntervals(values):
        k = int(math.log(len(values),2) + 2)
        return k


    # Calculate length of interval
    def calcLengthOfInterval(values,k):
        lenOfInterval = int((values[len(values) - 1] - values[0]) / k)
        if (values[len(values) - 1] - values[0]) % k != 0:
            lenOfInterval += 1
        return lenOfInterval


    # Calculate the mean
    def calcMean(values):
        mean = 0
        for i in values:
            mean += i
        mean /= len(values)
        return mean


    # Calculate the median
    def calcMedian(values):
        if (len(values) % 2 != 0):
            return values[int(len(values) / 2)]
        else:
            return (values[int(len(values) / 2)] + values[int(len(values) / 2) - 1]) / 2


    # Calculate the mode
    def calcMode(val):
        freq = {}
        mx = 0
        cnt = 0
        mode = 0
        for i in val:
            if (i in freq):
                freq[i] += 1
            else:
                freq[i] = 1
            mx = max(mx, freq[i])

        for key, val in freq.items():
            if val == mx:
                cnt += 1
                mode = key

        if cnt > 1:
            return -1
        return mode


    # Caclulate Q2
    def calcQ2(n, values):
        if (n % 2 != 0):
            return values[int(n / 2)]
        else:
            return (values[int(n / 2)] + values[int(n / 2) - 1]) / 2


    # Calculate Q1
    def calcQ1(n, values):  # hta5od numOfData/2 -1
        if (n % 2 == 0):
            return values[int(n / 2)]
        else:
            return (values[int(n / 2)] + values[int(n / 2) + 1]) / 2


    # Calculate Q3
    def calcQ3(n, n2, values):  # hta5od size of data , w el mkan elly htbda2 mn 3ando elly hwa n/2
        if (n % 2 != 0):
            n2 += 1

        if ((n - n2) % 2 != 0):
            return values[int((n + n2) / 2)]
        else:
            return (values[int((n + n2 - 1) / 2)] + values[int((n + n2 - 1) / 2) + 1]) / 2


    # Calculate IQR
    def calcIQR(n, values):
        return calcQ3(n, int(n / 2), values) - calcQ1(int(n / 2) - 1, values)


    # Calculate Smalest Out liers
    def calcSmallestOutliers(n, values):
        q1 = calcQ1(int(n / 2) - 1, values)
        IQR = calcIQR(n, values)
        return q1 - 1.5 * IQR


    # Calculate Largest Out liers
    def calcLargestOutliers(n, values):
        q3 = calcQ3(n, int(n / 2), values)
        IQR = calcIQR(n, values)
        return q3 + 1.5 * IQR


    # Showing histogram
    def showHistogram(values, k):
        plt.hist(values, bins=k, ec='k')
        plt.show()


    # showingDotPlot
    def showDotPlot(values):
        y = []
        cnt = 1;
        freq = {}
        for i in values:
            if (i in freq):
                freq[i] += 1
            else:
                freq[i] = 1

        for key, val in freq.items():
            tmp = val
            for i in range(1, tmp + 1):
                y.append(i)
        plt.plot(values, y, 'o', color="Black")
        plt.show()


    # showingBoxPlot
    def showBoxPlot(values):
        plt.boxplot(values)
        plt.title('Data')
        plt.show()


    # showing Pie Chart
    def showPieChart(n, values):
        freq = {}
        data = []
        frequncy = []
        for i in values:
            if (i in freq):
                freq[i] += 1
            else:
                freq[i] = 1
        for key, val in freq.items():
            data.append(key)
            frequncy.append(val)

        plt.pie(frequncy, labels=data, autopct='%.1f%%', startangle=90)
        plt.show()

    def cal(e2,e3,e4):
        try:

            s = e1.get().split()
            for i in s:
                values.append(int(i))
                print(i + "\n")
            values.sort()
            #show HestoGram
            def show_HestoGram():
                showHistogram(values, calNumOfIntervals(values))
            def Show_dotPlot():
                showDotPlot(values)
            def Show_BoxPlot():
                showBoxPlot(values)
            def show_PieChart():
                showPieChart(len(values),values)
            e2.delete(0,END)
            e2.insert(0,calcMean(values))
            e3.delete(0,END)
            e3.insert(0,calcMedian(values))
            e4.delete(0,END)
            e4.insert(0,calcMode(values))
            e5.delete(0,END)
            e5.insert(0,statistics.variance(values))
            e6.delete(0,END)
            e6.insert(0,statistics.variance(values)*statistics.variance(values))
            graphwindow = tkinter.Tk()
            graphwindow.geometry("250x250")
            lbl1 = tkinter.Label(graphwindow, text="Choose the graph  ")
            lbl1.place(x=60, y=0)
            # tkinter.Label(EnterData,text="Last Name").grid(row=1)
            btnHesto = tkinter.Button(graphwindow,text='HistoGram', width=25, command=show_HestoGram)
            btnHesto.place(x=30, y=25)

            btndot = tkinter.Button(graphwindow,text='Dot-Plot', width=25, command=Show_dotPlot)
            btndot.place(x=30, y=50)

            btnBoxPlot = tkinter.Button(graphwindow,text='Box-Plot', width=25, command=Show_BoxPlot)
            btnBoxPlot.place(x=30, y=75)

            btnPieChart= tkinter.Button(graphwindow, text='PieChart', width=25, command=show_PieChart)
            btnPieChart.place(x=30, y=100)

            bttnQuit = tkinter.Button(graphwindow, text='Quit', width=30, command=graphwindow.quit)
            bttnQuit.place(x=10, y=140)

            graphwindow.title("Graphs")
        except:
            tkinter.messagebox.showinfo("Invalid Data ","Enter valid Data")

    def ResetFields():
        e1.delete(0, END)
        e2.delete(0, END)
        e2.insert(0, 0)
        e3.delete(0, END)
        e3.insert(0, 0)
        e4.delete(0, END)
        e4.insert(0, 0)
        e5.delete(0,END)
        e5.insert(0, 0)
        e6.delete(0, END)
        e6.insert(0, 0)

    def help():
        tkinter.messagebox.showinfo("!", "The Entered Data should be Integer and separated by space")
    EnterData = tkinter.Tk()
    EnterData.geometry("250x250")
    lbl1=tkinter.Label(EnterData,text="Enter Numbers ")
    lbl1.place(x=0,y=0)


    e1 = tkinter.Entry(EnterData)
    e1.place(x=100,y=0)

    b1help = tkinter.Button(EnterData,text='!',command=help)
    b1help.place(x=235, y=0)

    btnShow = tkinter.Button(EnterData, text='Show Graphs', width=25, command=lambda:cal(e2,e3,e4))
    btnShow.place(x=25,y=25)

    lbl2 = tkinter.Label(EnterData, text=" Mean    = ")
    lbl2.place(x=0, y=55)

    e2 = tkinter.Entry(EnterData)
    e2.place(x=100, y=55)

    lbl3 = tkinter.Label(EnterData, text=" Medain = ")
    lbl3.place(x=0, y=75)

    e3 = tkinter.Entry(EnterData)
    e3.place(x=100, y=75)

    lbl4 = tkinter.Label(EnterData, text=" Mode    = ")
    lbl4.place(x=0, y=100)

    e4 = tkinter.Entry(EnterData)
    e4.place(x=100, y=100)

    lbl5 = tkinter.Label(EnterData, text=" Variance    = ")
    lbl5.place(x=0, y=125)

    e5 = tkinter.Entry(EnterData)
    e5.place(x=100, y=125)

    lbl6 = tkinter.Label(EnterData, text=" Standard Deviation   = ")
    lbl6.place(x=0, y=150)

    e6 = tkinter.Entry(EnterData)
    e6.place(x=100, y=150)

    btnRset=tkinter.Button(EnterData, text='Reset', width=25,command=ResetFields)
    btnRset.place(x=25, y=180)

    btnQuit=tkinter.Button(EnterData, text='Quit', width=25,command=EnterData.quit)
    btnQuit.place(x=25, y=210)

    e1.insert(0, temp)
    EnterData.title("Enter Data")

top = tkinter.Tk()
top.geometry("500x500")
corb=tkinter.Button(top,text="Correlation and regretion",width=30,command=corrletion_regression)
corb.place(x=120,y=380)

firstB = tkinter.Button(top, text="Central Tendency and Variability ",width=30, command=Central_Tendency_Variability)
firstB.place(x=120, y=415)

btttnQuit = tkinter.Button(top, text='Quit', command=top.quit)
btttnQuit.place(x=220, y=460)

signtur = tkinter.Label(top, text="GOATs",font="italic")
signtur.place(x=440, y=470)

# img = ImageTk.PhotoImage(Image.open("imp.png"))
# panel = tkinter.Label(top, image = img)
# panel.pack()

lblTitle=tkinter.Label(top,text="Work Aِttendance Registration System",width=40,font="large_font")
lblTitle.place(x=55,y=20)

btnRegester = tkinter.Button(top, text='Register',width=20,height=5,font="large_font",command=getCurrentTimeOfRegestration)
btnRegester.place(x=145, y=60)

top.title("Work Aِttendance Registration System")
top.mainloop()
#
