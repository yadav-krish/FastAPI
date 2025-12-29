from fastapi import FastAPI
import json
app=FastAPI()

@app.get("/")
def hello():
  return {"message":"Hello world"}

def load_data():
  with open('patients.json','r') as f:
    data=json.load(f)
  
  return data
    
@app.get('/view')
def view():
  data=load_data()

  return data