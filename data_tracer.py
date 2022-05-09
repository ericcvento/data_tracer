from os import walk

def make_file_list(path):
    filelist=[]
    for dir, subdirs, fnames in walk(path):
        for fname in fnames:
            fullpath=str('{}\{}'.format(dir,fname))
            filelist.append(fullpath)
    return filelist

def get_sas_programs(filelist):
    sasprograms=[]
    for f in filelist:
        if ".SAS" in f.upper(): 
            sasprograms.append(f)
    return sasprograms  

def get_stata_programs(filelist):
    stataprograms=[]
    for f in filelist:
        if ".DO" in f.upper(): 
            stataprograms.append(f)
    return stataprograms  

def data_tracer(): 
    filelist=make_file_list("TESTprojectfolder")
    sasprograms=get_sas_programs(filelist)
    stataprograms=get_stata_programs(filelist)

    print(sasprograms)
    print(stataprograms)

#call main
data_tracer() 
