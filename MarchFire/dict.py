import os

import csv

import json

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
fault = ''
remedy = ''
fault=db.execute("SELECT fault FROM doorfixes WHERE fault_id = 5",
                    )
remedy=db.execute("SELECT remedy FROM doorfixes WHERE fault_id = 5",
                    )
ic(remedy)
ic(fault)
ic(type(remedy))
ic(type(fault))

        #rows=dict(remedy,)  this did not work
        #ic(type(rows))
        # fault=str(fault)
        # remedy=str(remedy)