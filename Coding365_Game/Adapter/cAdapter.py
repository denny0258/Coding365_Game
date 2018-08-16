from subprocess import Popen, PIPE, STDOUT


class Adapter:

    def __init__(self, path):
        self.path = path
        self.proc = None

    def start(self):
        self.proc = Popen([self.path], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

    def write(self, input, end='\r\n'):
        self.proc.stdin.write((input + end).encode())
        self.proc.stdin.close()

    def readline(self):
        return self.proc.stdout.readline().decode().strip()

    def stop(self):
        self.proc.kill()


def GetAdapter(path):
    return Adapter(path)
