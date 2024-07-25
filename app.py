from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
API_KEY = '190bc3d516a1b3282acb89940466211a'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        complete_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(complete_url)
        weather_data = response.json()
        
        if weather_data['cod'] == 200: #which means that the data is successfully retrieved
            weather = {
                'city': weather_data['name'],
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon'],
                'humidity': weather_data['main']['humidity'],
                'wind': weather_data['wind']['speed'],
            }
            return render_template('index.html', weather=weather)
        else:
            error = "City not found"
            return render_template('index.html', error=error)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)