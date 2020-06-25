with open('demo.txt', 'r') as f1:
    with open("demo2.txt", "w+") as f2:
        list2 = f2.readlines()
        print(list2)
        list1 = f1.readlines()
        for row_data in list1:
            name, s_id = row_data.split(",")
            if name == "张三":
                row_data = row_data.replace("张三", "xx")

            f2.writelines(row_data)
