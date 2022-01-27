
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import secrets
from flask_login import LoginManager,login_required

app = Flask(__name__)

db = SQLAlchemy(app)

import pyodbc
from urllib.parse import quote_plus


parametros = (
"Driver={SQL Server Native Client 11.0};"
"Server=GABRIELA-PC;"
"Database=MercostorePrices;"
"UID=sa;"
"PWD=Mudar@123"

)


app = Flask(__name__)

url_db = quote_plus(parametros)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///?odbc_connect=%s' %url_db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#Classes das tabelas do BD/ Muito cuidado em fazer alterações
class Seller(db.Model):
    #classe tabela Sellers
    __tablename__ = 'sellers'
    idseller = db.Column(db.Integer, primary_key=True, unique=True)
    sellerid = db.Column(db.String(20), nullable=True, unique=False)
    sellername = db.Column(db.String(20), nullable=True, unique=False)
    selleremail = db.Column(db.String(200), nullable=True, unique=False)
    bitAtivo = db.Column(db.Boolean, nullable=True, unique=False)
    sellerresponsavel = db.Column(db.String(), nullable=True)
    senha = db.Column(db.String(20), nullable=False)
    logoseller = db.Column(db.String(), nullable=False)
    dataatualizado = db.Column(DateTime(timezone=True), server_default=func.now())
    refusers = db.relationship('User', back_populates='refsusers')
    refprodutos = db.relationship('Produtos', back_populates='sellersrefs')
    refsgoogle = db.relationship('Googleshopping', back_populates='google')

    def __init__(self, sellerid, sellername, selleremail, bitAtivo, sellerresponsavel, senha,logoseller = ''):
        self.sellerid = sellerid
        self.sellername = sellername
        self.selleremail = selleremail
        self.bitAtivo = bitAtivo
        self.sellerresponsavel = sellerresponsavel
        self.senha = senha
        self.logoseller = logoseller

class User(db.Model):
    #Classe Tabela Usuarios
    __tablename__ = 'users'
    idusuario = db.Column(db.Integer, primary_key=True, unique=True)
    sellernome = db.Column(db.String(40), nullable=True, unique=False)
    idseller = db.Column(db.String(40), nullable=True, unique=False)
    nome = db.Column(db.String(40), nullable=True, unique=False)
    email = db.Column(db.String(200), nullable=True, unique=False)
    senha = db.Column(db.String(20), nullable=True, unique=False)
    perfil = db.Column(db.String(1000), nullable=True, unique=False)
    logoseller = db.Column(db.String(1000), nullable=True, unique=False)
    ref_idseller = db.Column(db.Integer, unique=False)
    refsusers = db.relationship("Seller", back_populates='refusers')
    refiduser = db.Column(db.Integer, db.ForeignKey('sellers.idseller'))

    def __init__(self, sellernome, nome, email, senha,idseller, perfil='',logoseller='',ref_idseller=' ',):
        self.sellernome = sellernome
        self.nome = nome
        self.email = email
        self.senha = senha
        self.perfil = perfil
        self.logoseller = logoseller
        self.idseller = idseller


class Produtos(db.Model):
    #Classe tabela produtos
    __tablename__ = 'produtos'
    idproduto = db.Column(db.Integer, primary_key=True, unique=True)
    idseller = db.Column(db.Integer,  unique=False)
    id_vtex = db.Column(db.Integer, unique=False)
    referenciaseller = db.Column(db.String(1000), unique=False)
    nomeseller = db.Column(db.String(40), unique=False)
    ref_ean = db.Column(db.String(20), unique=False)
    ref_cod = db.Column(db.String(20), unique=False)
    nome_produto = db.Column(db.String(1000), unique=False)
    imagem = db.Column(db.String(1000), unique=False)
    perfilprod = db.Column(db.String(1000), unique=False)
    perfilgoogle = db.Column(db.String(1000), unique=False)
    marcaproduto = db.Column(db.String(50), unique=False)
    preco_seller = db.Column(db.Float,  unique=False)
    diferenca_preco = db.Column(db.Float,  unique=False)
    bitAtivo = db.Column(db.Boolean, nullable=True, unique=False)
    sellermenorpreco = db.Column(db.String(100), unique=False)
    menorpreco = db.Column(db.Float,  unique=False)
    sellermaiorpreco = db.Column(db.String(100), unique=False)
    maiorpreco = db.Column(db.Float,  unique=False)
    idcategoriaproduto = db.Column(db.Integer,  unique=False)
    categoriaproduto = db.Column(db.String, unique=False)
    dataatualizado = db.Column(DateTime(timezone=True), server_default=func.now())
    sellersrefs = db.relationship("Seller", back_populates='refprodutos')
    refidprodutos = db.Column(db.Integer, db.ForeignKey('sellers.idseller'))
    refsprodcategorias = db.relationship('CategoriasProdutos', back_populates='produtosref')

    def __init__(self,idseller,id_vtex,referenciaseller, nomeseller, ref_ean,
        ref_cod,nome_produto, imagem,perfilprod = 'Nao Informado', perfilgoogle = 'Nao Informado',marcaproduto='Nao Informado',preco_seller = 0,diferenca_preco = 0, bitAtivo=True,
        sellermenorpreco='Nao Informado',menorpreco=0,sellermaiorpreco='Nao Informado', maiorpreco= 0,idcategoriaproduto= 0,categoriaproduto='Nao Informado'):

        self.idseller = idseller
        self.id_vtex = id_vtex
        self.referenciaseller = referenciaseller
        self.nomeseller = nomeseller
        self.ref_ean = ref_ean
        self.ref_cod = ref_cod
        self.nome_produto = nome_produto
        self.imagem = imagem
        self.perfilprod = perfilprod
        self.perfilgoogle = perfilgoogle
        self.marcaproduto = marcaproduto
        self.preco_seller = preco_seller
        self.diferenca_preco = diferenca_preco
        self.bitAtivo = bitAtivo
        self.sellermenorpreco = sellermenorpreco
        self.menorpreco = menorpreco
        self.sellermaiorpreco = sellermaiorpreco
        self.maiorpreco = maiorpreco
        self.idcategoriaproduto = idcategoriaproduto
        self.categoriaproduto = categoriaproduto


class CategoriasProdutos(db.Model):
    #Classe Categorias MercoStore
    id = db.Column(db.Integer, primary_key=True, unique=True)
    iddepartamento = db.Column(db.Integer, unique=False)
    nomedepartamento = db.Column(db.String(100), unique=False)
    idcategoria = db.Column(db.Integer, unique=False)
    noemcategoria = db.Column(db.String(100), unique=False)
    urlcategoria = db.Column(db.String(600), unique=False)
    refsprods = db.Column(db.Integer, db.ForeignKey('produtos.idproduto'))
    produtosref  = db.relationship("Produtos", back_populates='refsprodcategorias')

    noemcategoria = db.Column(db.String, unique=False)
    def __init__(self,iddepartamento, nomedepartamento, idcategoria, noemcategoria,urlcategoria):
        self.iddepartamento = iddepartamento
        self.nomedepartamento = nomedepartamento
        self.idcategoria = idcategoria
        self.noemcategoria = noemcategoria
        self.urlcategoria = urlcategoria


class Googleshopping(db.Model):
    #Classe Google Shopping
    googleid = db.Column(db.Integer, primary_key=True, unique=True)
    eangoogle = db.Column(db.String(20), unique=False)
    urlgoogle = db.Column(db.String(1000), unique=False)
    sellermen = db.Column(db.String(100), unique=False)
    menorpreco = db.Column(db.Float,  unique=False)
    sellermai = db.Column(db.String(100), unique=False)
    maiorpreco = db.Column(db.String(100), unique=False)
    bitAtivo = db.Column(db.Boolean, nullable=True, unique=False)
    dataatualizado = db.Column(DateTime(timezone=True), server_default=func.now())
    google = db.relationship("Seller",back_populates="refsgoogle")
    refgoogle = db.Column(db.Integer, db.ForeignKey('sellers.idseller'))


    def __init__(self,eangoogle, urlgoogle,sellermen, menorpreco,sellermai,maiorpreco, bitAtivo):
        self.eangoogle = eangoogle
        self.urlgoogle = urlgoogle
        self.sellermen = sellermen
        self.menorpreco = menorpreco
        self.sellermai = sellermai
        self.maiorpreco = maiorpreco
        self.bitAtivo = bitAtivo

from wtforms_sqlalchemy.fields import QuerySelectField
from flask_wtf import FlaskForm

def choice_query():
    return Seller.query.all


class ChoiceForm(FlaskForm):
    opts = QuerySelectField(query_factory=choice_query,allow_blank=True)

@app.route("/registros",methods=['GET','POST'])
def teste():
    form = ChoiceForm()
    return render_template("CadastroUser.html",form=form)

app.run()

