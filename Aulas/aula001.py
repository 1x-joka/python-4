# ============= CONTEXTO HISTÓRICO =============
# -> Qual é o principal objetivo da OOP? Representar elementos (objetos) do mundo real nos sistemas computacionais
# -> De onde veio? Linguagem de Baixo Nível (1950): Assembly; Linguagens Lineares (1955): Cobol, Fortran, C, Basic ----> Dijkstra (matemático) ----> Linguagens Estruturadas (1960): ALGOrithmic Language, ALGOL60; Linguagens Modulares (1965): organizar códigos diferentes em módulos; Linguagens Orientadas a Objetos (1970): Simula (ALGOL60 + 1 funcionalidade, o objeto), Python
# OOAD: Object Oriented Analysis and Design (além de codar, é importante planejar o sistema/design)
    # UML: Princípio derivado da OOAD. Conjunto de pensamentos/diagramas de um sistema antes de programar

# ============= VANTAGENS =============
# -> Vantagens COMERNada: C = Confiabilidade; O = Oportunidade; M = Manutebilidade; E = Extensibilidade; R = Reutilizável; N = Naturalidade
    # Confiabilidade = O isolamento entre as partes gera algo mais seguro. Ao alterar uma das partes, nenhuma outra é afetada (ex.: trocar a roda de um carro não altera todo o mecanismo de dentro = mexer em um pedaço do software não fará você mexer em outros)
    # Oportunidade = Ao dividir tudo em partes, cada uma delas pode ser desenvolvida em paralelo (ex.: o farol e o banco de um carro pode estar sendo desenvolvimento separadamente e depois eles só juntam, claro que em uma ordem definida)
    # Manutebilidade = Atualizar é mais fácil. Uma pequena alteração vai beneficiar todas as partes relacionadas (ex.: trocar um motor de um carro por outro, todo o benefício de potência, etc. irá beneficiar as outras partes)
    # Extensibilidade = Um sistema não deve ser estático. Tudo deve mudar e crescer para permanecer útil (ex.: para carregar mais coisas no carro eu não preciso trocar de carro, eu posso colocar bagageiro, carretinha, etc.)
    # Reutilizável = Objetos que foram criados para um sistema podem ser aproveitados em outros sistemas (ex.: o motor do gol pode ser reaproveitado no fox)
    # Naturalidade = Mais fácil de entender. Maior atenção às funcionalidades do que aos detalhes de implementação (ex.: quando você for comprar um carro você precisa saber exatamente o processo de aceleração? Não, pois você é o usuário)

# ============= DEFINIÇÕES =============
# -> Classe: Formato a ser seguido sempre que for fazer um objeto do mesmo tipo ou com as mesmas características ou com os mesmos comportamentos (ex.: a forma de um biscoito, um chassi de um carro, etc.)
    # -> Diagrama de Classes UML: nome de classe, características que ela vai ter (atributos) e coisas que podem fazer (métodos)
# -> Instância: Seguir o padrão que foi definido na classe para poder criar um objeto (ex.: a forma do biscoito pressionando a massa, estou instanciando a forma)
# -> Objeto: Coisa material ou abstrata que é feita a partir de um modelo e pode ser descrita por meio das suas características, comportamentos e estado atual (ex.: o resultado do biscoito após pressionar a forma na massa pura)
# -> Estado: Especificação do objeto (ex.: um biscoito a 55°C, mordido, de pistache, etc.)
# -> Objetos Abstratos: Uma consulta marcada no médico, um processo de venda, um compromisso ou reunião, uma aula na faculdade, uma transação bancária, uma reserva de voo, um erro do sistema...