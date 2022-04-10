### Projeto Cálculo do MMC e MDC

> O presente projeto tem o objetivo de achar os algorítmos para calcular o Mínimo Múltiplo Comum (MMC) e Máximo Divisor Comum de entre 2 números.

As etapas para os cálculos serão:
- Como decompor um número em fatores primos - _concluído_
- Como decompor simultâneamente 2 números em fatores primos - _em andamento_
- Como calcular o MMC - _em andamento_
- Como Calcular o MDC - _concluído_

Para cada etapa haverá um código.

Desejo que o projeto contribua para insights para novos projetos!
Observações e contribuições para melhoria serão bem vindas!

> PROJETO EM ANDAMENTO

Andamento do projeto:

00 - Modulos Extras:
- > Criei o módulo primo para ser reutilizado para verificar se um número é primo
- > Criei o módulo contarrep para verificar quantas vezes um valor em uma lista se repete em outra lista

01 - Decompor:
- > Na primeira versão, pegávamos os números de uma sequência para validar se eram primos, para depois validar se eram divisores do número em questão
- > Na segunda versão, primeiro validamos se o número da sequência é divisor do número em análise para depois validarmos se ele é primo, tornando o processo mais ágil
- > Após aprender um pouco mais, simplifiquei o código da decomposição na versão 3 e gerei o modulo decomp1 que pode ser reutilizado

03 - MDC:
- > Na versão 1, tentamos criar um único array com as decomposições dos 2 números, que não gerou o resultado esperado
- > Na versão 2, conseguimos decompor os itens separadamente e construir um novo array apenas com os itens que se repetem nos 2
- > Na versão 3, criei 2 vetores com a quantidade de vezes que cada base em comum entre a decomposição dos 2 números - esses vetores contém os potenciais expoentes. Depois, criei um teste que identificava o menor valor para o expoente entre os valores nos vetores, calculei as potências entre as bases e os menores expoentes e as adicionei em um novo vetor. Então, calculei o produto entre os itens deste último vetor e achei o MDC. Realizei todas as conferências e teste e o código foi validado.
- > Na versão 4, eu limpei dos os resíduos comentados no código, deixei apenas o produto entre os itens do vetor final como return da função e colquei a opção para o usuário inserir seus próprios números para teste e formatei o retorno final do código.
- > Na versão 5, implementei diversas simplificações aplicando os módulos decomp1 e contarrep, excluindo variáveis denecessárias e gerando um módulo que pode ser reutilizado


> Desenvolver os cálculos para achar o MDC e o MMC estão sendo um bom exercício para desenvolver minha lógica. No entanto, descobri que o Python já tem funções para realizar esses cálculos em sua biblioteca nativa _"math"_:
>- ***MMC - lcm()***
>- ***MDC - gcd()***