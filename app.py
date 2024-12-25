from flask import Flask,render_template, url_for, jsonify
from database import load_jobs_from_db, load_job_from_db


app = Flask(__name__, template_folder='templates')



@app.route('/')
def index():
    jobs = load_jobs_from_db();
    return render_template('index.html', jobs = jobs)

# needs some modification
@app.route('/api/jobs')
def jobs():
    JOBS = load_jobs_from_db();
    return jsonify(JOBS)


@app.route('/jobs/<id>')
def show_jobs(id):
    jobs = load_job_from_db(id)
    if not jobs:
        return "Not found", 404
    return render_template('jobpage.html', job = jobs)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
