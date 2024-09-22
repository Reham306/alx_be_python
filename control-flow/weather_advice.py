#Utilize conditional statements to guide program execution based on user input regarding weather conditions.

weather_status = input("What's the weather like today? (sunny/rainy/cold): ").lower()
x = "sunny"
y = "rainy"
z = "cold"

if weather_status == x:
    print ("Wear a t-shirt and sunglasses.")
elif weather_status == y:
    print ("Don't forget your umbrella and raincoat.")
elif weather_status == z:
    print("Make sure to wear coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")