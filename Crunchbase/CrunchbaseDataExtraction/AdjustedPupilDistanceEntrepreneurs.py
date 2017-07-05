'''
Created on Jun 29, 2017

@author: kyriacos
'''

import json
import math

if __name__ == '__main__':
    e_file_in = open("../CrunchbaseDataDictionaries/Crunchbase_Entrepreneurs_FaceLandmarks_Dictionaries.json", "r")
    e_file_in_att = open("../CrunchbaseDataDictionaries/Crunchbase_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_in_rect = open("../CrunchbaseDataDictionaries/Crunchbase_Entrepreneurs_Rectangles_Dictionaries.json", "r")
    e_file_out = open("Crunchbase_Entrepreneurs_Adjusted_Pupil_Distance.txt", "w")
    
    leftY = 0
    leftX = 0
    rightY = 0
    rightX = 0
    yaw = 0
    partY = 0
    partX = 0
    dist = 0
    adjusted_dist = 0
    adjusted_dist_sum = 0
    count = 0
    
    e_file_out.write("Adjusted pupil distance of Entrepreneurs:\n\n")
    
    for record in e_file_in:   
        try:
            rectSide = -1
            yawRecord = e_file_in_att.readline()
            jDict = json.loads(record)
            
            for rectRecord in e_file_in_rect:
                rectDict = json.loads(rectRecord)
                if rectDict['_id'] == jDict['_id']:
                    rectSide = rectDict['faceRectangle']['width']
                    break
                
            if rectSide != -1:
                yawDict = json.loads(yawRecord)                                                                      
                leftY = jDict['faceLandmarks']['pupilLeft']['y']
                leftX = jDict['faceLandmarks']['pupilLeft']['x']
                rightY = jDict['faceLandmarks']['pupilRight']['y']
                rightX = jDict['faceLandmarks']['pupilRight']['x']
                yaw = math.fabs(yawDict['faceAttributes']['headPose']['yaw'])
                partY = math.pow((leftY - rightY), 2)
                partX = math.pow((leftX - rightX), 2)
                dist = math.sqrt(partY+partX)
                dist = math.sqrt(math.pow(dist,2)+math.pow(yaw, 2))
                adjusted_dist = dist*100/rectSide
                adjusted_dist_sum += adjusted_dist
                count += 1
                e_file_out.write(str(adjusted_dist)+"\n")
                
        except ValueError:
                print("Error in json to dictionary translation.")
            
    e_file_out.write("\nAverage distance: "+str(adjusted_dist_sum/count))