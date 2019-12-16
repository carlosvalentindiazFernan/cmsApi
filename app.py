
from cms_api import create_app, app_config

app = create_app()

if __name__ == "__main__":

    app.run(debug=app_config(app,'DEBUG',False), 
        host=app_config(app,'HOST','localhost'), 
        port=app_config(app,'PORT',5000))