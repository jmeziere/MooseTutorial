# MooseTutorial

Our setup.py
```
from setuptools import setup, find_packages
import os

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            if not filename.endswith('.pyc'):
                paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files('MooseTutorial')
setup(
        name='MOOSETutorial',
        version='0.1dev',
        packages=find_packages(),
        package_data ={'': extra_files},
        install_requires=['kivy','os','sys','subprocess','collection','image']
        )
```

Install command after getting the deb file
`sudo apt install ./name.deb`
