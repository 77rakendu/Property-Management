# app/routes.py
from flask import render_template, redirect, url_for, request
from app import app, db
from app.models import User, Property, Inquiry
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
def home():
    return "Welcome to the Real Estate Management System!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('home'))
        flash('Login failed. Check your email and/or password', 'danger')
    return render_template('login.html')
    # Handle user login here
    return "Login Page"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method='sha256')
        user = User(username=username, email=email, password_hash=hashed_password, role='Buyer')
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')
    # Handle user registration here
    return "Register Page"

# app/routes.py
@app.route('/add_property', methods=['GET', 'POST'])
@login_required
def add_property():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        price = request.form.get('price')
        location = request.form.get('location')
        size = request.form.get('size')
        agent_id = current_user.id
        property = Property(title=title, description=description, price=price, location=location, size=size, agent_id=agent_id)
        db.session.add(property)
        db.session.commit()
        flash('Property added successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('add_property.html')


# app/routes.py
@app.route('/property/<int:property_id>')
def view_property(property_id):
    property = Property.query.get_or_404(property_id)
    return render_template('view_property.html', property=property)


# app/routes.py
@app.route('/inquire/<int:property_id>', methods=['POST'])
@login_required
def inquire(property_id):
    message = request.form.get('message')
    inquiry = Inquiry(property_id=property_id, buyer_id=current_user.id, message=message, status='Pending')
    db.session.add(inquiry)
    db.session.commit()
    flash('Inquiry sent successfully!', 'success')
    return redirect(url_for('view_property', property_id=property_id))



