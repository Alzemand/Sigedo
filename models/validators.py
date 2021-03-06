# -*- coding: utf-8 -*-
# Author: Alzemand

# ----- Validador de aluno -----
Aluno.nome.requires = [IS_TITLE()]
Aluno.cpf.requires = [IS_CPF(),
IS_NOT_IN_DB(db, 'aluno.cpf', error_message="CPF já cadastrado"),
IS_NOT_EMPTY(error_message='Informe o CPF')]
Aluno.telefone.requires = IS_PHONE(error_message="Telefone inválido")
Aluno.email.requires = IS_EMAIL(error_message="E-mail inválido")
Aluno.data_nascimento.requires = IS_DATE(format=T('%d/%m/%Y'), error_message='Data no formato dd/mm/aaaa')
Aluno.curso.requires = IS_IN_SET([
    "Administração",
    "Engenharia de Produção",
    "Sistemas de Informação",
    "Matemática"], error_message="Selecione um curso")
Aluno.civil.requires = IS_IN_SET([
    "Solteiro(a)",
    "Casado(a)",
    "Viúvo(a)"],error_message="Estado civil")
# ----- Representação de aluno -----
Aluno.cpf.represent = lambda value, row: MASK_CPF()(value)
#Aluno.matricula.represent = lambda value, row: to_telefone(value)


# ----- Validador de professor -----
Professor.nome.requires = [IS_TITLE()]
Professor.cpf.requires = [IS_CPF(),
IS_NOT_IN_DB(db, 'professor.cpf', error_message="CPF já cadastrado"),
IS_NOT_EMPTY(error_message='Informe o CPF')]
Professor.telefone.requires = IS_PHONE(error_message="Telefone inválido")
Professor.email.requires = IS_EMAIL(error_message="E-mail inválido")


# ----- Validador de empresa -----
Empresa.nome.requires = [IS_TITLE()]
Empresa.razao.requires = [IS_TITLE()]
Empresa.cnpj.requires = [IS_CNPJ(),
IS_NOT_IN_DB(db, 'empresa.cnpj', error_message="CNPJ já cadastrado"),
IS_NOT_EMPTY(error_message='Informe o CNPJ')]
Empresa.telefone.requires = IS_PHONE(error_message="Telefone inválido")
Empresa.email.requires = IS_EMAIL(error_message="E-mail inválido")
# ----- Representação de aluno -----
Empresa.cnpj.represent = lambda value, row: MASK_CNPJ()(value)
Empresa.telefone.represent = lambda value, row: to_telefone(value)


# ----- Validador de estágio -----
Estagio.data_inicio.requires = IS_DATE(format=T('%d/%m/%Y'), error_message='Data no formato dd/mm/aaaa')
Estagio.data_fim.requires = IS_DATE(format=T('%d/%m/%Y'), error_message='Data no formato dd/mm/aaaa')
Estagio.situacao.requires = IS_IN_SET([
    "Matriculado",
    "Aprovado",
    "Cancelado",
    "Reprovado"], error_message="Selecione um estado")

Estagio.tipo.requires = IS_IN_SET([
    "Obrigatório - Estágio 1",
    "Obrigatório - Estágio 2",
    "Não Obrigatório"], error_message="Selecione uma tipo de estágio")

# Estagio.aluno.requires = IS_IN_DB(db, db.aluno.cpf, '%(nome)s')
# Estagio.professor.requires = IS_IN_DB(db, db.professor.cpf, '%(nome)s')
# Estagio.empresa.requires = IS_IN_DB(db, db.empresa.cnpj, '%(nome)s')
