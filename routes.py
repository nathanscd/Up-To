from flask import render_template, request, redirect, url_for, flash
from app import app, db
from models import Event, Activity
from datetime import datetime

@app.route('/')
def index():
    events = Event.query.all()
    return render_template('index.html', events=events)

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        title = request.form['title']
        activity_id = request.form['activity']
        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])
        start_time = datetime.fromisoformat(request.form['start_time'])
        end_time = datetime.fromisoformat(request.form['end_time'])

        new_event = Event(
            title=title,
            activity_id=activity_id,
            latitude=latitude,
            longitude=longitude,
            start_time=start_time,
            end_time=end_time,
            creator_id=1
        )
        db.session.add(new_event)
        db.session.commit()
        flash("Evento criado com sucesso!", "success")
        return redirect(url_for('index'))

    activities = Activity.query.all()
    return render_template('create_event.html', activities=activities)
