from euroleague_api import *
import pandas as pd

season = 2023
game_code = 1

#df_game_reports_season = game_stats.get_game_stats_single_season(season)
#ruta_del_archivo_csv = 'C:/Users/Ferran/Documents/EUROLIGA/export/game_reports_2023.csv'
#df_game_reports_season.to_csv(ruta_del_archivo_csv, sep='|', index=False)

from sqlalchemy import create_engine

username = 'root'
password = 'rootpass'
host = '127.0.0.1'
port = '3306'
database = 'euroliga'

engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}')
df = shot_data.get_game_shot_data(season, game_code)
df.to_sql('test_game_shot_data', con=engine, if_exists='replace', index=False)