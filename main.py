from fastapi import FastAPI, staticfiles

from database import SessionDep, create_db_and_tables

import uuid
app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.post("/scan")
def make_scanny():
    # create scan in db
    # start scan async/background, they will poll
    # fnish scan
    # write some results to db idk what results
    # point img at screenshoty

    return {"Hello": "World"}

app.mount("/screenshots", staticfiles.StaticFiles(directory="screenshots"), name="screenshots")

class Scan:
    """
    Scan
    represents a scan in any state.
    will contain scan result
    Takes: uuid(or autogen),  url, visibility
    or could load from the uuid from the db later, not now
    docstring

    """

    
    def __init__(self, uuid, url:str, visibility:str):
        self.uuid = str(uuid.uuid4())
        self.url = str(url)
        # self.status_code = 0 # 
        # self.status = "D"
        self.visibility = "public"
        pass

    # def delete_scan(self)
    # def retrieve(self)
class Scanner:
    """
    Docstring for Scanner
    Scanner - wrapper around playwright for now
    Scanner takes scans... and scans them
    """

    def __init__(self, uuid, country):
        pass

    def queue_scan():
        pass

    
@app.post("/api/v1/scan")
def create_scan(url:str,visibility:str | None = "public"):
    # return {"item_id": item_id, "q": q}
    # do stuff
    return {
            "uuid":123,
            "country":"ab", 
            "visibility": visibility,#"public",
            "url":url#"https://asd.com"
    }


# @app.post("/api/v1/scan")
# def create_scan(url:str,visibility:str="public" | None = None):
#     # return {"item_id": item_id, "q": q}

#     # do stuff
#     return {
#             "uuid":123,
#             "country":"ab", 
#             "visibility": "public",
#             "url":"https://asd.com"
#     }
