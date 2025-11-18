# app/controllers/hadith_controller.py
import requests
from flask import jsonify

def get_random_hadith():
    try:
        # Example API: https://api.sunnah.com/v1/hadiths/random

        response = requests.get("https://api.sunnah.com/v1/hadiths/random")  
        if response.status_code == 200:
            data = response.json()
            # Adjust based on API structure
            hadith_text = data.get("hadith", {}).get("text", "No Hadith found")
            reference = data.get("hadith", {}).get("reference", "")
            return jsonify({"hadith": hadith_text, "reference": reference})
        else:
            return jsonify({"error": "Could not fetch hadith"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500