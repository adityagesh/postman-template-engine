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
    # PATCH = "PATCH"
    # DELETE = "DELETE"
    # COPY = "COPY"
    # HEAD = "HEAD"
    # OPTIONS = "OPTIONS"
    # LINK = "LINK"
    # UNLINK = "UNLINK"


class BODY_MODE:
    FORMDATA = "formdata"
    FORM_URLENCODED = "urlencoded"


class Jinja:
    trim_blocks = False
    lstrip_blocks = False


class Language:
    html = "html"
    javascript = "javascript"
    json = "json"
    text = None
