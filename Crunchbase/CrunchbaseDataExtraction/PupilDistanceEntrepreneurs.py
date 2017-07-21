'''
Created on Jun 29, 2017

@author: kyriacos
'''

import json
import math

if __name__ == '__main__':
    # Opening the necessary files.
    # Input files:
    e_file_in = open("../../../../Documents/Crunchbase Project Data/Microsoft/Crunchbase Results/Data Dictionaries/Crunchbase_Entrepreneurs_FaceLandmarks_Dictionaries.json", "r")
    e_file_in_att = open("../../../../Documents/Crunchbase Project Data/Microsoft/Crunchbase Results/Data Dictionaries/Crunchbase_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_in_rect = open("../../../../Documents/Crunchbase Project Data/Microsoft/Crunchbase Results/Data Dictionaries/Crunchbase_Entrepreneurs_Rectangles_Dictionaries.json", "r")
    # Output files:
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Microsoft/Crunchbase Results/Data Extraction/Crunchbase_Entrepreneurs_Pupil_Distance.txt", "w")
    
    # Initialize variables.
    pos = 0
    adjusted_dist_sum = 0
    count = 0
    
    # Initialize a new list for adding the rectangle attributes dictionaries.
    rectList = []
    
    # Adding the rectangle attributes dictionaries in the list.
    for rectRecord in e_file_in_rect:
        rectList.append(rectRecord)
    
    # Adding titles to the output file.
    e_file_out.write("Pupil distance of Entrepreneurs:\n\n")
    e_file_out.write("ID\t\t\t\t\tDistance\n")
    e_file_out.write("-"*36+"\t"+"-"*13+"\n")
    
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
                
                # Isolating the x and y attributes of each pupil.
                leftY = jDict['faceLandmarks']['pupilLeft']['y']
                leftX = jDict['faceLandmarks']['pupilLeft']['x']
                rightY = jDict['faceLandmarks']['pupilRight']['y']
                rightX = jDict['faceLandmarks']['pupilRight']['x']          
                
                # Calculating pupil distance by using the distance between two points formula.
                partY = math.pow((leftY - rightY), 2)
                partX = math.pow((leftX - rightX), 2)
                dist = math.sqrt(partY+partX)
                
                # Using the Pythagorean theorem to adjust pupil distance based on yaw.
                dist = math.sqrt(math.pow(dist,2)+math.pow(yaw, 2))
                
                # Adjusting pupil distance based on the face rectangle size.
                adjusted_dist = dist*100/rectSide
                
                # Adding the distance to a sum in order to calculate the average distance.
                adjusted_dist_sum += adjusted_dist
                count += 1
                
                # Printing results to file.
                e_file_out.write(str(jDict['_id'])+"\t"+str(adjusted_dist)+"\n")
                
        except ValueError:
                print("Error in json to dictionary translation.")
    
    # Calculating the average pupil distance and writing in the output file.
    e_file_out.write("\nAverage distance: "+str(adjusted_dist_sum/count))