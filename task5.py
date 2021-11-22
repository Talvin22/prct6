col = input("Введите цвета введенные через запятую: ")


a = [i for i in col.split(",")]
print(",".join(sorted(list(set(a)))))