from pyrabbit.api import Client

cl = Client('192.168.99.100:15672', 'rabbitmq', 'rabbitmq')
cl.is_alive()
while(1):
    message=input()
    cl.publish('Client1', 'amq.default', 'Client1', message)

    print('Sent :'+message)