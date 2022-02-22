import pytest
from postmanrenderer.constants import BODY_MODE
from postmanrenderer.main import KeyValueData, KeyValueBody, RawBody, RequestBody


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
