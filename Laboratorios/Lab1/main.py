from Server import Server 
import sys

def main(argv):
    if("-p" in argv):
        server = Server("127.0.0.1", int(argv[argv.index("-p")+1]))
        server.escuchar()
        server.cerrar()

if __name__ == "__main__":
    main(sys.argv)