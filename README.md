### Set up project

1. Clone the repository or download as zip and extract it.
```
git clone https://github.com/omkar-334/Aqeeq-Assignment.git Aqeeq
```
2. Create a virtual environment
```
python -m venv .venv
```
3. Activate .venv
```
.venv\Scripts\activate
```
4. Install required libraries.
```python
pip install -r requirements.txt
```

### Project Details  
Language Used - Python 3.9  
API Framework - Flask  
Database - MongoDB  
Additional Libraries - Pandas, Numpy  

### API Endpoints 

##### /upload/\<filepath\>  
Functionality - uploading Excel/CSV files  
The file should atleast contain one column - "texts", consisting of unlabeled text records.  
It may contain another column - 'tags', consisting of arrays of tags. If not present, the column is added.  
The ID of the next record in the database is obtained and then assigned consecutively to current records.  
