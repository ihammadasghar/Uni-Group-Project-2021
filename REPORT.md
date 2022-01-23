# Report Projecto Final AP 
## Membros do grupo:
- Syed Anees Ur Rehman Asghar - 30008766
- Syed Hammad Ur Rehman Asghar - 30008767
- Walgidio dos Santos - 30009596
- André Castanheira - 30008972
- Igor Gerson Gonçalves Paulo - 30009443


## Descrição de todos os comandos e funcionalidades do programa

### Estado do programa
Quando a função "main" dentro do "cli.py" é executada, a variável "game_data" é inicializada utilizando a função "get_game_data" dentro de "GameController". A variável "game_data" acompanha o estado do nosso programa e tem dois chaves 'board' e 'player_records'.

### Registar Jogadores
Quando o comando "RJ NomeJogador" é executado, verificamos se o número correto de argumentos (1) foi passado pelo utilizador para chamar este comando usando a função "is_nargs_correct" (cli.py). Em seguida, a função "register_player" dentro do "GameController" é invocada, o que verifica, se um jogador com o nome dado já não existir, cria um novo instance de registo de jogador usando o nome dado e adiciona o novo registo do jogador à "player_records" de game_data. Finalmente, a função "register_player" de "cli.py" imprime a mensagem de saída relevante baseado no valor de retorno da função "register_player" de "GameController".

### Listar Jogadores
Para o comando "LJ", verificamos primeiro se o número correto de argumentos foi passado pelo utilizador, que é 0. Depois, através da função "list_players" de "cli.py", chamamos a função "get_sorted_players" de "GameController". O "get_sorted_players" chama a função "sort_players", que usa algoritmo de bubble sort para ordenar os registos dos jogadores por vitórias e, em seguida, pelo nome do jogador. Finalmente, a lista ordenada de jogadores é retornada, que é depois apresentada ao utilizador no formato relevante pela função "list_players" de "cli.py"

### Iniciar Jogo
Para o comando "IJ", verificamos primeiro se o número correto de argumentos foi passado pelo utilizador, que é 2 - o nome dos dois jogadores, utilizando a função "is_nargs_correct" (cli.py). Em seguida, através da função "start_game" em "cli.py", a função "start_game" de "GameController" é chamada, o que faz então o seguinte:
 - Verificar se um jogo ainda não está em curso usando a função "is_game_in_progress" (GameController), que retorna True se o nome player_1 no board não for "None"
 - Verificar se ambos os jogadores estão registados
 - Preparar o tabuleiro para o jogo
 - Atualizar os registos dos jogadores
 
Finalmente, a função "start_game" de "cli.py" imprime a mensagem de saída relevante baseado no dicionário "resultado" retornado pela função "start_game" de "GameController".

### Iniciar jogo automático
Para o comando "IJA", verificamos primeiro se o número correto de argumentos foi passado pelo utilizador, 2, o nome do jogador e o nível de jogo. Em seguida, através da função "start_auto_game" em "cli.py", a função "start_game" de "GameController" é chamada com parâmetro "player_2_name" igual a "CPU", a função "start_game" de "GameController" faz o seguinte:
 - Verificar se um jogo ainda não está em curso usando o "is_game_in_progress" (GameController)
 - Verificar se ambos os jogadores estão registados
 - Preparar o tabuleiro para o jogo
 - Atualizar os registos dos jogadores
 
Finalmente, a função "start_auto_game" de "cli.py" imprime a mensagem de saída relevante baseado no dicionário "resultado" retornado pela função "start_game" de "GameController".

### Detalhes do jogo
Para o comando "DJ", verificamos primeiro se o número correto de argumentos foi passado pelo utilizador, 0 neste caso. Em seguida, invocamos a função "display_game_detail" em "cli.py", que imprime o estado atual do conselho no formato requerido. Se nenhum jogo estiver em curso, a função "display_game_detail" imprime uma mensagem de erro.

### Jogada
Para o comando "J", verificamos primeiro se o número correto de argumentos foi passado pelo utilizador, 2 - o nome do jogador e a posição. Em seguida, o "player_move" (GameController) é invocado através da função "player_move" (cli.py), que faz o seguinte:
- Verificar se o jogo está em curso
- Verificar se o jogador está registado
- Verificar se o jogador faz parte do jogo atual utilizando a função "is_part_of_game"
- Executar a jogada do jogador utilizando a função "execute_move" (GameController), que faz o seguinte:
    - Espalhar sementes e update o Board.
    - Capturar se as condições de captura estiverem satisfeitas
    - Verificar se o jogador tem direito a outra jogada e retorna "has_another_move" que é True quando o jogador tem direito a outra jogada, False em caso contrário
- Verificar se as condições para o fim do jogo são satisfeitas utilizando a função "is_game_over", que retorna True se um ou ambos os jogadores não tiverem mais sementes para jogar. Se "is_game_over" (GameController) retorna True, chame a função "wrap_up_game", que faz o seguinte:
    - Atualizar os registos dos jogadores
    - Repôr a placa de programa
    - Retornar a pontuação final, ou seja, "game_over_data"
- Verificar se o jogador tem direito a outro jogada
- Se jogar contra o CPU, faça o CPU mover-se até que a CPU tenha o direito de agir. Depois de cada jogada CPU, verificar se o jogo pode terminar e chame o "wrap_up_game" (GameController) se puder. A posição para jogada CPU é encontrada utilizando a função "find_auto_move" (GameController) que faz o seguinte:
    - Se a dificuldade for “Normal”, retorna a posição mais à esquerda disponível
    - Se a dificuldade é "Avançada"
        - Retornar a posição que permite à CPU capturar
        - Retornar a posição que permite à CPU ter outra jogada
        - Retornar a posição mais à direita disponível
        
Finalmente, a função "player_move" (cli.py) apresenta a saída adequada ao utilizador baseado no dicionário "resultado" retornado pelo "player_move" (GameController).

### Desistir Jogo
Para o comando "D", verificamos primeiro se o número de argumentos transmitidos pelo utilizador está correto, ou 1 ou 2, ou seja, o(s) nome do jogador. Em seguida, invocamos a função "give_up_game" (GameController) através do "give_up_game"(cli.py), que faz o seguinte:
- Verificar se um jogo está em curso usando o "is_game_in_progress" (GameController)
- Verificar se o ou os jogadores com o ou os nomes do jogador ou o nome do jogador são registados
- Atualizar os registos dos jogadores baseado em se um ou ambos os jogadores desistiram do jogo
- Repôr o estado do Board

Finalmente, a função give_up_game (cli.py) apresenta a saída adequada ao utilizador baseado no dicionário "resultado" retornado pela função give_up_game (GameController).
### Gravar
Para o comando "G", verificamos primeiro se o número de argumentos recebidos pelo utilizador é correto, ou seja, 1 - o nome do ficheiro. Em seguida, invocamos a função save_game (PersistenceController), que faz o seguinte:
- Criar o diretório "saved" se já não existir
- Abrir um ficheiro com o nome de ficheiro dado e escreve o "game_data" dentro desse ficheiro

### Ler
Para o comando "L", verificamos primeiro se o número de argumentos recebidos pelo utilizador é correto, ou seja, 1 - o nome do ficheiro. Em seguida, invocamos a função load_game (PersistenceController) que abre o ficheiro com o nome de ficheiro dado e retorne o conteúdo do ficheiro.
