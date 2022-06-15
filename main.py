travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(countries_visited, times_visited, cities_visited):
    #empty curly braces to pass functions through
    new_country = {}
    #taking new_country with all keys and passing through data from add_new_country function 
    new_country["country"] = countries_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    #append to add new_country to travel_log
    travel_log.append(new_country)
    
    

    




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



