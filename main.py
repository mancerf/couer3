from until.function import get_formatted_data, get_filtered_data, get_last_values
from scr.get_file import file_open


def main():
    data = file_open()
    data = get_filtered_data(data)
    data = get_last_values(data, 5)
    data = get_formatted_data(data)
    print('INFO: Вывод транзакции...')
    for row in data:
        print(row, end='\n\n')


if __name__ == "__main__":
    main()
