class POSTMAN:
    schema = "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    
class APP:
    root_dir = "./postmanrenderer/"
    template_dir = "templates/"
    collections_template = "collection.j2"
    
class HTTP_METHOD:
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    
class Jinja:
    trim_blocks = False
    lstrip_blocks = False