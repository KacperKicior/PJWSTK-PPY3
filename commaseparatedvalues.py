csv = input("Podaj liczby oddzielone przecinkami: ")
csv_list = csv.split(',')

n_max = int(csv_list[0])
n_min = int(csv_list[0])

for csv in csv_list:
    if n_min > int(csv):
        n_min = int(csv)
    if n_max < int(csv):
        n_max = int(csv)

print("Max: ", n_max)
print("Min: ", n_min)
