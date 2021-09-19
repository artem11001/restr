from mod.visitor import CpallVisitor, SearchVisitor, ReStrVisitor
from mod.log import LogFile


flog = LogFile(printLog=1)


if __name__ == '__main__':
    import os
    abspath = os.path.abspath(os.path.dirname(__file__))  # абсолюьный путь
    fromDir = os.path.join(abspath, 'test1')              # объеденение путей
    toDir = os.path.join(abspath, 'test2')
    SearchObj = ReStrVisitor(fromDir='www/mysite',
                             toDir='www/copysite',
                             fromStr='htttp://site.ru/test',
                             toStr='http://sitenwe.ru/test',
                             flog=flog)
    SearchObj.run(fromDir)
