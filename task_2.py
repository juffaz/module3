print('Задача 2. Финансовый отчёт')

# Наде дали задание сформировать финансовый отчёт за последние 20 лет по полугодиям. 
# Нужно сумму дохода первых двух кварталов поделить на сумму последних двух кварталов, 
# чтобы понять динамику роста или падения дохода. И так за каждый год. 
# 
# Надя решила, 
# что быстрее будет написать простую программу, которая сделает всё за неё.
# 
# 
# Запросите у пользователя четыре числа.
# Отдельно сложите первые два и отдельно вторые два.
# Разделите первую сумму на вторую.
# Выведите результат на экран.

finReportOne = int(input("Введите первое число первого квартала: "))
finReportTwo = int(input("Введите второе число первого квартала: "))
finReportThree = int(input("Введите первое число второго квартала: "))
finReportFour = int(input("Введите второе число второго квартала: "))

finSumOneYear = finReportOne + finReportTwo
finSumTwoYear = finReportThree + finReportFour

finResult = finSumOneYear / finSumTwoYear

print("Результат финансового отчета по полугодию: ", finResult)