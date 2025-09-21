#datetime
import datetime
x=datetime.datetime.now()
print(x)

#printing only year
print(x.year)

#day
#printing only first three words of day 
print(x.strftime("%a"))

#printing all words words of day
print(x.strftime("%A"))

#month
#printing first three words of month
print(x.strftime("%b"))

#printing all words of month
print(x.strftime("%B"))

#year
#printing last two words/number of year
print(x.strftime("%y"))

#printing all words/number of year
print(x.strftime("%Y"))

#hour
#format 00-23 (24h format)
print(x.strftime("%H"))

#format 00-12 (12h format)
print(x.strftime("%I"))

#printing AM/PM
print(x.strftime("%p"))

#minutes
print(x.strftime("%M"))

#seconds
print(x.strftime("%S"))

#file handling-[deleteing]
# import os 
# os.remove("demo.txt")

# checking file exists
# import os 
# if os.path.exists("demo.txt"):
#     os.remove("demo.txt")
# else:
#     print("the file does not exist")

#deleting whole folder
# import os
# os.rmdir("MyFolder") #only remove empty folder

#creating a folder
# os.makedirs("myfolder")
# os.mkdir("MyFolder")

#movie rating system
movie_ratings={}

def add_rating(movie,rating):
    if movie in movie_ratings:
        movie_ratings[movie].append(rating) 
    else:
        movie_ratings[movie]=[rating]
        print("adding rating for {movie}:{rating}")

def display_ratings():
    if movie_ratings:
        print("Movie Rating:")
        for movie,ratings in movie_ratings.items():
            avg_rating=sum(ratings) / len(ratings)
            print(f"{movie}:Average Rating={avg_rating:.2f}({len(ratings)} ratings)")
    else:
        print("no ratings available")

def main():
    while True:
        print("\nOptions:")
        print("1. Add Rating")
        print("2. Display Rating")
        print("3. Exit")

        choice=input("choose an option(1-3):")

        if choice == '1':
            movie=input("enter the movie name:")
            rating=float(input("enter your rating(0-10):"))
            add_rating(movie,rating)

        elif choice == '2':
            display_ratings()

        elif choice == '3':
          print("exiting the program")
          break

        else:
            print("invalid choice,please choose again.")

if __name__ == "__main__":
    main()