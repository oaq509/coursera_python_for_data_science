# For loop example
dates = [1982,1980,1973]
N = len(dates)
for i in range(N):
    print(dates[i])    
    
# Example of for loop 
for i in range(0, 8):
    print(i) 

# Write your code below and press Shift+Enter to execute
for i in range(-4,5):
    print(i)
    
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)
    

squares=['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print(square)
    
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
for rating in PlayListRatings:
    if(rating<6):
        break
    print(rating)
    
# While loop -------------------------------------
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
Rating = PlayListRatings[0]
while(i < len(PlayListRatings) and Rating >= 6):
    print(Rating)
    i = i + 1 # This prints the value 10 only once 
    Rating = PlayListRatings[i]
    i = i + 1 #Try uncommenting the line and comment the previous i = i + 1, and see the difference, 10 value will get printed twice because when the loop starts it will print Rating and then with PlayListRatings[0], it will again assign the value 10 to Ratings. 
    
    
    
# Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange':
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)

