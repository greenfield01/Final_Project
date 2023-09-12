import csv
from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Ailment

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/display_ailments')
def display_ailments():
    # Query the User table to retrieve all records
    """ ailment = Ailment.query.all()

    if ailment is not None:
        ailment_data = {
            'id': ailment.id,
            'ailment_name': ailment.ailment_name,
            'symptoms': ailment.symptoms,
            'causes': ailment.causes,
            'effects': ailment.effectes,
            'natural_treatments': ailment.natural_treatments,
            'drugs': ailment.drugs,
            'diets': ailment.diets,
            'exercise': ailment.exercise
        } """
    ailments = Ailment.query.all()  

    return render_template('ailments.html', ailments=ailments)


@main.route('/update_ailment', methods=['GET', 'POST'])
@login_required
def update_ailment():
    if request.method == 'POST':
        ailment_name = request.form['ailment']
        symptoms = request.form['symptoms']
        causes = request.form['causes']
        effects = request.form['effects']
        natural_treatments = request.form['natural_treatments']
        drugs = request.form['drugs']
        diets = request.form['diets']
        exercise = request.form['exercise']


        ailment = Ailment(
            ailment_name=ailment_name,
            symptoms=symptoms,
            causes=causes,
            effects=effects,
            natural_treatments=natural_treatments,
            drugs=drugs,
            diets=diets,
            exercise=exercise
        )

        db.session.add(ailment)
        db.session.commit()

        flash('Ailment added successfully!', 'success')
    
        return redirect(url_for('main.profile'))
    flash('Please update Ailments')
    return render_template('profile.html')
