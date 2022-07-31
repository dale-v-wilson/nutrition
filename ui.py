import tkinter
from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master


root = Tk()
root.wm_title("Nutrition")
app = Window(root)
root.geometry("850x530")

gendervar = IntVar()
gendervar.set(2)

agevar = IntVar()
agevar.set(20)

heightvar = IntVar()
heightvar.set(150)

weightvar = IntVar()
weightvar.set(60)

bmivar = StringVar()

bmrvar = StringVar()

actvar = StringVar()
actvar.set("sedentary")

calburnvar = IntVar()

dummy=IntVar()
dummy.set(0)

def getGender():
    genderResultLabel = Label(root, text=gendervar.get())
    genderResultLabel.grid(row=4, column=1)

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def updatestats(event):
    bmivar.set(str(calcbmi(heightvar.get(), weightvar.get())))


    bmiLabel = Label(statsFrame, text="Your BMI is " + str(bmivar.get()))
    bmiLabel.grid(row=0, column=0)

    bmrvar.set(str(calcbmr(gendervar.get(), heightvar.get(), weightvar.get(), agevar.get())))

    bmrLabel = Label(statsFrame, text="Your BMR is " + str(bmrvar.get()))
    bmrLabel.grid(row=1, column=0)

    calburnvar.set(int(calcCaloricBurn(bmrvar.get(), actvar.get())))

    activityLabel = Label(statsFrame, text="Daily caloric burn is  " + str(calburnvar.get()))
    activityLabel.grid(row=3, column=0)

def calcbmi(height, weight):
    bmi = round(float(weight) / ((float(height) / 100) ** 2), 2)
    return bmi


def calcbmr(gender, height, weight, age):
    if gender == 1:
        bmr = round((88.4 + 13.4 * weight) + (4.8 * height) - (5.68 * age), 2)
        return bmr
    else:
        bmr = round((447.6 + 9.25 * weight) + (3.10 * height) - (4.33 * age), 2)
        return bmr

def calcCaloricBurn(bmr, activity):
    if activity == "sedentary":
        burn = float(bmr) * 1.2
        return burn
    elif activity == "lightly active":
        burn = float(bmr) * 1.375
        return burn
    elif activity == "moderately active":
        burn = float(bmr) * 1.55
        return burn
    elif activity == "active":
        burn = float(bmr) * 1.725
        return burn
    elif activity == "very active":
        burn = float(bmr) * 1.9
        return burn


genderRadioFrame = LabelFrame(root, text="Select your gender", width=20)
genderRadioFrame.grid(row=0, column=1)

genderRadioMale = Radiobutton(genderRadioFrame, variable=gendervar, text="Male", value=1, anchor=W)
genderRadioFemale = Radiobutton(genderRadioFrame, variable=gendervar, text="Female", value=2, anchor=W)
genderRadioMale.pack()
genderRadioFemale.pack()

ageFrame = LabelFrame(root, text="Select your age", width=100)
ageFrame.grid(row=5, column=1)

ageSlider = Scale(ageFrame, from_=1, to=120, orient=HORIZONTAL, variable=agevar, command=updatestats)
ageSlider.grid(row=6, column=1)

heightFrame = LabelFrame(root, text="Select your height in cm")
heightFrame.grid(row=6, column=1)

heightSlider = Scale(heightFrame, from_=30, to=250, orient=HORIZONTAL, variable=heightvar, command=updatestats)
heightSlider.pack()



weightFrame = LabelFrame(root, text="Select your weight in kg")
weightFrame.grid(row=7, column=1)

weightSlider = Scale(weightFrame, from_=5, to=300, orient=HORIZONTAL, variable=weightvar, command=updatestats)
weightSlider.pack()

statsFrame = LabelFrame(root, text="Your stats here")
statsFrame.grid(row=0, column=3)

try:
    bmrvar.set(str(calcbmr(gendervar.get(), heightvar.get(), weightvar.get(), agevar.get())))
except:
    bmrExcept = Label(statsFrame, text="Error", fg="red")
    bmrExcept.grid(row=0, column=1)

try:
    bmivar.set(str(calcbmi(heightvar.get(), weightvar.get())))
except:
    bmiExcept = Label(statsFrame, text="Error", fg="red")
    bmiExcept.grid(row=1, column=1)

bmiLabel = Label(statsFrame, text="Your BMI is" + str(bmivar.get()))
bmiLabel.grid(row=0, column=0)

bmrLabel = Label(statsFrame, text="Your BMR is" + str(bmrvar.get()))
bmrLabel.grid(row=1, column=0)

activityFrame = LabelFrame(root, text="Select an activity level")
activityFrame.grid(row=8, column=1)

activity_options = [
    "sedentary",
    "lightly active",
    "moderately active",
    "active",
    "very active"
]
i = 0
for activity_option in activity_options:
    activity_option = Radiobutton(activityFrame, variable=actvar, text=activity_option, value=activity_option, anchor=W, command=lambda: updatestats(dummy))
    activity_option.grid(row=i, column=0)
    i += 1

calburnvar.set(int(calcCaloricBurn(bmrvar.get(), actvar.get())))

activityLabel = Label(statsFrame, text="Daily caloric burn is  " + str(calburnvar.get()))
activityLabel.grid(row=3, column=0)

root.mainloop()
