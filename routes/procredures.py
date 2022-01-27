#Procredimentos Banco de dados

#Filtra todos os produtos Filtra todos os produtos pelo ID do seller
'''
CREATE OR ALTER PROCEDURE BuscadordeSeller (@referenciadoseller AS INT)
AS
BEGIN
	SELECT 
			[idproduto]
			  ,[idseller]
			  ,[id_vtex]
			  ,[referenciaseller]
			  ,[nomeseller]
			  ,[ref_ean]
			  ,[ref_cod]
			  ,[nome_produto]
			  ,[perfilgoogle]
			  ,[marcaproduto]
			  ,[preco_seller]
			  ,[diferenca_preco]
			  ,[bitAtivo]
			  ,[sellermenorpreco]
			  ,[menorpreco]
			  ,[sellermaiorpreco]
			  ,[maiorpreco]
			  ,[idcategoriaproduto]
			  ,[categoriaproduto]
			  ,[dataatualizado]
			  ,[refidprodutos]
		  FROM [MercostorePrices].[dbo].[produtos]
		  WHERE idseller = @referenciadoseller

END;

EXEC BuscadordeSeller @referenciadoseller = 4
'''


#Filtra produtos pelo nome do Concorrente do Google Shopping

'''
CREATE OR ALTER PROCEDURE Buscadorconcorrente (@nomeconcorrente AS VARCHAR, @identseller AS INT)
AS
BEGIN
	SELECT 
			[idproduto]
			  ,[idseller]
			  ,[id_vtex]
			  ,[referenciaseller]
			  ,[nomeseller]
			  ,[ref_ean]
			  ,[ref_cod]
			  ,[nome_produto]
			  ,[perfilgoogle]
			  ,[marcaproduto]
			  ,[preco_seller]
			  ,[diferenca_preco]
			  ,[bitAtivo]
			  ,[sellermenorpreco]
			  ,[menorpreco]
			  ,[sellermaiorpreco]
			  ,[maiorpreco]
			  ,[idcategoriaproduto]
			  ,[categoriaproduto]
			  ,[dataatualizado]
			  ,[refidprodutos]
		  FROM [MercostorePrices].[dbo].[produtos]
		  WHERE idseller = @identseller AND

			sellermenorpreco LIKE '%' + @nomeconcorrente +'%' and
			sellermenorpreco <> 'nan'
			
END;

EXEC Buscadorconcorrente @nomeconcorrente = 'Pontofrio.com', @identseller = 5
	

'''


#Filtra todos os produtos sem concorrencia ou que nao foram encontrados no Google

'''
CREATE OR ALTER PROCEDURE Buscaprodutossemconcorrentes (@identseller AS INT)
AS
BEGIN
	SELECT 
			[idproduto]
			  ,[idseller]
			  ,[id_vtex]
			  ,[referenciaseller]
			  ,[nomeseller]
			  ,[ref_ean]
			  ,[ref_cod]
			  ,[nome_produto]
			  ,[perfilgoogle]
			  ,[marcaproduto]
			  ,[preco_seller]
			  ,[diferenca_preco]
			  ,[bitAtivo]
			  ,[sellermenorpreco]
			  ,[menorpreco]
			  ,[sellermaiorpreco]
			  ,[maiorpreco]
			  ,[idcategoriaproduto]
			  ,[categoriaproduto]
			  ,[dataatualizado]
			  ,[refidprodutos]
		  FROM [MercostorePrices].[dbo].[produtos]

		  WHERE idseller = @identseller and [perfilgoogle] = 'nan' and sellermenorpreco = 'nan'
		  	  	
END;

EXEC Buscaprodutossemconcorrentes @identseller = 5
	


'''


#Ordena pelo menor preço de venda do concorrente

'''
CREATE OR ALTER PROCEDURE Ordenamenorvalor (@identseller AS INT)
AS
BEGIN
	SELECT 
		[idproduto]
		  ,[idseller]
		  ,[id_vtex]
		  ,[referenciaseller]
		  ,[nomeseller]
		  ,[ref_ean]
		  ,[ref_cod]
		  ,[nome_produto]
		  ,[perfilgoogle]
		  ,[marcaproduto]
		  ,[preco_seller]
		  ,[diferenca_preco]
		  ,[bitAtivo]
		  ,[sellermenorpreco]
		  ,[menorpreco]
		  ,[sellermaiorpreco]
		  ,[maiorpreco]
		  ,[idcategoriaproduto]
		  ,[categoriaproduto]
		  ,[dataatualizado]
		  ,[refidprodutos]
	  FROM [MercostorePrices].[dbo].[produtos]
	  WHERE idseller = @identseller and menorpreco <> 0
	  ORDER BY menorpreco,nome_produto
	  
END;

EXEC Ordenamenorvalor @identseller = 5
	
	
'''

#Ordena pelo maior valor de venda

'''
CREATE OR ALTER PROCEDURE Ordenamaiorvalor (@identseller AS INT)
AS
BEGIN
	SELECT 
		[idproduto]
		  ,[idseller]
		  ,[id_vtex]
		  ,[referenciaseller]
		  ,[nomeseller]
		  ,[ref_ean]
		  ,[ref_cod]
		  ,[nome_produto]
		  ,[perfilgoogle]
		  ,[marcaproduto]
		  ,[preco_seller]
		  ,[diferenca_preco]
		  ,[bitAtivo]
		  ,[sellermenorpreco]
		  ,[menorpreco]
		  ,[sellermaiorpreco]
		  ,[maiorpreco]
		  ,[idcategoriaproduto]
		  ,[categoriaproduto]
		  ,[dataatualizado]
		  ,[refidprodutos]
	  FROM [MercostorePrices].[dbo].[produtos]
	  WHERE idseller = @identseller and menorpreco <> 0
	  ORDER BY menorpreco DESC,nome_produto DESC
	  
END;

EXEC Ordenamaiorvalor @identseller = 5
	


'''


#Ganhando no preço de venda

'''
CREATE OR ALTER PROCEDURE GanhandoPreco (@identseller AS INT)
AS
BEGIN
	SELECT 
		[idproduto]
		  ,[idseller]
		  ,[id_vtex]
		  ,[referenciaseller]
		  ,[nomeseller]
		  ,[ref_ean]
		  ,[ref_cod]
		  ,[nome_produto]
		  ,[perfilgoogle]
		  ,[marcaproduto]
		  ,[preco_seller]
		  ,[diferenca_preco]
		  ,[bitAtivo]
		  ,[sellermenorpreco]
		  ,[menorpreco]
		  ,[sellermaiorpreco]
		  ,[maiorpreco]
		  ,[idcategoriaproduto]
		  ,[categoriaproduto]
		  ,[dataatualizado]
		  ,[refidprodutos]
	  FROM [MercostorePrices].[dbo].[produtos]
	  WHERE idseller = @identseller and menorpreco <> 0 and
	  preco_seller < menorpreco
  
END;

EXEC GanhandoPreco @identseller = 5
	
	
	
'''

#Perdendo no preço de venda


"""
CREATE OR ALTER PROCEDURE PerdendonoPreco (@identseller AS INT)
AS
BEGIN
	SELECT 
		[idproduto]
		  ,[idseller]
		  ,[id_vtex]
		  ,[referenciaseller]
		  ,[nomeseller]
		  ,[ref_ean]
		  ,[ref_cod]
		  ,[nome_produto]
		  ,[perfilgoogle]
		  ,[marcaproduto]
		  ,[preco_seller]
		  ,[diferenca_preco]
		  ,[bitAtivo]
		  ,[sellermenorpreco]
		  ,[menorpreco]
		  ,[sellermaiorpreco]
		  ,[maiorpreco]
		  ,[idcategoriaproduto]
		  ,[categoriaproduto]
		  ,[dataatualizado]
		  ,[refidprodutos]
	  FROM [MercostorePrices].[dbo].[produtos]
	  WHERE idseller = @identseller and menorpreco <> 0 and
	  preco_seller > menorpreco
  
END;

EXEC PerdendonoPreco @identseller = 5
	



"""