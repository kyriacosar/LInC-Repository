'''
Created on Jun 30, 2017

@author: kyriacos
'''

import json
import math

if __name__ == '__main__':
    # Opening the necessary files.
    # Input files:
    e_file_in = open("../TwitterDataDictionaries/Twitter_Entrepreneurs_FaceLandmarks_Dictionaries.json", "r")
    e_file_in_att = open("../TwitterDataDictionaries/Twitter_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_in_rect = open("../TwitterDataDictionaries/Twitter_Entrepreneurs_Rectangles_Dictionaries.json", "r")
    
    # Initialize variables.
    pos = 0
    dist_sum = 0
    count = 0
    
    # Initialize a new list for adding the rectangle attributes dictionaries.
    rectList = []
    
    # Adding the rectangle attributes dictionaries in the list.
    for rectRecord in e_file_in_rect:
        rectList.append(rectRecord)
    
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
                
                # Adding the distance to a sum in order to calculate the average distance.
                dist_sum += dist
                count += 1
                
        except ValueError:
                print("Error in json to dictionary translation.")
    
    print "Average distance: " + str(dist_sum/count)
    e_file_in = open("../TwitterDataDictionaries/Twitter_Entrepreneurs_FaceLandmarks_Dictionaries.json", "r")
    e_file_in_att = open("../TwitterDataDictionaries/Twitter_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_in_rect = open("../TwitterDataDictionaries/Twitter_Entrepreneurs_Rectangles_Dictionaries.json", "r")
    
    # Initialize variables.
    pos = 0
    avg_dist = dist_sum/count
    pos_distribution = 0
    neg_distribution = 0
    pos_count = 0
    neg_count = 0
    
    # Initialize a new list for adding the rectangle attributes dictionaries.
    rectList = []
    
    # Adding the rectangle attributes dictionaries in the list.
    for rectRecord in e_file_in_rect:
        rectList.append(rectRecord)
    
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

                # Adding the distance to a sum in order to calculate the average distance.
                if (dist > avg_dist):
                    pos_distribution += dist - avg_dist
                    pos_count += 1
                else:
                    neg_distribution += dist - avg_dist
                    neg_count += 1
        except ValueError:
                print("Error in json to dictionary translation.")
                
    print "Population size: "+str(count)
    print "Positive distribution: "+str(pos_distribution/pos_count)
    print "Negative distribution: "+str(neg_distribution/neg_count)