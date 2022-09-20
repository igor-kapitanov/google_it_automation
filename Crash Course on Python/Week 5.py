# class Apple:  # class creation
#     pass  # shows that the body is empty
#
#
# class Apple:
#     color = ""
#     flavor = ""
#
#
# jonagold = Apple()
# jonagold.color = "red"
# jonagold.flavor = "sweet"
#
# print(jonagold.color)
# print(jonagold.flavor)


# class Person:
#     apples = 0
#     ideas = 0
#
#
# johanna = Person()
# johanna.apples = 1
# johanna.ideas = 1
#
# martin = Person()
# martin.apples = 2
# martin.ideas = 1
#
#
# def exchange_apples(you, me):
#     temp = you.apples
#     you.apples = me.apples
#     me.apples = temp
#     return you.apples, me.apples
#
#
# def exchange_ideas(you, me):
#     temp = you.ideas
#     you.ideas += me.ideas
#     me.ideas += temp
#     return you.ideas, me.ideas
#
#
# exchange_apples(johanna, martin)
# print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
# exchange_ideas(johanna, martin)
# print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))

# class Piglet:
#     def speak(self):
#         print("oink oink")
#
#
# hamlet = Piglet()
# print(hamlet.speak())

# class Piglet:
#     name = "piglet"
#
#     def speak(self):
#         print("Oink! I'm {}! Oink!".format(self.name))
#
#
# hamlet = Piglet()
# hamlet.name = "Hamlet"
# print(hamlet.speak())
#
# petunia = Piglet()
# petunia.name = "Petunia"
# print(petunia.speak())

# class Piglet:
#     years = 0
#
#     def pig_years(self):
#         return self.years * 18
#
#
# piggy = Piglet()
# print(piggy.pig_years())
#
# piggy.years = 2
# print(piggy.pig_years())

# class Apple:
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavor = flavor
#
# jonagold = Apple("red", "sweet")
# print(jonagold.color)

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def greeting(self):
#         text = "hi, my name is " + self.name
#         return text
#
#
# some_person = Person("John")
# print(some_person.greeting())

# class Apple:
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavor = flavor
#
#     def __str__(self):
#         return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
#
#
# jonagold = Apple("red", "sweet")
# print(jonagold)

# def to_seconds(hours, minutes, seconds):
#     """Returns the amount of seconds in the given hours, minutes and seconds"""
#     return hours * 3600 + minutes * 60 + seconds
#
#
# help(to_seconds)

# class Piglet:
#     """Represents a piglet that can say their name"""
#     years = 0
#     name = ""
#
#     def speak(self):
#         """Outputs a message including the name of the piglet"""
#         print("Oink! I'm {}! Oink!".format(self.name))
#
#     def pig_years(self):
#         """Converts the surrent age to equivalent pig years"""
#         return self.years * 18
#
# help(Piglet)

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def greeting(self):
#         """Outputs a message with the name of the person"""
#         print("Hello! My name is {name}.".format(name=self.name))
#
#
# help(Person)


# class Elevator:
#     def __init__(self, bottom, top, current):
#         """Initializes the Elevator instance."""
#         self.bottom = bottom
#         self.top = top
#         self.current = current
#
#     def __str__(self):
#         """Information about Current floor"""
#         return "Current floor: {}".format(self.current)
#
#     def up(self):
#         """Makes the elevator go up one floor."""
#         if self.current < 10:
#             self.current += 1
#
#     def down(self):
#         """Makes the elevator go down one floor."""
#         if self.current > 0:
#             self.current -= 1
#
#     def go_to(self, floor):
#         """Makes the elevator go to the specific floor."""
#         if floor >= self.bottom and floor <= self.top:
#             self.current = floor
#         elif floor < 0:
#             self.current = 0
#         else:
#             self.current = 10
#
#
# elevator = Elevator(-1, 10, 0)


# class Fruit:
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavor = flavor
#
#
# class Apple(Fruit):
#     pass
#
#
# class Grape(Fruit):
#     pass
#
#
# granny_smith = Apple("green", "tart")
# carnelian = Grape("purple", "sweet")
#
# print(granny_smith.flavor)
# print(carnelian.color)

# class Animal:
#     sound = ""
#
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))
#
#
# class Piglet(Animal):
#     sound = "Oink!"
#
#
# hamlet = Piglet("Hamlet")
# print(hamlet.speak())
#
#
# class Cow(Animal):
#     sound = "Moooo"
#
#
# milky = Cow("Milky White")
# print(milky.speak())

# class Clothing:
#     material = ""
#
#     def __init__(self, name):
#         self.name = name
#
#     def checkmaterial(self):
#         print("This {} is made of {}".format(self.name, self.material))
#
#
# class Shirt(Clothing):
#     material = "Cotton"
#
#
# polo = Shirt("Polo")
# polo.checkmaterial()

# class Repository:
#     def __init__(self):
#         self.packages = {}
#
#     def add_package(self, package):
#         self.packages[package.name] = package
#
#     def total_size(self):
#         result = 0
#         for package in self.packages.values():
#             result += package.size
#         return result


# class Clothing:
#     stock = {'name': [], 'material': [], 'amount': []}
#
#     def __init__(self, name):
#         material = ""
#         self.name = name
#
#     def add_item(self, name, material, amount):
#         Clothing.stock['name'].append(self.name)
#         Clothing.stock['material'].append(self.material)
#         Clothing.stock['amount'].append(amount)
#
#     def Stock_by_Material(self, material):
#         count = 0
#         n = 0
#         for item in Clothing.stock['material']:
#             if item == material:
#                 count += Clothing.stock['amount'][n]
#                 n += 1
#         return count
#
#
# class shirt(Clothing):
#     material = "Cotton"
#
#
# class pants(Clothing):
#     material = "Cotton"
#
#
# polo = shirt("Polo")
# sweatpants = pants("Sweatpants")
# polo.add_item(polo.name, polo.material, 4)
# sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
# current_stock = polo.Stock_by_Material("Cotton")
# print(current_stock)

# import random
# print(random.randint(1,10))
# print(random.randint(1,10))
# print(random.randint(1,10))
# print(random.randint(1,10))

# import datetime
# now = datetime.datetime.now()
# print(now)
# print(now.year)
# print(now+datetime.timedelta(days=28))

# import random
#
#
# class Server:
#     def __init__(self):
#         """Creates a new server instance, with no active connections."""
#         self.connections = {}
#
#     def add_connection(self, connection_id):
#         """Adds a new connection to this server."""
#         connection_load = random.random() * 10 + 1
#         # Add the connection to the dictionary with the calculated load
#         self.connections[connection_id] = connection_load
#
#     def close_connection(self, connection_id):
#         """Closes a connection on this server."""
#         # Remove the connection from the dictionary
#         if connection_id in self.connections:
#             del self.connections[connection_id]
#
#     def load(self):
#         """Calculates the current load for all connections."""
#         total = 0
#         for load in self.connections.values():
#             total += load
#         # Add up the load for each of the connections
#         return total
#
#     def __str__(self):
#         """Returns a string with the current load of the server"""
#         return "{:.2f}%".format(self.load())
#
#
# server = Server()
# server.add_connection("192.168.1.1")
#
# print(server.load())
#
# server.close_connection("192.168.1.1")
# print(server.load())
#
#
# class LoadBalancing:
#     def __init__(self):
#         """Initialize the load balancing system with one server"""
#         self.connections = {}
#         self.servers = [Server()]
#
#     def add_connection(self, connection_id):
#         """Randomly selects a server and adds a connection to it."""
#         server = random.choice(self.servers)
#         # Add the connection to the dictionary with the selected server
#         # Add the connection to the server
#         server.add_connection(connection_id)
#         self.ensure_availability()
#
#     def close_connection(self, connection_id):
#         """Closes the connection on the server corresponding to connection_id."""
#         # Find out the right server
#         # Close the connection on the server
#         # Remove the connection from the load balancer
#         for server in self.servers:
#             if connection_id in server.connections:
#                 server.close_connection(connection_id)
#                 break
#
#     def avg_load(self):
#         """Calculates the average load of all servers"""
#         # Sum the load of each server and divide by the amount of servers
#         total_load = 0
#         total_server = 0
#         for server in self.servers:
#             total_load += server.load()
#             total_server += 1
#         return total_load / total_server
#
#     def ensure_availability(self):
#         """If the average load is higher than 50, spin up a new server"""
#         if self.avg_load() > 50:
#             self.servers.append(Server())
#
#     def __str__(self):
#         """Returns a string with the load for each server."""
#         loads = [str(server) for server in self.servers]
#         return "[{}]".format(",".join(loads))
#
# l = LoadBalancing()
# l.add_connection("fdca:83d2::f20d")
# print(l.avg_load())
#
# l.servers.append(Server())
# print(l.avg_load())
#
# l.close_connection("fdca:83d2::f20d")
# print(l.avg_load())
#
# for connection in range(20):
#     l.add_connection(connection)
# print(l)
#
# print(l.avg_load())


