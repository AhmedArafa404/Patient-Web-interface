from flask import Flask, render_template, request
from signup import SignupForm, SearchForm
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        nid = form.nid.data
        password = form.password.data

        conn = sqlite3.connect('patient.db')
        c = conn.cursor()
        c.execute("SELECT * FROM patients WHERE nid=?", (nid,))
        if c.fetchone():
            return "National ID already exists!"
        c.execute("INSERT INTO patients (name, email, nid, password) VALUES (?, ?, ?, ?)", 
                  (name, email, nid, password))
        conn.commit()
        conn.close()
        return "Signup successful!"
    return render_template('signup.html', form=form)

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        nid = form.nid.data
        conn = sqlite3.connect('patient.db')
        c = conn.cursor()
        c.execute("SELECT * FROM patients WHERE nid=?", (nid,))
        user = c.fetchone()
        conn.close()
        if user:
            return render_template('out.html', user=user)
        return "No record found"
    return render_template('search.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

