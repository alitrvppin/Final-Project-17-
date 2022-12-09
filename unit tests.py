import unittest
file = pd.read_csv('movies.csv')
exit = True
import pandas as pd

# Our code to be tested
class Movie(unittest.TestCase):
    def runTest(self):

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

unittest.main()