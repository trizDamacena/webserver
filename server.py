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
from urllib.parse import parse_qs, urlparse
import json


usuario = ""
senhaUsuario = ""
vezes = 0
from pathlib import Path
caminho_arquivo = Path("./filmes.json")

class Handler(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        try:
            f = open(os.path.join(path, './html/index.html'), encoding='utf-8')
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
    
        
    def register_movie(self, id_filme, nome, atores, diretor, data_lancamento, genero, produtora, sinopse):
        self.id_filme = id_filme
        self.nome = nome 
        self.atores = atores
        self.diretor = diretor
        self.data_lancamento = data_lancamento
        self.genero = genero
        self.produtora = produtora
        self.sinopse = sinopse

        filme = {
            "nome": f"{self.nome}",
            "atores": f"{self.atores}",
            "diretor": f"{self.diretor}",
            "data_lancamento": f"{self.data_lancamento}",
            "genero": f"{self.genero}",
            "produtora": f"{self.produtora}",
            "sinopse": f"{self.sinopse}"
        }


        if caminho_arquivo.exists():
            with open('./jsons/filmes.json', 'r+', encoding='utf-8') as f:
                dados = json.load(f)
                
                if self.id_filme == None:
                    if str(len(dados)+1) in dados:
                        dados[len(dados)+2] = filme
                    else:
                        dados[len(dados)+1] = filme
                else:
                    dados[id_filme]['nome'] = self.nome
                    dados[id_filme]['atores'] = self.atores
                    dados[id_filme]['diretor'] = self.diretor
                    dados[id_filme]['data_lancamento'] = self.data_lancamento
                    dados[id_filme]['genero'] = self.genero
                    dados[id_filme]['produtora'] = self.produtora
                    dados[id_filme]['sinopse'] = self.sinopse
                f.seek(0)
                json.dump(dados, f, indent=4)
                f.truncate()
            return 'Arquivo gerado'
        else:
            return 'Arquivo não encotrado'
                
        
    
    def deletar_filme(self, id_filme):
        self.id_filme = id_filme

        with open('filmes_teste.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
        dados_atualizados = [obj for obj in dados if obj['id'] != self.id_filme]

        with open('filmes_teste.json', 'w') as f:
            json.dump(dados_atualizados, f, indent=4)

    
    ##Métodos
    def do_GET(self): #definindo o método get para o endpoint indicados abaixo
        if self.path == "/index": #realizando o get da página index pelo endpoint /index 
            try:
                with open(os.path.join(os.getcwd(), "./html/index.html"), encoding='utf-8') as index:
                    content = index.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")

        elif self.path == "/login": #realizando o get da página index pelo endpoint /login 
            try:
                with open(os.path.join(os.getcwd(), "./html/login.html"), encoding='utf-8') as login:
                    content = login.read()
                self.send_response(200)
                self.send_header("Content-type", 'text/html')
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")

        elif self.path == "/cadastro": #realizando o get da página index pelo endpoint /cadastro 
            try:
                with open(os.path.join(os.getcwd(), "./html/cadastro.html"), encoding='utf-8') as cadastro:
                    content = cadastro.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileExistsError:
                self.send_error(404, "File not found")

        elif self.path == "/listarFilmes": #realizando o get da página index pelo endpoint /listaFilmes 
            try: 
                f = open(os.path.join(os.getcwd(), "./html/listarfilmes.html"), encoding='utf-8')
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))
                f.close()
                return None
            except FileExistsError:
                self.send_error(404, "File Not Found")

        elif self.path == "/get_listinha":
            arquivo = "./jsons/filmes.json"

            if os.path.exists(arquivo):
                with open(arquivo, encoding='utf-8') as listagem:
                    try:
                        filmes = json.load(listagem)
                    except json.JSONDecodeError:
                        filmes = []
            else:
                filmes = []
            
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(filmes).encode('utf-8'))

        elif self.path == "/atualizar": #realizando o get da página index pelo endpoint /cadastro 
            try:
                with open(os.path.join(os.getcwd(), "./html/atualizarFilme.html"), encoding='utf-8') as cadastro:
                    content = cadastro.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileExistsError:
                self.send_error(404, "File not found")
        

        #PROVAVELMENTE NÃO IREI USAR
        # elif self.path == "/deletar_Filmes": #realizando o get da página index pelo endpoint /listaFilmes 
        #     try: 
        #         f = open(os.path.join(os.getcwd(), "deletarFilme.html"), encoding='utf-8')
        #         self.send_response(200)
        #         self.send_header("Content-type", "text/html")
        #         self.end_headers()
        #         self.wfile.write(f.read().encode('utf-8'))
        #         f.close()
        #         return None
        #     except FileExistsError:
        #         self.send_error(404, "File Not Found")
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
            id_filme = None
            nome_filme = form_data.get('nome_filme', [""])[0]
            atores = form_data.get('atores', [""])[0]
            diretor = form_data.get('diretor', [""])[0]
            data_lancamento = form_data.get('data_lancamento', [""])[0]
            genero = form_data.get('genero', [""])[0]
            produtora = form_data.get('produtora', [""])[0]
            sinopse = form_data.get('sinopse', [""])[0]

            cadastro = self.register_movie(id_filme, nome_filme, atores, diretor, data_lancamento, genero, produtora, sinopse)
            
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(cadastro.encode('utf-8'))

        elif (self.path == '/send_atualizar'):
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            print("Data frame: ")
            id_filme = form_data.get('id_filme', [""])[0]
            post_ou_put = 1
            nome_filme = form_data.get('nome_filme', [""])[0]
            atores = form_data.get('atores', [""])[0]
            diretor = form_data.get('diretor', [""])[0]
            data_lancamento = form_data.get('data_lancamento', [""])[0]
            genero = form_data.get('genero', [""])[0]
            produtora = form_data.get('produtora', [""])[0]
            sinopse = form_data.get('sinopse', [""])[0]

            cadastro = self.register_movie(id_filme, nome_filme, atores, diretor, data_lancamento, genero, produtora, sinopse)
            
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(cadastro.encode('utf-8'))

        else: 
            super(Handler, self).do_POST()
        
    def do_DELETE(self):
        
        url = urlparse(self.path)
        separado = [parte for parte in url.path.split('/') if parte]
        id = separado[-1]

        with open('./jsons/filmes.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)

        del dados[id]
        with open('./jsons/filmes.json', 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        self.send_response(204)  
        self.end_headers()

        return None



porta = 8002 # definindo a porta
Hanlder = (f'http://localhost:{porta}') #definindo o endpoint 

def main(): #função main responsável por chamar a classe dos endpoint
    server_adress = ('', 8002)
    httpd = HTTPServer(server_adress, Handler)
    print("Server running in http://localhost:8002")
    httpd.serve_forever()

main()