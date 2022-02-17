# Script for combining CSVs

## Usage

The script can be run either on Jupyterhub or your own computer. Running the script on your own computer requires 
Python3 and package 'pandas', which can be installed by running ```pip install pandas```. The hub will have all the 
required tools installed by default.  
  
Run the following commands in a terminal:
1. First copy the script to your machine/server by running ```git clone https://github.com/lauri3k/csv-magic```. 
Alternatively you can click on the green 'Code' button and then 'Download ZIP'. Extract the files to a location of your choice.
2. Move to the new folder using ```cd csv-magic```
3. Run the script by running ```python combine.py```. The default filenames 'list_of_students.csv' and 
'eduflow_scores.csv' are expected to be present in the current folder.

### Optional flags when running the script
To specify the filename for the student list, run the script as:  
```python combine.py -l path/to/file/list.csv```  
To specify the filename for the scores, run:  
```python combine.py -s path/to/file/scores.csv```  
To specify the filename for the output file, run:  
```python combine.py -o path/to/file/output.csv```  

These can also be combined in whatever way needed, for example:  
```python combine.py -l list.csv -s scores.csv -o out.csv```
