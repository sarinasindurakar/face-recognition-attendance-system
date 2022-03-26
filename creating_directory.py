
"""
Created on Sun Feb 27 18:22:07 2022

@author: Dell
"""

import os

def creatingdir(fn_dir,faculty):
    #trying to create directory if it does not exist
    #if database folder not present then make new
    if not os.path.isdir(fn_dir): #image\
        os.mkdir(fn_dir)

    
    path1 = os.path.join(fn_dir,faculty) #image\csit
    #print(path1)    
    if not os.path.isdir(path1):
        os.mkdir(path1)
        
    return(path1) #returns data\batch
     
    """ this part is for batch directory which is not needed in case of information
    path2 = os.path.join(path1,batch) #imgdatabase\csit\2017
    print(path2)  
    if not os.path.isdir(path2):
        os.mkdir(path2)  
    """

def creatingbatchdir(path1,batch):
    path2 = os.path.join(path1,batch) #imgdatabase\csit\2017  
    if not os.path.isdir(path2):
        os.mkdir(path2)  
    return(path2) #returns database\faculty\  batch

def creatingpersondir(path2,name,id):
    folder_name = id + "_" + name; # 1_isha
    path3 = os.path.join(path2,folder_name)
    if not os.path.isdir(path3):
        os.mkdir(path3)  
    return(path3)



"""note
image ko lagi chahi hamro  database hierarchy structure main imagedb -> faculty ->batch ->person-> image file
infor ko lagi chahi hamro  database hierarchy structure main infordb -> faculty ->batch.xsls file
atten ko lagi chahi hamro  database hierarchy structure main attebdb -> faculty ->batch -> data.xsls file
"""
    
    
    