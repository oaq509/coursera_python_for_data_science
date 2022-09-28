# pandas | popular library for data analysis
# import pandas
import pandas as pd

# csv_path = 'csv/file1.csv'
# df = pd.read_csv(csv_path) # df = dataframe
# print(df.head())

songs = {'Album': ['Thriller','Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat Out of Hell'],
         'Released':[1982,1980,1973,1992,1977],
         'Length':['00:42:19','00:42:11','00:42:49','00:57:44','00:46:33']}

songs_frame = pd.DataFrame(songs)
songs_frame = pd.DataFrame(['Length']) # New dataframe with the Column
print(songs_frame)