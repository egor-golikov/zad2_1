import unittest
import os
from config_parser import parse_configuration


class TestConfigParser(unittest.TestCase):
    def test_file_creation(self):
        input_config = "def a = 5\nkey: value;\n"
        output_file = 'output.yaml'

        # Проверяем, создастся ли файл после обработки
        with open('test_input.conf', 'w') as f:
            f.write(input_config)

        parse_configuration(input_config)

        # Создаем файл, чтобы протестировать его создание
        with open(output_file, 'w') as outfile:
            outfile.write(parse_configuration(input_config))

        self.assertTrue(os.path.exists(output_file))

        # Чистим после теста
        os.remove('test_input.conf')
        os.remove(output_file)


if __name__ == '__main__':
    unittest.main()
