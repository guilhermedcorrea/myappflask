from flask_login.utils import login_user
from app import login_manager,db
from models.model import User, Produtos,Seller,Googleshopping
from flask_login import UserMixin,LoginManager
from sqlalchemy.exc import IntegrityError
from flask import session

#Funções de controle e ajuste

@login_manager.user_loader
def current_user(user_id):
    return User.query.get(user_id)

class Consultas_BD(UserMixin):
        
    def consulta_usuario(nom,key,addres):
        usuario = db.session.query(User).filter(User.nome == User.nome == nom, User.email == key, User.senha == addres).first()
        return usuario    

    def cadastro_usuario(seller,username, addres,key):

        user = User.query(User).filter(User.email, User.senha, User.nome).first()
        if user:
            print("Já tem cadastro")

        else:
            sell = db.session.query(Seller).filter(Seller.sellername ==seller).first()
            idsellerr = sell.sellerid
            idsel = sell.idseller
            try:
                user = User(sellernome=seller, nome=username, email=addres,senha=key, idseller=idsellerr, perfil='Usuario', logoseller='Nao tem', ref_idseller=idsel)
            except:
                print("Erro no cadastro do usuario")


    def cadastro_usuario(nameseller,nomeuser, email,senha):
        usuario = db.session.query(User).filter(User.email==email)
        if usuario:
            print("Ja tem cadastro")

        else:
            usuario = db.session.query(Seller).filter(Seller.sellernome==nameseller).first()
            idseller = usuario.idseller
            usuario = User(idseller=idseller,sellernome=nameseller,email=email,nome=nomeuser,
            senha=senha,logoseller='Nao tem',bitAtivo=True)
            db.session.add(usuario)
            db.session.commit()

  

  