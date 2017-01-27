from AngularFlask import app
import Configuration as cfg

def RunServer():
    app.run(host='0.0.0.0', port=cfg.SERVER_PORT)

if __name__ == '__main__':
    RunServer()
