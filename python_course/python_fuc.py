# Python Function

"""Parameters or Arguments?

The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called."""

def say_hi(name):
    return "Hello " + name



my_name = say_hi("Steve")
print(my_name)
print(type(my_name))

def cube(num):
    return num * num

result = cube(3)
print(result)
print(type(result))

"""When function is created, it does nothing yet. Actions listed in it will be executed only
when you call function."""

def config_intf(intf_name, ip, mask):
    print('interface', intf_name)
    print('ip address', ip, mask)

# calling a function
result = config_intf("Fa0/0", "10.1.1.1", "255.255.255.0")
print(result) # print None

def config_intf(intf_name, ip, mask):
    #config = "interface {}\nip address {} {}".format(intf_name, ip, mask)
    config = f"interface {intf_name}\nip address {ip} {mask}"
    return config

result = config_intf("Fa0/0", "10.1.1.2", "255.255.255.0")
print(result)

def config_intf(intf_name, ip, mask):
    config_intf = f'interface {intf_name}\n'
    config_ip = f'ip address {ip} {mask}'
    return config_intf, config_ip

result = config_intf("Fa0/0", "10.1.1.3", "255.255.255.0")
print(result)

print(type(result))
