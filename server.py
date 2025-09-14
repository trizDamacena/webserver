# from http.server import SimpleHTTPRequestHandler, HTTPServer

# #definir a porta
# porta = 8000

# #definindo o gerenciador/manipulador de requisições
# handler = SimpleHTTPRequestHandler

# #criando a instância com o servidor
# server = HTTPServer(('localhost',porta), handler)
# #Imprimindo mensagem de status
# print(f"Server Initiated in http://localhost:{porta}")
# server.serve_forever()

import os 
from http.server import SimpleHTTPRequestHandler, HTTPServer

class Handler(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        try:
            f = open(os.path.join(path, 'index.html'), encoding='utf-8')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f.read().encode('utf-8'))
            f.close()
            return None
        except FileNotFoundError:
            pass 
        return super().list_directory(path)
    
    def do_GET(self): #definindo o método get para o endpoint indicados abaixo
        if self.path == "/index": #realizando o get da página index pelo endpoint /index 
            try:
                with open(os.path.join(os.getcwd(), "index.html"), encoding='utf-8') as index:
                    content = index.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")

        elif self.path == "/login": #realizando o get da página index pelo endpoint /login 
            try:
                with open(os.path.join(os.getcwd(), "login.html"), encoding='utf-8') as login:
                    content = login.read()
                self.send_response(200)
                self.send_header("Content-type", 'text/html')
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")

        elif self.path == "/cadastro": #realizando o get da página index pelo endpoint /cadastro 
            try:
                with open(os.path.join(os.getcwd(), "cadastro.html"), encoding='utf-8') as cadastro:
                    content = cadastro.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileExistsError:
                self.send_error(404, "File not found")
        elif self.path == "/listarFilmes": #realizando o get da página index pelo endpoint /listaFilmes 
            try: 
                f = open(os.path.join(os.getcwd(), "listarfilmes.html"), encoding='utf-8')
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))
                f.close()
                return None
            except FileExistsError:
                self.send_error(404, "File Not Found")
        else:
            super().do_GET()
                

porta = 8000 # definindo a porta
Hanlder = (f'http://localhost:{porta}') #definindo o endpoint 

def main(): #função main responsável por chamar a classe dos endpoint
    server_adress = ('', 8000)
    httpd = HTTPServer(server_adress, Handler)
    print("Server running in http://localhost:8000")
    httpd.serve_forever()

main()