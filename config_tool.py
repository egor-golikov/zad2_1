import argparse
from config_parser import parse_configuration


def main():
    parser = argparse.ArgumentParser(description='Преобразовать пользовательский конфигурационный язык в YAML.')
    parser.add_argument('input_file', type=str, help='Путь к входному файлу конфигурации')
    parser.add_argument('output_file', type=str, help='Путь к выходному YAML файлу')

    args = parser.parse_args()

    with open(args.input_file, 'r') as infile:
        config_data = infile.read()

    yaml_data = parse_configuration(config_data)

    with open(args.output_file, 'w') as outfile:
        outfile.write(yaml_data)


if __name__ == "__main__":
    main()
