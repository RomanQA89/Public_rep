class Clients:
    def __init__(self, name, last_name, city):
        self.name = name
        self.last_name = last_name
        self.city = city
    def guests(self):
        return f'{self.name} {self.last_name}. {self.city}.'

client1 = Clients("Ivan", "Petrov", "Ypha")
client2 = Clients("Pavel", "Serov", "Vegas")
client3 = Clients("Donald", "Fazer", "Chicago")
client4 = Clients("Fil", "Newman", "Boston")

list_of_clients = [client1, client2, client3, client4]

for clients in list_of_clients:
    print(clients.guests())
