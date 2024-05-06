from flask import Blueprint, request, render_template, jsonify
from .services import find_resources

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    resources = []  # Initialize resources as an empty list
    if request.method == 'POST':
        problem = request.form.get('problem')
        location = request.form.get('location')
        if problem and location:  # Ensure both inputs are provided
            resources = find_resources(problem, location) or []  # Ensure resources is never None
    return render_template('index.html', resources=resources)

@bp.route('/about')
def about():
    return render_template('about.html')
