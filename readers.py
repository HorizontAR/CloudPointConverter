class cloudPointFileReader:
    def __init__(self, file_name): 
        self.file_name = file_name
      
    def __enter__(self): 
        self.file = open(self.file_name, 'r')
        return self        
  
    def __exit__(self, exception_type, exception_value, traceback):         
        self.file.close() 

    def __iter__(self):
        return self

    def __next__(self):
        raise NotImplementedError

    def totalPointsCount(self):
        oldPos = self.file.tell()
        self.file.seek(0)
        lineCount = sum(1 for _ in self.file) 
        self.file.seek(oldPos)
        return lineCount

class xyzFileReader(cloudPointFileReader):
    def __next__(self):
        line = self.file.readline()
        if line:
            lineValues = line.split(',')
            return lineValues[0],lineValues[1],lineValues[2]
        raise StopIteration

class txtFileReader(cloudPointFileReader):
    def __next__(self):
        line = self.file.readline()
        if line:
            lineValues = line.split(',')
            return lineValues[1],lineValues[2],lineValues[3]
        raise StopIteration

class pcdFileReader(cloudPointFileReader):
    def __enter__(self): 
        super().__enter__()
        line = self.file.readline()
        while line:            
            if line.startswith("DATA"):
                return self
            line = self.file.readline()
        return self 

    def __next__(self):        
        line = self.file.readline()
        if line:
            lineValues = line.split(' ')
            return lineValues[0],lineValues[1],lineValues[2]
        raise StopIteration

class objFileReader(cloudPointFileReader):
    def __next__(self):
        line = self.file.readline()
        while line:
            lineValues = line.split(' ')
            if lineValues[0] == 'v':        
                return lineValues[1],lineValues[2],lineValues[3]
            line = self.file.readline()
        raise StopIteration

    def totalPointsCount(self):
        pointCounter = 0
        oldPos = self.file.tell()
        self.file.seek(0)
        line = self.file.readline()        
        while line:
            lineValues = line.split(' ')
            if lineValues[0] == 'v':  
                pointCounter += 1
            line = self.file.readline()
        self.file.seek(oldPos)
        return pointCounter