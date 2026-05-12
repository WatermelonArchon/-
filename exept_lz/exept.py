import pandas as pd

class Except:

    def __init__(self):
        self.df = None

    def open_file(self):
        try:
            name_file = input('введите имя файла:')
            if name_file != 'var5.csv':
                raise ValueError('ПЕРЕСМОТРИ НАЗВАНИЕ ФАЙЛА!!!')
            
            self.df = pd.read_csv(name_file)
            print('Файл открыт')
            
        except (FileNotFoundError, ValueError) as e:
            print(e)  
        except Exception:
            print('Не удалось открыть файл')


    def check_empty(self):
        try:
            if self.df.empty: 
                raise ValueError  
            print('Файл содержит данные')
        except AttributeError:
            print('Файл не был открыт')
        except ValueError:
            print('Файл пуст')

    def check_structure(self):
        try:
            if not isinstance(self.df, pd.DataFrame):  
                raise TypeError
            print('Структура файла правильная')
        except AttributeError:
            print('Файл не был открыт')
        except TypeError:
            print('Неправильная структура файла: ожидается таблица, а получен текст')
        except pd.errors.ParserError:
            print('Ошибка парсинга: файл не является корректной таблицей')

    def check_header(self, expected_columns):
        try:
            actual_columns = list(self.df.columns)
            if actual_columns != expected_columns:
                raise ValueError
            print('Заголовок корректен')
        except AttributeError:
            print('Файл не был открыт')
        except ValueError:
            print('Ошибка в первом ряду: заголовок не соответствует ожидаемому')


file = Except()
file.open_file()
file.check_structure()
file.check_empty()
file.check_header(["Участники гражданского оборота", "Тип операции", "Сумма операции",
                           "Вид расчета","Место оплаты","Терминал оплаты","Дата оплаты","Время оплаты",
                           "Результат операции", "Cash-back","Сумма cash-back"])  
       
