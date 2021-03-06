'''
Created on Jul 21, 2017

@author: kyriacos
'''

import json
import math

if __name__ == '__main__':
    e_file_in = open("../../../../Documents/Crunchbase Project Data/FacePlusPlus/Crunchbase Results/Data Dictionaries/Crunchbase_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_out = open("../../../../Documents/Crunchbase Project Data/FacePlusPlus/Crunchbase Results/Data Extraction/Crunchbase_Entrepreneurs_Ethnicity_Gender_Percentages.txt", "w")
    
    male = 0
    female = 0
    white = 0
    black = 0
    asian = 0
    count=0
    
    for record in e_file_in:   
        try:
            jDict = json.loads(record)
            
            str_gender = str(jDict['attributes']['gender']['value'])
            if str_gender == 'Male':
                male += 1
            elif str_gender == 'female':
                female += 1
            
            str_ethn = str(jDict['attributes']['ethnicity']['value'])
            if str_ethn == 'White':
                white += 1
            elif str_ethn == 'Black':
                black += 1
            elif str_ethn == 'Asian':
                asian += 1                     
            
            count += 1
        except ValueError:
            print("Error in json to dictionary translation.")
            
    e_file_out.write("Ethnicity and gender percentages among Entrepreneurs:\n\n")
   
    e_file_out.write("Gender Percentages:\n")
    e_file_out.write("Males: "+str(male)+" out of "+str(count)+" with percentage "+str(math.ceil((male/float(count))*100.0)))
    e_file_out.write("\nFemales: "+str(female)+" out of "+str(count)+" with percentage "+str(math.floor((female/float(count))*100.0)))
    
    e_file_out.write("\n\nEthnicity Percentages:\n")
    e_file_out.write("White: "+str(white)+" out of "+str(count)+" with percentage "+str(math.ceil((white/float(count))*100.0)))
    e_file_out.write("\nBlack: "+str(black)+" out of "+str(count)+" with percentage "+str(math.floor((black/float(count))*100.0)))
    e_file_out.write("\nAsian: "+str(asian)+" out of "+str(count)+" with percentage "+str(math.floor((asian/float(count))*100.0)))