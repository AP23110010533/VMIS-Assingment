from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'secretkey123'

# Temporary storage for feedback
feedback_data = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback_form.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    message = request.form['feedback']

    if not name or not email or not message:
        flash("All fields are required.", "error")
    elif '@' not in email:
        flash("Invalid email address.", "error")
    else:
        feedback_data.append({'name': name, 'email': email, 'message': message})
        flash("Feedback submitted successfully!", "success")

    return redirect('/feedback')
