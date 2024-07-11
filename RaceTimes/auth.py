from flask import Blueprint, render_template, request, flash, json, url_for
from typing import Text
import numpy as np
import tkinter as tk
import math
import json
import os

auth = Blueprint('auth', __name__)

@auth.route('')
def home():
    return render_template('home.html')

@auth.route('home')
def login():
    return render_template('home.html')

@auth.route('logout')
def logout():
    return render_template('logout.html')

@auth.route('sign-up')
def signUp():
    return render_template('sign-up.html')