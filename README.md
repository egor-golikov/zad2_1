
## Задание №3
Разработать инструмент командной строки для учебного конфигурационного
языка, синтаксис которого приведен далее. Этот инструмент преобразует текст из
входного формата в выходной. Синтаксические ошибки выявляются с выдачей
сообщений.

Входной текст на языке json принимается из стандартного ввода. Выходной
текст на учебном конфигурационном языке попадает в файл, путь к которому
задан ключом командной строки.
Однострочные комментарии:
NB. Это однострочный комментарий
Словари:
table(
 имя => значение,
 имя => значение,
 имя => значение,
 ...
)
Имена:
[a-zA-Z]+
Значения:
• Числа.
71
• Строки.
• Словари.
Строки:
'Это строка'
Объявление константы на этапе трансляции:
значение -> имя;
Вычисление константы на этапе трансляции:
?[имя]
Результатом вычисления константного выражения является значение.
Все конструкции учебного конфигурационного языка (с учетом их
возможной вложенности) должны быть покрыты тестами. Необходимо показать 3
примера описания конфигураций из разных предметных областей.

## Cодержание проекта

json_to_custom - код программы

test_json_to_custom - тест программы


output1.txt - Вывод программы №1

output2.txt - Вывод программы №2

output3.txt - Вывод программы №3

## Тесты программы

Запуск программы 

``` python json_to_custom.py output.txt ```

Ввод программы №1
```
{
    "appName": "MyApp",
    "windowSize": {
        "width": 800,
        "height": 600
    },
    "theme": "dark"
}
```

Ввод программы №2
```   
{
      "deviceName": "Sensor",
      "parameters": {
          "maxTemp": 100,
          "minTemp": 0
      },
      "alerts": {
          "onMax": "Shutdown"
      }
}
```

Ввод программы №3
```
{
    "host": "localhost",
    "port": 5432,
    "username -> dbUser": "admin",
    "password -> dbPassword": "secret",
    "credentials": {
        "username": "?[dbUser]",
        "password": "?[dbPassword]"
    }
}
```
Для завершения ввода необходимо нажать "Ctrl" + "Z"
При использовании программы, вывод сохранаяется в output.txt
Цифры были добавлены для демонстрации примера.

## Тесты программы 

Все тесты прописаны в файле test_json_to_custom.py

Запускаются из командной строки

``` pytest test_json_to_custom.py ```

Результаты тестирования:
![image](https://github.com/user-attachments/assets/43b7ac6c-de15-4ac4-9fd3-5f8007274338)




