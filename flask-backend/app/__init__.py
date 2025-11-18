from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import blueprints
    from app.routes.prayer_route import prayer_bp
    from app.routes.hadith_route import hadith_bp
    # from app.routes.quiz_route import quiz_bp

    # Register blueprints
    app.register_blueprint(prayer_bp)
    app.register_blueprint(hadith_bp)
    # app.register_blueprint(quiz_bp)

    return app