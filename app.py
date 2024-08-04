from flask import Flask , render_template



app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/templates/projects.html')
def projects():
    return render_template('projects.html')

@app.route('/templates/skills.html')
def skills():
    return render_template('skills.html')

if __name__ == "__main__":
    app.run(debug=True)