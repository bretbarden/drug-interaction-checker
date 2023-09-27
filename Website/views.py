# Store standard roots in Wesbite (main directory)
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Bike
from . import db

views = Blueprint("views", __name__)



