from flask import Flask, request
from functions import astronaut as ast, launch as lnc, launcher as lcr

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "hello world"


    @app.route("/astronauts/search", methods=["GET"])
    def astro_search():
        return ast.astronaut_search(request.args)


    @app.route("/astronauts/<variable>/<value>", methods=["GET"])
    def astro_get(variable, value):
        return ast.astronaut_get(variable, value)


    @app.route("/astronauts", methods=["GET"])
    def astro_get_all():
        return ast.astronaut_get_all()


    @app.route("/astronauts", methods=["POST"])
    def astro_post():
        if request.is_json:
            return ast.astronaut_post(request)
        return {"error": "Request must be JSON"}, 415


    @app.route("/astronauts/<variable>/'<value>'", methods=["DELETE"])
    def astro_delete(variable, value):
        return ast.astronaut_delete(variable, value)


    @app.route("/astronauts/<variable>/'<value>'", methods=["PUT"])
    def astro_update(variable, value):
        return ast.astronaut_update(variable, value, request)


    @app.route("/launchers/search", methods=["GET"])
    def launcher_search():
        return lcr.launcher_search(request.args)


    @app.route("/launchers/<variable>/<value>", methods=["GET"])
    def launcher_get(variable, value):
        return lcr.launcher_get(variable, value)


    @app.route("/launchers", methods=["GET"])
    def launcher_get_all():
        return lcr.launcher_get_all()


    @app.route("/launchers", methods=["POST"])
    def launcher_post():
        if request.is_json:
            return lcr.launcher_post(request)
        return {"error": "Request must be JSON"}, 415


    @app.route("/launchers/<variable>/'<value>'", methods=["DELETE"])
    def launcher_delete(variable, value):
        return lcr.launcher_delete(variable, value)


    @app.route("/launchers/<variable>/'<value>'", methods=["PUT"])
    def launcher_update(variable, value):
        return lcr.launcher_update(variable, value, request)


    @app.route("/launches/search", methods=["GET"])
    def launch_search():
        return lnc.launch_search(request.args)


    @app.route("/launches/<variable>/<value>", methods=["GET"])
    def launch_get(variable, value):
        return lnc.launch_get(variable, value)


    @app.route("/launches", methods=["GET"])
    def launch_get_all():
        return lnc.launch_get_all()


    @app.route("/launches", methods=["POST"])
    def launch_post():
        if request.is_json:
            return lnc.launch_post(request)
        return {"error": "Request must be JSON"}, 415


    @app.route("/launches/<variable>/'<value>'", methods=["DELETE"])
    def launch_delete(variable, value):
        return lnc.launch_delete(variable, value)


    @app.route("/launches/<variable>/'<value>'", methods=["PUT"])
    def launch_update(variable, value):
        return lnc.launch_update(variable, value, request)

    app.run(debug=True, port=4533)
