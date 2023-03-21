import random

cities_str = "Warszawa,Kraków,Wrocław,Radom,Poznań,Gdańsk,Szczecin,Bydgoszcz,Lublin,Białystok"
cities_list = cities_str.split(",")
visit_city = []

while len(visit_city) < len(cities_list):
    cities = random.choice(cities_list)
    if cities not in visit_city:
        visit_city.append(cities)

print(visit_city)

for i, cities in enumerate(visit_city):
    print(f"{i + 1}.{cities}")

