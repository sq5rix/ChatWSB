GPT_4 = 'gpt-4-0613'
GPT_T = 'gpt-3.5-turbo'
GPT_MODEL = GPT_4

general_prompt = """

    Treść uprzednio podłączona do promptu składa się z ciągu odpowiedzi na pytania.
    Treśc ma następujące pola w każdej z kolejnych odpowiedzi:
        Imię, potem imię,
        Nazwisko, potem właściwe nazwisko,
        a później pytanie i po nim treśc pytania, treść odpowiedzi.
        Jakie jest Imię i Nazwisko osoby, która napisała o brokerach?

    """

odp_kolokwium_prompt = """

Jako inżynier IoT odpowiedz_krotko na poniższe pytanie:

"""
check_prompt = """ jako inżynier IoT powiedz krótko, bez szczegółów, czy to ChatGPT napisał ten tekst? : """
compare_prompt = """ porównaj z tym tekstem napisanym przez ChatGPT :"""
