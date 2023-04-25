import csv
import datetime

interest_date = None

months = {
    'Январь': 1, 'Февраль': 2, 'Март': 3, 'Апрель': 4, 'Май': 5, 'Июнь': 6,
    'Июль': 7, 'Август': 8, 'Сентябрь': 9, 'Октябрь': 10, 'Ноябрь': 11, 'Декабрь': 12
}


def check_date(temp_date):
    temp_date = temp_date.split()
    temp_date = datetime.datetime(int(temp_date[2]), months[temp_date[1]], int(temp_date[0]))
    return temp_date > interest_date


def main():
    # 06 04 2017
    print('Введите заданную дату...')

    global interest_date
    interest_date = list(map(int, input().split()))
    interest_date = datetime.datetime(interest_date[2], interest_date[1], interest_date[0])

    with open('input.csv', encoding='utf-8') as fin:
        # reader = csv.DictReader(fin, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        reader = csv.DictReader(fin, delimiter=',')

        # print(check_date('5 Май 2017 13:23'))

        students = 0
        check_students = 0
        for row in reader:
            if row['Состояние'] == 'Завершено':
                students += 1
                if check_date(row['Завершено']) and row['Оценка/10,00'] in ['8,00', '9,00', '10,00']:
                    check_students += 1
                    # print(row)
        print(f'{ 100 * check_students / students}% студентов')


if __name__ == '__main__':
    main()