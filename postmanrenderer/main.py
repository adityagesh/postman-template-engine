from abc import ABC, abstractmethod
from re import T
from constants import APP, HTTP_METHOD, POSTMAN, BODY_MODE, Language
import uuid
from jinja2 import Template, FileSystemLoader, Environment
from typing import List
import jinja_env


class Header:
    '''
    Representation of Header of a Request
    '''

    def __init__(self):
        pass


class Url:
    '''
    Representation of Request Url
    '''

    def __init__(self, url: str):
        url_split = url.split("://")
        self.protocol = url_split[0] if len(url_split) > 1 else None
        self.raw = url_split[-1]
        self.host = self.raw.split(".")


class RequestBodyData(ABC):
    @abstractmethod
    def to_json(self):
        pass


class KeyValueData():
    def __init__(self, key: str, value: str, description: str = ""):
        self.key = key
        self.value = value
        self.description = description
        self.type = "text"

    def to_json(self):
        return ""


class KeyValueBody(RequestBodyData):
    def __init__(self, data: List[KeyValueData] = []):
        self.data = data

    def addKeyValue(self, data: List[KeyValueData]):
        self.data += data


class RawBody(RequestBodyData):
    def __init__(self, data: str, language: Language = Language.text):
        self.data = data
        self.language = language

    def to_json(self):
        return self.data


class ProtocolProfileBehaviour:
    '''
    Used to change Protocol Behavior for Requests
    See docs:
    https://github.com/postmanlabs/postman-runtime/blob/develop/docs/protocol-profile-behavior.md
    '''

    def __init__(self):
        pass


class RequestBody:
    '''
    Adds body to a Request, body can be None, Raw, formdata, urlEncoded
    '''

    def __init__(self, mode: BODY_MODE):
        self.mode = mode
        self.require_options = False

    def addRawBody(self, content: RawBody):
        if self.mode != BODY_MODE.raw:
            raise("Mode incorrect")
        self.content = content
        if self.content.language != None:
            self.require_options = True

    def addurlEncodedBody(self, content: KeyValueBody):
        if self.mode != BODY_MODE.urlencoded:
            raise("Mode incorrect")
        self.content = content

    def addFormData(self, content: KeyValueBody):
        if self.mode != BODY_MODE.formdata:
            raise("Mode incorrect")
        self.content = content
        self.require_options = True

    def addFileData(self):
        pass


class Request:
    '''
    Representation of Request in a Collection
    '''

    def __init__(self, name: str, method: HTTP_METHOD, description: str, url: Url, body: RequestBody = None) -> None:
        self.name = name
        self.method = method
        self.description = description
        self.headers = dict()
        self.url = url
        self.body = None
        self.ProtocolProfileBehaviour = None

    def add_header(self, key: str, value: str):
        self.headers[key] = value

    def add_body(self, body: RequestBody):
        self.body = body

    def add_profile_protocol_behaviour(self, ppb: ProtocolProfileBehaviour):
        self.ProtocolProfileBehaviour = ppb


class Collection:
    '''
    Representation of Postman Collection
    '''

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


if __name__ == "__main__":
    collection = Collection("sample_collection")
    # request = Request("Yahoo request", HTTP_METHOD.GET,
    #                   "", Url("https://www.yahoo.com"))
    # collection.add_request(request)

    request = Request("Google request", HTTP_METHOD.GET,
                      "", Url("https://www.google.com"))
    request.add_header("Content-Type", "Application/json")

    body = RequestBody(BODY_MODE.raw)
    rawBodyData = RawBody("x = hello test")
    body.addRawBody(rawBodyData)
    request.add_body(body)
    collection.add_request(request)

    template = collection.get_template_object()
    render = collection.render(template)
    print(render)
