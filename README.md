# Odoo : premier module

Ici ce trouve juste le premier module que j'ai créé avec Odoo, en suivant le tutoriel de la documentation. 

J'ai tenté de faire fonctionner Odoo du mieux que je pouvais, mais malheureusement je n'ai pas pu tester mon code. 

Mes tentatives sur Odoo (côté installation) : 
-- 

* Créer un fichier `docker-compose.yml`, afin de ne pas avoir à installer Odoo sur ma machine, mais je ne trouvais pas comment relancer le serveur Odoo (quand on créé des modules dans un nouveau dossier, beh faut relancer le serveur).
* Installer Odoo avec la commande `dnf` de Fedora (soucis car la commande `odoo` ne reconnaissait pas l'extention python odoo :laughing: ).
* Installer via le code source fonctionne, mais le front_end ne s'activait pas, j'avais cette erreur : `odoo.addons.base.models.qweb.QWebException : 'ir.http' object has no attribute 'get_frontend_session_info'`.

J'ai fait de mon mieux pour débugger, mais je n'ai pas trouvé d'information qualitative sur le web, on pourra en parler pendant l'entretien, ça m'intéresserait de savoir ce qu'il s'est passé !

Mis à par ces soucis techniques, j'ai bien aimé découvrir Odoo dans son ensemble, j'ai hâte d'en apprendre plus (surtout sur la partie front end avec qWeb), j'ai bien aimé l'aisance dans le code aussi. 

Ce que j'ai utilisé :
* [Image Docker](https://hub.docker.com/_/odoo)
* [VS Code](https://code.visualstudio.com/)
* [Fedora](https://getfedora.org/)
* [FISH (The Friendly Interactive SHELL)](https://fishshell.com/)
* [Configuration de Postgres sur Fedora](https://doc.fedora-fr.org/wiki/Installation_et_configuration_de_PostgreSQL)
* Le forum d'aide d'Odoo, StackOverFlow, la documentation de Odoo (pour plus de détails)...