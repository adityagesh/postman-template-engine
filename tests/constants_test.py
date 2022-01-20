from importlib_metadata import re
from postmanrenderer.constants import APP, POSTMAN


def test_postman_constants():
    assert type(POSTMAN.schema) == str and len(POSTMAN.schema) > 0


def test_app_constants():
    assert type(APP.root_dir) == str and re.match(r"\.\/\w+\/", APP.root_dir)
    assert type(APP.template_dir) == str and re.match(
        r"^\w+\/", APP.template_dir)
    assert type(APP.collections_template) == str and len(
        APP.collections_template) > 0
