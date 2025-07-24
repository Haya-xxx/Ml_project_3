
from fastapi import FastAPI
from dummy_data import dummy_properties

app = FastAPI()

@app.get("/api/dummy-properties/")
def get_dummy_properties():
    return {"data": dummy_properties}
