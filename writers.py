class cloudPointFileWriter:
    def __init__(self, file_name): 
        self.file_name = file_name        
    
    def __enter__(self): 
        self.file = open(self.file_name, 'w')
        return self        
  
    def __exit__(self, exception_type, exception_value, traceback):         
        self.file.close() 

    def writeData(self, x, y, z):        
        raise NotImplementedError

class xyzFileWriter(cloudPointFileWriter):
    def writeData(self, x, y, z):
        self.file.writelines(f'{x},{y},{z}')

class txtFileWriter(cloudPointFileWriter):
    def __init__(self, file_name):
        super(txtFileWriter, self).__init__(file_name)
        self.pointNumber = 1
    
    def writeData(self, x, y, z):
        self.file.writelines(f'Point{self.pointNumber},{x},{y},{z}')
        self.pointNumber += 1

class pcdFileWriter(cloudPointFileWriter):
    def __init__(self, file_name, reader):
        # super(pcdFileWriter, self).__init__(file_name)
        super().__init__(file_name)
        self.reader = reader

    def writePCDHeader(self):    
        lineCount = self.reader.totalPointsCount()        
        self.file.write('VERSION .7\n')
        self.file.write('FIELDS x y z\n')
        self.file.write('SIZE 4 4 4\n')
        self.file.write('TYPE F F F\n')
        self.file.write('COUNT 1 1 1\n')
        self.file.write(f'WIDTH {lineCount}\n')
        self.file.write('HEIGHT 1\n')
        self.file.write('VIEWPOINT 0 0 0 1 0 0 0\n')
        self.file.write(f'POINTS {lineCount}\n')
        self.file.write('DATA ascii\n')

    def __enter__(self):                
        super().__enter__()
        self.writePCDHeader()
        return self

    def writeData(self, x, y, z):
        self.file.writelines(f'{x} {y} {z}')   