import pymongo
from flask import Flask, request, jsonify
import pandas as pd
from pathlib import Path
import numpy as np
import json

cred=open("connection.txt").read()

app=Flask(__name__)

@app.route('/upload/<path:filepath>',methods=['GET'])
def upload(filepath):
    if Path(filepath).suffix in ['.xls','.xlsx']:
        df=pd.read_excel(filepath)
    elif Path(filepath).suffix == '.csv':
        df=pd.read_csv(filepath)
    else:
        return jsonify({"Failure":"Invalid File Format"})

    client=pymongo.MongoClient(cred)
    db=client['text_db5']
    col=db['column_1']

    curr_id=col.find().sort('_id', -1).limit(1)[0]['_id']+1

    df['_id']=list(range(curr_id,len(df)+curr_id))
    if 'tags' not in df:
        df['tags'] = np.empty((len(df), 0)).tolist()
    df=df[['_id','text','tags']]

    data=json.loads(df.to_json(orient="records"))
    try:
        x = col.insert_many(data)
    except:
        return jsonify({"Failure":"File upload failed"})
    # return json.dumps(json.loads(data),indent=2)
    return jsonify({"Success":"File uploaded successfully"})


@app.route('/download/<filetype>',methods=['GET'])
def download(filetype):

    client=pymongo.MongoClient(cred)
    db=client['text_db5']
    col=db['column_1']

    downdf=pd.DataFrame(col.find())

    if filetype == 'xlsx':
        filepath=str(Path.home() / "Downloads" / 'aqeeqio.xlsx')
        downdf.to_excel(filepath)
    elif filetype == 'csv':
        filepath=str(Path.home() / "Downloads" / 'aqeeqio.csv')
        downdf.to_csv(filepath)
    else:
        return jsonify({"Failure":"Invalid File Format"})
    print(filepath)
    # return json.dumps(json.loads(data),indent=2)
    return jsonify({"Success":"File downloaded successfully"})

@app.route('/update/',methods=['GET'])
def update():
    pass