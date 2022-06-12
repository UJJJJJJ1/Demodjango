import os,twstock,sqlite3
import pandas as pd
from tqdm import tqdm
import time
import random
conn=sqlite3.connect(os.path.join(os.path.dirname(os.path.dirname(__file__)),'db.sqlite3'))

tenStock=['1301','1303','2317','2330','2412','2454','2603','2881','2882','6505']

def fetch_from(self,year:int,month:int):
    self.raw_data=[]
    self.data=[]
    today = datetime.datetime.today()
    for year,month in self._month_year_iter(month,year,today.month,today.year):
        self.raw_data.append(self.fetcher.fetch(year,month,self.sid))
        self.data.extend(self.raw_data[-1]['data'])
        time.sleep(random.randint(5,10))
    return self.data

for i in tqdm(tenStock,ncols=100):
    everyStock = twstock.Stock(i,initial_fetch=False)
    StockHistory = pd.DataFrame(everyStock.fetch(2021,1))
    StockHistory.to_sql(i,conn,if_exists='append',index=False)
    time.sleep(10)
conn.commit()
conn.close()
