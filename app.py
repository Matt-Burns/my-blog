import flaskr


def create_app(test_config=None):
    print(test_config)
    return flaskr.create_app(test_config)
