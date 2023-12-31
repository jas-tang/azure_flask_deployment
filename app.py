from flask import Flask, render_template
import pandas as pd
import random

from faker import Faker
fake = Faker()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/random')
def randomgen():
    number_var = random.randint(1,1000000)
    fake_address = fake.address()
    return render_template('random.html', single_number = number_var, single_address = fake_address)

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA_504_2023/main/WK1/data/113243405_StonyBrookSouthamptonHospital_StandardCharges.csv')
@app.route('/data')
def data(data=df):
    data = data.sample(15)
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )