from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "502159ce418d8161680033dc86229d6c"

@app.route("/", methods=["GET", "POST"])
def home():

    weather_data = []
    same_weather = {}

    if request.method == "POST":
        cities = request.form["cities"].split(",")

        for city in cities:
            city = city.strip()

            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

            response = requests.get(url)
            data = response.json()

            if data["cod"] == 200:
                weather_data.append({
                    "city": data["name"],
                    "temp": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "weather": data["weather"][0]["main"]
                })
                weather = data["weather"][0]["main"]

                if weather not in same_weather:
                    same_weather[weather] = []

                same_weather[weather].append(data["name"])


    return render_template(
    "index.html",
    weather_data=weather_data,
    same_weather=same_weather
)
if __name__ == "__main__":
    app.run(debug=True)