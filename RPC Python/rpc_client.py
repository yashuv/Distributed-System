
# Importing xmlrpc client
import xmlrpc.client

# specify the server in .ServerProxy
with xmlrpc.client.ServerProxy('http://127.0.0.1:8000/') as proxy:

    # client performs an RPC by sending an HTTP request to a server
    while True:
        n = int(input('\tEnter number for Factorial: '))
        print("\t",n,"! = ",proxy.factorial(n), end='\n\n')