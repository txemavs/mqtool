# -*- coding: utf-8 -*-

import py2exe
from distutils.core import setup

setup(
    name="MQTool",
    version="0.0.1",
    description="Simple MQTT publish/subscribe tool",
    author="Txema Vicente",
    console=[{"script": "mqtool.py"}],
    options={
        "py2exe":{
            "unbuffered": True,
            "optimize": 2,
            "bundle_files": 1,
            "excludes": [
                "pywin",
                "pywin.debugger",
                "pywin.debugger.dbgcon",
                "pywin.dialogs",
                "pywin.dialogs.list",
                "Tkconstants",
                "Tkinter",
                "tcl"
            ],
            "dll_excludes":["MSVCP90.dll"]
        }
    },
    zipfile = None
)
