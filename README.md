# Projeto 15: Buscador de Músicas com API 🎶

## O Cenário 👨‍💼

Você continua sua jornada na startup de streaming "PyTune". O serviço, que começou com uma lista de músicas fixa no código, agora precisa evoluir para se tornar um verdadeiro catálogo musical.

Sua nova missão é integrar a PyTune com um banco de dados musical externo através de uma API. A primeira funcionalidade a ser desenvolvida é uma ferramenta de busca: o usuário deve ser capaz de digitar o nome de qualquer artista e receber informações detalhadas sobre ele, como sua biografia e seus álbuns.

Você vai construir um script Python que se conecta a uma API de música, busca por um artista e exibe os dados encontrados de forma organizada no terminal.

## 📋 Requisitos da Missão

A equipe da PyTune precisa de um protótipo que prove que a integração é possível. Seu script deve atender aos seguintes requisitos:

1.  **Fazer uma Requisição Web:** Utilizar a biblioteca `requests` do Python para fazer uma chamada (`GET request`) à API do The Audio DB.
2.  **Busca por Artista:** O script deve ser interativo, perguntando ao usuário o nome do artista que ele deseja buscar.
3.  **Montar a URL Dinamicamente:** O nome do artista fornecido pelo usuário deve ser inserido na URL da API para realizar a busca correta.
      * **URL Base da API:** `https://www.theaudiodb.com/api/v1/json/2/search.php?s=NOME_DO_ARTISTA`
4.  **Processar a Resposta JSON:** O script deve "ler" a resposta JSON da API e extrair informações relevantes, como:
      * Biografia do artista (em português, se disponível).
      * Gênero musical.
      * Ano de formação da banda/início da carreira.
5.  **Exibir os Resultados:** As informações devem ser impressas de forma clara e organizada no terminal.
6.  **Tratamento de Erros:** Se o artista não for encontrado, a API retornará um resultado vazio. O script deve ser capaz de identificar isso e exibir uma mensagem amigável, como "Artista não encontrado.", em vez de quebrar.

## 💡 Roteiro Sugerido para o Sucesso

1.  **Instale a Biblioteca**: Se ainda não tiver, abra o terminal e rode: `pip install requests`.
2.  **Importe a Biblioteca**: No seu arquivo Python, comece com: `import requests`.
3.  **Peça o Nome do Artista**: Use a função `input()` para guardar o nome do artista em uma variável.
4.  **Monte a URL da Requisição**: Use uma f-string para construir a URL completa, inserindo o nome do artista.
    ```python
    nome_artista = input("Digite o nome de um artista: ")
    url = f"https://www.theaudiodb.com/api/v1/json/2/search.php?s={nome_artista}"
    ```
5.  **Faça a Requisição e Verifique o Status**: Chame a API e verifique se a comunicação ocorreu com sucesso (código 200).
    ```python
    response = requests.get(url)
    if response.status_code != 200:
        print("Erro ao conectar com a API.")
    ```
6.  **Converta para JSON e Verifique o Resultado**:
    ```python
    dados = response.json()

    # A API retorna {'artists': None} se não encontrar nada
    if dados['artists'] is None:
        print("Artista não encontrado.")
    else:
        # Se encontrou, os dados estarão no primeiro item da lista
        artista = dados['artists'][0]
    ```
7.  **Extraia e Imprima as Informações**: Acesse as chaves do dicionário `artista` para pegar os dados que você quer.
    ```python
    print(f"\n--- Informações sobre: {artista['strArtist']} ---")
    print(f"Gênero: {artista['strGenre']}")
    print(f"País: {artista['strCountry']}")
    print(f"Início da Carreira: {artista['intFormedYear']}")
    print(f"\nBiografia (PT): {artista['strBiographyPT']}")
    ```

