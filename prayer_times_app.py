from flask import Flask, render_template, request
import requests

app = Flask(__name__)

METHODS = {
    "Muslim World League": 3,
    "ISNA": 2,
    "Egyptian": 5,
    "Makkah": 4,
    "Karachi": 1,
    "Tehran": 7
}

# Static list of valid countries
VALID_COUNTRIES = {
    "afghanistan","albania","algeria","andorra","angola","antigua and barbuda","argentina",
    "armenia","australia","austria","azerbaijan","bahamas","bahrain","bangladesh","barbados",
    "belarus","belgium","belize","benin","bhutan","bolivia","bosnia and herzegovina",
    "botswana","brazil","brunei","bulgaria","burkina faso","burundi","cabo verde","cambodia",
    "cameroon","canada","central african republic","chad","chile","china","colombia","comoros",
    "congo","costa rica","croatia","cuba","cyprus","czech republic","denmark","djibouti",
    "dominica","dominican republic","ecuador","egypt","el salvador","equatorial guinea",
    "eritrea","estonia","eswatini","ethiopia","fiji","finland","france","gabon","gambia","georgia",
    "germany","ghana","greece","grenada","guatemala","guinea","guinea-bissau","guyana","haiti",
    "honduras","hungary","iceland","india","indonesia","iran","iraq","ireland","israel","italy",
    "jamaica","japan","jordan","kazakhstan","kenya","kiribati","kuwait","kyrgyzstan","laos",
    "latvia","lebanon","lesotho","liberia","libya","liechtenstein","lithuania","luxembourg",
    "madagascar","malawi","malaysia","maldives","mali","malta","marshall islands","mauritania",
    "mauritius","mexico","micronesia","moldova","monaco","mongolia","montenegro","morocco",
    "mozambique","myanmar","namibia","nauru","nepal","netherlands","new zealand","nicaragua",
    "niger","nigeria","north korea","north macedonia","norway","oman","pakistan","palau","palestine",
    "panama","papua new guinea","paraguay","peru","philippines","poland","portugal","qatar",
    "romania","russia","rwanda","saint kitts and nevis","saint lucia","saint vincent and the grenadines",
    "samoa","san marino","sao tome and principe","saudi arabia","senegal","serbia","seychelles",
    "sierra leone","singapore","slovakia","slovenia","solomon islands","somalia","south africa",
    "south korea","south sudan","spain","sri lanka","sudan","suriname","sweden","switzerland",
    "syria","taiwan","tajikistan","tanzania","thailand","timor-leste","togo","tonga","trinidad and tobago",
    "tunisia","turkey","turkmenistan","tuvalu","uganda","ukraine","united arab emirates",
    "united kingdom","united states","uruguay","uzbekistan","vanuatu","vatican city","venezuela",
    "vietnam","yemen","zambia","zimbabwe"
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
        city = request.form.get("city", "").strip()
        country = request.form.get("country", "").strip()
        method_name = request.form.get("method", "ISNA")
        method = METHODS.get(method_name, 2)

        # Basic input validation
        if not city or not country:
            error_message = "Please enter both a city and a country."
        elif not any(c.isalpha() for c in city):
            error_message = "City must contain at least one letter."
        elif not any(c.isalpha() for c in country):
            error_message = "Country must contain at least one letter."
        elif country.lower() not in VALID_COUNTRIES:
            error_message = f"Country '{country}' not recognized."
        else:
            try:
                # Call API
                url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method={method}"
                response = requests.get(url)
                data = response.json()

                # Check API response
                if response.status_code == 200 and data.get("code") == 200:
                    timings = data.get("data", {}).get("timings")
                    hijri = data.get("data", {}).get("date", {}).get("hijri", {}).get("date")

                    # Extra city validation
                    api_timezone = data.get("data", {}).get("meta", {}).get("timezone", "")
                    if api_timezone:
                        api_city = api_timezone.split('/')[-1].replace('_', ' ')
                        if api_city.lower() != city.lower():
                            error_message = f"City '{city}' not found. Did you mean '{api_city}'?"
                            timings = None
                            hijri = None

                    if timings and hijri:
                        prayer_times = timings
                        hijri_date = hijri
                    else:
                        if not error_message:
                            error_message = "Could not fetch prayer times. Check your city/country."
                else:
                    error_message = "City or country not recognized."
            except Exception:
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