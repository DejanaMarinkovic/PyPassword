from flask import Flask, render_template, request
import random
import string
import secrets

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password_route():
    # Pozivamo funkciju generate_password() i dobijamo rezultat
    password = generate_password()

    # Vraćamo rezultat kao odgovor na HTTP zahtev
    return render_template('index.html', password=password)

def generate_password():
    letters = int(request.form['letters'])
    symbols = int(request.form['symbols'])
    numbers = int(request.form['numbers'])

    full_password = []

    for _ in range(letters):
        full_password.append(secrets.choice(string.ascii_letters))
    for _ in range(symbols):
        full_password.append(secrets.choice(string.punctuation))
    for _ in range(numbers):
        full_password.append(secrets.choice(string.digits))

    random.shuffle(full_password)
    password = "".join(full_password)

    return password

if __name__ == '__main__':
    app.run(debug=True)


