##
##Create SQLTITE database
##

import pandas as pd
import sqlite3

users = pd.read_excel(r"C:\Users\Heinrich\OneDrive - Stellenbosch University\Desktop\Projects\SQLite Database Creation\Users.xlsx")
stock = pd.read_excel(r"C:\Users\Heinrich\OneDrive - Stellenbosch University\Desktop\Projects\SQLite Database Creation\Stockmaster.xlsx")
masterdata = pd.read_excel(r"C:\Users\Heinrich\OneDrive - Stellenbosch University\Desktop\Projects\SQLite Database Creation\MasterData.xlsx")


cxn = sqlite3.connect('testDatabase.db')


print(users.head())
print(stock.head())
print(masterdata.head())

users.to_sql(name="Users",con=cxn, )
stock.to_sql(name="Stock",con=cxn, )
masterdata.to_sql(name="Masterdata",con=cxn,)

cxn.commit()
cxn.close()