import csv
import datetime


def check_time(temp_time):
    time = datetime.time(0, 30, 0)

    temp_time = temp_time.split('.')
    h = m = s = 0
    for t in temp_time:
        if 'ч' in t:
            temp = t.strip().split()
            h = int(temp[0])
        elif 'мин' in t:
            temp = t.strip().split()
            m = int(temp[0])
        elif 'сек' in t:
            temp = t.strip().split()
            s = int(temp[0])

    temp_time = datetime.time(h, m, s)
    return temp_time > time


def main():
    # print(check_time('0 ч. 23 мин. 12 сек.'))

    with open('input.csv', encoding='utf-8') as fin:
        reader = csv.DictReader(fin, delimiter=',')

        students = []
        cnt_students = 0
        for row in reader:
            if row['Состояние'] == 'Завершено':
                if check_time(row['Затраченное время']) and row['Оценка/10,00'] == '9,00':
                    cnt_students += 1
                    students.append(row)

        for student in students:
            print(student)


if __name__ == '__main__':
    main()