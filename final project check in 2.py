import sys
import pandas as pd

file = pd.read_csv('movies.csv')
exit = True
#Here we will import pandas so we can use our database of movies from the excel sheet to use within our code

#In terms of performing/conducting unit tests, we will plan our unit tests based on trial and error concepts. Each function relies one another to be able to display all of the possible information to the user
#We will make unit tests everytime we make a breakthrough to see if we are on the right track. This will allow us to see if we have any errors within our code.
#We will do unit tests everytime the team comes together to work on the code, we will plan it around each specific function so we can get the full scope of how each one will work with another.
#Unit tests will be planned around our progression, but through these unit tests we will be able to know what questions to ask as well, since we will know what specific errors there are within our code.
#Conducting unit tests within each function to know what works within the function and what dosen't will help us narrow down what needs more focus in terms of problem solving within the function.

class Movie:

    #Create movie class

     def year(self, year):
        #Create year function
        """_summary_ This function will display the top 10 most rated movies within the selected year (selection must be within given years frame) from the movies.csv file

        Args:
            year (str): _description_
        """

        yearLabel = file[file['Year'] == year]

        yearLabel.sort_values(by=['Rotten Tomatoes %'], inplace=True, ascending=False)

        datafileLabel1 = yearLabel[['Film', 'Genre', 'Rotten Tomatoes %', 'Worldwide Gross', 'Year']].head(10)

        print(datafileLabel1.to_string(index=False))

       
      

        print('Top 10 movies of ' + str(year))

     def most_revenue(self):
        #Create most revenue function
        """_summary_ This function will extract and display the movie(s) with the most revenue
        """

        file.sort_values(by=['Worldwide Gross'], inplace=True, ascending=False)

        datafileLabel3 = file[['Film', 'Genre', 'Rotten Tomatoes %', 'Worldwide Gross', 'Year']].head(10)

        print(datafileLabel3.to_string(index=False))
        
        print('Top 10 highest grossing movies:')

     def top_rated_movies(self):
        #Create top rated movies function
        """_summary_ This function will read the file and extract the top 10 rated movies
        """ 
        

        file.sort_values(by=['Rotten Tomatoes %'], inplace=True, ascending=False)

        filelabels = file[['Film', 'Genre', 'Rotten Tomatoes %', 'Worldwide Gross', 'Year']].head(10)

        print(filelabels.to_string(index=False))

        print('Top 10 top rated movies:')

        #Here we will put the code on how the top rated movies function will extract the information from the excel movies.csv file 

     def least_rated_movies(self):
        #Create least rated movies function
        """_summary_: This function will extract the top 10 lowest rated movies from the movies.csv excel file
        """

        file.sort_values(by=['Rotten Tomatoes %'], inplace=True)

        labels2 = file[['Film', 'Genre', 'Rotten Tomatoes %', 'Worldwide Gross', 'Year']].head(10)

        print(labels2.to_string(index=False))

        print('Top 10 least rated movies:')

        


     def movie_genre(self, genre):
        #Create movie genre function
        """_summary_ This function will extract the top 10 rated movies from each genre from the movies.csv file

        Args:
            genre (_type_): _description_
        """

        #This will print the top 10 movies from the genre categories

        genreLabels = file[file['Genre'] == genre]

        labels4 = genreLabels[['Film', 'Genre', 'Rotten Tomatoes %', 'Worldwide Gross', 'Year']].head(10)

        print(labels4.to_string(index=False))
       
        print('Top 10 ' + genre + ' movies:')
       
       
        
        

def show_user_menu():
    """_summary_ This function is where the user will have the choice to make a selection of the multiple options prompted by the machine
    """

    #Print the menu for the user which would ask the user to make a selection, and print the list of options for the user to choose from

    print('What selection would you like to make?')
    print('A. Top movies released in a year')
    print('B. Top movies with the most revenue')
    print('C. Top rated movies')
    print('D. Least rated movies')
    print('E. Top movies by genre')

def genre_type(genre_number):
        """_summary_ This function will create the list of choices of the different genres of movies for the user to choose from and from the choice of the user, the code will return the movie within the genre(display movie(s) of selected genre)

        Args:
            genre_number (_type_): _description_
        """
    

    #Create conditional statement that allows the code to return the genre of the selection of the user to display the movie(s) from the selected genre

        
        pass





        

if __name__ == '__main__':
    movie = Movie()
    while True:
        show_user_menu()
        #Call on user menu function to display the main menu to the user

        #Create a while (conditional) statement which will show call the show user menu function which will show the user the selection menu

        choice = input('Enter your choice here: ').upper()
        #Create the user input option, and make it so the input returns a string where all characters are in upper case

        if choice == 'A':
            movie.year()


        elif choice == 'B':
            movie.most_revenue()



        elif choice == 'C':
            movie.top_rated_movies()

           
            
        elif choice == 'D':
            movie.least_rated_movies()
            
            
        elif choice == 'E':
            movie.movie_genre()

        
            
        #Create else if statements that correlate to the assigned function, and will call that function to display the top movies for that selection

        #We still have to implement a few more conditional statements that allows the system to display the function the user's imput calls on
            