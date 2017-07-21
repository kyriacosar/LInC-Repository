'''
Created on Jul 21, 2017

@author: kyriacos
'''

from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db=client['Twitter_Photos']
    collection_Entrepreneurs=db['Face_Points_Entrepreneurs']
    cursor = collection_Entrepreneurs.find({"$where" : "this.faceplusplus.length == 1"} ,{'faceplusplus.landmark':1})
    #"faceAttributes.0":{"$exists":"false"}
    e_file_out = open("../../../../Documents/Crunchbase Project Data/FacePlusPlus/Twitter Results/Data Output/Twitter_Entrepreneurs_FaceLandmarks_Output.json", 'w')
    
    for document in cursor:
        e_file_out.write(str(document)+"\n")