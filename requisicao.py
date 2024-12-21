import requests

class Requisicao:
    def __init__(self, https):
        self.requisicao_get = self.get(https)
        self.requisicao_post = self.post(https)
        self.requisicao_put = self.put(https)
        self.requisicao_delete = self.delete(https)
        self.requisicao_dicionario = self.json()
    
    def get(self, https):
        return requests.get(https)
    
    def post(self, https):
        return requests.post(https) 
    
    def put(self, https):
        return requests.put(https)      
    
    def delete(self, https):
        return requests.delete(https)   
           
    def json(self):
        if self.requisicao_get.status_code == 200:
            requisicao_json = self.requisicao_get.json()
            print(requisicao_json)
            return requisicao_json
        
    
    
request = Requisicao(f"https://api-receitas-pi.vercel.app/receitas/todas")
request.json

    
    