#Movie Watchlist Manager

movies = {}

while True:
    print("\n Movie Watch list Manager ")
    print("1. Add Movies")
    print("2. Display All Movies")
    print("3. Search Movie")
    print("4. Display Watched Movies")
    print("5. Display Unwatched Movies")
    print("6. Update Movie")
    print("7. Remove Movie from List")
    print("8. Exit")

    choice = int(input("Hey user, Please Enter your Choice :"))

    match choice:
         case 1:
              print("----- Add Movies in the list ----- ")

              id = int(input("Enter Movie Id : "))

              if id in movies:
                   print("Movie Already Exists")
              else:
                   movieName = input("Enter a Movie name : ")
                   movieGenre = input("Enter a Movie Genre : ")
                   movieStatus = input("Enter your Movie Status (Watched / Unwatched) : ")
                   movieRating = float(input("Enter a Movie rating : "))
                   releaseYear = int(input("Enter a Movie release year : "))
              
                   movies[id] = {
                      "movieName": movieName,
                      "movieGenre": movieGenre,
                      "movieStatus": movieStatus,
                      "movieRating": movieRating,
                      "releaseYear": releaseYear
                    }


                   print("Movie added successfully")

         case 2:
              print("------ Display All Movies in the list")

              if len(movies) == 0:
                   print("No Movies Available")
              else:
                   for movieId,details in movies.items():
                        print("\nid : ",movieId)
                        print("Name : ",details["movieName"])
                        print("Genre : ",details["movieGenre"])
                        print("MRating : ",details["movieRating"])
                        print("Release Year : ",details["releaseYear"])

         case 3:
              print("---- Search Movies -----")

              movieId = int(input("Enter Movie id to search : "))

              if movieId in movies:
                    print("\nid : ",movieId)
                    print("Name : ",movies[movieId]["movieName"])
                    print("Genre : ",movies[movieId]["movieGenre"])
                    print("MRating : ",movies[movieId]["movieRating"])
                    print("Release Year : ",movies[movieId]["releaseYear"])
              else:
                   print("Sorry Movie not found")

         case 4:
              print("-----Watched Movies------")

              for movieId,details in movies.items():
                   if details["movieStatus"] == "Watched":
                          print("\nid : ",movieId)
                          print("Name : ",details["movieName"])
                          print("Genre : ",details["movieGenre"])
                          print("MRating : ",details["movieRating"])
                          print("Release Year : ",details["releaseYear"])

         case 5:
              print("------Unwatched Movies-------")

              for movieId,details in movies.items():
                   if details["movieStatus"] == "Unwatched":
                        print("\nid : ",movieId)
                        print("Name : ",details["movieName"])
                        print("Genre : ",details["movieGenre"])
                        print("MRating : ",details["movieRating"])
                        print("Release Year : ",details["releaseYear"])

         case 6:
              print("------Update Movies Information------")

              movieId = int(input("Enter Movie Id to update : "))

              if movieId in movies:
                   movieName = input("Enter Updated Movie Name : ")
                   movieGenre = input("Enter Updated Movie Genre : ")
                   movieStatus = input("Enter Updated Movie Status : ")
                   movieRating = float(input("Enter Updated Movie Rating : "))
                   releaseYear = int(input("Enter Updated Release Year : "))

                   movies[movieId]["movieName"] = movieName
                   movies[movieId]["movieGenre"] = movieGenre
                   movies[movieId]["movieStatus"] = movieStatus
                   movies[movieId]["movieRating"] = movieRating
                   movies[movieId]["releaseYear"] = releaseYear

                   print("Movie Data Updated Successfully")
              else:
                   print("Movie Id not found")

         case 7:
              print("------Remove Movie From Watchlist-------")

              mid = int(input("Enter Movie ID to remove : "))

              if mid in movies:
                   del movies[mid]
                   print("Movie removed from list successfully")
              else:
                   print("Movie Not found")
         case 8:
              print("Thank you for using Movie Watchlist Manager")
              break

         case _:
              print("Invalid Choice")
    
                   
                          
                                      

              
    
                                                        