# import pandas as pd
# import json
# import numpy as np

# df=pd.DataFrame({"text":['a','b','c','d','e','f','g','h','i','j']})
# df['_id']=list(range(1,len(df)+1))
# df=df[['_id','text']]
# if 'tags' not in df:
#     df['tags'] = np.empty((len(df), 0)).tolist()
# x=json.dumps(json.loads(df.to_json(orient="records")))

# print(json.dumps(json.loads(x),indent=2))

import pymongo
from flask import Flask
import pandas as pd
from pathlib import Path
import json
import numpy as np

cred=open("connection.txt").read()
argdict={
    '_id':1,
    "id": "3",
    "aspect": "Update",
    "sentiment": "Neutral"
}
client=pymongo.MongoClient(cred)
db=client['text_db5']
col=db['column_1']

_id=int(argdict['_id'])
# del argdict['_id']

s_query={"_id":_id,"tags.id": "3"}
# p_query={'_id':0,"tags":{ "$elemMatch": { "id": "1" }}}
p_query={"_id": 0,"tags.$": 1}
result=col.find_one(s_query,p_query)
print(result)

col.update_one(
  {
    "_id": int(argdict['_id']),
    "tags.id": argdict['id']
  },
  {
    "$set": {
      "tags.$.aspect": argdict['aspect'],
      "tags.$.sentiment": argdict['sentiment']
    }
  }
)

# new_value={"$set":{"tags":argdict}}


# col.update_one(result,new_value)
result=col.find_one(s_query,p_query)
print(result)


# tags.append(argdict)
# new_value={"$set":{"tags":tags}}


# row1={
#     "_id":3,
#     "text":"The room was terrible but the staff was friendly.",
#     "tags":[
        # {"id":"1",
        #  "aspect":"Room",
        #  "sentiment":"NEG"}
        # {"id":"2",
        #  "aspect":"Staff",
        #  "sentiment":"POS"}
#         ]
# }