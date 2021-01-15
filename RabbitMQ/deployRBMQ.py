from pyrabbit2.api import Client

cl = Client('192.168.99.100:15672', 'rabbitmq', 'rabbitmq')
x=len(cl.get_vhost_names())
print("Combient de nouveau client ?")
y=int(input())+x

while(x<y):
    name="Client"+str(x)
    cl.create_vhost(name)
    cl.create_queue(vhost=name, name=name)
    cl.publish('Client1', 'amq.default', 'Client1', 'Welcome On Board')
    x=x+1