from postmanrenderer.constants import BODY_MODE,  HTTP_METHOD, Script_Type
from postmanrenderer.main import KeyValueData, KeyValueBody, RawBody, RequestBody, Request, Script, Url
import pytest


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


def test_formdata():
    keyvaluedata1 = KeyValueData("key1", "value1", "test1")
    keyvaluedata2 = KeyValueData("key2", "value2", "test2")
    keyvaluebody = KeyValueBody([keyvaluedata1, keyvaluedata2])
    assert keyvaluebody.to_json(
    ) == '[{"key": "key1", "value": "value1", "description": "test1", "type": "text"}, {"key": "key2", "value": "value2", "description": "test2", "type": "text"}]'


def test_rawbody():
    rawbody = RawBody("raw-data")
    assert rawbody.to_json() == 'raw-data'


def test_RequestBody_formdata():
    body = RequestBody(mode=BODY_MODE.formdata)
    assert body.mode == BODY_MODE.formdata
    with pytest.raises(Exception):
        body.addRawBody("raw-body")
    keyvaluedata = KeyValueData("key1", "value1", "test1")
    body.addFormData(keyvaluedata)

    assert body.content == keyvaluedata
    assert body.require_options == True


def test_RequestBody_rawdata():
    body = RequestBody(mode=BODY_MODE.raw)
    assert body.mode == BODY_MODE.raw
    with pytest.raises(Exception):
        keyvaluedata = KeyValueData("key1", "value1", "test1")
        body.addFormData(keyvaluedata)
    raw_body = RawBody("hello-world")
    body.addRawBody(raw_body)

    assert body.content == raw_body
    # TODO: check if require options should be True for "raw"
    assert body.require_options == True
