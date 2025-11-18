import requests

METHODS = {
    "Muslim World League": 3,
    "ISNA": 2,
    "Egyptian": 5,
    "Makkah": 4,
    "Karachi": 1,
    "Tehran": 7
}

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

def get_prayer_times(city, country, method_name):
    method = METHODS.get(method_name, 2)

    if not city or not country:
        return None, "Please enter both a city and a country."
    elif country.lower() not in VALID_COUNTRIES:
        return None, f"Country '{country}' not recognized."

    try:
        url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method={method}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and data.get("code") == 200:
            timings = data.get("data", {}).get("timings")
            hijri = data.get("data", {}).get("date", {}).get("hijri", {}).get("date")
            if timings and hijri:
                return {"timings": timings, "hijri": hijri}, None
        return None, "Could not fetch prayer times. Check your city/country."
    except Exception:
        return None, "An error occurred while fetching prayer times."