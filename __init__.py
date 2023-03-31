from flask import Flask

app = Flask(__name__)

from main import main as main_blueprint
from errors import error_bp as error_blueprint

app.register_blueprint(main_blueprint)
app.register_blueprint(error_blueprint)
if __name__ == "__main__":
    app.run(debug=True)
