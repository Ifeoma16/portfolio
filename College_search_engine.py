import webbrowser

print("""Select language
1. English
2. Français
3. Español
4. Deutsch
5. русский""")

choice = int(input("Enter choice:  / Entrer le choix: / Ingrese su elección: / Geben Sie Ihre Wahl ein: / Введите свой выбор: "))

if choice == 1:
    print("""Select criteria
1. Selectivity(highest to lowest)
2. Selectivity(lowest to highest)
3. Public
4. Private for-profit
5. Privat not-for-profit
6. 4-year institution
7. 2-year institution""")

    choice2 = input("Enter choice: ")

    if choice2 == "1":
        webbrowser.open("https://www.cappex.com/colleges?refinementList%5Bselectivity%5D%5B0%5D=Most%20Selective%20%280%20-%2010%25%29")
        if choice2 == "2":
            webbrowser.open("https://www.cappex.com/colleges?refinementList%5Bselectivity%5D%5B0%5D=Not%20Very%20Selective%20%2875%25%20-%20100%25%29")
        if choice2 == "3":
            webbrowser.open("https://www.cappex.com/colleges?refinementList%5BinstitutionType%5D%5B0%5D=Public")
        if choice2 == "4":
            webbrowser.open("https://www.cappex.com/colleges?refinementList%5BinstitutionType%5D%5B0%5D=Private%20for-profit")
        if choice2 == "5":
            webbrowser.open("https://www.cappex.com/colleges?refinementList%5BinstitutionType%5D%5B0%5D=Private%20not-for-profit")
        if choice2 == "6":
            webbrowser.open("https://www.cappex.com/colleges?refinementList%5BlevelOfInstitution%5D%5B0%5D=4%20Year")
        if choice2 == "7":
            webbrowser.open("https://www.cappex.com/colleges?refinementList%5BlevelOfInstitution%5D%5B0%5D=2%20Year"); breakpoint



elif choice == 2:
    print("""Sélectionner des critères
    1. Sélectivité (du plus haut au plus bas)
    2. Sélectivité (du plus bas au plus élevé)
    3. Université publique
    4. Privé à but lucratif
    5. Privé à but non lucratif
    6. Établissement de 4 ans
    7. Établissement de 2 ans""")

    choice3 = input("Entrer le choix: ")

    if choice3 == "1":
        webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5Bselectivity%5D%5B0%5D=Most+Selective+(0+-+10%25)&_x_tr_sl=en&_x_tr_tl=fr&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice3 == "2":
            webbrowser.open("https://translate.google.com/translate?sl=en&tl=fr&u=https://www.cappex.com/colleges?refinementList%255Bselectivity%255D%255B0%255D%3DNot%2520Very%2520Selective%2520%252875%2525%2520-%2520100%2525%2529")
        if choice3 == "3":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5BinstitutionType%5D%5B0%5D=Public&_x_tr_sl=en&_x_tr_tl=fr&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice3 == "4":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5BinstitutionType%5D%5B0%5D=Private+for-profit&_x_tr_sl=en&_x_tr_tl=fr&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice3 == "5":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5BinstitutionType%5D%5B0%5D=Private+not-for-profit&_x_tr_sl=en&_x_tr_tl=fr&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice3 == "6":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5BlevelOfInstitution%5D%5B0%5D=4+Year&_x_tr_sl=en&_x_tr_tl=fr&_x_tr_hl=en-GB&_x_tr_pto=nui")  
        if choice3 == "7":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5BlevelOfInstitution%5D%5B0%5D=2+Year&_x_tr_sl=en&_x_tr_tl=fr&_x_tr_hl=en-GB&_x_tr_pto=nui"); breakpoint
        
elif choice == 3:
    print ("""Seleccionar criterios
    1. Selectividad (de mayor a menor)
    2. Selectividad (de menor a mayor)
    3. Universidad pública
    4. Universidad privada con fines de lucro
    5. Universidad privada sin fines de lucro
    6. Institución de 4 años
    7. Institución de 2 años""")

    choice4 = input("Ingrese su elección: ")

    if choice4 == "1":
        webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5Bselectivity%5D%5B0%5D=Most+Selective+(0+-+10%25)&_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice4 == "2":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5Bselectivity%5D%5B0%5D=Not+Very+Selective+(75%25+-+100%25)&_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice4 == "3":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5BinstitutionType%5D%5B0%5D=Public&_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice4 == "4":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5BinstitutionType%5D%5B0%5D=Private+for-profit&_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice4 == "5":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5BinstitutionType%5D%5B0%5D=Private+not-for-profit&_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice4 == "6":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5BlevelOfInstitution%5D%5B0%5D=4+Year&_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice4 == "7":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5BlevelOfInstitution%5D%5B0%5D=2+Year&_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=en-GB&_x_tr_pto=nui"); breakpoint

elif choice == 4:
    print("""Kriterien auswählen:
    1. Selektivität (vom höchsten zum niedrigsten)
    2. Selektivität (vom niedrigsten zum höchsten)
    3. öffentliche Universität
    4. Privat gewinnorientiert
    5. Privat nicht gewinnorientiert
    6. 4-Jahres-Institution
    7. 2-Jahres-Institution""")

    choice5 = input("Geben Sie Ihre Wahl ein: ")

    if choice5 == "1":
        webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5Bselectivity%5D%5B0%5D=Most+Selective+(0+-+10%25)&_x_tr_sl=en&_x_tr_tl=de&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice5 == "2":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5Bselectivity%5D%5B0%5D=Not+Very+Selective+(75%25+-+100%25)&_x_tr_sl=en&_x_tr_tl=de&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice5 == "3":
            webbrowser.open("https://translate.google.com/translate?sl=en&tl=de&u=https://www.cappex.com/colleges?refinementList%255BinstitutionType%255D%255B0%255D%3DPublic")
        if choice5 == "4":
            webbrowser.open("https://translate.google.com/translate?sl=en&tl=de&u=https://www.cappex.com/colleges?refinementList%255BinstitutionType%255D%255B0%255D%3DPrivate%2520for-profit")
        if choice5 == "5":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5BinstitutionType%5D%5B0%5D=Private+not-for-profit&_x_tr_sl=en&_x_tr_tl=de&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice5 == "6":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5BlevelOfInstitution%5D%5B0%5D=4+Year&_x_tr_sl=en&_x_tr_tl=de&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice5 == "7":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5BlevelOfInstitution%5D%5B0%5D=2+Year&_x_tr_sl=en&_x_tr_tl=de&_x_tr_hl=en-GB&_x_tr_pto=nui"); breakpoint

elif choice == 5:
    print("""Выберите критерии:
    1. Избирательность (от самой высокой к самой низкой)
    2. Избирательность (от наименьшей к высшей)
    3. Государственный университет
    4. Частный коммерческий
    5. Частная некоммерческая организация
    6. 4-летнее заведение
    7. 2-летнее заведение""")

    choice6 = input("Введите свой выбор: ")

    if choice6 == "1":
        webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5Bselectivity%5D%5B0%5D=Most+Selective+(0+-+10%25)&_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice6 == "2":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5Bselectivity%5D%5B0%5D=Not+Very+Selective+(75%25+-+100%25)&_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice6 == "3":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5BinstitutionType%5D%5B0%5D=Public&_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice6 == "4":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5BinstitutionType%5D%5B0%5D=Private+for-profit&_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice6 == "5":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5BinstitutionType%5D%5B0%5D=Private+not-for-profit&_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice6 == "6":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5BlevelOfInstitution%5D%5B0%5D=4+Year&_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=en-GB&_x_tr_pto=nui")
        if choice6 == "7":
            webbrowser.open("https://www-cappex-com.translate.goog/colleges?refinementList%5BlevelOfInstitution%5D%5B0%5D=2+Year&_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=en-GB&_x_tr_pto=nui"); breakpoint
