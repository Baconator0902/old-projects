from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Oh no secret key
    app.config['SECRET_KEY'] = 'jkfdashghiuogeharwu'
    
    from .views import views
    from .auth import auth
    from .runningForm import runningForm
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(runningForm, url_prefix="/")
    
    return app