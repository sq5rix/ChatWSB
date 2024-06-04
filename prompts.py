GPT_4o = 'gpt-4o'
GPT_4 = 'gpt-4-0613'
GPT_T = 'gpt-3.5-turbo'
GPT_MODEL = GPT_4o

general_prompt = """

    Treść uprzednio podłączona do promptu składa się z ciągu odpowiedzi na pytania.
    Treśc ma następujące pola w każdej z kolejnych odpowiedzi:
        Imię, potem imię,
        Nazwisko, potem właściwe nazwisko,
        a później pytanie i po nim treśc pytania, treść odpowiedzi.
        Jakie jest Imię i Nazwisko osoby, która napisała o brokerach?

    """

odp_kolokwium_prompt = """

Jako inżynier IoT odpowiedz krotko na poniższe pytanie:

"""
check_prompt = """ jako inżynier IoT powiedz krótko, bez szczegółów, czy to ChatGPT napisał ten tekst? : """
compare_prompt = """ porównaj z tym tekstem napisanym przez ChatGPT :"""

ocen = "oceń w skali 1-5,bez opisu, samą liczbą, "

wstep = "Jako surowy nauczyciel akademicki oceń kolowium, podane poniżej, na temat: "

ocen_strukture = f"{ocen}, czy struktura kolokwium jest poprawna"
ocen_punkty = f"{ocen} czy punkty wyczerpują temat w odpowiedzi"
ocen_zawartosc_merytoryczna = f"{ocen} zawartość merytoryczną punktów, czy wyczerpują temat z pytania "
ocen_odnosniki = f"{ocen} czy są odnośniki i linki do zewnętrznych źródeł informacji, takich jak artykuły, strony web, repozytoria gitub"
parametry_oceny = f"oceny podaj w formacie: str:[ocena struktury], pun[ocena punktow], zaw[ocena zawartości], odn[ocena odnosników]. Nie uzywaj znakow końca linii tylko przecinków"

def ocena_kolokwium(pyt, odp):
    return f"""

    {wstep}{pyt}
    {ocen_strukture}
    {ocen_punkty}
    {ocen_zawartosc_merytoryczna}
    {ocen_odnosniki}
    {parametry_oceny}
    Kolokwium do oceny: {odp}
    """

