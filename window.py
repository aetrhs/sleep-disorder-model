from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("650x600")
window.title("Sleep Disorder Predictor")
from SleepDecisionTree import MyDecisionTree

decisionTree = MyDecisionTree()

def trainData():
    newSeedValue = int(seedsVar.get())
    decisionTree.updateSeed(newSeedValue)
    decisionTree.trainData()

def testData():
    text.delete("1.0", "end")
    text.insert(END, decisionTree.readCategories())
    result, accuracy = decisionTree.testData()
    text.insert(END, '\n[' + str(result[0]))
    text.insert(END, '\n ' + str(result[1]))
    text.insert(END, '\n ' + str(result[2]) + ']')
    text.insert(END, '\n\nAccuracy: ' + str(int(accuracy * 100)) + '%')

def makeNewPrediction():
    try:
        gender = int(entry41.get())
        age = int(entry42.get())
        sleep_duration = float(entry43.get())
        quality_of_sleep = int(entry44.get())
        physical_activity = int(entry45.get())
        stress_level = int(entry46.get())
        bmi_category = int(entry47.get())
        blood_pressure = float(entry48.get())
        heart_rate = int(entry49.get())
        daily_steps = int(entry50.get())

        prediction_Res = decisionTree.makePrediction(
            gender, age, sleep_duration, quality_of_sleep,
            physical_activity, stress_level, bmi_category,
            blood_pressure, heart_rate, daily_steps
        )

        print(f"Prediction Result: {prediction_Res}")

        entry52.delete(0, END)
        entry52.insert(END, str(prediction_Res))

    except ValueError as e:
        print(f"Input error: {e}")
        entry52.delete(0, END)
        entry52.insert(END, "Input error")


frame = Frame(window, width=650, height=600)
frame.place(x=10, y=100)

label0 = Label(window, text="Sleep Disorder Predictor", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label0.place(x=190, y=30)

label01 = Label(window, text="Enter Seed Value for Random No Generator", fg="red", font=("arial", 11, "bold"))
label01.place(x=160, y=70)

label1 = Label(frame, text="Enter Seed Value", fg="blue", width=15, font=("arial", 10, "bold"))
label1.grid(row=0, column=0, sticky=W + E)

list1 = ['1', '2', '3', '4', '5']
seedsVar = StringVar()
combo1 = OptionMenu(frame, seedsVar, *list1)
seedsVar.set("1")
combo1.grid(row=0, column=1, sticky=W + E)

button1 = Button(frame, text="Train Data", fg="black", font=("arial", 10, "bold"), command=trainData)
button1.grid(row=1, column=0, sticky=W + E)

button2 = Button(frame, text="Test Data", fg="black", font=("arial", 10, "bold"), command=testData, width=20)
button2.grid(row=1, column=1, sticky=W + E)

label3 = Label(frame, text="Output", fg="blue", width=15, font=("arial", 10, "bold"))
label3.grid(row=2, column=0)

text = Text(frame, height=7, width=12)
text.grid(row=2, column=1, ipadx=100)

label03 = Label(frame, text="Now Test for New Data", fg="red", font=("arial", 14, "bold"))
label03.grid(row=3, column=0, columnspan=2, sticky=W + E)

label41 = Label(frame, text="Gender (0=Female, 1=Male)", fg="blue", width=20, font=("arial", 10, "bold"))
label41.grid(row=4, column=0, sticky=W + E)
entry41 = Entry(frame)
entry41.insert(END, '')
entry41.grid(row=4, column=1, sticky=W + E)

label42 = Label(frame, text="Age", fg="blue", width=15, font=("arial", 10, "bold"))
label42.grid(row=5, column=0, sticky=W + E)
entry42 = Entry(frame)
entry42.insert(END, '')
entry42.grid(row=5, column=1, sticky=W + E)

label43 = Label(frame, text="Sleep Duration (hrs/day)", fg="blue", width=20, font=("arial", 10, "bold"))
label43.grid(row=6, column=0, sticky=W + E)
entry43 = Entry(frame)
entry43.insert(END, '')
entry43.grid(row=6, column=1, sticky=W + E)

label44 = Label(frame, text="Quality of Sleep (1-10)", fg="blue", width=20, font=("arial", 10, "bold"))
label44.grid(row=7, column=0, sticky=W + E)
entry44 = Entry(frame)
entry44.insert(END, '')
entry44.grid(row=7, column=1, sticky=W + E)

label45 = Label(frame, text="Physical Activity (min/day)", fg="blue", width=20, font=("arial", 10, "bold"))
label45.grid(row=8, column=0, sticky=W + E)
entry45 = Entry(frame)
entry45.insert(END, '')
entry45.grid(row=8, column=1, sticky=W + E)

label46 = Label(frame, text="Stress Level (1-10)", fg="blue", width=20, font=("arial", 10, "bold"))
label46.grid(row=9, column=0, sticky=W + E)
entry46 = Entry(frame)
entry46.insert(END, '')
entry46.grid(row=9, column=1, sticky=W + E)

label47 = Label(frame, text="BMI Category (1=Normal, 2=Overweight, 3=Obese)", fg="blue",
                font=("arial", 10, "bold"))
label47.grid(row=10, column=0, sticky=W + E)

entry47 = Entry(frame)
entry47.insert(END, '')
entry47.grid(row=10, column=1, sticky=W + E)

label48 = Label(frame, text="Blood Pressure Average", fg="blue", width=25, font=("arial", 10, "bold"))
label48.grid(row=11, column=0, sticky=W + E)
entry48 = Entry(frame)
entry48.insert(END, '')
entry48.grid(row=11, column=1, sticky=W + E)

label49 = Label(frame, text="Heart Rate (bpm)", fg="blue", width=20, font=("arial", 10, "bold"))
label49.grid(row=12, column=0, sticky=W + E)
entry49 = Entry(frame)
entry49.insert(END, '')
entry49.grid(row=12, column=1, sticky=W + E)

label50 = Label(frame, text="Daily Steps", fg="blue", width=20, font=("arial", 10, "bold"))
label50.grid(row=13, column=0, sticky=W + E)
entry50 = Entry(frame)
entry50.insert(END, '')
entry50.grid(row=13, column=1, sticky=W + E)

button3 = Button(frame, text="Make Prediction", fg="black", font=("arial", 10, "bold"), command=makeNewPrediction)
button3.grid(row=14, column=0, sticky=W + E)

entry52 = Entry(frame)
entry52.insert(END, '')
entry52.grid(row=14, column=1, sticky=W + E)

mainloop()
