[Read this in **English**](README.md) · [Llegiu això en **català**](README.ca.md)

# Copia de seguridad simple y segura
## Descarga segura de ficheros remotos a nuestro ordenador usando SSH / SFTP

Sencillo programa en Python con el que se descargan ficheros desde una carpeta en un servidor remoto, para almacenarlos como copias de seguridad en nuestro ordenador local.  Es útil para descargar copias de seguridad de paneles de control web, bases de datos, etc. 

Se puede automatizar la descarga programándola mediante Cron o Systemd (Linux), Automator (Mac OS) o el Programador de Tareas (Windows). Funciona mediante protocolo SSH/SFTP y se establece una conexión segura entre nuestro ordenador y el servidor remoto, alejada de miradas indiscretas.

A los archivos descargados se les añade automáticamente la fecha actual en el nombre de archivo, por lo que se pueden almacenar siempre en la misma carpeta local y no se sobreescribirán archivos con el mismo nombre.

Opciones configurables:

- Escribir un registro de actividad (log).
- Borrar automáticamente los archivos remotos una vez descargados localmente.

Requisitos:

- El servidor remoto debe permitir un acceso mediante SSH y quizá tener activada la opción SFTP. Se puede configurar fácilmente en su panel de control del dominio.
- Disponer de los datos de acceso por terminal al servidor remoto: usuario, contraseña,puerto (normalmente 22) y carpeta en la que están los archivos.
- Python 3 instalado con el módulo `paramiko`. Válido para cualquier sistema: Windows, Mac OS, Linux. Testeado en Python 3.8.

Instrucciones:

- Descargar estos ficheros a su ordenador clonando el proyecto o como zip comprimido.
- Abrir el fichero `download_config.py` con cualquier editor de texto plano, añadirle los datos de conexión y las opciones deseadas. Hay ejemplos en el fichero `download_config_sample.py`
- Ejecutar el fichero `download_backup.py` llamando al intérprete Python (`python3 download_backup.py`). En Linux y Mac OS puede darle permisos en línea de comandos para que se ejecute sin llamar al intérprete: `chmod +x download_backup.py`
