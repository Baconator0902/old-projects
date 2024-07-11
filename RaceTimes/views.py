from flask import Blueprint, render_template, request, flash, json, url_for
from typing import Text
import numpy as np
import tkinter as tk
import math
import json
import os

# & C:/Users/lucas/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/lucas/Documents/TSA/RaceTimes Website/main.py"

views = Blueprint('views', __name__)

@views.route('/views', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form["submitNumber"] == "1":
            data = request.form
            print(data)
            
            minutes = request.form.get('minutes')
            seconds = request.form.get('seconds')
            
            firstEvent = request.form.get('firstRace')
            endDistance = request.form.get('secondRace')
            
            if minutes.isnumeric() and seconds.isnumeric():
                raceTime = (int(minutes) * 60) + int(seconds)
                if firstEvent == endDistance:
                    flash('Choose different distances', category='error')
                    return render_template('race.html')
                else:
                    flash('Submitted correctly!', category='success')
                    
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
                            self.firstEvent = firstEvent
                            
                        def usertimes(self):
                            
                            try:
                                #train
                                if (self.firstEvent == '400 meter'):
                                    if (endDistance == '800 meter'):
                                        neural_network1.train(quarter_to_800_inputs, quarter_to_800_outputs, 5000)
                                        self.outputs = neural_network1.think(int(raceTime))
                                        
                                    elif (endDistance == '1600 meter'):
                                        neural_network2.train(quarter_to_mile_inputs, quarter_to_mile_outputs, 5000)
                                        self.outputs = neural_network2.think(int(raceTime))
                                    elif (endDistance == '5k'):
                                        neural_network3.train(quarter_to_5k_inputs, quarter_to_5k_outputs, 5000)
                                        self.outputs = neural_network3.think(int(raceTime))
                                        
                                elif (self.firstEvent == '800 meter'):
                                    if (endDistance == '400 meter'):   
                                        neural_network4.train(half_to_quarter_inputs, half_to_quarter_outputs, 5000)
                                        self.outputs = neural_network4.think(int(raceTime))
                                    elif (endDistance == '1600 meter'):
                                        neural_network5.train(half_to_mile_inputs, half_to_mile_outputs, 5000)
                                        self.outputs = neural_network5.think(int(raceTime))
                                    elif (endDistance == '5k'):
                                        neural_network6.train(half_to_5k_inputs, half_to_5k_outputs, 5000)
                                        self.outputs = neural_network6.think(int(raceTime))

                                elif (self.firstEvent == '1600 meter'):
                                    if (endDistance == '400 meter'):   
                                        neural_network7.train(mile_to_quarter_inputs, mile_to_quarter_outputs, 5000)
                                        self.outputs = neural_network7.think(int(raceTime))
                                    elif (endDistance == '800 meter'):
                                        neural_network8.train(mile_to_half_inputs, mile_to_half_outputs, 5000)
                                        self.outputs = neural_network8.think(int(raceTime))
                                        print("here")
                                    elif (endDistance == '5k'):
                                        neural_network9.train(mile_to_5k_inputs, mile_to_5k_outputs, 5000)
                                        self.outputs = neural_network9.think(int(raceTime))
                                    
                                elif (self.firstEvent == '5k'):
                                    if (endDistance == '400 meter'):   
                                        neural_network10.train(fivek_to_quarter_inputs, fivek_to_quarter_outputs, 5000)
                                        self.outputs = neural_network10.think(int(raceTime))
                                    elif (endDistance == '800 meter'):
                                        neural_network11.train(fivek_to_half_inputs, fivek_to_half_outputs, 5000)
                                        self.outputs = neural_network11.think(int(raceTime))
                                    elif (endDistance == '1600 meter'):
                                        neural_network12.train(fivek_to_mile_inputs, fivek_to_mile_outputs, 5000)
                                        self.outputs = neural_network12.think(int(raceTime))
                                
                                #convert to minutes and seconds
                                if (str(math.floor((self.outputs - self.outputs % 60) / 60)) == "0"):
                                    secondsToOutput = math.ceil(self.outputs % 60)
                                    if secondsToOutput < 10:
                                        return "0" + str(secondsToOutput) + " seconds"
                                    else:
                                        return str(secondsToOutput) + " seconds"
                                else:
                                    secondsToOutput = math.ceil(self.outputs % 60)
                                    minutesToOutput = math.floor((self.outputs - self.outputs % 60) / 60)
                                    if secondsToOutput == 60:
                                        secondsToOutput = secondsToOutput - 60
                                        minutesToOutput = minutesToOutput + 1
                                    if secondsToOutput < 10:
                                        return str(minutesToOutput) + ":" + "0" + str(secondsToOutput)
                                    else:
                                        return str(minutesToOutput) + ":" + str(secondsToOutput)
                                
                                
                            except:
                                print("Please enter a valid number")

                    #read data file
                    a_file = open("data.json", "r")
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
                    return render_template('firstSubmit.html', predictedTime=currentText.usertimes(), oldRaceTimeMinutes=minutes, oldRaceTimeSeconds=seconds, oldRace=firstEvent, newRace=endDistance)
                            
            else:
                flash('Make sure the time is valid', category='error')
                return render_template('race.html')
        else:
            def improveAI(oldRace, oldRaceTime, currentRace, realRaceTime):
                        
                        
                #change variable
                if (oldRace == '400 meter'):
                    if (currentRace == '800 meter'):
                        a_file = open("data.json", "r")
                        json_object = json.load(a_file)
                        a_file.close()
                        json_object["quarter_to_800_inputs"].append(oldRaceTime)
                        json_object["quarter_to_800_outputs"].append(realRaceTime)
                        a_file = open("data.json", "w")
                        json.dump(json_object, a_file)
                        a_file.close()
                    elif (currentRace == '1600 meter'):
                        a_file = open("data.json", "r")
                        json_object = json.load(a_file)
                        a_file.close()
                        json_object["quarter_to_mile_inputs"].append(oldRaceTime)
                        json_object["quarter_to_mile_outputs"].append(realRaceTime)
                        a_file = open("data.json", "w")
                        json.dump(json_object, a_file)
                        a_file.close()
                    elif (currentRace == '5k'):
                        a_file = open("data.json", "r")
                        json_object = json.load(a_file)
                        a_file.close()
                        json_object["quarter_to_5k_inputs"].append(oldRaceTime)
                        json_object["quarter_to_5k_outputs"].append(realRaceTime)
                        a_file = open("data.json", "w")
                        json.dump(json_object, a_file)
                        a_file.close()
                                    
                elif (oldRace == '800 meter'):
                    if (currentRace == '400 meter'):
                        a_file = open("data.json", "r")
                        json_object = json.load(a_file)
                        a_file.close()
                        json_object["half_to_quarter_inputs"].append(oldRaceTime)
                        json_object["half_to_quarter_outputs"].append(realRaceTime)
                        a_file = open("data.json", "w")
                        json.dump(json_object, a_file)
                        a_file.close()
                    elif (currentRace == '1600 meter'):
                        a_file = open("data.json", "r")
                        json_object = json.load(a_file)
                        a_file.close()
                        json_object["half_to_mile_inputs"].append(oldRaceTime)
                        json_object["half_to_mile_outputs"].append(realRaceTime)
                        a_file = open("data.json", "w")
                        json.dump(json_object, a_file)
                        a_file.close()
                    elif (currentRace == '5k'):
                        a_file = open("data.json", "r")
                        json_object = json.load(a_file)
                        a_file.close()
                        json_object["half_to_5k_inputs"].append(oldRaceTime)
                        json_object["half_to_5k_outputs"].append(realRaceTime)
                        a_file = open("data.json", "w")
                        json.dump(json_object, a_file)
                        a_file.close()

                elif (oldRace == '1600 meter'):
                    if (currentRace == '400 meter'):
                        a_file = open("data.json", "r")
                        json_object = json.load(a_file)
                        a_file.close()
                        json_object["mile_to_quarter_inputs"].append(oldRaceTime)
                        json_object["mile_to_quarter_outputs"].append(realRaceTime)
                        a_file = open("data.json", "w")
                        json.dump(json_object, a_file)
                        a_file.close()
                    elif (currentRace == '800 meter'):
                        a_file = open("data.json", "r")
                        json_object = json.load(a_file)
                        a_file.close()
                        json_object["mile_to_half_inputs"].append(oldRaceTime)
                        json_object["mile_to_half_outputs"].append(realRaceTime)
                        a_file = open("data.json", "w")
                        json.dump(json_object, a_file)
                        a_file.close()
                    elif (currentRace == '5k'):
                        a_file = open("data.json", "r")
                        json_object = json.load(a_file)
                        a_file.close()
                        json_object["mile_to_5k_inputs"].append(oldRaceTime)
                        json_object["mile_to_5k_outputs"].append(realRaceTime)
                        a_file = open("data.json", "w")
                        json.dump(json_object, a_file)
                        a_file.close()
                                
                elif (oldRace == '5k'):
                    if (currentRace == '400 meter'):
                        a_file = open("data.json", "r")
                        json_object = json.load(a_file)
                        a_file.close()
                        json_object["fivek_to_quarter_inputs"].append(oldRaceTime)
                        json_object["fivek_to_quarter_outputs"].append(realRaceTime)
                        a_file = open("data.json", "w")
                        json.dump(json_object, a_file)
                        a_file.close()
                    elif (currentRace == '800 meter'):
                        a_file = open("data.json", "r")
                        json_object = json.load(a_file)
                        a_file.close()
                        json_object["fivek_to_half_inputs"].append(oldRaceTime)
                        json_object["fivek_to_half_outputs"].append(realRaceTime)
                        a_file = open("data.json", "w")
                        json.dump(json_object, a_file)
                        a_file.close()
                    elif (currentRace == '1600 meter'):
                        a_file = open("data.json", "r")
                        json_object = json.load(a_file)
                        a_file.close()
                        json_object["fivek_to_mile_inputs"].append(oldRaceTime)
                        json_object["fivek_to_mile_outputs"].append(realRaceTime)
                        a_file = open("data.json", "w")
                        json.dump(json_object, a_file)
                        a_file.close()
            oldRaceTimeMinutes = request.form.get('oldRaceTimeMinutes')
            oldRaceTimeSeconds = request.form.get('oldRaceTimeSeconds')
            oldRaceTime = (int(oldRaceTimeMinutes) * 60) + int(oldRaceTimeSeconds)
            oldRace = request.form.get('oldRace')
            
            currentRace = request.form.get('newRace')
            currentRaceTimeMinutes = request.form.get('minutes')
            currentRaceTimeSeconds = request.form.get('seconds')
            currentRaceTime = (int(currentRaceTimeMinutes) * 60) + int(currentRaceTimeSeconds)
            
            print(str(oldRace)  + " " + str(oldRaceTime)  + " " + str(currentRace) + " " +  str(currentRaceTime))
            improveAI(oldRace, oldRaceTime, currentRace, currentRaceTime)
            flash('Thank you for helping us improve our AI!', category='success')
            return render_template('race.html')
    else:
        return render_template('race.html')
