import main
import os, sys

create = [sys.executable, 'main.py']

def test_output(capfd):
  os.system('python ./main.py')
  captured = capfd.readouterr()
  assert captured.out == 'Hello World!\n', "Output is not 'Hello World!'"