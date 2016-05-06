import os

def create_directories(rootDir):
    lstOfDirs = ["/app/templates"
                 ,"/app/static"
                 ,"/app/auth"
                 ,"/migrations"
                 ,"/tests"]
    
    for aDir in lstOfDirs:
        os.makedirs("{0}/{1}".format(rootDir,aDir))
        
    