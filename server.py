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
from urllib.parse import parse_qs

usuario = ""
senhaUsuario = ""

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
    
    def accont_user(self, login, senhaa):
        self.login = login
        self.senhaa = senhaa

        loga = "beatriz"
        senha = 1234

        if (self.login == loga and self.senhaa == senha):
            return "Usuário logado"
        else: 
            return "Usuário não encontrado"
    
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
    
    def do_POST(self):
        
        if self.path == '/send_login':
            content_length = int(self.headers['Content-length']) #tamanho do conteúdo
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body) 

            print("Data Form:") 
            print("Usuario: ", form_data.get('nome_usuario', [""])[0])         
            print("Password: ", form_data.get('senha', [""])[0])    

            username = form_data.get('nome_usuario', [""])[0]
            senhauser= int(form_data.get('senha', [""])[0])

            logou = self.accont_user(username, senhauser)

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(logou.encode("utf-8"))
        

        elif (self.path == '/send_cadastro'):
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            print("Data frame: ")
            nome_filme = form_data.get('nome_filme', [""])[0]
            atores = form_data.get('atores', [""])[0]
            diretor = form_data.get('diretor', [""])[0]
            data_lancamento = form_data.get('data_lancamento', [""])[0]
            genero = form_data.get('genero', [""])[0]
            produtora = form_data.get('produtora', [""])[0]
            sinopse = form_data.get('sinopse', [""])[0]
            print(nome_filme)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(logou.encode("utf-8"))
        else: 
            super(Handler, self).do_POST()

porta = 8000 # definindo a porta
Hanlder = (f'http://localhost:{porta}') #definindo o endpoint 

def main(): #função main responsável por chamar a classe dos endpoint
    server_adress = ('', 8000)
    httpd = HTTPServer(server_adress, Handler)
    print("Server running in http://localhost:8000")
    httpd.serve_forever()

main()