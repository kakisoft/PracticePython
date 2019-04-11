import os,re,sys,shutil,zipfile
import datetime

WORK_DIRECTORY = "D:\kaki\wPython\workDirectory"
TARGET_FILE_NAME_HEAD  = "SYSNAME"
TARGET_FILE_EXTENTIONS = ["dmp","log","txt"]

controlTargetFolder = ""

def editfileFilter(fileName):
    # Filtering in FileName Header
    if not re.findall('^'+TARGET_FILE_NAME_HEAD,fileName):
        return False
    # Filtering in Extention
    body, ext = os.path.splitext(fileName)
    if re.sub('^.','',ext).lower() not in map(lambda x:x.lower(), TARGET_FILE_EXTENTIONS):
        return False
    #　Returns true if the match conditions
    return True


def createFolderEachManagementUnit():
    try:
        global controlTargetFolder
        createdFolderName = TARGET_FILE_NAME_HEAD + '_' +datetime.date.today().strftime("%Y%m%d")
        controlTargetFolder = WORK_DIRECTORY + os.sep + createdFolderName
        if not os.path.exists(controlTargetFolder):
            os.mkdir(controlTargetFolder)
        return True
    except Exception as e:
        return False

def delFileFilter(fileName):
    # Filtering in FileName Header
    if not re.findall('^'+TARGET_FILE_NAME_HEAD,fileName):
        return False
    # Filtering in Extention
    body, ext = os.path.splitext(fileName)
    if re.sub('^.','',ext).lower() not in map(lambda x:x.lower(), TARGET_FILE_EXTENTIONS):
#    if re.sub('^.','',ext).lower(),'zip'):
        return False
    #　Returns true if the match conditions
    return True

#======================
#        Main
#======================
if not createFolderEachManagementUnit():
    sys.exit(0)

# Move the files to be compressed
fileExists = False
for fileName in filter(editfileFilter,os.listdir(WORK_DIRECTORY)):
    fileExists = True
    mvFileName = fileName
    if os.path.exists(controlTargetFolder + os.sep + mvFileName):
        body, ext = os.path.splitext(fileName)
        mvFileName = body + "_" + datetime.datetime.today().strftime("%Y%m%d_%H%M%S") + ext
    shutil.move(WORK_DIRECTORY + os.sep + fileName,
                controlTargetFolder + os.sep + mvFileName)

if not fileExists:
    shutil.rmtree(controlTargetFolder)
    sys.exit(0)

# To compress the folder
zipFolder = controlTargetFolder + ".zip"
if os.path.exists(zipFolder):
    body, ext = os.path.splitext(zipFolder)
    zipFolder = body + "_" + datetime.datetime.today().strftime("%Y%m%d_%H%M%S") + ext

zipFile = zipfile.ZipFile(zipFolder,"w",zipfile.ZIP_DEFLATED)
zipFile.write(controlTargetFolder)
zipFile.close()

# delete base folder
shutil.rmtree(controlTargetFolder)

# delete old files
for fileName in filter(delfileFilter,os.listdir(WORK_DIRECTORY)):
    print(fileName)
    pass
    pass
