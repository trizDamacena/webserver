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
    
        
    def register_movie(self, nome, atores, diretor, data_lancamento, genero, produtora, sinopse):
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
                
                dados[len(dados)+1] = filme
                f.seek(0)
                json.dump(dados, f, indent=7)
                f.truncate()
                
        return 'Arquivo gerado'
    
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
        
        elif self.path == "/deletar_Filmes": #realizando o get da página index pelo endpoint /listaFilmes 
            try: 
                f = open(os.path.join(os.getcwd(), "deletarFilme.html"), encoding='utf-8')
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

            cadastro = self.register_movie(nome_filme, atores, diretor, data_lancamento, genero, produtora, sinopse)
            
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(cadastro.encode('utf-8'))

        else: 
            super(Handler, self).do_POST()
        
    def do_DELETE(self):
        # print("PRimeiro")
        # path = urlparse(self.path).path
        
        # if not path.startswith('/delete/'):
        #     self.send_error(404, "Caminho DELETE inválido. Use /delete/<ID>.")
        #     return

        # id_para_excluir = path.split('/')[-1]
        # print("aqui")

        # try:
        #         # 2. Abrir o arquivo no modo 'r+' (leitura e escrita)
        #     with open('./jsons/filmes.json', 'r+', encoding='utf-8') as f:
                    
        #             # Carrega o JSON em um dicionário Python
        #         dados = json.load(f)
                    
        #         if id_para_excluir in dados:
        #                 # 3. Excluir o item do dicionário
        #             filme_excluido = dados.pop(id_para_excluir)
                        
        #                 # 4. Preparar o arquivo para reescrita
        #             f.seek(0)  # Move o cursor para o início do arquivo
        #             f.truncate() # Remove o conteúdo antigo (a partir da posição do cursor, que é 0)
                        
        #                 # 5. Escrever o novo conteúdo modificado
        #             json.dump(dados, f, ensure_ascii=False, indent=4)
                        
        #                 # 6. Enviar resposta de sucesso HTTP
        #             self.send_response(204) # 204 No Content é o padrão para DELETE bem-sucedido
        #             self.end_headers()
        #             print(f"✅ Filme excluído: ID '{id_para_excluir}' - {filme_excluido.get('nome', 'Sem Nome')}")
                    
        #         else:
        #                 # ID não encontrado
        #             self.send_error(404, f"ID '{id_para_excluir}' não encontrado no JSON.")
        # except FileNotFoundError:
        #     self.send_error(404, f"Arquivo JSON não encontrado")
        # except json.JSONDecodeError:
        #     self.send_error(500, f"Erro ao decodificar o JSON no arquivo")
        # except Exception as e:
        #     self.send_error(500, f"Erro interno do servidor: {e}")
        pass




porta = 8002 # definindo a porta
Hanlder = (f'http://localhost:{porta}') #definindo o endpoint 

def main(): #função main responsável por chamar a classe dos endpoint
    server_adress = ('', 8002)
    httpd = HTTPServer(server_adress, Handler)
    print("Server running in http://localhost:8002")
    httpd.serve_forever()

main()