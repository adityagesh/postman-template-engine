from constants import APP, HTTP_METHOD, POSTMAN
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

# Representation of Request in a Collection
class Request:
    def __init__(self, name: str, method: HTTP_METHOD, description: str, headers: List[Header], url: Url) -> None:
        self.name = name
        self.method = method
        self.description = description
        self.headers = headers
        self.url = url

# Representation of Postman Collection
class Collection:
    def __init__(self, name, id = None) -> None:
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
        rendered_template = template.render(collection= self)
        return rendered_template
        
    
if __name__ == "__main__":
   collection = Collection("sample_collection")
   request = Request("Yahoo request", HTTP_METHOD.GET,"", [], Url("https://www.yahoo.com"))
   collection.add_request(request)
   
   request = Request("Google request", HTTP_METHOD.GET,"", [], Url("https://www.google.com"))
   collection.add_request(request)
   
   template = collection.get_template_object()
   render = collection.render(template)
   print(render)
   