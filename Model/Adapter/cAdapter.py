import pexpect

def GetAdapter(pathToExe):
    proc = pexpect.spawn(pathToExe)