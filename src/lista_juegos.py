def read_csv(file_name):
    f = open(file_name, "r")
    f.readline()
    data = []
    for row in f:
        values = row.strip().split(",")
        data.append(values)
    f.close()
    return data

juegos = read_csv("C:/Users/jorge/Downloads/vgsales.csv")

print(juegos[179])
