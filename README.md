# Домашнее задание 2
## Добавление фич в скрипт для статического анализа кода.

https://gist.github.com/VladimirFilonov/775853d680f4ea7f0ce5a75d094490f7

Нужно доработать скрипт из первого задания. Вот что он должен уметь:

* клонировать репозитории с Гитхаба;
* выдавать статистику самых частых слов по глаголам или существительным (в зависимости от параметра отчёта);
* выдавать статистику самых частых слов названия функций или локальных переменных внутри функций (в зависимости от параметра отчёта);
* выводить результат в консоль, json-файл или csv-файл (в зависимости от параметра отчёта);
* принимать все аргументы через консольный интерфейс.

При доработке предусмотреть, что вскоре в программу понадобится добавлять:

* получение кода из других места, не только с Гитхаба;
* парсеры других ЯП, не только Python;
* сохранение в кучу разных форматов;
* более сложные типы отчётов (не только частота частей речи в различных местах кода).

## Установка
В корневой директории проекта выполнить:
	python setup.py install

## Использование
### Вызов
	words_count --repo <путь_к_репозиторию> [--local <локальный_путь>] [--pos <часть_речи>] [--nametype <тип_элементов_кода>] [{--csv <путь_к_файлу_csv> | --json <путь_к_файлу_json>}]

### Опции
**--repo <путь_к_репозиторию>**
Путь к клонируемому репозиторию.

**--local <локальный_путь>**
Путь на локальном диске, куда будет клонирован репозиторий. Если параметр не задан, по умолчанию используется значение **/tmp/tmp_repo**.

**--pos <часть_речи>**
Часть речи, частоту использования которой требуется подсчитать. Принимает значения **noun** (существительное) и **verb** (глагол). Если параметр не задан, по умолчанию используется значение **noun**.

**--nametype <тип_элементов_кода>**
Тип элементов кода, в которых требуется подчитать использование заданных частей речи. Принимает значения **functions** (названия функций) и **variables** (локальные переменные в телах функций). Если параметр не задан, по умолчанию используется значение **functions**.

**--csv <путь_к_файлу_csv>**
Указание на то, что отчёт должен формироваться в формате CSV, и путь к формируемому CSV-файлу.

**--json <путь_к_файлу_json>**
Указание на то, что отчёт должен формироваться в формате JSON, и путь к формируемому JSON-файлу.

Если не заданы параметры --json и --csv, то отчёт выводится на экран.

### Пример
words_count --repo "https://github.com/lanceotus/hw1" --local "/tmp/repo_hw1" --nametype variables --pos noun --csv "/tmp/res.csv"
