import sys 
import readers
import writers

def getReader(fullFileName):     
    fileFormat = fullFileName.split('.')[1]
    reader = {
        'xyz': readers.xyzFileReader(fullFileName),
        'txt': readers.txtFileReader(fullFileName),
        'pcd': readers.pcdFileReader(fullFileName),
        'obj': readers.objFileReader(fullFileName)
    }.get(fileFormat)
    if not reader:
        raise Exception(f'Conversion from .{fileFormat} is not supported')
    return reader

def getWriter(fullFileName, reader):
    fileFormat = fullFileName.split('.')[1]
    writer = {
        'txt': writers.txtFileWriter(fullFileName),
        'pcd': writers.pcdFileWriter(fullFileName,reader),
        'xyz': writers.xyzFileWriter(fullFileName)
    }.get(fileFormat)
    if not writer:
        raise Exception(f'Conversion to .{fileFormat} is not supported')
    return writer

srcFileName = sys.argv[1]
reader = getReader(srcFileName)

if len(sys.argv) > 2:
    targetFileName = sys.argv[2]
else:
    fileName = srcFileName.split('.')[0]
    targetFileName =  f'{fileName}.xyz'

writer = getWriter(targetFileName, reader)

pointNumber = 0
with reader:
    with writer:
        for (x,y,z) in reader:                         
            writer.writeData(x,y,z)            
            pointNumber += 1

print(f'Done! File {srcFileName} converted to {targetFileName}. Total points:{pointNumber}')

