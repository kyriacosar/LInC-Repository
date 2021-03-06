'''
Created on Jun 22, 2017

@author: kyriacos
'''

import json
import math

if __name__ == '__main__':
    # Opening the necessary files.
    # Input files:
    e_file_in = open("../../../../Documents/Crunchbase Project Data/Microsoft/Twitter Results/Data Dictionaries/Twitter_Non_Entrepreneurs_FaceLandmarks_Dictionaries.json", "r")
    e_file_in_att = open("../../../../Documents/Crunchbase Project Data/Microsoft/Twitter Results/Data Dictionaries/Twitter_Non_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_in_rect = open("../../../../Documents/Crunchbase Project Data/Microsoft/Twitter Results/Data Dictionaries/Twitter_Non_Entrepreneurs_Rectangles_Dictionaries.json", "r")
    # Output file:
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Microsoft/Twitter Results/Data Extraction/Twitter_Non_Entrepreneurs_Mouth_Length.txt", "w")
    
    # Initialize variables.
    pos = 0
    adjusted_len_sum = 0
    count = 0
    
    # Initialize a new list for adding the rectangle attributes dictionaries.
    rectList = []
    
    # Adding the rectangle attributes dictionaries in the list.
    for rectRecord in e_file_in_rect:
        rectList.append(rectRecord)
    
    # Adding titles to the output file.
    e_file_out.write("Mouth length of non Entrepreneurs:\n\n")
    e_file_out.write("ID\t\t\tDistance\n")
    e_file_out.write("-"*9+"\t\t"+"-"*13+"\n")
    
    # Reading the JSON formatted face landmarks records.   
    for record in e_file_in:   
        try:
            # Reading the JSON formatted face attributes records.
            yawRecord = e_file_in_att.readline()
            
            # Converting the JSON record to a dictionary and isolating the ID field.
            jDict = json.loads(record)
            jID = jDict['_id']
        
            # Converting the JSON record to a dictionary and isolating the ID field.
            rectDict = json.loads(rectList[pos])
            rectID = rectDict['_id']
            
            # This loop is used to find matching IDs for the face landmarks and rectangle attributes records.
            while rectID < jID:
                pos += 1
                rectDict = json.loads(rectList[pos])
                rectID = rectDict['_id']
            
            # If the IDs match after the loop then the distance is calculated.
            # If not, there's no match because the records are sorted based on the ID field.   
            if rectID == jID:
                # Fetching the side of the face rectangle.
                rectSide = rectDict['faceRectangle']['width']
                
                # Converting the face attributes JSON record to a dictionary and isolating the yaw field.
                yawDict = json.loads(yawRecord)            
                yaw = math.fabs(yawDict['faceAttributes']['headPose']['yaw'])
                
                # Isolating the x and y attributes of each edge of the mouth.
                leftY = jDict['faceLandmarks']['mouthLeft']['y']
                leftX = jDict['faceLandmarks']['mouthLeft']['x']
                rightY = jDict['faceLandmarks']['mouthRight']['y']
                rightX = jDict['faceLandmarks']['mouthRight']['x']
                
                # Calculating mouth length by using the distance between two points formula.
                partY = math.pow((leftY - rightY), 2)
                partX = math.pow((leftX - rightX), 2)
                length = math.sqrt(partY+partX)
                
                # Using the Pythagorean theorem to adjust mouth length based on yaw.
                length = math.sqrt(math.pow(length,2)+math.pow(yaw, 2))
                
                # Adjusting mouth length based on the face rectangle size.
                adjusted_len = length*100/rectSide
                
                # Adding the length to a sum in order to calculate the average distance.
                adjusted_len_sum += adjusted_len
                count += 1
            
                # Based on the ID length, the right amount of tabs are written to the output file.
                if str(jDict['_id']).__len__() >= 16:
                        e_file_out.write(str(jDict['_id'])+"\t"+str(adjusted_len)+"\n")
                elif str(jDict['_id']).__len__() >= 8:
                    e_file_out.write(str(jDict['_id'])+"\t\t"+str(adjusted_len)+"\n")
                else:
                    e_file_out.write(str(jDict['_id'])+"\t\t\t"+str(adjusted_len)+"\n")
                
        except ValueError:
            print("Error in json to dictionary translation.")
    
    # Calculating the average mouth length and writting in the output file.
    e_file_out.write("\nAverage length: "+str(adjusted_len_sum/count))