from flask import Blueprint, render_template, request
from app.controllers.prayer_controller import get_prayer_times

prayer_bp = Blueprint("prayer", __name__)

@prayer_bp.route("/prayer", methods=["GET", "POST"])
def prayer():
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
        result, error_message = get_prayer_times(city, country, method_name)
        if result:
            prayer_times = result["timings"]
            hijri_date = result["hijri"]

    return render_template(
        "prayer.html",
        prayer_times=prayer_times,
        hijri_date=hijri_date,
        city=city,
        country=country,
        method_name=method_name,
        error_message=error_message
    )