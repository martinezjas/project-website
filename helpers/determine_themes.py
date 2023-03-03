import validators


def determine_themes(hymn_number):
    if 1 <= hymn_number <= 52:
        # "El Culto"
        # "El Culto"#'https://cdn-icons-png.flaticon.com/512/1769/1769039.png'
        hymn_supertheme = 'https://cdn-icons-png.flaticon.com/512/1769/1769039.png'
        if 1 <= hymn_number <= 21:
            # "Adoración y Alabanza"#'https://source.unsplash.com/3pCRW_JRKM8'
            hymn_subtheme = 'https://source.unsplash.com/3pCRW_JRKM8'
            # "Adoración y Alabanza"
        elif 22 <= hymn_number <= 34:
            # "Inicio del Culto"#'https://source.unsplash.com/_86u_Y0oAaM'
            hymn_subtheme = 'https://source.unsplash.com/_86u_Y0oAaM'
            # "Inicio del Culto"
        elif 35 <= hymn_number <= 45:
            # "Cierre del Culto"#'https://source.unsplash.com/yhEgkxZqkkk'
            hymn_subtheme = 'https://source.unsplash.com/yhEgkxZqkkk'
            # "Cierre del Culto"
        elif 46 <= hymn_number <= 47:
            # "Culto Matutino"#'https://source.unsplash.com/sYffw0LNr7s'
            hymn_subtheme = 'https://source.unsplash.com/sYffw0LNr7s'
            # "Culto Matutino"
        elif 48 <= hymn_number <= 52:
            # "Culto Vespertino"#'https://source.unsplash.com/GPPAjJicemU'
            hymn_subtheme = 'https://source.unsplash.com/GPPAjJicemU'
            # "Culto Vespertino"
    elif 53 <= hymn_number <= 77:
        # "Dios el Padre"#'https://cdn-icons-png.flaticon.com/512/3608/3608948.png'
        hymn_supertheme = 'https://cdn-icons-png.flaticon.com/512/2883/2883130.png'
        # "Dios el Padre"
        if 53 <= hymn_number <= 59:
            # "Amor y Fidelidad de Dios"#'https://source.unsplash.com/Twvvfgeh-f8'
            hymn_subtheme = 'https://source.unsplash.com/Twvvfgeh-f8'
            # "Amor y Fidelidad de Dios"
        elif 59 <= hymn_number <= 77:
            # "Majestad y Poder de Dios"#'https://source.unsplash.com/H3giJcTw__w'
            hymn_subtheme = 'https://source.unsplash.com/H3giJcTw__w'
            # "Majestad y Poder de Dios"
    elif 78 <= hymn_number <= 189:
        # "Jesucristo"#'https://cdn-icons-png.flaticon.com/512/1051/1051474.png'
        hymn_supertheme = 'https://cdn-icons-png.flaticon.com/512/1051/1051474.png'
        # "Jesucristo"
        if 78 <= hymn_number <= 92:
            # "Nacimiento de Cristo"# 'https://source.unsplash.com/dABKxsPTAEk'
            hymn_subtheme = 'https://www.care-net.org/hubfs/iStock-1290099165.jpg'
            # "Nacimiento de Cristo"
        elif 93 <= hymn_number <= 102:
            hymn_subtheme = 'https://images.pexels.com/photos/415571/pexels-photo-415571.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'  # "Muerte de Cristo"
            # 'https://images.pexels.com/photos/415571/pexels-photo-415571.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
            # "Muerte de Cristo"
        elif 103 <= hymn_number <= 106:
            hymn_subtheme = 'https://assets.answersingenesis.org/img/cms/content/contentnode/og_image/empty-tomb-easter.jpg'
            # "Resurrección de Cristo"
        elif 107 <= hymn_number <= 126:
            # "Amor de Cristo"
            hymn_subtheme = 'https://images.pexels.com/photos/217893/pexels-photo-217893.jpeg'
        elif 127 <= hymn_number <= 157:
            hymn_subtheme = 'https://source.unsplash.com/xec7srO4U5c'  # "Alabanza a Cristo"
        elif 158 <= hymn_number <= 189:
            # "Segunda Venida de Cristo"
            hymn_subtheme = 'https://record.adventistchurch.com/wp-content/uploads/2019/07/Greater-works.jpg'
    elif 190 <= hymn_number <= 203:
        hymn_supertheme = 'https://cdn-icons-png.flaticon.com/512/9844/9844643.png'
        # "El Espíritu Santo"
        hymn_subtheme = 'https://images.pexels.com/photos/75973/pexels-photo-75973.jpeg'
    elif 204 <= hymn_number <= 208:
        hymn_supertheme = 'https://cdn-icons-png.flaticon.com/512/3389/3389381.png'
        hymn_subtheme = 'https://source.unsplash.com/TNlHf4m4gpI'  # "Las Sagradas Escrituras"
    elif 209 <= hymn_number <= 344:
        hymn_supertheme = 'https://cdn-icons-png.flaticon.com/512/75/75574.png'  # "El Evangelio"
        if 209 <= hymn_number <= 237:
            hymn_subtheme = 'https://antrimbic.org/wp-content/uploads/2015/01/welcome.jpg'  # "Invitación"
        if 238 <= hymn_number <= 244:
            hymn_subtheme = 'https://source.unsplash.com/NWu79O4kekw'  # "Arrepentimiento"
        if 245 <= hymn_number <= 283:
            hymn_subtheme = 'https://thepreachersword.files.wordpress.com/2018/08/prayer-bible-hands.jpg'  # "Consagración"
        if 284 <= hymn_number <= 310:
            hymn_subtheme = 'https://source.unsplash.com/UTY4N-NU6Wg'  # "Salvación y Redención"
        if 311 <= hymn_number <= 315:
            hymn_subtheme = 'https://i0.wp.com/ebcelkhorn.com/wp-content/uploads/2014/11/wooden-judges-gavel.jpg?resize=930%2C620&ssl=1'  # "Juicio"
        if 316 <= hymn_number <= 344:
            hymn_subtheme = 'https://source.unsplash.com/FIKD9t5_5zQ'  # "Hogar Celestial"
    elif 345 <= hymn_number <= 527:
        # "La Vida Cristiana"
        hymn_supertheme = 'https://cdn-icons-png.flaticon.com/512/4212/4212802.png'
        if 345 <= hymn_number <= 364:
            hymn_subtheme = 'https://source.unsplash.com/RbbdzZBKRDY'  # "Gozo y Paz"
        elif 365 <= hymn_number <= 372:
            hymn_subtheme = 'https://source.unsplash.com/EAvS-4KnGrk'  # "Gratitud"
        elif 373 <= hymn_number <= 390:
            hymn_subtheme = 'https://source.unsplash.com/y4kMCLR7LBo'  # "Oración y Comunión"
        elif 391 <= hymn_number <= 438:
            # "Confianza y Seguridad"
            hymn_subtheme = 'https://live.staticflickr.com/453/32580378846_0598dc35fa_b.jpg'
        elif 439 <= hymn_number <= 465:
            hymn_subtheme = 'https://source.unsplash.com/doOCoW955NQ'  # "Petición y Anhelo"
        elif 466 <= hymn_number <= 473:
            hymn_subtheme = 'https://source.unsplash.com/3Dtu6_XfqIk'  # "Dirección Divina"
        elif 474 <= hymn_number <= 486:
            hymn_subtheme = 'https://source.unsplash.com/iXU_zV0S62o'  # "Peregrinación"
        elif 487 <= hymn_number <= 490:
            hymn_subtheme = 'https://windows10spotlight.com/wp-content/uploads/2019/09/b51276f3ed3353fd4d6d581f79619a68.jpg'  # "Obediencia"
        elif 491 <= hymn_number <= 504:
            # "Servicio Cristiano"
            hymn_subtheme = 'https://oakridgebiblechapel.org/wp-content/uploads/2021/09/Sharing-the-Gospel-in-Huaraz.jpg'
        elif 505 <= hymn_number <= 520:
            hymn_subtheme = 'https://source.unsplash.com/s0PD-FogBjo'  # "Lucha Contra el Mal"
        elif 521 <= hymn_number <= 525:
            hymn_subtheme = 'https://source.unsplash.com/1dGMs4hhcVA'  # "Mayordomía"
        elif 526 <= hymn_number <= 527:
            hymn_subtheme = 'https://source.unsplash.com/AnGx1n-gtw8'  # "Amor a la Patria"
    elif 528 <= hymn_number <= 588:
        hymn_supertheme = 'https://cdn-icons-png.flaticon.com/512/9742/9742773.png'  # "La Iglesia"
        if 528 <= hymn_number <= 533:
            hymn_subtheme = 'https://source.unsplash.com/hKKJnp-nWdQ'  # "Iglesia"
        elif hymn_number == 534:
            hymn_subtheme = 'https://source.unsplash.com/UIib0bAvWfs'  # "Escuela Sabática"
        elif 535 <= hymn_number <= 550:
            hymn_subtheme = 'https://source.unsplash.com/rT6EmOueb3s'  # "Sábado"
        elif 551 <= hymn_number <= 578:
            # "Misión de la Iglesia"
            hymn_subtheme = 'https://pewtopractice.files.wordpress.com/2011/09/outreach-image.jpg'
        elif 579 <= hymn_number <= 580:
            hymn_subtheme = 'https://source.unsplash.com/klk3Lt75K_o'  # "Bautismo"
        elif 581 <= hymn_number <= 586:
            hymn_subtheme = 'https://files.adventistas.org/noticias/es/2022/05/23144357/shutterstock_600525530.jpg'  # "Cena del Señor"
        elif hymn_number == 587:
            hymn_subtheme = 'https://source.unsplash.com/sgdyBq6kheQ'  # "Dedicación de un Templo"
        elif hymn_number == 588:
            hymn_subtheme = 'https://source.unsplash.com/q6e4zwgtUcM'  # "Funeral"
    elif 589 <= hymn_number <= 613:
        # "El Hogar Cristiano"
        hymn_supertheme = 'https://cdn.pixabay.com/photo/2014/04/02/10/38/house-304072_1280.png'
        if hymn_number == 589:
            hymn_subtheme = 'https://source.unsplash.com/p0vZplFhKYI'  # "Boda"
        elif 590 <= hymn_number <= 596:
            hymn_subtheme = 'https://www.focusonthefamily.com/wp-content/uploads/2019/07/87F04C59F20A4BBF96906F6DFA4B221D.jpeg'  # "Hogar Cristiano"
        elif hymn_number == 597:
            hymn_subtheme = 'https://source.unsplash.com/oOnJWBMlb5A'"Dedicación de un Niño"
        elif 598 <= hymn_number <= 607:
            hymn_subtheme = 'https://source.unsplash.com/DqgMHzeio7g'  # "Niños"
        elif 608 <= hymn_number <= 613:
            hymn_subtheme = 'https://www.adventist.org/wp-content/uploads/2019/12/youth-scaled.jpg'  # "Jóvenes"

    if validators.url(hymn_supertheme, hymn_subtheme):
        return hymn_supertheme, hymn_subtheme
    else:
        return 'https://cdn-icons-png.flaticon.com/512/1769/1769039.png', 'https://i.pinimg.com/originals/6d/6f/0e/6d6f0e4099b30c8993d460e5e565144d.jpg'
