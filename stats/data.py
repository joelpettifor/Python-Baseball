import os
import glob
import pandas as pd

game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))
list.sort(game_files)

for game_file in game_files
    game_frame = pd.read_csv(game_file,names = ['type','multi2','multi3','multi4','multi5','multi6','event'])
