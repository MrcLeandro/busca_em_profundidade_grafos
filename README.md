#Projeto: Busca em profundidade em grafos

## Etapas do projeto:

## rede_social.py : Criação de uma rede social com as seguintes características:
    ## É fictícia e modelada através de um grafo;
    ## Possui um caminho alternante entre os sexos masculino e feminino;
    ## O número de membros e o número de arcos podem ser definidos;
    ## Cria os membros aleatoriamente usando identificadores gerados pela biblioteca uuid;
    ## Cria os arcos que definem relações entre os membros da rede aleatoriamente até atingir o número definido pelo usuário

## Realizar busca em profundidade entre amigos na rede social gerando um caminho entre eles

## Calcula o grau de separação entre os amigos pesquisados

## app.py : usa o Streamlit para criação de uma interface web para que o usuário insira a quantidade de membros da rede social e receba os resultados do cálculo do Grau de separação e tempo de execução

## Para rodar a aplicação no contêiner foi necessário iniciá-lo com mapeamento da porta padrão do Streamlit (8501) para acessar ao browser do host.