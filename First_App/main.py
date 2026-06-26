from fastapi import FastAPI

app = FastAPI()

# default page 
@app.get('/')
def home():
    return {"name":"Kaustav Mondal"}
# Path parameter 1 
@app.get("/square/{num}")
def square(num:int):
    return {"Square":num*num}
# Try with abc at the and 5 at the end of the url 

