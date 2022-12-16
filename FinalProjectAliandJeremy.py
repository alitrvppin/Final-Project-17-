import sys
import pandas as pd

file = pd.read_csv('Usethisfile_updated_movies.csv')
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
        """_summary_ This function will display the top 10 most rated movies within the selected year 
        (selection must be within given years frame) from the Usethisfile_updated__movies.csv file

        Args:
            year (str):


        """

        #Year function takes in a year argument and prints a list of the top 10 movies in selected year. 
        #it accomplishes this by filtering a DataFrame object called file to only include movies with the given/selected year, and then printing the resulting DataFrame. 
        
        yearLabel = file[file['Release year'] == year]

        #The first line uses the DataFrame's [] operator to select rows where the 'Year' column is equal to a specified year, which is stored in the year variable. 
        #This creates a new DataFrame called yearLabel that only includes rows from where the 'Year' column has the value stored in year.

        yearLabel.sort_values(by=['Rating'], inplace=True, ascending=False)

        #The second line sorts the DataFrame yearLabel by the 'Rating' column in descending order. 
        #The sort_values() method is used to sort the DataFrame and the inplace parameter is set to True to sort the DataFrame in place. 
        #The ascending parameter is set to False to sort the values in descending order.

        datafileLabel1 = yearLabel[['Movie', 'Genre', 'Rating', 'Global revenue', 'Release year']].head(10)

        #The third line uses the [] operator to select specific columns from the sorted DataFrame and the head() method to select the top 10 rows. 
        #The resulting DataFrame is stored in a new DataFrame called datafileLabel1.

        print(datafileLabel1.to_string(index=False))

        #Finally, the to_string() method is used to print the contents of datafileLabel1 as a string. 
        #The index parameter is set to False to prevent the index values from being included in the output.

       
      

        print('Top 10 movies of ' + str(year))

        #Prints out the top 10 movies of the selected year.




     def most_revenue(self):
        #Create most revenue function
        """_summary_ This function will extract and display the top 10 movie(s) with the most revenue
        """

        #most_revenue is a function that reads in a file (containing information about movies) and prints a list of the top 10 highest revenue movies. 
        #it accomplishes this by sorting the DataFrame object by the Global Revenue column, and then printing the resulting DataFrame

        file.sort_values(by=['Global Revenue'], inplace=True, ascending=False)

        
        #This line sorts the DataFrame yearLabel by the 'Global Revenue' column in descending order. 
        #The sort_values() method is used to sort the DataFrame and the inplace parameter is set to True to sort the DataFrame in place. 
        #The ascending parameter is set to False to sort the values in descending order.

        datafileLabel2 = file[['Movie', 'Genre', 'Rating', 'Global revenue', 'Release year']].head(10)

        #This line uses the [] operator to select specific columns from the sorted DataFrame and the head() method to select the top 10 rows. 
        #The resulting DataFrame is stored in a new DataFrame called datafileLabel2.




        print(datafileLabel2.to_string(index=False))

        #the to_string() method is used to print the contents of datafileLabel2 as a string. 
        #The index parameter is set to False to prevent the index values from being included in the output.


        
        print('Top 10 highest revenue movies:')

        #Prints out the top 10 highest revenue movies






     def top_rated_movies(self):
        #Create top rated movies function
        """_summary_ This function will read the file and extract the top 10 rated movies
        """ 

        #top rated movies is a function that reads in a file (containing information about movies) and prints a list of the top 10 highest rated movies. 
        #it accomplishes this by sorting the DataFrame object by the Worldwide Gross column, and then printing the resulting DataFrame

        file.sort_values(by=['Rating'], inplace=True, ascending=False)
        
        #This line sorts the DataFrame filelabels by the 'Rating' column in descending order. 
        #The sort_values() method is used to sort the DataFrame and the inplace parameter is set to True to sort the DataFrame in place. 
        #The ascending parameter is set to False to sort the values in descending order.

        filelabels = file[['Movie', 'Genre', 'Rating', 'Global revenue', 'Release year']].head(10)

        #This line uses the [] operator to select specific columns from the sorted DataFrame and the head() method to select the top 10 rows. 
        #The resulting DataFrame is stored in a new DataFrame called filelabels.

        print(filelabels.to_string(index=False))

        #the to_string() method is used to print the contents of filelabels as a string. 
        #The index parameter is set to False to prevent the index values from being included in the output.


        

        print('Top 10 top rated movies:')

        #Prints the top 10 rated movies

        

     def least_rated_movies(self):
        #Create least rated movies function
        """_summary_: This function will extract the top 10 lowest rated movies from the Usethisfile_updated__movies.csv excel file
        """

        #least rated movies is a function that reads in a file and prints a list of the top 10 least rated movies. 
        #it accomplishes this by sorting the DataFrame object by the least rated movies column, and then printing the resulting DataFrame

        #This will print the top 10 movies from the lowest rated movie categories
        #The least rated movies takes in a lowest movie argument and prints a list of the top 10 movies in that genre. 
        #it accomplishes this by filtering a DataFrame object called file to only include movies with the given genre, and then printing the resulting DataFrame. 

        file.sort_values(by=['Rating'], inplace=True)

        #The first line uses the DataFrame's [] operator to select rows where the 'Rating' column is equal to the value of the rating of the movie.
        #This creates a new DataFrame called labels2 that only includes rows from dataframe where the 'Rating' column has the value stored.



        labels2 = file[['Movie', 'Genre', 'Rating', 'Global revenue', 'Release year']].head(10)

         #This line uses the [] operator to select specific columns from the sorted DataFrame and the head() method to select the top 10 rows. 
        #The resulting DataFrame is stored in a new DataFrame called labels2.


        print(labels2.to_string(index=False))

        #Finally, the to_string() method is used to print the contents of filelabels as a string. 
        #The index parameter is set to False to prevent the index values from being included in the output.

        print('Top 10 least rated movies:')

        #Prints the top 10 least rated movies

        


     def movie_genre(self, genre):
        #Create movie genre function
        """_summary_ This function will extract the top 10 rated movies from each genre from the Usethisfile_updated__movies.csv file

        Args:
            genre (_type_):
        """

        #This will print the top 10 movies from the genre categories
        #The movies genre takes in a genre argument and prints a list of the top 10 movies in that genre. 
        #it accomplishes this by filtering a DataFrame object called file to only include movies with the given genre, and then printing the resulting DataFrame. 
        

        genreLabels = file[file['Genre'] == genre]

        #The first line uses the DataFrame's [] operator to select rows where the 'Genre' column is equal to a specified genre, which is stored in the genre variable. 
        #This creates a new DataFrame called genreLabels that only includes rows from where the 'Genre' column has the value stored in year.

        

        labels4 = genreLabels[['Movie', 'Genre', 'Rating', 'Global revenue', 'Release year']].head(10)

        #The line uses the [] operator to select specific columns from the sorted DataFrame and the head() method to select the top 10 rows. 
        #The resulting DataFrame is stored in a new DataFrame called labels4.




        print(labels4.to_string(index=False))

         #Finally, the to_string() method is used to print the contents of filelabels as a string. 
        #The index parameter is set to False to prevent the index values from being included in the output.


       
       
        print('Top 10 ' + genre + ' movies:')

        #Print top 10 movies within genre
       
       
        
        

def show_user_menu():
    """_summary_ This function is where the user will have the choice to make a selection of the multiple options prompted by the machine
    """

    #Print the menu for the user which would ask the user to make a selection, and print the list of options for the user to choose from

    """Display the available options to the user.
    """
    print('Please choose from the following options:')
    print('A. Show movies released in year.')
    print('B. Show data for the highest revenue movies.')
    print('C. Show data for the highest rated movies.')
    print('D. Show data for the lowest rated movies.')
    print('E. Show data for top movies in selected genre.')


def genre_type(genre_number):
        """_summary_ This function will create the list of options (by using a dictionary) of the different genres of movies for the user to choose from and from the choice of the user, the code will return the movie within the genre(display movie(s) of selected genre)

        Args:
            genre_number (_type_): _description_
        """
    
    #Create dictionary for the user to choose from for the selection of categories.
        genre_number = {
        1: 'Romance',
        2: 'Thriller',
        3: 'Mystery',
        4: 'Fantasy',
        5: 'Horror',
        6: 'Drama',
        7: 'Action',
        8: 'Comedy'}
        
        #Return the genre selected

        return genre_number.get(genre_number)

    

        
        





        

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

        
            
       #Call on every function that corresponds with the choice that the user decides to make in regards of the movie. This will print the prompt for the user of the top 10 rated movies in whatever category was selected.

    