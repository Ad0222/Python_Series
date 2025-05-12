from  fastapi import FastAPI,UploadFile

app=FastAPI()

@app.get('/')
def home():
    return{'data':'Welcome to home page'}
@app.get('/contact')
def contact():
    return {'data':'We;come to contact page'}

@app.post('/UploadFile')
def handleImage(files: list[UploadFile]):
    print(files)
    return {'status': 'got the files'}

import uvicorn
uvicorn.run(app)