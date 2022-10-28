from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Movie
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        movie = request.form.get('movie')

        if len(movie) < 1:
            flash('Movie is too short!', category='error')
        else:
            new_movie = Movie(data=movie, user_id=current_user.id)
            db.session.add(new_movie)
            db.session.commit()
            flash('Movie added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-movie', methods=['POST'])
def delete_movie():
    movie = json.loads(request.data)
    movieId = movie['movieId']
    movie = Movie.query.get(movieId)
    if movie:
        if movie.user_id == current_user.id:
            db.session.delete(movie)
            db.session.commit()

    return jsonify({})