# coding: utf-8

import pymysql
import time

class Connection():
	def __init__(self):
		try:
			self.con = pymysql.connect( host = "localhost", 
									user = "Milton-Luis", 
									password = "cocytusbreath1+",
									charset = "utf8mb4"
									)
			self.con.cursor()
		except Exception as e:
			return  e
		

		self.CreateDB()


	def CreateDB(self):
		with self.con.cursor() as cursor:		
			try:

				sqlDB = ("CREATE DATABASE imc")
				cursor.execute(sqlDB)
				print("\n+------------------------------------------+")

			
				print("|Banco criado com sucesso!!                |")
				print("+------------------------------------------+")
				time.sleep(2)
			
			except pymysql.DatabaseError as e:
				return e
				print("\nErro ao criar banco - {}".format(e))

			finally:
				cursor.close()

		self.CreateTable()

	def CreateTable(self):
		with self.con.cursor() as new_cursor:
			try:
				tabela = "imc.paciente"

				sql=""" CREATE TABLE {} ( 
						id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL COLLATE utf8_bin,
						nome  CHAR(20) NOT NULL COLLATE utf8_bin,
						endereco CHAR(20) NOT NULL COLLATE utf8_bin,
						altura FLOAT NOT NULL COLLATE utf8_bin,
						peso FLOAT NOT NULL COLLATE utf8_bin,
						resultado FLOAT NOT NULL COLLATE utf8_bin
						) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin""".format(tabela)

				new_cursor.execute(sql)
				print("|Tabela criada com sucesso!!               |")
				print("+------------------------------------------+")
				time.sleep(2)

			except pymysql.DatabaseError as tableError:
				print("\nErro ao criar tabela - {}".format(tableError))
				print("+------------------------------------------+")
				return tableError

			finally:
				new_cursor.close()
		
db = Connection()

