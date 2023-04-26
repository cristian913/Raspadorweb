import requests
from bs4 import BeautifulSoup as bs
numero = 0
print("ALERTA TENGA ENCUENTA:"+"\n"+"  *Los usuarios con cuenta administrador no se pueden buscar por los privilegios de seguridad."+"\n"+
"  *Para buscar se ingresa nombre de consulta que esta debajo del nombre de perfil.")
while numero < 10:
   
    print()
    print("**************INGRESE EL NOMBRE DEL USUARIO QUE DESEA CONSULTAR****************** ")
    github_user = input('Input Github user: ')
    url = 'https://github.com/'+github_user
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    print()
    print("**************RESULTADO DE BUSQUEDA DATOS USUARIO****************** ")
    print()

    element = soup.find("div", {"class": "mi-clase"})

    # nombre de perfil
    profile_nombre = soup.find('span', {'class': 'p-name vcard-fullname d-block overflow-hidden'}).contents[0]
    print("   *Nombre del usuario: "+profile_nombre)
    #pagina de perfil usuario
    print("  *Pagina del usuario en github: "+url)
    # compañia de trabajo
    profile_compañia = soup.find('span', {'class': 'p-org'})
    if profile_compañia:
        profile_compañia = profile_compañia['title']
    else:
        profile_compañia = 'DATOS SIN REGISTRAR  "SIN INFORMACION"'
    print("  *Compañia de trabajo: "+profile_compañia)

    # pais donde se encuentra
    profile_pais = soup.find('span', {'class': 'p-label'})
    if profile_pais:
        profile_pais = profile_pais.contents[0]
    else:
        profile_pais = 'DATOS SIN REGISTRAR  "SIN INFORMACION"'
    print("   *Su pais es:  "+profile_pais)

    # comentario, este esta en los datos de perfil usuario
    profile_comentario_perfil = soup.find('div', {'class': 'p-note user-profile-bio mb-3 js-user-profile-bio f4'})
    if profile_comentario_perfil:
        profile_comentario_perfil = profile_comentario_perfil['data-bio-text']
    else:
        profile_comentario_perfil = 'DATOS SIN REGISTRAR  "SIN INFORMACION"'
    print("   *Comentario de perfil : "+profile_comentario_perfil)

    #link otros perfiles
    profile_link_perfile = soup.find('a',{'class':'Link--primary'})
    if profile_link_perfile :
       profile_link_perfile  = profile_link_perfile.contents[0]
    else:
        profile_link_perfile = 'DATOS SIN REGISTRAR  "SIN INFORMACION"'
    print("   *Link : "+profile_link_perfile )

    # fecha de inicio en esta cuenta
    profile_union = soup.find('relative-time', {'class': 'no-wrap'})
    if profile_union:
        profile_union = profile_union.contents[0]
    else:
        profile_union = 'DATOS SIN REGISTRAR  "SIN INFORMACION"'
    print("   *Se unio en: "+profile_union)

    print("********************FIN DE RESULTADOS ESTE USUARIO******************")