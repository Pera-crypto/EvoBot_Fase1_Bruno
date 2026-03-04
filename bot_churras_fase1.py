# ==========================================
# Churras.AI - Fase 1
# Chatbot Determinístico (Base Raiz)
# ==========================================

# Mensagem inicial exibida ao iniciar o programa
print("=== Churras.AI Fase 1 ===")
print("Digite: oi, valor, data ou sair\n")

# Estado da conversa
data_evento = ""

# Datas já ocupadas internamente (não devem ser exibidas ao cliente)
datas_ocupadas = {
    "10/10/2026",
    "15/10/2026",
    "20/10/2026",
}

link_agenda = "https://calendar.google.com"

saudacoes = {
    "oi",
    "ola",
    "olá",
    "eai",
    "e aí",
    "bom dia",
    "boa tarde",
    "boa noite",
    "salve",
}

palavras_valor = {
    "valor",
    "preco",
    "preço",
    "orcamento",
    "orçamento",
    "quanto custa",
    "investimento",
}

palavras_data = {
    "data",
    "datas",
    "agenda",
    "calendario",
    "calendário",
    "disponibilidade",
    "dia",
}

palavras_sair = {
    "sair",
    "encerrar",
    "tchau",
    "ate logo",
    "até logo",
    "fim",
}

# Loop infinito para manter o bot ativo
while True:

    # Recebe a mensagem do usuário
    mensagem_original = input("Você: ")
    mensagem = mensagem_original.strip().lower()

    # Estrutura de decisão
    # Verifica exatamente o que foi digitado

    if mensagem in saudacoes:
        print("Churras.AI: Olá! Posso te ajudar com orçamento e disponibilidade para seu churrasco.")

    if mensagem in palavras_valor:
        print(
            "Churras.AI: Para passar o valor certinho preciso da data do evento. "
            "Envie no formato Data: DD/MM/AAAA."
        )

    if mensagem in palavras_data:
        print("Churras.AI: Consulte nossa agenda neste link: " f"{link_agenda}")
        if data_evento:
            if data_evento in datas_ocupadas:
                print("Churras.AI: A data informada está indisponível no momento. Pode enviar outra data?")
            else:
                print("Churras.AI: A data informada está com disponibilidade.")
        else:
            print("Churras.AI: Me informe a data desejada para eu validar disponibilidade.")

    if mensagem.startswith("data:"):
        data_evento = mensagem_original.split(":", 1)[1].strip()
        if data_evento:
            if data_evento in datas_ocupadas:
                print("Churras.AI: Essa data está indisponível. Me envie outra opção de data.")
                data_evento = ""
            else:
                print("Churras.AI: Data recebida e disponível!")

    if mensagem in palavras_sair:
        print("Churras.AI: Encerrando conversa...")
        break  # Interrompe o loop e encerra o programa

    # Persistência no assunto: continua pedindo apenas a data
    if mensagem not in palavras_sair:
        if not data_evento:
            print("Churras.AI: Para avançar no orçamento, preciso da data. Ex.: Data: 25/12/2026")
        else:
            print("Churras.AI: Perfeito! Já tenho a data e posso seguir com o orçamento.")

    # Caso a mensagem não seja nenhuma das esperadas
    if (
        mensagem not in saudacoes
        and mensagem not in palavras_valor
        and mensagem not in palavras_data
        and mensagem not in palavras_sair
        and not mensagem.startswith("data:")
    ):
        print("Churras.AI: Não entendi. Tente: oi, valor, data, data: ou sair.")
