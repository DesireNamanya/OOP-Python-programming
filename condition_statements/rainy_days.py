rain = input("Is it raining outside? ")
rain = str.lower(rain)
if rain == "yes":
    windy = input("Is it windy? ")
    windy = str.lower(windy)
    if windy == "yes":
        print("Bro!!! it's too windy for an umbrella.")
    else:
        print("You need to go with an umbrella or else you'll wet the Jordans and you know we don't mess with the Jordans!")
else:
    print("Enjoy your day.")