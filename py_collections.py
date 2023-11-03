# list, dictionary , set, tuple
cities = ["kingdom", "kigali", "Nairobi", "Lilongwe", "Johannesburg", "Porto", "Malaysia"]
scores = [56, 67, 43, 67, 78, 90, 34]

car = {
    "make": "Toyota",
    "model": "Probox",
    "year": 2017,
    "gear": "Manual",
    "color": "White",
    "Owners": ["Jane", "Jerry", "Marry"]
}

friends = {"Mike", "Walid", "Ahmed", "John", "Walid", "Mike"}  # unique elements

workers = ("Jane", "Jack", "Jim")  # never change it programmatically
print(cities)
print(car)
print(friends)
print(workers)
print(cities[0])
print(cities[4])
print(cities[-2])
print(car["model"])  # accessing elements in a dictionary
print(car["make"])  # accessing elements in a dictionary

#loop
for city in cities: # for each city in cities
    print(city)

for key, value in car.items():
    print(key, value)