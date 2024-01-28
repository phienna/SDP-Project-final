from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    from flaskr.view import index
    app.register_blueprint(index.bp)

    from flaskr.view import cpu
    app.register_blueprint(cpu.bp)

    from flaskr.view import disk
    app.register_blueprint(disk.bp)

    from flaskr.view import config
    app.register_blueprint(config.bp)

    return app
