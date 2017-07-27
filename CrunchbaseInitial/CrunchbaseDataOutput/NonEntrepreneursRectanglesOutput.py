'''
Created on Jun 27, 2017

@author: kyriacos
'''

from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db=client['Twitter_Photos']
    collection_Entrepreneurs=db['Crunchbase_Faces_Non_Entrepreneurs']
    cursor = collection_Entrepreneurs.find({"faceAttributes":{"$exists":True}, "$where" : "this.faceAttributes.length == 1"} ,{'faceAttributes.faceRectangle':1})
    #"faceAttributes.0":{"$exists":"false"}
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Microsoft/Crunchbase Results/Data Output/Crunchbase_Non_Entrepreneurs_Rectangles_Output.json", 'w')
    
    for document in cursor:
        e_file_out.write(str(document)+"\n")