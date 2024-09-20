weather_condition = input("What's the weather like today?(sunny/rainy/cold) ").lower()
sunny = "Wear a t-shirt and sunglasses."
rainy = "Don't forget your umbrella and a raincoat."
cold = "Make sure to wear a warm coat and a scarf."
if weather_condition == "sunny":
    print(sunny)
elif weather_condition == "rainy":
    print(rainy)
elif weather_condition == "cold":
    print(cold)
else:
    print("Sorry, I don't have recommendations for this weather.")
