[Read this in **English**](README.md) · [Lea esto en **castellano**](README.es.md)

# Còpia de seguretat simple i segura
## Descàrrega segura de fitxers remots al nostre ordinador utilitzant SSH / SFTP

Senzill programa en Python amb el qual es descarreguen fitxers d'una carpeta d'un servidor remot, per a emmagatzemar-los com a còpies de seguretat al nostre ordinador local. És útil per a descarregar còpies de seguretat de taulers de control web, bases de dades, etc.

Es pot automatitzar la descàrrega programant-la amb Cron o Systemd (Linux), Automator (Mac OS) o el Programador de Tasques (Windows). Funciona mitjançant protocol SSH / SFTP i s'estableix una connexió segura entre el nostre ordinador i el servidor remot, allunyada de mirades indiscretes.

Als arxius descarregats se'ls afegeix automàticament la data actual al nom d'arxiu, de manera que es poden emmagatzemar sempre a la mateixa carpeta local i no se sobreescriuran arxius amb el mateix nom.

Opcions configurables:

- Escriure un registre d'activitat (log).
- Esborrar automàticament els fitxers remots un cop descarregats localment.

Requisits:

- El servidor remot ha de permetre un accés via SSH i potser tenir activada l'opció SFTP. Es pot configurar fàcilment al vostre tauler de control del domini.
- Disposar de les dades d'accés per terminal a servidor remot: usuari, contrasenya, port (normalment 22) i carpeta en la qual hi ha els arxius.
- Python 3 instal·lat amb els mòduls `paramiko` i `regex`. Vàlid per a qualsevol sistema: Windows, Mac OS, Linux. Provat amb Python 3.8.

Instruccions:

- Descarregueu aquests fitxers al vostre ordinador clonant el projecte o com a zip comprimit.
- Obriu el fitxer `download_config.py` amb qualsevol editor de text pla, afegiu-li les dades de connexió i les opcions desitjades. Hi ha exemples al fitxer `download_config_sample.py`
- Executar el fitxer `download_backup.py` cridant l'intèrpret Python (`python3 download_backup.py`). A Linux i Mac OS podeu donar-li permisos en línia de comandes per tal que s'executi sense cridar l'intèrpret: `chmod +x download_backup.py`