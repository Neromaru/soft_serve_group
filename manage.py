from app.app import app

from flask_script import Manager

manager = Manager(app)


@manager.option('-p', '--port', dest='port', default=5000)
@manager.option('-h', '--host', dest='host', default='127.0.0.1')
@manager.option('-d', '--debug', dest='debug', default=False)
def runserver(host, port, debug):
    app.run(host=host, port=port, debug=debug)


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()