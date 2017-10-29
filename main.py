#!/usr/bin/env python

from graph import Graph, VertexNotFoundException
from curriculum import Curriculum
import graph_func as funcs

if __name__ == "__main__":
    c = Curriculum()
    
    print("Ordem topologica do curriculo:")
    print(c.g.get_topological_sorting())

    print("*"*120)
    
    print("Quantos semestres voce ja cursou?")
    semester = int(input(""))

    print("Digite o codigo das disciplinas que voce ja foi aprovado, ine5401 por exemplo:")
    print("Digite 'fim' para finalizar a insercao")

    course = input("")
    completed = list()
    while course != "fim":
        completed.append(course)
        course = input("")

    for course in completed:
        c.g.remove_vertex(course)

    print("*"*120)
    print("Plano para semestres subsequentes: ")

    while c.g.order() > 0:
        fonts = c.g.fonts()

        total_hours = 0
        recommended = list()

        for v in fonts:
            if total_hours + c.g.as_dict()[v][0].credits <= 28:
                recommended.append(v)
                total_hours += c.g.as_dict()[v][0].credits

        semester += 1
        print("Faca no "+str(semester)+"o semestre:")
        for course in recommended:
            print("{} ".format(course), end='')
        print("\n")

        for course in recommended:
            c.g.remove_vertex(course)

    print("*"*120)
    print("Desenvolvido por Ramna Sidharta e Vinicius Macelai UFSC-2017")
