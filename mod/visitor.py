import os
import option


class FileVisitor:
    def __init__(self,
                 context: str = None,
                 flog: any = print) -> None:
        self.fcount = 0
        self.dcount = 0
        self.context = context
        self.flog = flog

    def run(self,
            startDir: str = os.curdir,
            reset: bool = True) -> None:
        if reset:
            self.reset()
        for (thisDir, dirsHere, filesHere) in os.walk(startDir):
            self.visitdir(thisDir)
            for fname in filesHere:
                fpath = os.path.join(thisDir, fname)
                self.visitfile(fpath)

    def reset(self):
        self.fcount = self.dcount = 0

    def visitdir(self, dirpath):
        self.dcount += 1
        if self.flog:
            self.flog(f'{dirpath} ....')

    def visitfile(self, filepath):
        self.fcount += 1
        if self.flog:
            self.flog(f'{self.fcount} => {filepath}')


class SearchVisitor(FileVisitor):
    """
    Класс поиска строчных данных в файлах с указанным расширением
    SearchObj = SearchVisitor(serch='TextSears', extFile='.txt .py')
    SearchObj.run(startDir)
    """
    skipexts = ''              # игнор список
    testexts = '.txt .py'      # осуществлять поиск в файлах с расширением

    def __init__(self,
                 serchS: str = 'test',
                 extFile: str = testexts,
                 extSkip: str = skipexts,
                 flog: any = print) -> None:
        FileVisitor.__init__(self, serchS, flog)
        self.scount = 0
        try:
            self.extSkip = extSkip.split(' ')
            self.extFile = extFile.split(' ')
        except AttributeError:
            self.flog(f'{extSkip} or {extFile} not forat')

    def reset(self):
        self.scount = 0

    def visitdir(self, dirpath):
        print(dirpath, 1)
        self.dcount += 1

    def candidate(self, fname):
        ext = os.path.splitext(fname)[1]
        if self.extFile:
            return ext in self.extFile
        else:
            return ext not in self.extSkip

    def visitfile(self, fname):
        self.fcount += 1
        if not self.candidate(fname):
            if self.flog:
                pass
                # self.flog(f'skipping {fname}')
        else:
            text = open(fname).read()
            if self.context in text:
                self.visitmatch(fname, text)
                self.scount += 1

    def visitmatch(self, fname, test):
        self.flog(f'{fname} has {self.context}')


class CpallVisitor(FileVisitor):
    """
    Копирование дерева каталогов
    init  = CpallVisitor('/CopyCatFrom', '/CopeCatTo')
    init.run(startDir='/CopyCatFrom')
    """
    def __init__(self,
                 fromDir: str,
                 toDir: str,
                 flog: any = print) -> None:  # допилить наследование
        self.fromDirLen = len(fromDir) + 1
        self.toDir = toDir
        FileVisitor.__init__(self, flog)

    def visitdir(self, dirpath: str) -> None:
        toPath = os.path.join(self.toDir, dirpath[self.fromDirLen:])
        if self.flog:
            self.flog(f'dir copy {dirpath} => {toPath}')
        try:                                  # проверка сущестования каталога
            os.mkdir(toPath)
        except FileExistsError:
            print(f'\n {toPath} Error dir exists')
            self.flog(f'\n {toPath} Error dir exists')
            os._exit(1)
        self.dcount += 1

    def visitfile(self, filepath: str) -> None:
        toPath = os.path.join(self.toDir, filepath[self.fromDirLen:])
        if self.flog:
            self.flog(f'file colpy {filepath} => {toPath}')
        self.copyfile(filepath, toPath)
        self.fcount += 1

    @staticmethod
    def copyfile(pathFrom, pathTo, maxfileload=option.maxfileload):
        """ Копирует один файл из pathFrom from pathTO"""
        if os.path.getsize(pathFrom) <= maxfileload:
            bytesFrom = open(pathFrom, 'rb').read()
            open(pathTo, 'wb').write(bytesFrom)
        else:
            fileFrom = open(pathFrom, 'rb')
            fileTo = open(pathTo, 'wb')
            while True:
                bytesFrom = fileFrom.read(option.blksize)
                if not bytesFrom:
                    break
                fileTo.read(bytesFrom)


class ReStrVisitor(CpallVisitor, SearchVisitor):
    def __init__(self,
                 fromDir: str,
                 toDir: str,
                 fromStr: str,
                 toStr: str = None,
                 extFile: str = SearchVisitor.testexts,
                 extSkip: str = SearchVisitor.skipexts,
                 flog: any = print) -> None:
        SearchVisitor.__init__(self, fromStr, extFile, extSkip, flog=flog)
        self.fromDirLen = len(fromDir) + 1
        self.toDir = toDir
        self.toStr = toStr

    def visitfile(self, fname):
        SearchVisitor.visitfile(self, fname)

    def visitmatch(self, fname, test):
        CpallVisitor.visitfile(self, fname)

    def copyfile(self, pathFrom, pathTo, maxfileload=option.maxfileload):
        if self.toStr is None:
            CpallVisitor.copyfile(pathFrom, pathTo)
        else:
            text = open(pathFrom).read()
            fromStr, toStr = self.context, self.toStr
            text = text.replace(fromStr, toStr)
            open(pathTo, 'w').write(text)
