from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/olympians')
def olympians():
    return render_template('olympians.html')

# Add other routes for different pages

if __name__ == '__main__':
    app.run(debug=True)