from fastapi import FastAPI
import uuid
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}



class Scan:
    
    def __init__(self, uuid, url:str, visibility:str):
        self.uuid = str(uuid.uuid4())
        self.url = str(url)
        # self.status_code = 0 # 
        # self.status = "D"
        self.visibility = "public"
        pass

    # def delete_scan(self):
    
@app.post("/api/v1/scan")
def create_scan(url:str,visibility="public":str | None = None):
    # return {"item_id": item_id, "q": q}

    # do stuff
    return {
            "uuid":123,
            "country":"ab", 
            "visibility": visibility,#"public",
            "url":url#"https://asd.com"
    }


@app.post("/api/v1/scan")
def create_scan(url:str,visibility:str="public" | None = None):
    # return {"item_id": item_id, "q": q}

    # do stuff
    return {
            "uuid":123,
            "country":"ab", 
            "visibility": "public",
            "url":"https://asd.com"
    }
