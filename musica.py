import requests
from datetime import datetime
import textwrap



def buscar_artista(nome_artista):
    """
    Função responsável por buscar as informações do artista na API TheAudioDB.
    Retorna um dicionário com os dados, ou None se não encontrar.
    """
    url = f"https://www.theaudiodb.com/api/v1/json/2/search.php?s={nome_artista}"
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()  
        dados = resposta.json()

      
        if dados["artists"] is None:
            return None
        else:
            return dados["artists"][0]
    except requests.exceptions.RequestException as erro:
        print(f"\n⚠️  Erro na conexão com a API: {erro}")
        return None


def exibir_informacoes(artista):
    """
    Exibe as informações do artista formatadas de forma agradável no terminal.
    """
    nome = artista.get("strArtist", "Não disponível")
    genero = artista.get("strGenre", "Não disponível")
    pais = artista.get("strCountry", "Não disponível")
    inicio = artista.get("intFormedYear", "Não disponível")
    bio_pt = artista.get("strBiographyPT") or "Biografia em português não disponível."
    site = artista.get("strWebsite") or "Nenhum site disponível"
    estilo = artista.get("strStyle") or "Não informado"
    data_consulta = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print("\n🎤🎶  INFORMAÇÕES DO ARTISTA  🎶🎤")
    print("=" * 70)
    print(f"🧑‍🎤 Nome: {nome}")
    print(f"🎵 Estilo: {estilo}")
    print(f"🎶 Gênero: {genero}")
    print(f"🌍 País: {pais}")
    print(f"📅 Início da carreira: {inicio}")
    print(f"🔗 Site: {site}")
    print(f"🕓 Consulta realizada em: {data_consulta}")
    print("-" * 70)

    print("📝 Biografia:")
    print(textwrap.fill(bio_pt, width=80))
    print("=" * 70)




print("🎧 PyTune - Buscador de Músicas com API 🎧")
print("=" * 70)
print("Pesquise informações sobre qualquer artista musical!")
print("Exemplo: Queen, Michael Jackson, Anitta, Coldplay...")
print("=" * 70)


nome_artista = input("Digite o nome do artista que deseja buscar: ").strip()

if not nome_artista:
    print("\n⚠️  Você precisa digitar o nome de um artista!")
else:
    print("\n🔎 Buscando informações, aguarde...\n")
    artista_encontrado = buscar_artista(nome_artista)

    if artista_encontrado:
        exibir_informacoes(artista_encontrado)
    else:
        print("❌ Artista não encontrado. Verifique o nome e tente novamente.")