# Платформа
Проект разрабатывался под Debian jessie x64, Python 3.6.

# Структура
Файлы dummy.service и dummy.sh - это юнит-файл для systemd и сама служба.

# Допущения
* Случай, когда несколько человек одновременно взаимодействуют с приложением, не обрабатывается
* Предполагается, что у пользователя разрешено выполнение js-кода
* ~~Если сервис убьёт кто-то посторонний, приложение об этом не узнает~~ (FIXED)
