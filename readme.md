# AUTOMATIZAÇÃO WEB PARA CAPTURA DE PREÇOS

## Tarefa escolhida e a motivação para automatizá-la

A tarefa escolhida foi automatizar a captura de preços de um tênis em dois sites de e-commerce, Netshoes e Buscapé. O código usa a biblioteca Selenium para interagir automaticamente com as páginas, coletando dados do produto pesquisado. A motivação para essa automação surgiu da necessidade de acompanhar as flutuações de preço para realizar uma compra no momento mais vantajoso. Esse processo manual de verificar preços é repetitivo e propenso a erros. A automação facilita a coleta dos dados de forma mais precisa e rápida, proporcionando uma comparação mais eficiente e informativa.

## Os objetivos específicos da automação

-   Realizar uma pesquisa em dois sites diferentes com base em um termo de busca específico.
-   Extrair o nome, preço, data e hora dos produtos retornados na pesquisa.
-   Armazenar esses dados em arquivos CSV separados para cada site, com registros de data e hora para facilitar a comparação futura.
-   Garantir que o processo seja estável e capaz de lidar com pequenas variações no layout dos sites.

## Os desafios enfrentados durante o desenvolvimento e as soluções adotadas

Durante o desenvolvimento, alguns dos desafios encontrados incluíram a localização de elementos no HTML dinâmico das páginas e o gerenciamento de variações de layout entre os sites. Para superar esses obstáculos, foi utilizado XPath para selecionar elementos de forma mais flexível, permitindo encontrar itens específicos mesmo com mudanças de estrutura ou atributos. Além disso, um `try-except` foi implementado para capturar e gerenciar erros, evitando que uma falha interrompa todo o processo. Pausas (`sleep`) foram adicionadas para garantir que os elementos tivessem tempo de carregar antes de serem acessados, minimizando falhas por carregamento incompleto.

## Possíveis melhorias ou extensões futuras para o projeto

Para aprimorar o projeto, uma possível melhoria seria adicionar um banco de dados para armazenar as informações de forma mais estruturada e evitar a criação de múltiplos arquivos CSV. Além disso, a implementação de uma função de notificação que alerte o usuário quando o preço atingir um valor-alvo específico seria interessante e útil.

---
