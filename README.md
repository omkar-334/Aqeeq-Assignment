### Set up project  
  
1. Clone the repository or download as zip and extract it.  
  
```  
git clone https://github.com/omkar-334/MongoDB-API.git  
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
  
**Language Used** - Python 3.9  
**API Framework** - Flask  
**Database** - MongoDB  
**Additional Libraries** - Pandas, Numpy  
  
### API Endpoints  
  
##### /upload/\<filepath\>  
  
**\<filepath\>** - Replace this with the path of the file  
**Functionality** - uploading Excel/CSV files  
The file should atleast contain one column - "texts", consisting of unlabeled text records.  
*Note - Any name can be used for the column, but it will be assigned 'texts' while inserting data into the database.*  
It may contain another column - 'tags', consisting of an array of tags. If not present, the column is added with an empty array in each row.  
The ID of the next record in the database is obtained and then assigned consecutively to current records.  
  
##### /download/\<filetype\>  
  
**\<filetype\>** - Replace this with the required file extension (xlsx or csv)  
**Functionality** - Downloads the dataset as a Excel/CSV file into the Downloads folder.  

##### /insert/  
**Functionality** - Labeling the data (inserting new tags)  
**Query parameters** -   
1. _id - Primary Key, id of 'text', (integer)  
2. id - Id of 'tag' (integer)  
3. aspect  
4. sentiment  
  
Sample endpoint - 
```
http://127.0.0.1:5000/insert/?_id=1&id=1&aspect=Room&sentiment=NEG
```
The record with given _id is obtained and the input tag is appended to the list of tags.  
The record is then updated.  
