#!/usr/bin/env python
import os
import tempfile
import shutil

FILE_UPLOAD_DIR = '/home/nyros/Desktop/newprojects/remotedbi/sqlitedatabase'


def upload_handle(source):
    #print source.name
    #fd, filepath = tempfile.mkstemp(prefix=source.name, dir=FILE_UPLOAD_DIR)
    #print fd
    with open(FILE_UPLOAD_DIR+'/'+source.name, 'wb') as dest:
        shutil.copyfileobj(source, dest)
    return FILE_UPLOAD_DIR+'/'+source.name
