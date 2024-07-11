from typing import Text
import numpy as np
import tkinter as tk
import math
import json


#make GUI
window = tk.Tk()
window.title("Run time Guessing")
window.geometry("1000x500")

window.rowconfigure(0, minsize=50)
window.columnconfigure(0, minsize=50)

#neural network
class neural_network:
    def __init__(self):
        self.weights = 0.9

    def train(self, inputs, outputs, num):
        for iteration in range(num):
            
            output = self.think(inputs)
            error = outputs - output
            adjustment = 0.0000001 * np.dot(inputs.T, error)
            print(adjustment)
            self.weights += adjustment

    def think(self, inputs):
        return (np.dot(inputs, self.weights))

neural_network1 = neural_network()
neural_network2 = neural_network()
neural_network3 = neural_network()
neural_network4 = neural_network()
neural_network5 = neural_network()
neural_network6 = neural_network()
neural_network7 = neural_network()
neural_network8 = neural_network()
neural_network9 = neural_network()
neural_network10 = neural_network()
neural_network11 = neural_network()
neural_network12 = neural_network()

class messaging():
    def __init__(self):
        
        self.firstEvent = 0;
        
        label = tk.Label(text="Put your time (any distance)", bg="green", fg="black")
        label.grid(row = 0, column = 0, sticky="w")

        self.labelMinutes = tk.Label(text="Minutes", bg="green", fg="black")
        self.labelMinutes.grid(row = 1, column = 1, sticky="w")
        
        self.textInputMinutes = tk.Entry(bg="white", fg="black")
        self.textInputMinutes.grid(row=1, column=2, sticky="w")
        
        self.labelSeconds = tk.Label(text="Seconds", bg="green", fg="black")
        self.labelSeconds.grid(row = 1, column = 3, sticky="w")
        
        self.textInputSeconds = tk.Entry(bg="white", fg="black")
        self.textInputSeconds.grid(row=1, column=4, sticky="w")
        
        firstEvent = tk.Button(text="400", width=10, height=2, bg="blue", command= lambda : self.setFirstTime(400))
        firstEvent.grid(row=2, column=5, sticky="e")
        firstEvent2 = tk.Button(text="800", width=10, height=2, bg="blue", command= lambda : self.setFirstTime(800))
        firstEvent2.grid(row=2, column=6, sticky="e")
        firstEvent3 = tk.Button(text="1600", width=10, height=2, bg="blue", command= lambda : self.setFirstTime(1600))
        firstEvent3.grid(row=2, column=7, sticky="e")
        firstEvent4 = tk.Button(text="5k", width=10, height=2, bg="blue", command= lambda : self.setFirstTime(5000))
        firstEvent4.grid(row=2, column=8, sticky="e")
        

        
    def setFirstTime(self, firstTime):
        self.firstEvent = firstTime
        
        self.nowEndTime = tk.Label(text="Choose the distance to convert to", bg="green", fg="black")
        self.nowEndTime.grid(row=3, column=0, sticky="w")
        
        enterButton = tk.Button(text="400", width=10, height=2, bg="blue", command= lambda : self.usertimes(400))
        enterButton.grid(row=4, column=5, sticky="e")
        enterButton2 = tk.Button(text="800", width=10, height=2, bg="blue", command= lambda : self.usertimes(800))
        enterButton2.grid(row=4, column=6, sticky="e")
        enterButton3 = tk.Button(text="1600", width=10, height=2, bg="blue", command= lambda : self.usertimes(1600))
        enterButton3.grid(row=4, column=7, sticky="e")
        enterButton4 = tk.Button(text="5k", width=10, height=2, bg="blue", command= lambda : self.usertimes(5000))
        enterButton4.grid(row=4, column=8, sticky="e")
    
    def improveAI(self, oldRace, oldRaceTime, currentRace):
        
        raceTimeRealMinutes = self.realTimeInputMinutes.get()
        raceTimeRealSeconds = self.realTimeInputSeconds.get()
        raceRealTime = (int(raceTimeRealMinutes) * 60) + int(raceTimeRealSeconds)
        print(str(oldRace) + " time " + str(oldRaceTime) + " currentRace " + str(currentRace) + " realTime " + str(raceRealTime))
        
        #change variable
        if (oldRace == 400):
            if (currentRace == 800):
                json_object["quarter_to_800_inputs"].append(oldRaceTime)
                json_object["quarter_to_800_outputs"].append(raceRealTime)
                a_file = open("./data.json", "w")
                json.dump(json_object, a_file)
                a_file.close()
            elif (currentRace == 1600):
                json_object["quarter_to_mile_inputs"].append(oldRaceTime)
                json_object["quarter_to_mile_outputs"].append(raceRealTime)
                a_file = open("./data.json", "w")
                json.dump(json_object, a_file)
                a_file.close()
            elif (currentRace == 5000):
                json_object["quarter_to_5k_inputs"].append(oldRaceTime)
                json_object["quarter_to_5k_outputs"].append(raceRealTime)
                a_file = open("./data.json", "w")
                json.dump(json_object, a_file)
                a_file.close()
                    
        elif (oldRace == 800):
            if (currentRace == 400):
                json_object["half_to_quarter_inputs"].append(oldRaceTime)
                json_object["half_to_quarter_outputs"].append(raceRealTime)
                a_file = open("./data.json", "w")
                json.dump(json_object, a_file)
                a_file.close()
            elif (currentRace == 1600):
                json_object["half_to_mile_inputs"].append(oldRaceTime)
                json_object["half_to_mile_outputs"].append(raceRealTime)
                a_file = open("./data.json", "w")
                json.dump(json_object, a_file)
                a_file.close()
            elif (currentRace == 5000):
                json_object["half_to_5k_inputs"].append(oldRaceTime)
                json_object["half_to_5k_outputs"].append(raceRealTime)
                a_file = open("./data.json", "w")
                json.dump(json_object, a_file)
                a_file.close()

        elif (oldRace == 1600):
            if (currentRace == 400):
                json_object["mile_to_quarter_inputs"].append(oldRaceTime)
                json_object["mile_to_quarter_outputs"].append(raceRealTime)
                a_file = open("./data.json", "w")
                json.dump(json_object, a_file)
                a_file.close()
            elif (currentRace == 800):
                json_object["mile_to_half_inputs"].append(oldRaceTime)
                json_object["mile_to_half_outputs"].append(raceRealTime)
                a_file = open("./data.json", "w")
                json.dump(json_object, a_file)
                a_file.close()
            elif (currentRace == 5000):
                json_object["mile_to_5k_inputs"].append(oldRaceTime)
                json_object["mile_to_5k_outputs"].append(raceRealTime)
                a_file = open("./data.json", "w")
                json.dump(json_object, a_file)
                a_file.close()
                
        elif (oldRace == 5000):
            if (currentRace == 400):
                json_object["fivek_to_quarter_inputs"].append(oldRaceTime)
                json_object["fivek_to_quarter_outputs"].append(raceRealTime)
                a_file = open("./data.json", "w")
                json.dump(json_object, a_file)
                a_file.close()
            elif (currentRace == 800):
                json_object["fivek_to_half_inputs"].append(oldRaceTime)
                json_object["fivek_to_half_outputs"].append(raceRealTime)
                a_file = open("./data.json", "w")
                json.dump(json_object, a_file)
                a_file.close()
            elif (currentRace == 1600):
                json_object["fivek_to_mile_inputs"].append(oldRaceTime)
                json_object["fivek_to_mile_outputs"].append(raceRealTime)
                a_file = open("./data.json", "w")
                json.dump(json_object, a_file)
                a_file.close()

        #rewrite json file with new variable
        
    def usertimes(self, endDistance):
        raceTimeMinutes = self.textInputMinutes.get()
        raceTimeSeconds = self.textInputSeconds.get()
        raceTime = (int(raceTimeMinutes) * 60) + int(raceTimeSeconds)
        
        try:
            #train
            if (self.firstEvent == 400):
                if (endDistance == 800):
                    neural_network1.train(quarter_to_800_inputs, quarter_to_800_outputs, 5000)
                    self.outputs = neural_network1.think(int(raceTime))
                    
                elif (endDistance == 1600):
                    neural_network2.train(quarter_to_mile_inputs, quarter_to_mile_outputs, 5000)
                    self.outputs = neural_network2.think(int(raceTime))
                elif (endDistance == 5000):
                    neural_network3.train(quarter_to_5k_inputs, quarter_to_5k_outputs, 5000)
                    self.outputs = neural_network3.think(int(raceTime))
                    
            elif (self.firstEvent == 800):
                if (endDistance == 400):   
                    neural_network4.train(half_to_quarter_inputs, half_to_quarter_outputs, 5000)
                    self.outputs = neural_network4.think(int(raceTime))
                elif (endDistance == 1600):
                    neural_network5.train(half_to_mile_inputs, half_to_mile_outputs, 5000)
                    self.outputs = neural_network5.think(int(raceTime))
                elif (endDistance == 5000):
                    neural_network6.train(half_to_5k_inputs, half_to_5k_outputs, 5000)
                    self.outputs = neural_network6.think(int(raceTime))

            elif (self.firstEvent == 1600):
                if (endDistance == 400):   
                    neural_network7.train(mile_to_quarter_inputs, mile_to_quarter_outputs, 5000)
                    self.outputs = neural_network7.think(int(raceTime))
                elif (endDistance == 800):
                    neural_network8.train(mile_to_half_inputs, mile_to_half_outputs, 5000)
                    self.outputs = neural_network8.think(int(raceTime))
                elif (endDistance == 5000):
                    neural_network9.train(mile_to_5k_inputs, mile_to_5k_outputs, 5000)
                    self.outputs = neural_network9.think(int(raceTime))
                
            elif (self.firstEvent == 5000):
                if (endDistance == 400):   
                    neural_network10.train(fivek_to_quarter_inputs, fivek_to_quarter_outputs, 5000)
                    self.outputs = neural_network10.think(int(raceTime))
                elif (endDistance == 800):
                    neural_network11.train(fivek_to_half_inputs, fivek_to_half_outputs, 5000)
                    self.outputs = neural_network11.think(int(raceTime))
                elif (endDistance == 1600):
                    neural_network12.train(fivek_to_mile_inputs, fivek_to_mile_outputs, 5000)
                    self.outputs = neural_network12.think(int(raceTime))
            
            #convert to minutes and seconds
            if (str(math.floor((self.outputs - self.outputs % 60) / 60)) == "0"):
                self.fulloutputs = "Your time would be " + str(math.ceil(self.outputs % 60)) + " seconds"
            else:
                self.fulloutputs = "Your time would be " + str(math.floor((self.outputs - self.outputs % 60) / 60)) + " Minutes and " + str(math.ceil(self.outputs % 60)) + " seconds"
            self.label2 = tk.Label(text=self.fulloutputs, bg="green", fg="black")
            self.label2.grid(row = 5, column = 0, sticky="w")
            
            #improve ai
            self.label3 = tk.Label(text="Input your actual time to help us improve our ai", bg="green", fg="black")
            self.label3.grid(row = 7, column = 0, sticky="w")
            
            self.realTimeMinutes = tk.Label(text="Minutes", bg="green", fg="black")
            self.realTimeMinutes.grid(row = 8, column = 1, sticky="w")
        
            self.realTimeInputMinutes = tk.Entry(bg="white", fg="black")
            self.realTimeInputMinutes.grid(row=8, column=2, sticky="w")
        
            self.realTimeSeconds = tk.Label(text="Seconds", bg="green", fg="black")
            self.realTimeSeconds.grid(row = 8, column = 3, sticky="w")
        
            self.realTimeInputSeconds = tk.Entry(bg="white", fg="black")
            self.realTimeInputSeconds.grid(row=8, column=4, sticky="w")
            submitRealTime = tk.Button(text="Submit", width=10, height=2, bg="blue", command= lambda : self.improveAI(self.firstEvent, raceTime, endDistance))
            submitRealTime.grid(row=8, column=5, sticky="e")
            
        except:
            print("Please enter a valid number")

#read data file
a_file = open("./data.json", "r")
json_object = json.load(a_file)
a_file.close()


#training data
half_to_mile_inputs = np.array(json_object["half_to_mile_inputs"])
half_to_mile_outputs = np.array(json_object["half_to_mile_outputs"])

half_to_5k_inputs = np.array(json_object["half_to_5k_inputs"])
half_to_5k_outputs = np.array(json_object["half_to_5k_outputs"])

half_to_quarter_inputs = np.array(json_object["half_to_quarter_inputs"])
half_to_quarter_outputs = np.array(json_object["half_to_quarter_outputs"])

quarter_to_800_inputs = np.array(json_object["quarter_to_800_inputs"])
quarter_to_800_outputs = np.array(json_object["quarter_to_800_outputs"])

quarter_to_5k_inputs = np.array(json_object["quarter_to_5k_inputs"])
quarter_to_5k_outputs = np.array(json_object["quarter_to_5k_outputs"])

quarter_to_mile_inputs = np.array(json_object["quarter_to_mile_inputs"])
quarter_to_mile_outputs = np.array(json_object["quarter_to_mile_outputs"])

mile_to_5k_inputs = np.array(json_object["mile_to_5k_inputs"])
mile_to_5k_outputs = np.array(json_object["mile_to_5k_outputs"])

mile_to_quarter_inputs = np.array(json_object["mile_to_quarter_inputs"])
mile_to_quarter_outputs = np.array(json_object["mile_to_quarter_outputs"])

mile_to_half_inputs = np.array(json_object["mile_to_half_inputs"])
mile_to_half_outputs = np.array(json_object["mile_to_half_outputs"])

fivek_to_mile_inputs = np.array(json_object["fivek_to_mile_inputs"])
fivek_to_mile_outputs = np.array(json_object["fivek_to_mile_outputs"])

fivek_to_half_inputs = np.array(json_object["fivek_to_half_inputs"])
fivek_to_half_outputs = np.array(json_object["fivek_to_half_outputs"])

fivek_to_quarter_inputs = np.array(json_object["fivek_to_quarter_inputs"])
fivek_to_quarter_outputs = np.array(json_object["fivek_to_quarter_outputs"])

currentText = messaging()

window.mainloop()