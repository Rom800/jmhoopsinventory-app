from fastapi import FastAPI

app = FastAPI()

inventory = {"shoes": 10, "sandals": 5}

@app.get("/")
def read_root():
    return {"status": "Inventory API running"}

@app.get("/inventory")
def get_inventory():
    return inventory

