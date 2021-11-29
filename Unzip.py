from zipfile import ZipFile
import os
import json
import shutil

badChars = ['/', '\\', '?', ':', '*', '"', '<', '>', '|']

fileList = os.listdir()


for file in fileList:
    if '.zip' in file:
        f = ZipFile(file, 'r')
        fileName = file.rstrip('.zip')
        f.extractall('temp')

        infoFile = open('temp' + '/info.dat', 'r')
        infoFile = json.load(infoFile)
        
        songName = infoFile['_songName']
        songAuthor = infoFile['_songAuthorName']
        levelAuthor = infoFile['_levelAuthorName']

        outputName = songAuthor + ' - ' + songName + ' (' + levelAuthor + ')'
        print(outputName)

        newOutputName = ''
        for char in outputName:
            if char not in badChars:
                newOutputName = newOutputName + char
        try:
            os.rename('temp', newOutputName)
        except:
            print("FAILED: " + newOutputName)
            shutil.rmtree('temp')
        f.close()
        
