import gs
import mdb
from datetime import datetime

def getQsum(donedict):
    return sum(list(donedict.values()))
def main():
    data = mdb.selectperfdata()
    #print(data)
    df = gs.read()
    #print(df)
    testnum = {'Нулевое': '0', 'Первое': '1', 'Второе': '2', 'Третье': '3', 'Четвёртое': '4', 'Упражнение 1': '5', 'Упражнение 2': '6', 'Упражнение 3': '7', 'Упражнение 4': '8'}
    donedict = {'Нулевое': 3, 'Первое': 5, 'Второе': 5, 'Третье': 4, 'Четвёртое': 7, 'Упражнение 1': 4, 'Упражнение 2': 4, 'Упражнение 3': 4, 'Упражнение 4': 5}
    performance = []
    attempts = []
    #print(df)
    #print(df['FIO'])
    for name in df['FIO'].tolist():
        #print(name)
        performance.append({'FIO': name, 'Нулевое': '', 'Первое': '', 'Второе': '', 'Третье': '', 'Четвёртое': '', 'Упражнение 1': '', 'Упражнение 2': '', 'Упражнение 3': '', 'Упражнение 4': '', 'О себе.py': '', 'Ошибки': [], 'Последняя активность': 'Никогда', 'AllDone': '', 'Успех': 0, '% Успех': 0, 'att': '', 'slot': ''})

    #print(data[0:2])
    for student in performance:
        tries = {}
        # 0 - Тест, 1 - ФИО, 2 - № попытки, 4 - № вопроса, 6 - шаг, 7 - состояние, 9 - дата, 12 - О себе.py, 13 - attempt id, 14 - question usage id
        for row in data:
            #print(row)
            if student['FIO'] == row[1]:
                #print(type(row[9]), row[9])
                if student['Последняя активность'] == 'Никогда' or datetime.strptime(row[9], '%Y-%m-%d %H:%M:%S') > datetime.strptime(student['Последняя активность'], '%Y-%m-%d %H:%M:%S'):
                    student['Последняя активность'] = row[9]#.strftime("%Y.%m.%d %H:%M:%S")
                    student['att'] = str(row[13])
                    student['slot'] = str(row[4])
                if row[7] == 'complete' and float(row[6]) > 0:
                    if student[row[0].split(' ')[0]+(' ' + row[0].split(' ')[1] if row[0].split(' ')[0]=='Упражнение' else '')] == '' or int(student[row[0].split(' ')[0]+(' ' + row[0].split(' ')[1] if row[0].split(' ')[0]=='Упражнение' else '')].split('.')[-2]) < float(row[4]):
                        student[row[0].split(' ')[0]+(' ' + row[0].split(' ')[1] if row[0].split(' ')[0]=='Упражнение' else '')] = "=HYPERLINK(\"https://moodle.surgu.ru/mod/quiz/review.php?attempt={}#question-{}-{}\"; \"{}\")".format(str(row[13]), str(row[14]), str(row[4]), str(row[2])+'.'+str(row[4])+'.'+str(row[6])) #П.В.Ш https://moodle.surgu.ru/mod/quiz/review.php?attempt=1355811#question-1529449-2
                    tries[testnum[row[0].split(' ')[0]+(' ' + row[0].split(' ')[1] if row[0].split(' ')[0]=='Упражнение' else '')] + '.' + str(row[4])] = 'complete'
                    # индекс теста.номер вопроса = 'complete'
                if not testnum[row[0].split(' ')[0]+(' ' + row[0].split(' ')[1] if row[0].split(' ')[0]=='Упражнение' else '')]+'.'+str(row[4]) in tries or not tries[testnum[row[0].split(' ')[0]+(' ' + row[0].split(' ')[1] if row[0].split(' ')[0]=='Упражнение' else '')]+'.'+str(row[4])] == 'complete':
                    if float(row[6]) > 0:
                        tries[testnum[row[0].split(' ')[0]+(' ' + row[0].split(' ')[1] if row[0].split(' ')[0]=='Упражнение' else '')] + '.' + str(row[4])] = '\''+testnum[row[0].split(' ')[0]+(' ' + row[0].split(' ')[1] if row[0].split(' ')[0]=='Упражнение' else '')] + '.' + str(row[2])+'.'+str(row[4])+'.'+str(row[6])
                #print(row[12])
                if not student['О себе.py'] == "'+" and (not row[12] == None) and row[12] == "2.0":
                     student['О себе.py'] = "'+"
                     student['Успех'] += 1

        alldone = 0
        nullisdone = True
        for k in donedict:
            testdone = True
            for q in range(donedict[k]):
                if not (testnum[k]+'.'+str(q+1) in tries) or not tries[testnum[k]+'.'+str(q+1)] == 'complete':
                    testdone = False
            if testdone:
                student[k] = '\'+'
                alldone += 1
        if student['Первое'] == '\'+' and student['Второе'] == '\'+':
            for q in range(donedict['Нулевое']):
                if not (testnum['Нулевое']+'.'+str(q+1) in tries) or not tries[testnum['Нулевое'] + '.' + str(q + 1)] == 'complete':
                    nullisdone = False
                tries[testnum['Нулевое'] + '.' + str(q + 1)] = 'complete'
            student['Нулевое'] = '\'+'
            if not nullisdone:
                alldone += 1
        if alldone == len(donedict):
            student['AllDone'] = '\'+'

        for k in tries:
            if not tries[k] == 'complete':
                student['Ошибки'].append(tries[k])
            else:
                student['Успех'] += 1
        student['% Успех'] = str((student['Успех']/getQsum(donedict))*100)[0:5]
        student['Ошибки'] = ', '.join(student['Ошибки'])
    #print(performance)
    for dict in performance:
        if not dict['Последняя активность'] == 'Никогда':
            dict['Последняя активность'] = "=HYPERLINK(\"https://moodle.surgu.ru/mod/quiz/reviewquestion.php?attempt={}&slot={}\";\"{}\")".format(dict['att'], dict['slot'], dict['Последняя активность'])
    newperformance = [[key for key in performance[0].keys()]]
    newperformance += [list(row.values())[0:-2] for row in performance]
    for row in newperformance:
        print(row)
    #gs.write(newperformance[1:], 'Performance2023')
    # newdata = []
    # newdata += [list(row)[0:-4] for row in data]
    # #print(newdata)
    # gs.write(newdata, 'data')

if __name__ == '__main__':
    #print(__name__)
    main()