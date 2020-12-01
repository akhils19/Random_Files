#A function to convert file names in a given folder to ascending numerical order
# File names:
#Before - Jajdn.jpg, sadsn.jpg, asdSAf.jpg, sdfs.jpg...
#After = 0.jpg, 1.jpg, 2.jpg, 3.jpg...


import os

path = '/'

def filenameconversion(path,filetype = '.jpg'):
    '''
    
    Parameters
    ----------
    path : String
        Enter the path of the folder in which files are located.
    filetype : String, optional
        DESCRIPTION. The default is '.jpg'.
        Enter the desired output extension

    Returns
    -------
    Renamed files in the entered destination. 

    '''

    for count,filename in enumerate(os.listdir(path)):
        src = filename
        dst = str(count)+filetype

        os.rename(src,dst)