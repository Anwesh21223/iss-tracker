from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://api.wheretheiss.at/v1/satellites/25544')
    data = response.json()

    latitude = data['latitude']
    longitude = data['longitude']

    return render_template('index.html', lat=latitude, lon=longitude)

if __name__ == '__main__':
    app.run(debug=True)