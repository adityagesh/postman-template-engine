from importlib_metadata import re
from postmanrenderer.constants import APP, POSTMAN, HTTP_METHOD, BODY_MODE, Language


def test_postman_constants():
    assert type(POSTMAN.schema) == str and len(POSTMAN.schema) > 0


def test_app_constants():
    assert type(APP.root_dir) == str and re.match(r"\.\/\w+\/", APP.root_dir)
    assert type(APP.template_dir) == str and re.match(
        r"^\w+\/", APP.template_dir)
    assert type(APP.collections_template) == str and len(
        APP.collections_template) > 0


def test_http_method_constants():
    assert HTTP_METHOD.GET == "GET"
    assert HTTP_METHOD.POST == "POST"
    assert HTTP_METHOD.PUT == "PUT"


def test_body_mode_constants():
    assert BODY_MODE.formdata == "formdata"
    assert BODY_MODE.urlencoded == "urlencoded"
    assert BODY_MODE.file == "file"
    assert BODY_MODE.raw == "raw"


def test_language_constants():
    assert Language.html == "html"
    assert Language.javascript == "javascript"
    assert Language.json == "json"
    assert Language.text == "text"
