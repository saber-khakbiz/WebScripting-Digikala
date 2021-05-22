import mysql.connector
from InPutSetting import User, Host, PassWord, DataBase, tb
from WebScripting import Ram_lst

cnx = mysql.connector.connect(user=User, password=PassWord,
                              host=Host,
                              database=DataBase)

mycursor=cnx.cursor()

mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {DataBase}")
mycursor.execute(f'''
                    CREATE TABLE IF NOT EXISTS {tb} (  NameBrand VARCHAR(255),
                                        Capacity INT(255), 
                                        DDRX INT(255), 
                                        Frequency INT(255),
                                        Price INT(255))
                                        ''')

for ram in range(len(Ram_lst)):
    
    sql=f"INSERT INTO {tb} (NameBrand, Capacity, DDRX, Frequency, Price)\
    SELECT * FROM ( SELECT %s as col1, %s as col2, %s as col3, %s as col4, %s as col5) as temp\
    WHERE NOT EXISTS \
        (SELECT * FROM {tb} WHERE \
            NameBrand=%s AND Capacity=%s AND DDRX=%s AND Frequency=%s AND Price=%s) \
                LIMIT 1"
    
    val = ( Ram_lst[ram]["BrandName"],
            Ram_lst[ram]["Capacity"], 
            Ram_lst[ram]["DDRX"], 
            Ram_lst[ram]["frequency"], 
            Ram_lst[ram]["Price"],
            Ram_lst[ram]["BrandName"],
            Ram_lst[ram]["Capacity"], 
            Ram_lst[ram]["DDRX"], 
            Ram_lst[ram]["frequency"], 
            Ram_lst[ram]["Price"])
    
    mycursor.execute(sql, val)


print("\nCompleted!")
print(f"\n\nDone, Name & Capacity & Model & Frequency & Price of RAM Memorey inserted.\n")


cnx.commit()
cnx.close()