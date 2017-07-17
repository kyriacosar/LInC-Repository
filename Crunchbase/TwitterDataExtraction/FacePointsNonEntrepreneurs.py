'''
Created on Jul 17, 2017

@author: kyriacos
'''

import json

if __name__ == '__main__':
    e_file_in = open("../../../../Documents/Crunchbase Project Data/Twitter Results/Data Dictionaries/Twitter_Non_Entrepreneurs_FacePoints_Dictionaries.json", "r")
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Twitter Results/Data Extraction/Twitter_Non_Entrepreneurs_FHWR.txt", "w")
    
    e_file_out.write("Face Points of non Entrepreneurs:\n\n")
    
    e_file_out.write("ID\t\t\tLeft Contour\tRight Contour\tChin Contour\tLeft Eyebrow Right corner\tRight Eyebrow Left corner\n")
    e_file_out.write("-"*9+"\t\t"+"-"*14+"\t"+"-"*14+"\t"+"-"*14+"\t"+"-"*25+"\t"+"-"*26+"\n")
    
    for record in e_file_in:   
        try:
            jDict = json.loads(record)
            
            # Based on the ID length, the right amount of tabs are written to the output file.
            if str(jDict['_id']).__len__() >= 16:
                e_file_out.write(str(jDict['_id'])+"\t")
            elif str(jDict['_id']).__len__() >= 8:
                e_file_out.write(str(jDict['_id'])+"\t\t")
            else:
                e_file_out.write(str(jDict['_id'])+"\t\t\t")
                
            e_file_out.write("x: "+str(jDict['landmark']['contour_left1']['x'])+"\ty: "+str(jDict['landmark']['contour_left1']['y'])+"\t")
            e_file_out.write("x: "+str(jDict['landmark']['contour_right1']['x'])+"\ty: "+str(jDict['landmark']['contour_right1']['y'])+"\t")
            e_file_out.write("x: "+str(jDict['landmark']['contour_chin']['x'])+"\ty: "+str(jDict['landmark']['contour_chin']['y'])+"\t")
            e_file_out.write("x: "+str(jDict['landmark']['left_eyebrow_right_corner']['x'])+"\ty: "+str(jDict['landmark']['left_eyebrow_right_corner']['y'])+"\t\t\t")
            e_file_out.write("x: "+str(jDict['landmark']['right_eyebrow_left_corner']['x'])+"\ty: "+str(jDict['landmark']['right_eyebrow_left_corner']['y'])+"\n")
        except ValueError:
            print("Error in json to dictionary translation.")