import cAdapter
import os

adapter = cAdapter.GetAdapter(os.path.abspath('./a.exe'))
adapter.start()
result = adapter.call('2')
print('the result is', result)