'''
Created on Jul 17, 2017

@author: kyriacos
'''

import json

if __name__ == '__main__':
    e_file_in = open("../../../../Documents/Crunchbase Project Data/Crunchbase Results/Data Dictionaries/Crunchbase_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Excel Imports/Crunchbase Imports/Crunchbase_Entrepreneurs_White_Happiness.txt", "w")
    
    i=1
    
    for record in e_file_in:
        try:
            jDict = json.loads(record)
            e_file_out.write(str(jDict['faceAttributes']['emotion']['happiness'])+",")
            """
            if (str(jDict['faceAttributes']['ethnicity'])=="White"):
                e_file_out.write("1"+"\n")
            else:
                e_file_out.write("0"+"\n")
            """
            print str(i)+". "
            print str(jDict['faceAttributes']['ethnicity'])
            i += 1
        except ValueError:
            print("Error in json to dictionary translation.")