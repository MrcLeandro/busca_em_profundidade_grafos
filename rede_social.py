#!/usr/bin/env python
# coding: utf-8

# Cria uma classe Person

# In[78]:


import uuid
from typing_extensions import Self
from collections import deque
import random
import time
import sys
import os
import pandas as pd

# Caminho para a pasta raiz do projeto
ROOT_DIR = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(ROOT_DIR)

# In[79]:


class Person(object):

    def __init__(self, uid, genre):
        self._uid = uid
        self._genre = genre

    def get_uid(self):
        return self._uid

    def get_genre(self):
        return self._genre

# Cria a classe FriendNetwork com o número de membros (nós) e amizades(arcos) definidos no notebook main

# In[80]:


class FriendNetwork(object):

    def __init__(self, people_num, connections_num):
        self._people_num = people_num
        self._connections_num = connections_num
        self._graph = self._generate_graph()

    def _generate_graph(self):

        people = []
        for person_index in range(self._people_num):
#Gera um UUID aleatório versão 4 e o converte para uma string
            uid = str(uuid.uuid4()) 
            genre = 'female' if person_index % 2 else 'male'
            people.append(Person(uid, genre))

        conn_num = 0
        graph = {}
# criando um grafo auxiliar para agilizar algumas buscas
        graph_aux = {}  

# início - criando um caminho alternante

# cria uma entrada no dicionário graph com a chave person_uid, e o valor associado a essa chave é um dicionário 
# contendo informações sobre a pessoa, incluindo o objeto Person correspondente e uma lista inicialmente
# vazia para armazenar seus amigos.
        person = people[conn_num]
        person_uid = person.get_uid()
        graph[person_uid] = {
            'this': person,
            'friends': []
        }

        graph_aux[person_uid] = {}

#Como a lista people alterna seus elementos entre homem e mulher, ao preencher uma lista de amigos
 #de forma sequencial nesta lista será criado um caminho alternante
        while conn_num < self._people_num - 1:
            friend = people[conn_num + 1]
            friend_uid = friend.get_uid()
            graph[friend_uid] = {
                'this': friend,
                'friends': []
            }
            graph_aux[friend_uid] = {}

#Adiciona os amigos na lista de uma pessoa e vice-vers e gera grafos auxiliares que indicam essas
 #relações entre eles como se fossem um matriz entre todas as pessoas em que o valor "true" indica 
 #uma relação de amizade entre elas

            graph[person_uid]['friends'].append(friend)
            graph[friend_uid]['friends'].append(person)
            graph_aux[person_uid][friend_uid] = True
            graph_aux[friend_uid][person_uid] = True
            conn_num += 1

            person = friend
            person_uid = friend_uid

# fim - criando um caminho alternante

#Escolhe aleatoriamente 2 pessoas na lista people, checa se não se tratam da mesma pessoa ou se já existe
#  relação entre eles e caso negativo, adiciona a relação. Esta ação é realizada até que o número de arcos seja alcançado

        while conn_num < self._connections_num:
            person, friend = random.sample(people, 2)
            person_uid = person.get_uid()
            friend_uid = friend.get_uid()

          
            if person_uid not in graph:
                graph[person_uid] = {
                    'this': person,
                    'friends': []
                }
# Criando um índice auxiliar para os vizinhos de cada vértice inserido no grafo

                graph_aux[person_uid] = {}

            if friend_uid not in graph:
                graph[friend_uid] = {
                    'this': friend,
                    'friends': []
                }

# criando um índice auxiliar para os vizinhos de cada vértice inserido no grafo

                graph_aux[friend_uid] = {}
            
            if person_uid == friend_uid or \
                    friend_uid in graph_aux[person_uid]:
                continue

            graph[person_uid]['friends'].append(friend)
            graph[friend_uid]['friends'].append(person)

# Adicionar vizinho também nos índices do grafo auxiliar

            graph_aux[person_uid][friend_uid] = True
            graph_aux[friend_uid][person_uid] = True
            conn_num += 1
        return graph
        
    def get_person_by_uid(self, uid):
        return self._graph[uid]['this']

#Algoritmo de busca em profundidade

    def _search(self, person_uid, friend_uid):
        self.person_uid = person_uid
        self.friend_uid = friend_uid

# iniciando os auxiliares da busca
        color=dict()
        predecessor=dict()
        d=dict()
        Q = deque()
        C = 'C'
        P = 'P'
        B = 'B'
        path = []

        for u in self._graph:
            color[u]= B
            predecessor[u]= None
            d[u]= None

 # realiza a busca entre person and friend sorteados e gera o caminho da busca

        color[self.person_uid] = C
        d[self.person_uid] = 0
        Q.append(self.person_uid)

        while Q[0] != self.friend_uid:
          u = Q.popleft()
          #if u == self.friend_uid:
           # break
          for v in self._graph[u]['friends']:
            v_uid = v.get_uid()
            v_genre = v.get_genre()
            if color[v_uid] == B:
             g = self._graph[u]['this'].get_genre()
             if v_genre != g:
              color[v_uid] = C
              predecessor[v_uid] = u
              d[v_uid] = d[u] + 1
              Q.append(v_uid)
          color[u] = P
        path.append(self.friend_uid)
        while path[-1] != self.person_uid:
            path.append(predecessor[path[-1]])
     # path.append(self.person_uid)
        path.reverse()

        return path
    
#Calcula o grau de separação entre dois amigos para o caminho de busca gerado na busca em profundidade        
    def get_separation_degree(self):

        total_paths_len = 0
        for _ in range(100):
            person_uid, friend_uid = random.sample([*self._graph.keys()], 2)
            path = self._search(person_uid, friend_uid)
            total_paths_len += len(path) - 1
        for i in path:
          person = self._graph[i]['this']
          genre = person.get_genre()
          #print(genre)
        return total_paths_len / 100      

# Código que passa o número de amigos (nós) e o número de relações de amizade (arcos do grafo)

# In[81]:


def main():
    dfe = pd.read_csv("entradas.csv")
    friend_network = FriendNetwork(dfe.iloc[0,1],dfe.iloc[0,2])
    s_time = time.time()
    separation_degree = friend_network.get_separation_degree()
    e_time = time.time()
    resultados = {
        'Grau de separação': [separation_degree],
        'Tempo de cálculo': [e_time - s_time]
    }
    print(resultados)
    print("Grau de separação:", separation_degree)
    print("Tempo =", e_time - s_time)
    df = pd.DataFrame(resultados)
    df.to_csv('resultados.csv', index=False)


if __name__ == '__main__':
    main()

# %%
