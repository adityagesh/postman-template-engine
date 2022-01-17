from constants import APP, POSTMAN
import uuid
from jinja2 import Template, FileSystemLoader, Environment
from typing import List

class Header:
    pass


class Url: 
    def __init__(self, url: str):
        self.raw = url
        self.host = url.split(".")

class Request:
    def __init__(self, name, method, description, headers: List[Header], url: Url) -> None:
        self.name = name
        self.method = method
        self.description = description
        self.headers = headers
        self.url = url


class Collection:
    def __init__(self, name, id = None) -> None:
        self.id = uuid.uuid4() if id == None else id
        self.name = name
        self.schema = POSTMAN.schema
        self.request = []
        
    def add_request(self, request: Request):
        self.request.append(request)
    
    
    def get_template_object(self) -> Template:
        print(APP.root_dir + APP.template_dir)
        file_loader = FileSystemLoader(APP.root_dir + APP.template_dir)
        print(file_loader.list_templates())
        env = Environment(loader=file_loader)

        template = env.get_template(APP.collections_template)
        return template
    
    def render(self, template: Template) -> str:
        rendered_template = template.render(collection = self, requests= self.request)
        return rendered_template
        
        

    
if __name__ == "__main__":
   collection = Collection("sample_collection")
   template = collection.get_template_object()
   render = collection.render(template)
   print(render)
   