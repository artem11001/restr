from datetime import datetime
import os

# Путь до настоящего скрипта
scripDirAbs = os.path.abspath(os.path.dirname(__file__))
pathcd = str(os.path.split(scripDirAbs)[0])  # путь на каталог ниже
dirlog = (os.path.join(pathcd, 'log'))       # объеденение путей


class LogFile:
    """
    Класс логгера, иницируется по умолчанию flog = LogFile()
    Предполагает, что существует папка log на каталог выше
    Допонительные параменты:
        file_log = 'Mylog'   название файла
        cat      = '/log'    путь до каталога с логами
        dateFile = 0         Не добавлять в название файла дату
        printLog = 1         Доплнительно выводить логи в консль
    Запись flog('text')
    """
    def __init__(self,
                 cat: str = dirlog,
                 file_log: str = 'log.txt',
                 dateFile: bool = 1,
                 printLog: bool = 0) -> None:
        self.printLog = printLog
        self.cat = cat
        self.file_log = file_log
        if dateFile:
            self.dateFile = (datetime.now()).strftime("/%d-%m-%Y-")
        else:
            self.dateFile = '/'
        self.file_log_name = cat+self.dateFile+file_log

    def writefile(self, string: str) -> None:
        try:
            linestr = str(string)+'\n'
            self.file_log = open(self.file_log_name, 'a')
            self.file_log.write(linestr)
            if self.printLog:
                print(linestr)
        except IOError:
            print("msg Error!")
        finally:
            self.file_log.close()

    def __call__(self, string: str) -> None:
        self.writefile(string)

    def re(self):  # Стереть содиржимое файла
        f = open(self.file_log_name, 'w')
        f.close()
