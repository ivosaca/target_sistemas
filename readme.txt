 ## **Programas criados para o desafio técnico para vaga de Desenvolvedor Jr. **

******************************

#- `Desafio 1`:

*** 1. Considerando que o json abaixo tem registros de vendas de um time comercial, ***
*** faça um programa que leia os dados e calcule a comissão de cada vendedor, ***
 ***seguindo a seguinte regra para cada venda:***
 ***- Vendas abaixo de R$100,00 não gera comissão***
0 ***- Vendas abaixo de R$500,00 gera 1% de comissão***
 ***- A partir de R$500,00 gera 5% de comissão***
  
Utilizando a biblioteca pandas foi feito uma ordenação dos dados vindos do json para obter uma melhor visualização e organização dos mesmos.
Resultados obtidos em arquivo json com as taxas de comissão final para cada vendedor e arquivo .xlsx com 2 páginas sendo a primeira 
uma lista de comissão final aplicada para cada vendedor, e uma segunda pagina com a demonstração pontual de valor para cada venda realizada pelo vendedor. 

******************************

#- `Desafio 2`

***2. Faça um programa onde eu possa lançar movimentações ***
***de estoque dos produtos que estão no json abaixo, ***
***dando entrada ou saída da mercadoria no meu depósito, ***
***onde cada movimentação deve ter:***

    ***- Um número identificador único.    ***
    ***- Uma descrição para identificar o tipo da movimentação***
***realizada***
    ***- E que ao final da movimentação me retorne a qtde ***
***final do estoque do produto movimentado.***

Desafio feio levando em consideração o tempo de funcionamento do programa. Quando o programa inicia utiliza um json original dado pelo cliente,
dando a possibilidade de fazer movimentações de estoque listando todas as movimentações com data e hora. 
Podemos caso fosse necessário adicionar um local novo para aplicação de tambem um usuário responsável por tal movimentação.

******************************

#-`Desafio 3`

***Faça um programa que a partir de um valor e de uma data de vencimento, ***
***calcule o valor dos juros na data de hoje considerando que a multa seja ***
***de 2,5% ao dia.***

Para este desafio consideramos o valor de multa fixa, dando apenas a possilidade do usuário apresentar o valor a ser calculado como inicial
e a quantidade de dias nos quais a multa será aplicada. 

******************************

