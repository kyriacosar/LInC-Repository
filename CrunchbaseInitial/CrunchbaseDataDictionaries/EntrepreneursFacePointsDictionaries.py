'''
Created on Jul 19, 2017

@author: kyriacos
'''

#import json
from TwitterDataDictionaries.JsonFormatter import jsonFormatter
    
if __name__ == '__main__':
    e_file_in = open("../../../../Documents/Crunchbase Project Data/Microsoft/Crunchbase Results/Data Output/Crunchbase_Entrepreneurs_FacePoints_Output.json", 'r')
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Microsoft/Crunchbase Results/Data Dictionaries/Crunchbase_Entrepreneurs_FacePoints_Dictionaries.json", "w")
    
    for line in e_file_in:   
        record = jsonFormatter(line)
        e_file_out.write(record)
        """
        try:
            jdict = json.loads(record)
            e_file_out.write(str(jdict)+"\n")
        except ValueError:
            print("Error!!!")
        """