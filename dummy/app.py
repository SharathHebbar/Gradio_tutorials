from flask import Flask, render_template, request, redirect, url_for, session
import gradio as gr

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a secure secret key

# Mock user database (replace with a real database in production)
users = {"user1": "password1", "user2": "password2"}

# Gradio interface
def greet(name):
    return f"Hello, {name}!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")

# Web routes
@app.route('/')
def home():
    if 'username' in session:
        return f'Logged in as {session["username"]} | <a href="/logout">Logout</a>'
    return 'You are not logged in | <a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Run Flask app in the main thread
    iface.launch()
    app.run(debug=True)
