import pandas as pd

# Pandas has The method unique
# to determine the unique elements 
# in a column of a data frame.  

songs = {'Album': ['Thriller','Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat Out of Hell'],
         'Released':[1982,1980,1973,1992,1977],
         'Length':['00:42:19','00:42:11','00:42:49','00:57:44','00:46:33']}

# Let's say we would like to create a new database consisting of songs from the 1980s and after.
# We can look at the column released for songs made after 1979, then select the corresponding columns.
# We can accomplish this within one line of code in Pandas.
songs_frame = pd.DataFrame(songs) # df = dataframe | pd = pandas
df1 = songs_frame[songs_frame['Released']>=1980]
df1.to_csv('csv/new_songes.csv')
# print(df1)


# Another Ex. ----------------------------------------------------------------------------------------
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
# print(df)

# Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
# print(x)

#check the type of x
type(x) # <class 'pandas.core.frame.DataFrame'>


#Retrieving the Department, Salary and ID columns and assigning it to a variable z
z = df[['Department','Salary','ID']]
# print(z)

#LAB-----------------------------------------------------
students = {'Student':['David','Samuel','Terry','Evan'],'Age':[27,24,22,32],
            'Country':['UK','Canada','China','USA'],
            'Course':['Python','Data Structures','Machine Learning','Web Development'],
            'Marks':['85','72','89','76']
           }

df2 = pd.DataFrame(students)
b = df2['Marks']

c = df2[['Country','Course']]
print(b)




# Read data from CSV file
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)

# Print first five rows of the dataframe
df.head()




# Read data from Excel File and print the first five rows
xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'
df = pd.read_excel(xlsx_path)
df.head()

# Access to the column Length
x = df[['Length']]
x