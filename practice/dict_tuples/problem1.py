# Write a program that asks user for three type of inputs,
# print: if user enter print then it should print all countries with their population in this format,
# china==>143
# india==>136
# usa==>32
# pakistan==>21
# add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
# remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
# query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.

population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}

def add():
    country = input("Enter the Country name:")
    country = country.lower()
    if country in population:
        print(f"country name {country} already exists. Please enter another country.")
        return
    p = float(input(f"Enter population for the Country name {country}:"))
    population[country]= p
    print_all()

def remove():
    country = input("Enter the Country name:")
    country = country.lower()
    if country not in population:
        print(f"country name {country} does not exists. Please enter another country.")
        return
    population.pop(country)
    print_all()

def query():
    country = input("Enter the Country name:")
    country = country.lower()
    if country not in population:
        print(f"country name {country} does not exists. Please enter another country.")
        return
    print(f"Population of the country {country} is {population[country]} crore.")

def print_all():
    for key, value in population.items():
        print(f"{key}==>{value}")

def main():
    machine = True
    while machine:
        op = input("Enter operation (add, remove, query, print, stop):")
        if op.lower() == 'add':
            add()
        elif op.lower() == 'remove':
            remove()
        elif op.lower() == 'query':
            query()
        elif op.lower() == 'print':
            print_all()
        elif op.lower() == 'stop':
            machine = False

if __name__ == "__main__":
    main()