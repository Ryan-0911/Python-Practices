import pandas as pd
import sqlalchemy 
from sqlalchemy import create_engine

print('sqlalchemy version: ', sqlalchemy.__version__)

con_str = "mysql://ami_ro_ryan:Rjhf5v^a9Wke@192.168.102.159/wBSC"
engine = create_engine(con_str)
query = """select * from devices where type = 1 and timestamp > 2024-06-27"""

pd.set_option('display.max_columns', 500)
df_read_sql = pd.read_sql(query, engine)
print(df_read_sql)