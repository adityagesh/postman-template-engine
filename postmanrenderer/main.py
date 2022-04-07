import json
from constants import APP, HTTP_METHOD, POSTMAN, Script_Type
import uuid
from jinja2 import Template, FileSystemLoader, Environment
from typing import List
import jinja_env

# Representation of Header of a Request


class Header:
    def __init__(self):
        pass

# Representation of Request Url


class Url:
    def __init__(self, url: str):
        url_split = url.split("://")
        self.protocol = url_split[0] if len(url_split) > 1 else None
        self.raw = url_split[-1]
        self.host = self.raw.split(".")


class Script:
    def __init__(self, script_type: Script_Type, filename):
        self.script_type = script_type
        self.script = []
        with open(filename, "r") as f:
            self.script = f.readlines()
        self.script = [s.strip() for s in self.script]


# Representation of Request in a Collection

class Request:
    def __init__(self, name: str, method: HTTP_METHOD, description: str, url: Url) -> None:
        self.name = name
        self.method = method
        self.description = description
        self.headers = dict()
        self.url = url
        self.events = {}

    def add_script(self, script: Script):
        self.events[script.script_type] = script

    def add_header(self, key: str, value: str):
        self.headers[key] = value


# Representation of Postman Collection
class Collection:
    def __init__(self, name, id=None) -> None:
        self.id = uuid.uuid4() if id == None else id
        self.name = name
        self.schema = POSTMAN.schema
        self.requests = []

    def add_request(self, request: Request):
        self.requests.append(request)

    def get_template_object(self) -> Template:
        file_loader = FileSystemLoader(APP.root_dir + APP.template_dir)
        env = Environment(loader=file_loader)
        jinja_env.init(env)
        template = env.get_template(APP.collections_template)
        return template

    def render(self, template: Template) -> str:
        rendered_template = template.render(collection=self)
        return rendered_template

    def write_to_file(self, rendered_collection, filename):
        with open(filename, "w") as f:
            f.write(rendered_collection)


if __name__ == "__main__":
    collection = Collection("sample_collection")
    request = Request("Yahoo request", HTTP_METHOD.GET,
                      "", Url("https://www.yahoo.com"))
    collection.add_request(request)

    request = Request("Google request", HTTP_METHOD.GET,
                      "", Url("https://www.google.com"))
    request.add_header("Content-Type", "Application/json")
    pre_script = Script(Script_Type.prerequest, "tests/data/pre-request.js")
    request.add_script(pre_script)
    request.add_script(Script(Script_Type.test,
                       "tests/data/post-request.js"))
    collection.add_request(request)

    template = collection.get_template_object()
    render = collection.render(template)
    collection.write_to_file(render, "out.collection")
    print(render)
