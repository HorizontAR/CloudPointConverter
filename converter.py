import sys

def writePCDHeader(sourceFile,targetFile):    
    lineCount = sum(1 for _ in sourceFile) 
    sourceFile.seek(0)   
    targetFile.write('VERSION .7\n')
    targetFile.write('FIELDS x y z\n')
    targetFile.write('SIZE 4 4 4\n')
    targetFile.write('TYPE F F F\n')
    targetFile.write('COUNT 1 1 1\n')
    targetFile.write(f'WIDTH {lineCount}\n')
    targetFile.write('HEIGHT 1\n')
    targetFile.write('VIEWPOINT 0 0 0 1 0 0 0\n')
    targetFile.write(f'POINTS {lineCount}\n')
    targetFile.write('DATA ascii\n')    

def convertToPCD(fileName):
    convertedFileName = fileName.split('.')[0] + '.pcd'
    lineCounter = 1

    with open(fileName, 'r') as originalFile:
        with open(convertedFileName, 'w') as targetFile:
            writePCDHeader(originalFile, targetFile)
            line = originalFile.readline()
            while line:
                (x,y,z) = line.split(',')
                newLine = f'{x} {y} {z}'           
                targetFile.writelines(newLine)        
                line = originalFile.readline()
                lineCounter += 1
    return convertedFileName, lineCounter

def convertToTXT(fileName):
    convertedFileName = fileName.split('.')[0] + '.txt'
    lineCounter = 1

    with open(fileName, 'r') as originalFile:
        with open(convertedFileName, 'w') as targetFile:
            line = originalFile.readline()
            while line:
                newLine = f'Point{lineCounter},{line}'            
                targetFile.writelines(newLine)                     
                line = originalFile.readline()
                lineCounter += 1
    return convertedFileName, lineCounter

fileName = sys.argv[1]
targetFormat = 'pcd'
if len(sys.argv) > 2:
    targetFormat = sys.argv[2]

if targetFormat == 'txt':
    rezFileName, totalLines = convertToTXT(fileName)
else:
    rezFileName, totalLines = convertToPCD(fileName)

print(f'Done! File {fileName} converted to {rezFileName}. Total lines:{totalLines}')

