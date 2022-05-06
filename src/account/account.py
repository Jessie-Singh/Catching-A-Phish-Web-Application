from wtforms.widgets.core import CheckboxInput
from src.adapters.memory_repo import MemoryRepository
from datetime import date

from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

from flask_wtf import FlaskForm
from wtforms import RadioField, TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

import src.adapters.repo as repo
import src.utilities.utilities as utilities
import src.utilities.services as services

from src.authentication.authentication import login_required 
from src.domain.model import User, Question

account_blueprint = Blueprint('account_bp', __name__)

@account_blueprint.route('/my_account', methods=['GET'])
def view_account():
    user_name = session['user_name']
    score = utilities.get_user_score(user_name)
   
    return render_template(
        'account/account.html',
        score = score
    )
