 Копирование/поиск/замена в дереве каталогов
 from mod.visitor import CpallVisitor, SearchVisitor, ReStrVisitor
 from mod.log import LogFile
 
 Поиск строк в файлах каталогов
 MyObjS = SearchVisitor(serchS='http://mysite.ru', extFile='.html .htm .py')
 MyObjS.run(startDir='www/mysite')   каталог поиска, полный путь
    serchS   строка поиска
    extFile  расширения файлов в которых происходит поиск, через пробел
    skipexts необязательный параметр, расширения файлов игнора
 
 Копирование каталог1 в каталог2
 MyObjC = CpallVisitor(fromDir='/cat', toDir='/copyCat')
 MyObjC.run(startDir='/cat')
 
 Копирование с поиском и заменой строк
 MyObjRe = ReStrVisitor(fromDir='www/mysite',
                       toDir='www/copysite',
                       fromStr='htttp://site.ru/test',
                       toStr='http://sitenwe.ru/test',)
 MyObjC.run(startDir='www/mysite')
      fromDir копируемый каталог
      toDir   скопированный каталог
      fromStr строка поиска для заемны
      toStr   строка замены
        доступный также
          extFile  расширения файлов в которых происходит поиск, через пробел
          skipexts необязательный параметр, расширения файлов игнора
 
 Необязательный параметр для инициализации всех объектов
 flog = LogFile(printLog=1)  объект логгера, записывает логи в папку log
 MyObjC = CpallVisitor(fromDir='/cat', toDir='/copyCat', flog=flog)
