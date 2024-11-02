import os

import csv

import json

import sqlite3

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from icecream import ic

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)



db = SQL("sqlite:///final.db")
    #trouble trying to get the data from the databases to use in the next db.execute to produce the RESULTS
conn = sqlite3.connect('final.db')

fault = ''
remedy = ''
faultDict = ()
faultStr = {}

remedyDict = ()
remedyStr = {}
fault=db.execute("SELECT fault FROM doorfixes WHERE fault_id = 5",
                    )
remedy=db.execute("SELECT remedy FROM doorfixes WHERE fault_id = 5",)

faultDict   = fault [0]
faultStr = faultDict  ['fault']

remedyDict = remedy [0]
remedyStr= remedyDict  ['remedy']

ic(faultDict )
ic(type(faultDict))
ic(faultStr )
ic(type(faultStr))
ic(remedyDict )
ic(type(remedyDict ))
ic(remendyStr  )
ic(type(remendyStr ))
ic(remedy)
ic(fault)
ic(type(remedy))
ic(type(fault))
