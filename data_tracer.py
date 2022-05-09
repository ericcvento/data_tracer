from os import walk

def MakeFileList(path):
    print("Scanning Directory...")
    filelist=[]
    for dir, subdirs, fnames in walk(path):
        for fname in fnames:
            fullpath=str('{}\{}'.format(dir,fname))
            filelist.append(fullpath)
    print(str('{} files found!'.format(len(filelist))))
    return filelist

def data_tracer(): 
    print(MakeFileList("TESTprojectfolder")) 


data_tracer() 
