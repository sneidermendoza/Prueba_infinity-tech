# Prueba Infinity Tech 

**API para gestionar el acceso a la aplicación y así poder gestionar
el listar,crear,editar y eliminar  usuarios**


> *Despues de haber descargado de [GitHub](https://github.com/sneidermendoza/Prueba_infinity-tech "Infinity Tech")  la carpeta que contiene los archivos, y haber instalado las dependencias*


## Rutas
* [Login](http://localhost:8000/api/login/ "Login")
* [Listar](http://localhost:8000/v1/users/ "Listar")
* [Listar un usuario](http://localhost:8000/v1/users/1/ "Listar un usuario")
* [Crear](http://localhost:8000/v1/users/ "Crear")
* [Editar](http://localhost:8000/v1/users/1/ "Editar")
* [Eliminar](http://localhost:8000/v1/users/1/ "Eliminar")



## Login


> Habiendo corrido nuestro proyecto, lo Primero que hacemos es loguearnos con nuestro *username* y nuestro *password* en la ruta [Login](http://localhost:8000/api/login/ "Login"), mandándoles en el body y en formato JSON el username y el password de la siguiente manera

![Login](imagenes_apis/Login.png)

La respuesta que esto nos devolverá será un JSON con un token, refresh_token, usuario con sus datos y un mensaje


![Login](imagenes_apis/Respuesta_login.PNG)



 Con el token dado de **login**, tendremos acceso a las rutas de listar, listar un *usuario*, *creación*, *edición* y *eliminación*.



## Listar



Para acceder a esta ruta [Listar](http://localhost:8000/v1/users/ "Listar") necesitamos el método **GET** y en **Autorización** un token de tipo **Bearer token** el cual nos lo provee el login.

![Listar](imagenes_apis/Listar_usuarios_creados.PNG)



Esto nos dará por respuesta, todos los usuarios que estén registrados en la base de datos.

![Respuesta](imagenes_apis/Respuesta_Listar_usuarios.PNG)





## Listar un solo usuario


Para acceder a esta ruta [Listar un usuario](http://localhost:8000/v1/users/1/ "Listar un usuario") necesitamos el método **GET** en **Authorization** un token de tipo **Bearer token** el cual nos lo provee el login y en la ruta enviarle el **ID** del usuario a listar de la siguiente manera.

![Listar un usuario](imagenes_apis/Listar_un_usuario.PNG)



Esto nos dará por respuesta, el usuario solicitado.

![Respuesta](imagenes_apis/Respuesta_listar_un_usuario.PNG)







## Crear

Para acceder a esta ruta [Crear](http://localhost:8000/v1/users/ "Crear") necesitamos el método **POST**, en **Authorization** un token de tipo **Bearer token** el cual nos lo provee el login, y en el **Body** y en formato **Json** estos datos.

 ```Json

 {


    "first_name" : "CharField()",

    "last_name" : "CharField()",

    "date_birth" : "DateField()",

    "address" : "CharField()",

    "password" : "CharField()",

    "mobile_phone" : "IntegerField()"

}

 ```

De la siguiente manera.



![Crear](imagenes_apis/Crear_usuario.PNG)



Esto nos dará por respuesta, el usuario creado con todos sus datos y la **password** encriptada.

![Respuesta](imagenes_apis/respuesta_crear_usuario.PNG)





## Editar

Para acceder a esta ruta [Editar](http://localhost:8000/v1/users/1/ "Editar") necesitamos el metodo **PUT**, en **Authorization** un token de tipo **Bearer token** el cual nos lo provee el login, en la ruta el **ID** del usuario que queremos editar y en el **Body** y en formato **JSON** con los datos a editar.

 ```Json

{


    "first_name": "sneider-2.1",

    "last_name": "mendoza-2.1",

    "date_birth": "1991-06-03",

    "address": "cll 7A # 58-121",

    "password": "544548",

    "mobile_phone": 3176711594

}

 ```

De la siguiente manera.



![Editar](imagenes_apis/Actualizar_un_usuario.PNG)



Esto nos dará por respuesta, el usuario editado con todos sus datos y la **password** encriptada.

![Respuesta](imagenes_apis/Respuesta_editar_un_usuario.PNG)





## Eliminar



Para acceder a esta ruta [Eliminar](http://localhost:8000/v1/users/1/ "Eliminar") necesitamos el metodo **Delete** en **Authorization** un token de tipo **Bearer token** el cual nos lo provee el login y en la ruta enviarle el **ID** del usuario a eliminar de la siguiente manera.

![Eliminar](imagenes_apis/Eliminar.PNG)



Esto nos dará por respuesta, el usuario eliminado.

![Respuesta](imagenes_apis/Respuesta_eliminar.PNG)