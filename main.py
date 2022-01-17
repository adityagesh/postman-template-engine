import uuid


class Collection:
    def __init__(self, name, id = None ) -> None:
        self.postman_id = uuid.uuid4() if id == None else id
        self.name = name
        self.schema = "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        self.item = []
        

class Request:
    pass

class Header:
    pass
        
    
if __name__ == "__main__":
    print("Main execution")