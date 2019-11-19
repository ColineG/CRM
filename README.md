# AVP - AnneVachonProduction 

## Présentation du projet: 

L'entreprise AVP a aujourd'hui une problématique de structuration et de sécurisation de la donnée de ses clients. l'idée est également d'optimiser la configuration de la partie data de ce entreprise pour gagner en efficacité. 

Le projet se découpe en deux parties, l'une est de créer un outil de type CRM pour stocker de manière structurée l'ensemble des données de l'entreprise AVP. 

La deuxième partie du projet, est de créer un outil de type Dashboard pour obtenir un suivi des performances de l'ensemble des KPI's important de la société. Cette étape sera mise à jour de manière automatisée et en temps réel en fonction des données insérée dans la BDD en première partie du projet ici. 

## Cahier des charges

### 1. Contexte

L'entreprise AVP- AnneVachonProduction a été créée en 2010 par Anne Vachon une entrepreneur basée à Lyon. Après quasiment 10 ans d'exercices étant seule employé de la structure, un besoin d'aide à l'organisation a été pour moi l'occasion de réaliser mon projet de fin de formation en mettant mes compétences acquises au service d'un veritable projet. 

 - **Enjeux** : gagner en efficacité, productivité
 - **Stratégies**: 
	 - Centraliser les informations dans un CRM pour faciliter la recherche et l'enregistrement de nouvelles données par l'utilisateur. 
	 - Réaliser un analyse de performances dans le temps afin de faciliter la prise de décision.
 - **Domaine d'application**: Recueil du fichier clients, prospect et prestataire afin de créer une base de donnée & récupération de l'historique des ventes pour mise en place d'un dashboard de suivi des performances. Si possible étendre l'outil avec une base de donnée des banques images achetées ainsi que de la partie production (repérage, lieux louées), idéalement intégrer également un système de facturation. 

### 2. Objectifs 

 - Saisir des informations
 - Recherche des informations
 - Obtenir les indicateurs de performances de façon inéligible
 - Centraliser les informations sur une application 
 - Sécuriser les données 

### 3. Contraintes

- de coût : sans budget 
- de temps : 2 mois de délais 
- critère de stockage : `à déterminer` 

### 4. Périmètre

Collaboration avec Anne Vachon, Dirigeante de l'entreprise AVP pour la récupération des données, le recueil du besoin spécifique lié à l'activité. Elle sera également la future utilisatrice de l'outil. Moi-même serait en charge de la création, de la mise en place de l'outil selon le besoin client. 

Les ressources matérielles, ordinateur perso utilisé.  


### Modèle conceptuel des données 

    A compléter

### Modèle organisationnel des données

    A compléter

### Import de données

Les données sont déjà existante, ici il n'y aura pas de création d'un dataset. Nous utiliserons l'existant. 

Les données sont fournis par l'entreprise.

Vcard metada: [https://en.wikipedia.org/wiki/VCard](https://en.wikipedia.org/wiki/VCard)

````python
{'adr': {'box': <class 'str'>,
         'city': <class 'str'>,
         'code': <class 'str'>,
         'country': <class 'str'>,
         'extended': <class 'str'>,
         'region': <class 'str'>,
         'street': <class 'str'>},
 'bday': <class 'str'>,
 'categories': <class 'list'>,
 'email': <class 'str'>,
 'fn': <class 'str'>,
 'n': {'additional': <class 'str'>,
       'family': <class 'str'>,
       'given': <class 'str'>,
       'prefix': <class 'str'>,
       'suffix': <class 'str'>},
 'nickname': <class 'str'>,
 'note': <class 'str'>,
 'org': <class 'list'>,
 'photo': <class 'bytes'>,
 'prodid': <class 'str'>,
 'tel': <class 'str'>,
 'title': <class 'str'>,
 'uid': <class 'str'>,
 'url': <class 'str'>,
 'version': <class 'str'>,
 'x-abadr': <class 'str'>,
 'x-ablabel': <class 'str'>,
 'x-abrelatednames': <class 'str'>,
 'x-abshowas': <class 'str'>,
 'x-abuid': <class 'str'>,
 'x-apple-subadministrativearea': <class 'str'>,
 'x-imagehash': <class 'str'>,
 'x-imagetype': <class 'str'>,
 'x-socialprofile': <class 'str'>}
 ````
### Requêtes

    A compléter sous forme de liste

### Interface

    Réalisation d'une maquette à définir
L'idée est de créer une application Flask, nous auront un système de recherche (ex: par nom, prénom, email, date...) puis une possibilité de mettre à jour l'outil en insérant des données fraîches dans une fiche client existant ou en créant une nouvelle fiche. 

La partie dashboard permettra de simplement visualiser des graphiques représentatif de l'activité. 

### Conclusion 
# flask_CRM
