'''
Created on Jul 17, 2017

@author: kyriacos
'''

import json
import math

if __name__ == '__main__':
    e_file_in = open("../../../../Documents/Crunchbase Project Data/Twitter Results/Data Dictionaries/Twitter_Entrepreneurs_FacePoints_Dictionaries.json", "r")
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Twitter Results/Data Extraction/Twitter_Entrepreneurs_FHWR.txt", "w")
    
    e_file_out.write("Face Points:\n\n")
    
    for record in e_file_in:   
        try:
            jDict = json.loads(record)
            print str(jDict['landmark'])
            e_file_out.write(str(jDict['landmark']))
        except ValueError:
            print("Error in json to dictionary translation.")