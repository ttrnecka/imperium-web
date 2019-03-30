
# A very simple Flask Hello World app for you to get started with...
import sys
#sys.path.insert(0, '/home/trnecka/imperium-bot')
sys.path.insert(0, '../imperium-bot')

from coach import Coach

from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return render_template("index.html", coaches = Coach.all())

# run the application
if __name__ == "__main__":  
    app.run(debug=True)
