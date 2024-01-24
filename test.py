from euroleague_api import *
import pandas as pd
from sqlalchemy import create_engine

season = 2023
game_code = 1


#ruta_del_archivo_csv = 'C:/Users/Ferran/Documents/EUROLIGA/export/game_reports_2023.csv'
#df_game_reports_season.to_csv(ruta_del_archivo_csv, sep='|', index=False)

username = 'root'
password = 'rootpass'
host = '127.0.0.1'
port = '3306'
database = 'euroliga'

engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}')

df_game_reports_season = game_stats.get_game_stats_single_season(season)
df_game_reports_season.to_sql('game_reports_season_v2', con=engine, if_exists='replace', index=False)
