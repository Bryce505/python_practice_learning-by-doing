Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'C:\\ProgramData\\Anaconda3\\Lib\\idlelib'
>>> os.chdir('D:\python\pythonscripts')
>>> os.getcwd()
'D:\\python\\pythonscripts'
>>> import census2010
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    import census2010
ModuleNotFoundError: No module named 'census2010'
>>> import CENSUS2010
>>> CENSUS2010.all_data['AK']['Anchorage']
{'pop': 291826, 'tracts': 55}
>>> 