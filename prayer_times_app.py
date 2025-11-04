from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

METHODS = {
    "Muslim World League": 3,
    "ISNA": 2,
    "Egyptian": 5,
    "Makkah": 4,
    "Karachi": 1,
    "Tehran": 7
}

@app.route("/", methods=["GET", "POST"])
def index():
    prayer_times = None
    hijri_date = None
    city = ""
    country = ""
    method_name = "ISNA"
    error_message = None

    if request.method == "POST":
        city = request.form.get("city")
        country = request.form.get("country")
        method_name = request.form.get("method", "ISNA")
        method = METHODS.get(method_name, 2)

        try:
            url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method={method}"
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200 and data["code"] == 200:
                prayer_times = data["data"]["timings"]
                hijri_date = data["data"]["date"]["hijri"]["date"]
            else:
                error_message = "Could not fetch prayer times. Check your city/country."
        except Exception as e:
            error_message = "An error occurred while fetching prayer times."

    return render_template(
        "index.html",
        prayer_times=prayer_times,
        hijri_date=hijri_date,
        city=city,
        country=country,
        method_name=method_name,
        error_message=error_message,
        methods=METHODS.keys()
    )

if __name__ == "__main__":
    app.run(debug=True)