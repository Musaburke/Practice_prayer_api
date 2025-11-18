from flask import Blueprint
from app.controllers.hadith_controller import get_random_hadith

hadith_bp = Blueprint("hadith", __name__, url_prefix="/api/hadith")

@hadith_bp.route("/random", methods=["GET"])
def random_hadith():
    return get_random_hadith()