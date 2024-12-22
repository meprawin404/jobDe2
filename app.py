from flask import Flask,render_template, url_for, jsonify

app = Flask(__name__, template_folder='templates')


JOBS = [
    {
        'id':1,
        'title':'Data Analyst',
        'location': 'kathmandu',
        'salary': "10,00,000"
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location': 'Pokhara',
        'salary': "15,00,000"
    },
    {
        'id':3,
        'title':'Backend Engineer',
        'location': 'Janakpur',
        'salary': "13,00,000"
    },
    {
        'id':4,
        'title':'Frontend Engineer',
        'location': 'Hetauda',
    }

]

@app.route('/')
def index():
    return render_template('index.html', jobs = JOBS)

@app.route('/api/jobs')
def jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
