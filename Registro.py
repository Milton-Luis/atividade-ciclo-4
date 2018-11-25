# coding:utf-8

from ConexaoBD import *
class Paciente():
	def __init__(self, id=0, nome=" ", end=" ", altura=0.0, peso=0.0, result=0.0):
		self.id = id
		self.nome = nome
		self.end = end
		self.altura = altura
		self.peso = peso
		self.result = result
		


	def InserirRegistro(self):
		db = Connection()
	
		sqlCursor = db.con.cursor()

		sql="""INSERT INTO imc.paciente (nome, endereco, altura, peso, resultado)
         	   VALUES ('{}', '{}', '{}', '{}', '{}')""".format(self.nome, self.end,
         	   self.altura, self.peso, self.result)
		try:

			sqlCursor.execute(sql)

			db.con.commit()
			return "Inserido com sucesso"
			print ("Inserido com sucesso")

		except:
			return "Erro ao Inserir no Banco"
			print("Erro ao Inserir no Banco")
			db.con.rollback()


		db.con.close()
		
	def Exibir_registro(self):
		db = Connection()

		selectCursor = db.con.cursor()

		query="SELECT * FROM imc.paciente"
		try:

			selectCursor.execute(query)

			results = selectCursor.fetchall()
			for row in results:
				self.id = row[0]
				self.nome = row[1]
				self.end = row[2]
				self.altura = row[3]
				self.peso = row[4]
				self.result = row[5]

				return "{}\t{}\t\t{}\t\t\t{}\t\t{}\t\t{}\n\n".format(self.id, self.nome,\
				 self.end, self.altura, self.peso, self.result)
				# caso utilize terminal
				'''
				print("{}\t{}\t\t{}\t\t{}\t{}\t{}\n".format(self.id, self.nome,\
				self.end, self.altura, self.peso, self.result))'''

		except pymysql.DataError as e:
		   	return "Erro ao exibir dados - {}".format(e)

		db.con.close()
		
paciente = Paciente()
