from postmanrenderer.main import Collection, Request, Url, Collection
from postmanrenderer.constants import HTTP_METHOD,  POSTMAN


def test_collection():
    collection = Collection("sample_collection")
    request = Request("Yahoo request", HTTP_METHOD.GET,
                      "", Url("https://www.yahoo.com"))
    collection.add_request(request)
    template = collection.get_template_object()
    render = collection.render(template)
    assert request in collection.requests
    collection.write_to_file(render, "/tmp/out.collection")
    assert open("/tmp/out.collection")


def test_simple_collection():
    collection = Collection("sample_collection")
    assert collection.id != None
    assert collection.schema == POSTMAN.schema
    assert collection.requests == []
