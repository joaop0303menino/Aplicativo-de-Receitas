from flask import *

class Servidor:
    def __init__(self, nome):
        self.app = Flask(nome)
    
        @self.app.route("/")
        def Login():
            return self.login()

    def login(self):
        return render_template("index.html")
    
    def Run(self):
        self.app.run(debug=True)

def main():
    servidor = Servidor(__name__)
    servidor.Run()
    
if __name__ == "__main__":
    main()