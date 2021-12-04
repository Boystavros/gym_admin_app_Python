from flask import Flask, render_template

from controllers.member_controller import members_blueprint
from controllers.fit_class_controller import fit_classes_blueprint
from controllers.booking_controller import bookings_blueprint
import repositories.fit_class_repository as fit_class_repository

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(fit_classes_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route('/')
def home():
    fit_classes = fit_class_repository.select_all()
    return render_template('index.html', fit_classes=fit_classes)

if __name__ == '__main__':
    app.run(debug=True)