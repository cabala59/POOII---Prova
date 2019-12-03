import pessoa
import aluno
import professor

#Retorna na tela dados de uma pessoa
pessoa1 = pessoa.Pessoa('Raimundo','Nonato')
print("Retornando as caracteristicas de pessoa com nome e sobrenome:")
print("Nome da pessoa: {0} {1} ".format(pessoa1.getNome(),pessoa1.getSobrenome()))

#Retorna na tela dados de um aluno
aluno1 = aluno.Aluno(91604176, 'Luis','Carlos')
print("\nRetornando as caracteristicas de aluno com nome,sobrenome e matricula:")
print("Nome do aluno: {0} {1} ".format(aluno1.getNome(),aluno1.getSobrenome()),"\nMatricula do aluno:{} ".format(aluno1.getMatricula()))

#Retorna na tela dados de um professor
professor1 = professor.Professor(3540, 'Alan','Souza')
print("\nRetornando as caracteristicas de professor com nome, sobrenome e codigo:")
print("Nome do professor: {0} {1}".format(professor1.getNome(),professor1.getSobrenome()),"\nCodigo do professor:{} ".format(professor1.getCodigo()))

