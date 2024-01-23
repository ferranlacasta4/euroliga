from euroleague_api import shot_data

season = 2024
game_code = 1

df = shot_data.get_game_shot_data(season, game_code)
df