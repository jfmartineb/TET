import socket

class Server():
    def __init__(self, ip, port):
        # Create socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((ip, port))
        self.server_socket.listen(1)
        print('Starting server, use <Ctrl-C> to stop')
        print('Listening on port %s ...' % port)

    def escuchar(self):
        while True:    
            # Wait for client connections
            client_connection, client_address = self.server_socket.accept()

            # Get the client request
            request = client_connection.recv(1024).decode()
            if (request != " "):
                request = request.split('\n')

                # Send HTTP response
                response = "HTTP/1.1 200 OK\n"
                try: 
                    file  = request[0].split()[1]
                except:
                    pass

                if (file == "/"):
                    archivo = open("files/index.html")
                    contenido = archivo.read()
                    archivo.close()
                    response = response + "\n" + contenido
                    client_connection.sendall(response.encode())

                elif (file == "/request"):
                    response = response + "\n<p><b>REQUEST REALIZADO: </b></p><p>Direccion del cliente: "+ str(client_address) +"</p>"
                    for i in request:
                        response =response+"<p>"+i+"</p>"
                    client_connection.sendall(response.encode())    

                elif (file == "/response"):
                    response = response + "\n<p><b>RESPONSE A REALIZAR: </b></p>"
                    response = response + "\n<p>HTTP/1.0 200 OK - version y codigo de respuesta</p>"
                    response = response + "\n<p>Dom, 7/08/2022 10:01 BGT - Fecha y hora de envio</p>"
                    response = response + "\n<p>Content-Type:   text/html - tipo de archivo a enviar</p>"
                    response = response + "\n<p>Content-Length: 1998 - Longitud del archivo a enviar</p>"
                    response = response + "\n<p>- Espacio reservado para enviar el contenido - </p>"
                    client_connection.sendall(response.encode())

                elif (file == "/close"):
                    break

                else:
                    try:
                        archivo = open("files"+file, 'rb')
                        contenido = archivo.read()
                        archivo.close()
                        tipo = "text/html; charset"
                        if (file.endswith(".jpg") or file.endswith(".JPG")):
                            tipo = "image/jpg"
                        elif(file.endswith("png")):
                            tipo = "image/png"
                        elif(file.endswith("pdf")):
                            tipo = "application/pdf"
                        
                        response = response + "Content-Type: "+ tipo +" \n\n"
                        response = response.encode('utf-8') + contenido
                        client_connection.sendall(response)
                    except FileNotFoundError:
                        response = "HTTP/1.0 404 NOT FOUND\n\n<h1>ERROR: File Not Found</h1>"
                
                
                client_connection.close()

            
    def cerrar(self):
        self.server_socket.close()