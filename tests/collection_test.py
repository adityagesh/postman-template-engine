from postmanrenderer.main import Collection, Request, Script, Url, Collection
from postmanrenderer.constants import HTTP_METHOD, Script_Type


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
