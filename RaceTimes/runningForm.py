from flask import Blueprint, render_template, request, flash, json, url_for
from typing import Text
import numpy as np
import tkinter as tk
import math
import json
import os

# & C:/Users/lucas/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/lucas/Documents/TSA/RaceTimes Website/main.py"

runningForm = Blueprint('runningForm', __name__)

@runningForm.route('/runningForm', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        videoSource = request.form.get('video')
        return render_template('runningForm.html', videoSource=videoSource)
    else:
        return render_template('runningForm.html', videoSource="static/stockRunning.mp4")
