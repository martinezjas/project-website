def determine_themes(hymn_number):
    if 1 <= hymn_number <= 52:
        # "El Culto"
        hymn_supertheme = 'https://cdn-icons-png.flaticon.com/512/1769/1769039.png'
        if 1 <= hymn_number <= 21:
            hymn_subtheme = 'https://source.unsplash.com/3pCRW_JRKM8'
            # "Adoración y Alabanza"
        elif 22 <= hymn_number <= 34:
            hymn_subtheme = 'https://source.unsplash.com/_86u_Y0oAaM'
            # "Inicio del Culto"
        elif 35 <= hymn_number <= 45:
            hymn_subtheme = 'https://source.unsplash.com/yhEgkxZqkkk'
            # "Cierre del Culto"
        elif 46 <= hymn_number <= 47:
            hymn_subtheme = 'https://source.unsplash.com/sYffw0LNr7s'
            # "Culto Matutino"
        elif 48 <= hymn_number <= 52:
            hymn_subtheme = 'https://source.unsplash.com/GPPAjJicemU'
            # "Culto Vespertino"
    elif 53 <= hymn_number <= 77:
        hymn_supertheme = 'https://cdn-icons-png.flaticon.com/512/3608/3608948.png'
        # "Dios el Padre"
        if 53 <= hymn_number <= 59:
            hymn_subtheme = 'https://source.unsplash.com/Twvvfgeh-f8'
            # "Amor y Fidelidad de Dios"
        elif 59 <= hymn_number <= 77:
            hymn_subtheme = 'https://source.unsplash.com/H3giJcTw__w'
            # "Majestad y Poder de Dios"
    elif 78 <= hymn_number <= 189:
        hymn_supertheme = 'https://cdn-icons-png.flaticon.com/512/1051/1051474.png'
        # "Jesucristo"
        if 78 <= hymn_number <= 92:
            hymn_subtheme = 'https://source.unsplash.com/dABKxsPTAEk'
            # "Nacimiento de Cristo"
        elif 93 <= hymn_number <= 102:
            hymn_subtheme = 'https://images.pexels.com/photos/415571/pexels-photo-415571.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
            # "Muerte de Cristo"
        elif 103 <= hymn_number <= 106:
            hymn_subtheme = ''
            # "Resurrección de Cristo"
        elif 107 <= hymn_number <= 126:
            hymn_subtheme = "Amor de Cristo"
        elif 127 <= hymn_number <= 157:
            hymn_subtheme = "Alabanza a Cristo"
        elif 158 <= hymn_number <= 189:
            hymn_subtheme = "Segunda Venida de Cristo"
    elif 190 <= hymn_number <= 203:
        hymn_supertheme = hymn_subtheme = "El Espíritu Santo"
    elif 204 <= hymn_number <= 208:
        hymn_supertheme = hymn_subtheme = "Las Sagradas Escrituras"
    elif 209 <= hymn_number <= 344:
        hymn_supertheme = "El Evangelio"
        if 209 <= hymn_number <= 237:
            hymn_subtheme = "Invitación"
        if 238 <= hymn_number <= 244:
            hymn_subtheme = "Arrepentimiento"
        if 245 <= hymn_number <= 283:
            hymn_subtheme = "Consagración"
        if 284 <= hymn_number <= 310:
            hymn_subtheme = "Salvación y Redención"
        if 311 <= hymn_number <= 315:
            hymn_subtheme = "Juicio"
        if 316 <= hymn_number <= 344:
            hymn_subtheme = "Hogar Celestial"
    elif 345 <= hymn_number <= 527:
        hymn_supertheme = "La Vida Cristiana"
        if 345 <= hymn_number <= 364:
            hymn_subtheme = "Gozo y Paz"
        elif 365 <= hymn_number <= 372:
            hymn_subtheme = "Gratitud"
        elif 373 <= hymn_number <= 390:
            hymn_subtheme = "Oración y Comunión"
        elif 391 <= hymn_number <= 438:
            hymn_subtheme = "Confianza y Seguridad"
        elif 439 <= hymn_number <= 465:
            hymn_subtheme = "Petición y Anhelo"
        elif 466 <= hymn_number <= 473:
            hymn_subtheme = "Dirección Divina"
        elif 474 <= hymn_number <= 486:
            hymn_subtheme = "Peregrinación"
        elif 487 <= hymn_number <= 490:
            hymn_subtheme = "Obediencia"
        elif 491 <= hymn_number <= 504:
            hymn_subtheme = "Servicio Cristiano"
        elif 505 <= hymn_number <= 520:
            hymn_subtheme = "Lucha Contra el Mal"
        elif 521 <= hymn_number <= 525:
            hymn_subtheme = "Mayordomía"
        elif 526 <= hymn_number <= 527:
            hymn_subtheme = "Amor a la Patria"
    elif 528 <= hymn_number <= 588:
        hymn_supertheme = "La Iglesia"
        if 528 <= hymn_number <= 533:
            hymn_subtheme = "Iglesia"
        elif hymn_number == 534:
            hymn_subtheme = "Escuela Sabática"
        elif 535 <= hymn_number <= 550:
            hymn_subtheme = "Sábado"
        elif 551 <= hymn_number <= 578:
            hymn_subtheme = "Misión de la Iglesia"
        elif 579 <= hymn_number <= 580:
            hymn_subtheme = "Bautismo"
        elif 518 <= hymn_number <= 586:
            hymn_subtheme = "Cena del Señor"
        elif hymn_number == 587:
            hymn_subtheme = "Dedicación de un Templo"
        elif hymn_number == 588:
            hymn_subtheme = "Funeral"
    elif 589 <= hymn_number <= 613:
        hymn_supertheme = "El Hogar Cristiano"
        if hymn_number == 589:
            hymn_subtheme = "Boda"
        elif 590 <= hymn_number <= 596:
            hymn_subtheme = "Hogar Cristiano"
        elif hymn_number == 597:
            hymn_subtheme = "Dedicación de un Niño"
        elif 598 <= hymn_number <= 607:
            hymn_subtheme = "Niños"
        elif 608 <= hymn_number <= 613:
            hymn_subtheme = "Jóvenes"

    return hymn_supertheme, hymn_subtheme
