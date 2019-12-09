import codecs

filepath = r"E:\data\kf_id.txt"# r进行特殊处理，不用加转义字符
file=codecs.open(filepath,'r',encoding='utf-8',errors='ignore')
mylist = file.readlines()
file.close()
savegoodfilepath =r"E:\data\good.txt"
goodfile = open(savegoodfilepath,'wb')
savebadfilepath =r"E:\data\bad.txt"
badfile = open(savebadfilepath,'wb')
for line in mylist:

    linelist = line.split(' ')
    #print(linelist)
    idlist=linelist[2].strip()
    print(idlist)
    if len(idlist)==15 or len(idlist) == 18:
            #good
        goodfile.write(line.encode('utf-8'))
    else:
            #bad
        badfile.write(line.encode('utf-8'))


goodfile.close()
badfile.close()