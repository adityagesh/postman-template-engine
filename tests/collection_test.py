

from postmanrenderer.constants import POSTMAN
from postmanrenderer.main import Collection


def test_simple_collection():
    collection = Collection("sample_collection")
    assert collection.id != None
    assert collection.schema == POSTMAN.schema
    assert collection.requests == []
