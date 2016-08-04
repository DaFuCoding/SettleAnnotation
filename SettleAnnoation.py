import os
import cv2
import shutil
import numpy


'''
    Get valid annotating information from file
    Format:
        imageName
        faceNum
        [x,y,w,h] ....
    Example:
        image00001.jpg
        2
        [1,10,40,40] [3,5,50,50]
'''

# Annotating info to ACF format
# e.g.:
# image00001.jpg
# face 1 10 40 40 0 0 0 0 0
# face 3 5 50 50 0 0 0 0 0

def annotation2ACF(imageSrcDir,imageFacePos,facePosOutDir,imageOutDir):
    fp = open(imageFacePos,"r")
    done = 0
    while not done:
        imageName = fp.readline().strip('\n')
        # feedback info
        print imageName

        if imageName == '':
            done = 1
            continue

        faceNum = int(fp.readline())

        if faceNum :
            shutil.copy(imageSrcDir + imageName,imageOutDir+imageName)
            purName = imageName.split('.')[0]
            fout = open(facePosOutDir + purName + '.txt',"w")

            for id in range(faceNum):
                #bbox = fp.readline().strip('\n').split(' ')
                #[x,y,w,h] = [int(x) for x in bbox]
                fout.write('face ')
                fout.write(fp.readline().strip('\n'))
                fout.write(' 0 0 0 0 0\n')
            fout.close()

# Because of some algorithm only need rgb image such as ACF
def deleteGrayImage(imageSrcDir,txtSrcDir):
    # scan all image file
    for parent,dirNames,fileNames in os.walk(imageSrcDir):
        for imageName in fileNames:
            image = cv2.imread(imageSrcDir+imageName)
            channelNum = image.shape[2]
            if channelNum != 3:
                # delete image and txt
                txtName = imageName.strip('.')[0]+'.txt'
                print txtName
                os.remove(imageSrcDir + imageName)
                os.remove(txtSrcDir + txtName)

'''
annotation2ACF('E:\FaceDetectionBenchmark\AFLW\Data\data2\\flickr\\2/',
               'E:\FaceDetectionBenchmark\AFLW\Data\data2_DetectResult/aflw_2FacePos.txt',
               'E:\MatlabProject\piotr_toolbox\\toolbox\FaceData\\train\posProfileGt/',
               'E:\MatlabProject\piotr_toolbox\\toolbox\FaceData\\train\posProfile/')
'''

'''

deleteGrayImage('E:\MatlabProject\piotr_toolbox\\toolbox\FaceData\\train\posProfile/',
                'E:\MatlabProject\piotr_toolbox\\toolbox\FaceData\\train\posProfileGt/')
'''
