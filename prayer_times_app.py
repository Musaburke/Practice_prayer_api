from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prayer_times = None
    city = None
    country = None

    if request.method == "POST":
        city = request.form.get("city")
        country = request.form.get("country")

        # Call AlAdhan API
        url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            prayer_times = data["data"]["timings"]
        else:
            prayer_times = {"Error": "Could not fetch prayer times"}

    return render_template("index.html", prayer_times=prayer_times, city=city, country=country)

if __name__ == "__main__":
    app.run(debug=True)