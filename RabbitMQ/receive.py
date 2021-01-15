from pyrabbit2.api import Client

cl = Client('192.168.99.100:15672', 'rabbitmq', 'rabbitmq')
cl.is_alive()

while(1):
    message=cl.get_messages('Client1', 'Client1')
    if(len(message)>0):
        message=message[0]['payload']
    print(message)
    input()