from postmanrenderer.main import Request, Script, Url
from postmanrenderer.constants import HTTP_METHOD, Script_Type


def test_postman_script():
    script = Script(Script_Type.prerequest, "tests/data/post-request.js")
    assert script.script == ['console.log("done")']


def test_postman_request():
    request = Request("Google request", HTTP_METHOD.GET,
                      "test", Url("https://www.google.com"))
    request.add_header("Content-Type", "Application/json")
    pre_script = Script(Script_Type.prerequest, "tests/data/pre-request.js")
    request.add_script(pre_script)
    request.add_script(Script(Script_Type.test,
                       "tests/data/post-request.js"))

    assert request.method == HTTP_METHOD.GET
    assert request.name == "Google request"
    assert request.description == "test"
    assert request.url.host == ['www', 'google', 'com']
    assert request.headers["Content-Type"] == "Application/json"
    assert request.events[Script_Type.test].script_type == Script_Type.test
    assert request.events[Script_Type.test].script == ['console.log("done")']
