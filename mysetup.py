# mysetup.py
from distutils.core import setup
import glob
import py2exe

setup(console=["main.py"],
      data_files=[("conf.json")
                  ]
      )
