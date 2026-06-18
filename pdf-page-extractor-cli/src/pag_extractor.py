import os
from pathlib import Path
from pypdf import PdfReader, PdfWriter

# --- LÓGICA DE ANCORAGEM ---
# O script sobe 3 níveis a partir de 'src' para encontrar a pasta 'Carreira'
PASTA_RAIZ = Path(__file__).resolve().parents[3]
PASTA_SAIDA = Path.home() / "Desktop" / "Paginas_Extraidas"

PASTA_SAIDA.mkdir(parents=True, exist_ok=True)

def extrair_seletivo():
    if not PASTA_RAIZ.exists():
        print(f"\n[ERRO] Raiz não detectada em: {PASTA_RAIZ}")
        return False

    # NÍVEL 1: Seleção de Pasta
    subpastas = sorted([p for p in PASTA_RAIZ.iterdir() if p.is_dir() and not p.name.startswith('.')])
    
    if not subpastas:
        print(f"[AVISO] Nenhuma subpasta encontrada em {PASTA_RAIZ.name}")
        return False

    print("\n" + "═"*60)
    print(f"EXTRATOR DE PDF | RAIZ: {PASTA_RAIZ.name}")
    print("═"*60)
    for idx, pasta in enumerate(subpastas, 1):
        print(f"{idx:02d} | [PASTA] {pasta.name}")
    print("00 | SAIR")
    print("═"*60)

    try:
        escolha_p = int(input("\nSelecione a PASTA (número): "))
        if escolha_p == 0: 
            return "sair"
        if not (1 <= escolha_p <= len(subpastas)): 
            print("[ERRO] Opção de pasta inválida.")
            return False
        
        pasta_escolhida = subpastas[escolha_p - 1]

        # NÍVEL 2: Seleção de Arquivo
        arquivos_pdf = sorted(list(pasta_escolhida.glob("*.pdf")))
        if not arquivos_pdf:
            print(f"\n[AVISO] Nenhum PDF em: {pasta_escolhida.name}")
            return False

        print("\n" + "─"*60)
        print(f"ARQUIVOS EM: {pasta_escolhida.name}")
        for idx, arq in enumerate(arquivos_pdf, 1):
            print(f"{idx:02d} | {arq.name}")
        print("─"*60)

        escolha_a = int(input("\nSelecione o ARQUIVO (número): "))
        if not (1 <= escolha_a <= len(arquivos_pdf)):
            print("[ERRO] Opção de arquivo inválida.")
            return False
            
        arquivo_alvo = arquivos_pdf[escolha_a - 1]

        # NÍVEL 3: Extração
        reader = PdfReader(str(arquivo_alvo))
        total_pags = len(reader.pages)
        print(f"\n[INFO] {arquivo_alvo.name} | Total: {total_pags} páginas")

        inicio = int(input("Página INICIAL: "))
        fim = int(input("Página FINAL: "))

        if inicio < 1 or inicio > total_pags or inicio > fim:
            print("[ERRO] Intervalo de páginas inválido.")
            return False

        writer = PdfWriter()
        fim_real = min(fim, total_pags)
        for i in range(inicio - 1, fim_real):
            writer.add_page(reader.pages[i])

        nome_saida = f"EXT_{arquivo_alvo.stem}_P{inicio}-{fim_real}.pdf"
        caminho_final = PASTA_SAIDA / nome_saida
        
        with open(caminho_final, "wb") as out_f:
            writer.write(out_f)

        print(f"\n[SUCESSO] Gerado em: Desktop/Paginas_Extraidas/{nome_saida}")
        return True

    except ValueError:
        print("[ERRO] Entrada inválida. Use apenas números.")
        return False
    except Exception as e:
        print(f"[FALHA] Erro inesperado: {e}")
        return False

if __name__ == "__main__":
    while True:
        resultado = extrair_seletivo()
        if resultado == "sair":
            break
        print("\n" + "."*40)
        input("Pressione Enter para nova operação...")