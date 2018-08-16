import cAdapter
import os

adapter = cAdapter.GetAdapter(os.path.abspath('./a.exe'))
adapter.start()
adapter.write('2')
result = adapter.readline()
print('the result is', result)