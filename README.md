### Тестовое задание для вакансии «Инженер по автоматизации тестирования»

***

### Tests and linter status:
[![Actions Status](https://github.com/ajib6ept/testtask-qa-automator-reg-ru/workflows/docmain-counter-check/badge.svg)](https://github.com/ajib6ept/testtask-qa-automator-reg-ru/actions) [![Maintainability](https://api.codeclimate.com/v1/badges/8585576eea5c677b2cb3/maintainability)](https://codeclimate.com/github/ajib6ept/testtask-qa-automator-reg-ru/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/8585576eea5c677b2cb3/test_coverage)](https://codeclimate.com/github/ajib6ept/testtask-qa-automator-reg-ru/test_coverage)

## Утилита для обработки доменов

### Установка
* Установить [poetry](https://python-poetry.org/docs/#installation)
* ```git clone https://github.com/ajib6ept/testtask-qa-automator-reg-ru.git```
* ```cd testtask-qa-automator-reg-ru/ && make install```
* ```make build```
* ```make package-install```

#### Использование
* ```domain-counter myfile.txt```
***
###### Пример работы 
[![asciicast](https://asciinema.org/a/OmhoUG2D7lngzgnV3oG8Sz39G.svg)](https://asciinema.org/a/OmhoUG2D7lngzgnV3oG8Sz39G)


## Задание


Предлагается создать утилиту командной строки, которая обрабатывает данные способом, описанным ниже, и возвращает результат в STDOUT.

### ВХОДНЫЕ ДАННЫЕ:
В командной строке указывается имя текстового файла. Текстовый файл с email-адресами (разделитель — перевод строки). Пример:
info@mail.ru  
support@vk.com  
ddd@rambler.ru  
roxette@mail.ru  
sdfsdf@@@@@rdfdf  
example@localhost  
иван@иванов.рф  
ivan@xn--c1ad6a.xn--p1ai  
### СУТЬ ОБРАБОТКИ:
Группировка адресов по имени домена, подсчёт email-адресов для каждого домена.

### ВЫХОДНЫЕ ДАННЫЕ:
Имена доменов и количество адресов в каждом домене. Сортировка по количеству адресов в домене, по убыванию. Отдельной строкой — количество невалидных адресов. Пример:
mail.ru	2  
vk.com	1  
rambler.ru	1  
INVALID	1  

Задача может быть решена на любом языке программирования, но предпочтительно Perl, Python или Ruby. Созданная программа, должна быть максимально покрыта автоматическими тестами (юнит тесты и т.п.), валидирующими все аспекты функционирования программы и покрывающими максимальное количество кода программы.


https://www.reg.ru/company/jobs/testtask-qa-automator
