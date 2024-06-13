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

ocen_strukture = f"{ocen}, czy struktura kolokwium jest poprawna, czyli czy glowne punkty prawidlowo opisuja odpowiedz na pytanie. Wygeneruj wlasne glowne punkty i sprawdz, czy są równoważne z punktami z odpowiedzi. Jesli nue na punktow, tylko sam opis ocen strukturę na 1. "
ocen_punkty = f"{ocen} czy punkty wyczerpują temat w odpowiedzi"
ocen_zawartosc_merytoryczna = f"{ocen} zawartość merytoryczną punktów, czy kazdy z opisow pod glownymi punktami jest obszerny i opisuje glowne punkty wyczerpują temat z pytania. jesli bie ma odpowiedzi punkt-opis sprawdź czy odpowiedz jest obszerna i wtczerpujaca. porownaj ją z odpowiedzią, jakiej sam bys udzielił. "
ocen_odnosniki = f"{ocen} czy są odnośniki i linki do zewnętrznych źródeł informacji, takich jak artykuły, strony web, repozytoria gitub w:"
ocen_samodzielnosc = f"{ocen}, czy kolokwium zostało napisane samodzielnie, 1 jeśli jest to dokladna kopia odpowiedzi, jaką sam bys udzielil, 5 jeśli jest zupelnie inna."
ocen_zrozumienie = f"{ocen} czy student rozumie to co napisal. sprobuj  zmnienić format oytania i sprawdź, czy odpowiedź pasuje do zmienionej formy pytania. "
parametry_oceny = f"oceny podaj w formacie: struktura:[ocena struktury], punkty[ocena punktow], zawartość[ocena zawartości], odnośniki[ocena odnosników], zrozumienie[ocena zrozumienia], samodzielność[ocena samodzielności]. Nie używaj znakow końca linii tylko przecinków"

def ocena_kolokwium(pyt, odp, zrodla):
    return f"""

    {wstep}{pyt}
    ocena struktury: {ocen_strukture}
    ocena punktów: {ocen_punkty}
    ocena zawartości: {ocen_zawartosc_merytoryczna}
    ocena odnośników: {ocen_odnosniki}{zrodla}
    ocena zrozumienia: {ocen_zrozumienie}
    ocena struktury: {ocen_samodzielnosc}
    {parametry_oceny}
    Oceń poniższe kolokwium: {odp}
    """

