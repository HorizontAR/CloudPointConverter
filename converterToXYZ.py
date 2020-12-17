import sys

def convertToXYZ(fileName):
    convertedFileName = fileName.split('.')[0] + '.xyz'
    lineCounter = 1

    with open(fileName, 'r') as originalFile:
        with open(convertedFileName, 'w') as targetFile:
            line = originalFile.readline()
            while line:
                lineValues = line.split(' ')
                if lineValues[0] == 'v':
                    newLine = f'{lineValues[1]},{lineValues[2]},{lineValues[3]}\n'            
                    targetFile.writelines(newLine)                                         
                    lineCounter += 1
                line = originalFile.readline()
    return convertedFileName, lineCounter

fileName = sys.argv[1]
sourceFormat = fileName.split('.')[1]
if sourceFormat != 'obj':    
    sys.exit(f'Unsupported file format {sourceFormat}')


rezFileName, totalLines = convertToXYZ(fileName)

print(f'Done! File {fileName} converted to {rezFileName}. Total lines:{totalLines}')

