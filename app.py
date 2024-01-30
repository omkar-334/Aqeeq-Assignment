import pymongo
from flask import Flask

cred=open("connection.txt").read()
client=pymongo.MongoClient(cred)
db=client['text_db5']
col=db['column_1']

app=Flask(__name__)

@app.route('/upload/<path:filepath>',methods=['GET'])
def upload(filepath):
    pass

@app.route('/download/<filetype>',methods=['GET'])
def download(filetype):
    pass

@app.route('/update/',methods=['GET'])
def update():
    pass