"""
This Test :
------------------------------------------------------
'init' in                           0.011628 secs
'GetCursorImageArray' in            0.000872 secs
'SaveImage' in                      0.010361 secs
------------------------------------------------------


Test Inside Xcursor :
------------------------------------------------------
Import Libs : 0.152991 secs

Finished '__init__' in         0.012024 secs

        --- 'GetCursorImageArray' ---
Finished    'GetCursorImageData'  in            0.000074 secs
Finished    'argbdata_to_pixdata' in            0.000734 secs
        --- Finished in 0.000886 secs ---

Finished 'SaveImage' in        0.011071 secs
------------------------------------------------------
"""

import time
def timer(func):
    def wrapper_timer(*args, **kwargs):
        #start_time = time.perf_counter()
        start_time = time.time() 
        value = func(*args, **kwargs)
        #run_time = time.perf_counter() - start_time
        run_time = time.time() - start_time
        print(f"{func.__name__!r} in {' '*(30-len(func.__name__))}{run_time:.6f} secs")
        return value
    return wrapper_timer

from pyxcursor import Xcursor

@timer
def init(): 
    return Xcursor()

cursor = init()

@timer
def GetCursorImageArray():
    return cursor.GetCursorImageArray()

@timer
def SaveImage(imgarray,text):
    cursor.SaveImage(imgarray,text)


imgarray = GetCursorImageArray()
SaveImage(imgarray,'cursor_image.png')
