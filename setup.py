from cx_Freeze import setup, Executable

executables = [
    Executable('welcome.py')
]

setup(name='cxfreeze_demo',
      version='1.0',
      description='Sample cx_Freeze script',
      executables=executables
      )
