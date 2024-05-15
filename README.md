# Syslog-generator
Random Syslog Message Generator
This Python script is a random Syslog message generator that sends messages to a specified IP address and port using the UDP protocol. The script generates random messages with different priority levels and sends them to a given network address.

# Usage
To use the script, you must pass the IP address, port, and number of events per second as arguments when running. For example:

<code>python script.py [IP ADDRESS] [PORT] [EPS] [MODE] [BACKGROUND (optional)]<code>
> python script.py 192.168.1.100 514 100 random

where 192.168.1.100 is the IP address, 514 is the port number, and 100 is the number of events per second.

## Mode
- random - generate random messages
- file - read messages from file

Option <code>background<code> run the application in the background process

## requirements
The script is written in Python 3 and uses the following libraries:
- faker
- python-daemon

# Генератор случайных Syslog-сообщений
Этот Python-скрипт представляет собой генератор случайных Syslog-сообщений, который отправляет сообщения на указанный IP-адрес и порт с использованием протокола UDP. Скрипт генерирует случайные сообщения с разными уровнями приоритета и отправляет их на заданный сетевой адрес.

# Использование
Для использования скрипта необходимо передать IP-адрес, порт и количество событий в секунду в качестве аргументов при запуске. Например:

> <code>python script.py 192.168.1.100 514 100</code>
где 192.168.1.100 - это IP-адрес, 514 - номер порта, а 100 - количество событий в секунду.

## Требования
Скрипт написан на Python 3 и использует следующие библиотеки, которые необходимо установить:
- faker
- python-daemon

# Описание работы
Скрипт генерирует случайное сообщение с уровнем приоритета от 0 до 7.
Для каждого сообщения генерируется текущее время в формате "Месяц День Час:Минута:Секунд".
В сообщении также включается случайно выбранный тип сообщения из вариантов "alert", "info", "warn" и "event".
После формирования сообщения оно отправляется на указанный IP-адрес и порт с использованием протокола UDP.

## Примечание
Данный скрипт может быть использован для тестирования и отладки систем, обрабатывающих Syslog-сообщения, или в качестве примера использования многопоточности для отправки сообщений на удаленный сервер.

### Автор
Автор: Anton Kalinin
