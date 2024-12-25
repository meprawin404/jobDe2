from flask import Flask,render_template, url_for, jsonify
from database import load_jobs_from_db

app = Flask(__name__, template_folder='templates')



@app.route('/')
def index():
    jobs = load_jobs_from_db();
    return render_template('index.html', jobs = jobs)

@app.route('/api/jobs')
def jobs():
    JOBS = load_jobs_from_db();
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
