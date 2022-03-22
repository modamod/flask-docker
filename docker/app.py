
from flask import render_template, Flask, url_for, send_file
import os


app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    print(url_for('index'))
    return render_template("index.html")


port = int(os.environ.get('PORT', 5000))
app.run(debug=True, host='0.0.0.0', port=port)
