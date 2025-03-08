def slam_book():
    print("Welcome to the Digital Slam Book!")
    print("Please answer the following questions.")
    print("Your answers will be shown and stored in memory.")
    print("Let's get started!\n")

    name = input("What is your name? ")
    age = input("How old are you? ")
    favorite_color = input("What is your favorite color? ")
    dream_job = input("What is your dream job? ")
    favorite_movie = input("What is your favorite movie? ")
    message = input("Write a short message for future readers: ")

    print("\n--- Your Slam Book Entry ---")
    print("Name:", name)
    print("Age:", age)
    print("Favorite Color:", favorite_color)
    print("Dream Job:", dream_job)
    print("Favorite Movie:", favorite_movie)
    print("Message:", message)
    print("---------------------------\n")

    slam_entry = {
        "Name": name,
        "Age": age,
        "Favorite Color": favorite_color,
        "Dream Job": dream_job,
        "Favorite Movie": favorite_movie,
        "Message": message,
    }

    print("Your response has been stored in memory.")
    print("\nThank you for participating!")

slam_book()