import csv
import datetime

# interest_date = None
#
# months = {
#     'Январь': 1, 'Февраль': 2, 'Март': 3, 'Апрель': 4, 'Май': 5, 'Июнь': 6,
#     'Июль': 7, 'Август': 8, 'Сентябрь': 9, 'Октябрь': 10, 'Ноябрь': 11, 'Декабрь': 12
# }
#
#
# def check_date(temp_date):
#     temp_date = temp_date.split()
#     temp_date = datetime.datetime(int(temp_date[2]), months[temp_date[1]], int(temp_date[0]))
#     return temp_date > interest_date


def main():
    # 06 04 2017
    # print('Введите заданную дату...')

    # global interest_date
    # interest_date = list(map(int, input().split()))
    # interest_date = datetime.datetime(interest_date[2], interest_date[1], interest_date[0])

    with open('input.csv', encoding='utf-8') as fin:
        # reader = csv.DictReader(fin, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        reader = csv.DictReader(fin, delimiter=',')

        # print(check_date('5 Май 2017 13:23'))

        # students = 0
        check_students = 0
        students = {}
        for row in reader:
            if row['Состояние'] == 'Завершено':
                fio = f'{row["Имя"]} {row["Фамилия"]}'
                if row['Оценка/10,00'] in ['0,00', '1,00', '2,00', '3,00', '4,00'] or fio in students.keys():
                    if students.setdefault(fio) is None:
                        students[fio] = {
                            'data': row,
                            'tries': []
                        }
                    else:
                        date = row['Тест начат'].split()
                        date = f'{date[0]} {date[1]} {date[2]}'
                        students[fio]['tries'].append(date)

        for fio, info in students.items():
            print(info['data'])
            print(f'Next tries: {info["tries"]}')
            print()


if __name__ == '__main__':
    main()