from constants import POSTMAN
import uuid
from jinja2 import Template
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
    def __init__(self, name, id = None ) -> None:
        self.id = uuid.uuid4() if id == None else id
        self.name = name
        self.schema = POSTMAN.schema
        self.request = []
        
    def add_request(self, request: Request):
        self.request.append(request)
    
    def read_templatefile(self, path):
        pass
    
    def get_template_object(self, template):
        pass
    
    def render_json(self, template: Template):
        json = template.render(collection = self, requests= self.request)
        


        
    
if __name__ == "__main__":
    print("Main execution")