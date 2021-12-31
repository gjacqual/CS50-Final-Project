# add the ability to work with operation system
import os

# add the ability to work with databases
from cs50 import SQL

# add flask framework 
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

# Generate temporary files and directories
from tempfile import mkdtemp

# add module for puthon exceptions
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

# add a set of tools for hashing and creating passwords in the application 
from werkzeug.security import check_password_hash, generate_password_hash

