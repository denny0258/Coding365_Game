from subprocess import Popen, PIPE, STDOUT

class Adapter:

    def __init__(self, path):
        self.path = path
        self.proc = None

    def start(self):
        self.proc = Popen([self.path], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    
    def call(self,input, end='\r\n'):
        output = self.proc.communicate(input=(input+end).encode())[0]
        return output.decode()
    
    def stop(self):
        self.proc.kill()


def GetAdapter(path):
    return Adapter(path)
    