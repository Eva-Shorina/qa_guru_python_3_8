from selene.support.shared import browser
import os
import tests


def get_path(relative_path):
    abs_path = os.path.abspath(
        os.path.join(os.path.dirname(tests.__file__), relative_path))

    return abs_path

#get_path('resources\pic.jpg')
