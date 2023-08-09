from flask_app import app
from flask_app.controllers import controllers_dojo
from flask_app.controllers import controllers_ninja

if __name__=='__main__':
    app.run(debug=True)
