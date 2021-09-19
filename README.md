 Копирование/поиск/замена в дереве каталогов<br>
 from mod.visitor import CpallVisitor, SearchVisitor, ReStrVisitor<br>
 from mod.log import LogFile<br><br>
 
 Поиск строк в файлах каталогов<br>
 MyObjS = SearchVisitor(serchS='http://mysite.ru', extFile='.html .htm .py') <br>
 MyObjS.run(startDir='www/mysite')   каталог поиска, полный путь<br>
    1. serchS   строка поиска<br>
    2. extFile  расширения файлов в которых происходит поиск, через пробел<br>
    3. skipexts необязательный параметр, расширения файлов игнора<br>
 
 Копирование каталог1 в каталог2<br>
 MyObjC = CpallVisitor(fromDir='/cat', toDir='/copyCat')<br>
 MyObjC.run(startDir='/cat')<br>
 
 Копирование с поиском и заменой строк<br>
 MyObjRe = ReStrVisitor(fromDir='www/mysite', toDir='www/copysite', fromStr='htttp://site.ru/test',toStr='http://sitenwe.ru/test')<br>
 MyObjC.run(startDir='www/mysite')<br>
      1. fromDir копируемый каталог<br>
      2. toDir   скопированный каталог<br>
      3. fromStr строка поиска для заемны<br>
      4. toStr   строка замены<br>
        доступный также<br>
          1. extFile  расширения файлов в которых происходит поиск, через пробел<br>
          2. skipexts необязательный параметр, расширения файлов игнора<br>
 
 Необязательный параметр для инициализации всех объектов<br>
 flog = LogFile(printLog=1)  объект логгера, записывает логи в папку log<br>
 MyObjC = CpallVisitor(fromDir='/cat', toDir='/copyCat', flog=flog)<br>
