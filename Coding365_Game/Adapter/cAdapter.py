from subprocess import Popen, PIPE, STDOUT


class Adapter:

    def __init__(self, path):
        self.path = path
        self.proc = None

    def start(self):
        self.proc = Popen([self.path], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

    def write(self, input, end='\n'):
        self.proc.stdin.write((input + end).encode())
        print('input')

    def readline(self):
        result = self.proc.stdout.readline().decode().strip()
        return result

    def stop(self):
        self.proc.kill()


def GetAdapter(path):
    return Adapter(path)
