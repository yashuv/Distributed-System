
# firstly, importing from xmlrpc.server, SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer

# Start the server 
with SimpleXMLRPCServer(('127.0.0.1', 8000)) as server:

    print("Listening on port 8000...")

    def factorial(n):
        if (n==0 or n==1):
            return 1
        else:
            return n * factorial(n-1)
    
    # register the name and function (both) when calling the server from the client
    server.register_function(factorial, "factorial")
    server.serve_forever()