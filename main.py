from os import getenv
from socket import gethostbyname, gethostname

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    hostname = gethostname()
    ip_address = gethostbyname(hostname)
    return {"ContainerIp": ip_address}