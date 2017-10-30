#!/usr/bin/env python

from graph import Graph, VertexNotFoundException
from curriculum import Curriculum
import graph_func as funcs


### Functions ###

def read_courses():
    course = input("")
    completed = list()
    while course != "fim":
        completed.append(course)
        course = input("")
    return completed


def define_plan(n_smts):
    while g.order() > 0:
        fonts = g.fonts()  # getting vertices that has exit degree equals to 0
        total_hours = 0
        recommended = list()

        for v in fonts:
            v_credits = g.as_dict()[v][0].credits  # [0]: get Course object
            if total_hours + v_credits <= 28:
                recommended.append(v)
                total_hours += v_credits

        n_smts += 1
        print(str(n_smts) + "º semestre:")
        for course in recommended:
            print("{} ".format(course), end='')
        print("\n")

        for course in recommended:
            g.remove_vertex(course)


### RUN ###

c = Curriculum()
g = c.graph
    
print("Ordem topológica do currículo:")
print(g.get_topological_sorting())
print("*"*80, end='\n\n')


print("Quantos semestres você já cursou?")
n_smts = int(input(""))


print("Digite o código das disciplinas nas quais você já foi aprovado (ine5413, por exemplo):")
print("Digite 'fim' para finalizar a inserção")
completed = read_courses()
for course in completed:
    g.remove_vertex(course)


print("*"*80, end='\n\n')
print("Plano para semestres subsequentes\n")
define_plan(n_smts)

print("*"*80)
print("Desenvolvido por Ramna Sidharta e Vinicius Macelai UFSC-2017")
