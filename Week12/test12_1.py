import csv

line_counter = 0
data_header = []
employee = []
customer_France_only_list = []
customer = None

with open("C://Dongduk//4-1summer//Bigdata//DONGDUK_4_1_SUMMER//Week12//customers.csv", "r") as customer_data :
    while 1 :
        """csv_data = csv.reader(customer_data)
        for row in csv_data :
            if line_counter == 0:
                header = row

        if row[10].upper() == "FRANCE" :
            customer_France_only_list.append(row)
        line_counter +=1 """
        data = customer_data.readline()
        if not data :
            break
        if line_counter == 0 :
            data_header = data.split(",")

        else :
            customer = data.split(",")
            if customer[10].upper() == "FRANCE" :
                customer_France_only_list.append(customer)
        line_counter += 1

    print("Header:", data_header)
    for i in range(0, 10) :
        print("Data:", customer_France_only_list[i])
    print(len(customer_France_only_list))

    with open("customers_France_only.csv", "w") as customer_france_only_csv :
        for customer in customer_France_only_list :
            customer_france_only_csv.write(",".join(customer).strip('\n') +"\n")