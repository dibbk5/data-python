open_file = open("CupcakeInvoices.csv")

total_order = 0

for line in open_file:
    line = line.strip()
    values = line.split(",")
    print(values[2])
    print(int(values[3])*float(values[4]))
    total_order += int(values[3])*float(values[4])

print(total_order)

open_file.close()
