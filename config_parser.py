import yaml
import re


def parse_configuration(config_data):
    # Убираем комментарии
    config_data = re.sub(r'!.*', '', config_data)
    config_lines = config_data.splitlines()

    # Словарь для хранения пар ключ-значение
    config_dict = {}

    # Основная логика парсинга
    for line in config_lines:
        line = line.strip()
        if line:
            # Обработка объявления константы
            if line.startswith('def'):
                match = re.match(r'def (\w+) = (.+)', line)
                if match:
                    key, value = match.groups()
                    config_dict[key] = parse_value(value)
            else:
                match = re.match(r'(\w+)\s*:\s*(.+);', line)
                if match:
                    key, value = match.groups()
                    config_dict[key] = parse_value(value)

    return yaml.dump(config_dict, default_flow_style=False)


def parse_value(value):
    if value.startswith('#(') and value.endswith(')'):
        # Обработка массива
        return [v.strip() for v in value[2:-1].split(',')]
    elif value.startswith('{') and value.endswith('}'):
        # Обработка словаря
        items = value[1:-1].split(',')
        dict_items = {}
        for item in items:
            k, v = item.split(':')
            dict_items[k.strip()] = parse_value(v.strip())
        return dict_items
    elif re.match(r'^\d+\.?\d*$', value):
        # Обработка чисел
        return float(value) if '.' in value else int(value)
    elif re.match(r'^\w+$', value):
        return value
    return value
