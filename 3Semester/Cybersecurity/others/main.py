import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyCQy8TwUu_dCzOLaANP_E7Dk8Ad7-FFgrc",
  "authDomain": "sistemas-de-informacao-743c3.firebaseapp.com",
  "projectId": "sistemas-de-informacao-743c3",
  "storageBucket": "sistemas-de-informacao-743c3.firebasestorage.app",
  "messagingSenderId": "355455377931",
  "appId": "1:355455377931:web:9a2656d7b49baf792b9d0e",
  "databaseURL": ""
}

APP = pyrebase.initialize_app(firebaseConfig)


#API pra acessar a aplicação de autenticação
AUTH = APP.auth()


def register():
  #criar usuario
  print("Digite o email: ")
  email = input()
  print("Digite a senha: ")
  senha = input()
  if exists(email):
    print("Usuario ja existe")
  else:
    create_user(email, senha)


def exists(email):
  try:
    AUTH.get_account_info(email)
    return True
  except:
    return False
  
def create_user(email, senha):
  try:
      user = AUTH.create_user_with_email_and_password(email, senha)
      print("Usuario criado com sucesso")
      print(user)
      
      AUTH.send_email_verification(user['idToken'])
  except Exception as e:
      print("Erro ao criar usuario: ", e)
      
def login():
  token = AUTH.sign_in_with_email_and_password("isabel-mendonca@tuamaeaquelaursa.com", '123qweqwe')
  print(AUTH.get_account_info(token['idToken']))
  
  
  
register()
      
  
  

#autenticar usuario


#1. criar dois usuarios
#1.1 solicitar credenciais pelo terminal // feito
#1.2 verificar se o usuario ja existe
#1.3 criar usuario no firebase caso email n exista
#2 mostrar as informações do token do usuario
#3. Enviar e-mail de confirmação de email