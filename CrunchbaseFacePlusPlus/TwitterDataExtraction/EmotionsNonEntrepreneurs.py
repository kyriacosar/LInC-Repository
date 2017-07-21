'''
Created on Jul 21, 2017

@author: kyriacos
'''

import json

if __name__ == '__main__':
    e_file_in = open("../../../../Documents/Crunchbase Project Data/FacePlusPlus/Twitter Results/Data Dictionaries/Twitter_Non_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_out = open("../../../../Documents/Crunchbase Project Data/FacePlusPlus/Twitter Results/Data Extraction/Twitter_Non_Entrepreneurs_Emotions.txt", "w")
    
    sadness = 0
    neutral = 0
    contempt = 0
    disgust = 0
    anger = 0
    surprise = 0
    fear = 0
    happiness = 0
    count = 0
    
    for record in e_file_in:   
        try:
            jDict = json.loads(record)
            sadness += jDict['faceAttributes']['emotion']['sadness']
            neutral += jDict['faceAttributes']['emotion']['neutral']
            contempt += jDict['faceAttributes']['emotion']['contempt']
            disgust += jDict['faceAttributes']['emotion']['disgust']
            anger += jDict['faceAttributes']['emotion']['anger']
            surprise += jDict['faceAttributes']['emotion']['surprise']
            fear += jDict['faceAttributes']['emotion']['fear']
            happiness += jDict['faceAttributes']['emotion']['happiness']
            count += 1
        except ValueError:
            print("Error in json to dictionary translation.")
    
    e_file_out.write("Average non Entrepreneur emotions:\n\n")
    e_file_out.write('Sadness: '+str(sadness/count)+"\n")
    e_file_out.write('Neutral: '+str(neutral/count)+"\n")
    e_file_out.write('Contempt: '+str(contempt/count)+"\n")
    e_file_out.write('Disgust: '+str(disgust/count)+"\n")
    e_file_out.write('Anger: '+str(anger/count)+"\n")
    e_file_out.write('Surprise: '+str(surprise/count)+"\n")
    e_file_out.write('Fear: '+str(fear/count)+"\n")
    e_file_out.write('Happiness :'+str(happiness/count))   