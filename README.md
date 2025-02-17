# ft_transcendence
### Chapitre III  
### Partie obligatoire  

Ce projet consiste à créer un site web pour le grand concours de Pong !  

- ***WARNING***
	- **Règles générales** :  
	◦ L’utilisation de bibliothèques ou d’outils offrant une solution immédiate et complète pour une fonctionnalité globale ou un module est interdite.  
	◦ Toute instruction directe concernant l’utilisation (autorisée, obligatoire ou interdite) d’une bibliothèque ou d’un outil tiers **doit être suivie**.  
	◦ L’utilisation de bibliothèques ou d’outils simples résolvant une tâche unique et spécifique, représentant un sous-composant d’une fonctionnalité globale, est **autorisée**.  
	◦ Lors de l’évaluation, l’équipe devra **justifier** toute utilisation d’une bibliothèque ou d’un outil qui n’est pas explicitement approuvé dans le sujet, tout en respectant les contraintes imposées.  
	◦ Pendant l’évaluation, l’évaluateur prendra la responsabilité de déterminer si l’usage d’une bibliothèque ou d’un outil est légitime (**autorisé**) ou si cela résout presque toute une fonctionnalité ou un module (**interdit**).  

### III.1 Vue d’ensemble  

Grâce à votre site web, les utilisateurs pourront jouer à **Pong** en ligne et en temps réel contre d'autres joueurs. Vous devez fournir une **interface utilisateur agréable** et des parties multijoueurs en temps réel !  

- **Exigences minimales** :  
  ◦ Votre projet doit respecter ces lignes directrices comme **condition minimale**. Elles ne contribuent qu'à une petite partie de la note finale.  

- **Modules complémentaires** :  
  ◦ La seconde partie de ce sujet propose des modules supplémentaires qui peuvent remplacer ou compléter ces règles de base.  

Dans ce sujet, certains mots sont surlignés en vert pour indiquer des choix technologiques susceptibles d’évoluer. Assurez-vous de prêter attention à la version du sujet.  

### III.2 Exigences techniques minimales  

Votre projet doit respecter les règles suivantes :  

*** info :**
	Certaines de ces contraintes peuvent être contournées par le choix de modules spécifiques.  
 
◦ Vous êtes libre de développer le site avec ou sans backend.  
  - Si vous choisissez d'inclure un backend, il doit être écrit en **Ruby pur**. Cependant, cette exigence peut être contournée par le **module Framework**.  
  - Si votre backend ou framework utilise une base de données, vous devez suivre les contraintes définies dans le **module Base de données**.  
 
◦ Le frontend doit être développé en **JavaScript pur (vanilla JavaScript)**. Cependant, cette exigence peut être modifiée par le **module Frontend**.  
 
◦ Votre site web doit être une application monopage (Single-Page Application). L’utilisateur doit pouvoir utiliser les boutons **Précédent** et **Suivant** de son navigateur sans problème.  
 
◦ Votre site doit être compatible avec la ***dernière version stable et à jour de Google Chrome***.  
 
◦ L’utilisateur ne doit rencontrer aucune erreur non gérée ni aucun avertissement en parcourant le site.  

◦ Tout doit être lancé avec une **seule commande** permettant de démarrer un conteneur autonome fourni par Docker. Exemple : `docker-compose up --build`  

- ***WARNING***  
	Si votre solution utilise Docker et que vos machines fonctionnent sous Linux en mode cluster,vous devez exécuter Docker en mode rootless pour des raisons de sécurité.  
	◦ Vos fichiers runtime Docker doivent être situés dans /goinfre ou /sgoinfre.  
	◦ Vous ne pouvez pas utiliser les volumes "bind-mount" entre l'hôte et le conteneur si des UID non-root sont utilisés dans le conteneur.  

	En fonction du projet, de votre situation et du contexte, les solutions suivantes peuvent être envisagées :  
	- Utiliser Docker dans une machine virtuelle (VM).  
	- Recréer le conteneur après chaque modification.  
	- Créer une image Docker personnalisée avec un UID root unique.  

### III.3 Jeu  

L’objectif principal de ce site web est de permettre de jouer à Pong contre d’autres joueurs.  

#### **Fonctionnalités essentielles**  

**Jeu en direct entre deux joueurs** :  
   - Les utilisateurs doivent pouvoir participer à un match de Pong en direct contre un autre joueur directement sur le site web.  
   - Les deux joueurs partageront **le même clavier** pour jouer.  
   - Le module **Joueurs à distance** peut étendre cette fonctionnalité pour inclure des joueurs connectés à distance.  

**Tournois** :  
   - Un joueur doit pouvoir jouer contre un autre joueur, mais il doit également être possible de proposer un **tournoi**.  
   - Ce tournoi inclura plusieurs joueurs qui joueront les uns contre les autres à tour de rôle.  
   - Le tournoi doit afficher clairement qui joue contre qui, ainsi que l’ordre des matchs.  

**Système d’inscription** :  
   - Lors du démarrage d’un tournoi, chaque joueur doit entrer un **alias** (nom d’utilisateur).  
   - Les alias seront réinitialisés à chaque début de tournoi.  
   - Cette exigence peut être modifiée en utilisant le **module de gestion standard des utilisateurs**.  

**Système de matchmaking** :  
   - Le système de tournoi doit organiser le **matchmaking** des participants et annoncer le prochain combat.  

**Règles uniformes** :  
   - Tous les joueurs doivent respecter les mêmes règles :  
     ◦ Par exemple, la vitesse des raquettes doit être identique pour tous les joueurs.  
     ◦ Si une IA est utilisée, elle doit respecter les mêmes contraintes de vitesse qu’un joueur humain.  

**Conformité des contraintes frontend** :  
  ◦ Le jeu doit être développé conformément aux contraintes frontend par défaut mentionnées précédemment (JavaScript pur).  
  ◦ Alternativement, vous pouvez choisir d’utiliser le **module Frontend** ou de le remplacer par le **module Graphismes**.  

- **Esthétique** :  
  ◦ Les visuels peuvent varier, mais le jeu doit refléter l’essence du **Pong original (1972)**.  

***WARNING***

	- L’utilisation de bibliothèques ou d’outils offrant une solution immédiate et complète pour une fonctionnalité ou un module global est interdite.  
	- Toute instruction concernant l’utilisation (autorisée, obligatoire ou interdite) d’une bibliothèque ou d’un outil tiers doit être suivie.  
	- L’utilisation de bibliothèques ou outils simples, résolvant une tâche unique et spécifique, est autorisée.  
	- Lors de l’évaluation, l’équipe devra **justifier** l’utilisation de toute bibliothèque ou outil non explicitement approuvé, tout en respectant les contraintes du sujet.  
	- L’évaluateur décidera si l’usage est légitime (**autorisé**) ou s’il résout presque toute une fonctionnalité ou un module (**interdit**).  

### III.4 Considérations de sécurité  

Pour créer un site web fonctionnel de base, vous devez répondre aux préoccupations de sécurité suivantes :  
 
- Tout mot de passe stocké dans votre base de données, si applicable, doit être haché.    
- Votre site web doit être protégé contre :  
  ◦ Les **injections SQL**.  
  ◦ Les attaques de type **Cross-Site Scripting (XSS)**. 
- Si vous utilisez un backend ou toute autre fonctionnalité, il est obligatoire d’activer une connexion sécurisée **HTTPS** pour tous les aspects du site.  
  ◦ Si vous utilisez WebSockets, remplacez `ws` par `wss` pour une connexion sécurisée.  
- Vous devez mettre en œuvre une validation des formulaires et des entrées utilisateur :  
  ◦ Si aucun backend n’est utilisé, la validation doit être réalisée dans la page de base (frontend).  
  ◦ Si un backend est utilisé, la validation doit être effectuée côté serveur.  
  
- Même si vous ne mettez pas en œuvre le module de sécurité JWT avec 2FA, vous devez prioriser la sécurité :  
  ◦ Si vous créez une **API**, assurez-vous que vos routes sont protégées.  
  ◦ Même sans jetons JWT, protéger le site reste une priorité.  

*** WARNING ***
	◦ Toutes les informations sensibles (identifiants, clés API, variables d’environnement, etc.) doivent être enregistrées localement dans un fichier `.env`.  
	◦ Ce fichier `.env` doit être ignoré par Git (via un fichier `.gitignore`).  
	◦ Les informations d’identification ou clés stockées publiquement entraîneront l’échec direct du projet pour des raisons de sécurité évidentes.  


### Chapitre IV  
**Modules**

Félicitations, vous avez accompli 25 % du projet !  
Avec un site web de base fonctionnel en place, l’étape suivante consiste à choisir les modules pour améliorer davantage le projet.  
Pour atteindre 100 % de la réalisation du projet, un minimum de **7 modules principaux** est requis.  
Il est essentiel d'examiner attentivement chaque module, car il pourrait nécessiter des modifications de votre site web de base. Par conséquent, nous vous recommandons vivement de lire ce sujet en entier.

*** WARNING ***
	• L’utilisation de bibliothèques ou d’outils fournissant une solution immédiate et complète pour une fonctionnalité ou un module global est interdite.  
	• Toute instruction directe concernant l'utilisation (peut, doit, ne peut pas) d’une bibliothèque ou d’un outil tiers doit être suivie.  
	• L'utilisation d'une petite bibliothèque ou d’un outil résolvant une tâche simple et unique, représentant un sous-composant d’une fonctionnalité ou d'un module global, est autorisée.  
	• Lors de l’évaluation, l’équipe justifiera toute utilisation de bibliothèque ou d’outil qui n'est pas explicitement approuvée par le sujet, et qui ne contrevient pas aux contraintes du sujet.  
	• Lors de l’évaluation, l’évaluateur prendra ses responsabilités et définira si l'utilisation d’une bibliothèque ou d’un outil spécifique est légitime (et autorisée) ou résout presque toute une fonctionnalité ou un module (et est interdite).

*** INFO ***
	Deux modules mineurs équivalent à un module majeur.

### IV.1 Vue d'ensemble  

- **Web**  
  ◦ **Module majeur** : Utiliser un framework pour construire le backend.  
  ◦ **Module mineur** : Utiliser un framework ou un toolkit pour construire le frontend.  
  ◦ **Module mineur** : Utiliser une base de données pour le backend.  
  ◦ **Module majeur** : Stocker le score d'un tournoi dans la blockchain.  

- **Gestion des utilisateurs**  
  ◦ **Module majeur** : Gestion standard des utilisateurs, authentification, utilisateurs participant à plusieurs tournois.  
  ◦ **Module majeur** : Mise en place d'une authentification à distance.  

- **Gameplay et expérience utilisateur**  
  ◦ **Module majeur** : Joueurs distants.  
  ◦ **Module majeur** : Mode multijoueur (plus de 2 joueurs dans une même partie).  
  ◦ **Module majeur** : Ajouter un autre jeu avec un historique utilisateur et un système de matchmaking.  
  ◦ **Module mineur** : Options de personnalisation du jeu.  
  ◦ **Module majeur** : Chat en direct.  

- **IA-Algorithmes**  
  ◦ **Module majeur** : Introduire un adversaire IA.  
  ◦ **Module mineur** : Tableaux de bord pour les statistiques des utilisateurs et du jeu.  

- **Cybersécurité**  
  ◦ **Module majeur** : Implémenter un WAF/ModSecurity avec une configuration renforcée et utiliser HashiCorp Vault pour la gestion des secrets.  
  ◦ **Module mineur** : Options de conformité au RGPD incluant l'anonymisation des utilisateurs, la gestion locale des données, et la suppression de compte.  
  ◦ **Module majeur** : Implémenter une authentification à deux facteurs (2FA) et JWT.  

- **DevOps**  
  ◦ **Module majeur** : Mise en place de l'infrastructure pour la gestion des journaux.  
  ◦ **Module mineur** : Système de monitoring.  
  ◦ **Module majeur** : Conception du backend sous forme de microservices.  

- **Graphismes**  
  ◦ **Module majeur** : Utilisation de techniques avancées en 3D.  

- **Accessibilité**  
  ◦ **Module mineur** : Prise en charge sur tous les appareils.  
  ◦ **Module mineur** : Extension de la compatibilité avec les navigateurs.  
  ◦ **Module mineur** : Support multilingue.  
  ◦ **Module mineur** : Ajouter des fonctionnalités pour les utilisateurs malvoyants.  
  ◦ **Module mineur** : Intégration du rendu côté serveur (Server-Side Rendering - SSR).  

- **Pong côté serveur**  
  ◦ **Module majeur** : Remplacer le Pong basique par un Pong côté serveur et implémenter une API.  
  ◦ **Module majeur** : Permettre le gameplay Pong via CLI contre des utilisateurs Web avec une intégration API.  

  ### IV.2 Web  

Ces modules permettent l'intégration de fonctionnalités web avancées dans votre jeu Pong.  

- **Module majeur : Utiliser un framework pour construire le backend**  
  ◦ Dans ce module majeur, il est obligatoire d'utiliser **Django** comme framework pour le développement du backend. 

***Info*** 
  Vous pouvez développer le backend sans respecter les contraintes de ce module en utilisant le langage/framework par défaut (voir la section obligatoire précédente). Cependant, ce module sera uniquement validé si vous respectez ses exigences.  

- **Module mineur : Utiliser un framework ou un toolkit pour construire le frontend**  
  ◦ Le développement frontend doit utiliser le **toolkit Bootstrap** en complément de **vanilla JavaScript**, et rien d'autre. 

***Info*** 
  Vous pouvez créer un frontend sans suivre les contraintes de ce module en utilisant les directives frontend par défaut (voir la section obligatoire précédente). Cependant, ce module sera uniquement validé si vous respectez ses exigences.  

- **Module mineur : Utiliser une base de données pour le backend (et plus)**  
La base de données désignée pour toutes les instances de votre projet est **PostgreSQL**.  
Ce choix garantit la cohérence des données et la compatibilité entre tous les composants du projet. Il peut également être une condition préalable pour d'autres modules, comme le module du framework backend.  

- **Module majeur : Stocker les scores d’un tournoi dans la blockchain**  
Ce module se concentre sur l’implémentation d’une fonctionnalité permettant de stocker de manière sécurisée les scores des tournois sur une blockchain dans le cadre du site Pong.  
Pour le développement et les tests, un environnement de blockchain de test sera utilisé.  
La blockchain désignée pour cette implémentation est **Ethereum**, et le langage de programmation pour le développement des smart contracts sera **Solidity**.  
 
- **Intégration de la blockchain** :  
	◦ L'objectif principal est d'intégrer de manière fluide la technologie blockchain, spécifiquement **Ethereum**, dans le site Pong.  
	Cette intégration garantit un stockage sécurisé et immuable des scores de tournoi, offrant aux joueurs un enregistrement transparent et infalsifiable de leurs performances.  

- **Smart Contracts en Solidity** :  
	Des **smart contracts en Solidity** seront développés pour interagir avec la blockchain. Ces contrats seront responsables de l'enregistrement, de la gestion et de la récupération des scores des tournois.  

- **Test de la Blockchain** :
	◦ Comme mentionné précédemment, une blockchain de test sera utilisée à des fins de développement et de test. Cela garantit que toutes les fonctionnalités liées à la blockchain sont soigneusement validées sans les risques associés à une blockchain en production.

- **Interopérabilité** : 
	◦ Ce module peut avoir des dépendances avec d’autres modules, en particulier le module de framework Backend. L'intégration des fonctionnalités de blockchain pourrait nécessiter des ajustements dans le backend pour faciliter les interactions avec la blockchain.  

En implémentant ce module, l'objectif est d'améliorer le site de Pong en introduisant un système de stockage des scores basé sur la blockchain. Les utilisateurs bénéficieront d'une couche supplémentaire de sécurité et de transparence, assurant l'intégrité de leurs scores de jeu. Le module met l’accent sur l’utilisation d’un environnement de test de blockchain afin de minimiser les risques liés au développement de la blockchain.

**IV.3 Gestion des utilisateurs**  
Ce module explore le domaine de la gestion des utilisateurs, en abordant les aspects cruciaux des interactions des utilisateurs et du contrôle d'accès au sein de la plateforme Pong. Il englobe deux composants majeurs, chacun axé sur des éléments essentiels de la gestion des utilisateurs et de l’authentification : la participation des utilisateurs à plusieurs tournois et la mise en place d’une authentification à distance.

• **Module majeur : gestion standard des utilisateurs, authentification, utilisateurs à travers les tournois.**  
	◦ Les utilisateurs peuvent s’inscrire sur le site de manière sécurisée.  
	◦ Les utilisateurs enregistrés peuvent se connecter de manière sécurisée.  
	◦ Les utilisateurs peuvent choisir un nom d'affichage unique pour participer aux tournois.  
	◦ Les utilisateurs peuvent mettre à jour leurs informations.  
	◦ Les utilisateurs peuvent télécharger un avatar, avec une option par défaut si aucun n’est fourni.  
	◦ Les utilisateurs peuvent ajouter d’autres personnes comme amis et voir leur statut en ligne.  
	◦ Les profils des utilisateurs affichent des statistiques, telles que les victoires et les défaites.  
	◦ Chaque utilisateur a un historique de matchs incluant les jeux en 1v1, les dates, et les détails pertinents, accessibles aux utilisateurs connectés.

***WARNING***
	La gestion des noms d’utilisateurs et des adresses email en double est à votre discrétion. Vous devez fournir une solution logique.

• **Module majeur : Mise en place d’une authentification à distance.**  
Dans ce module majeur, l'objectif est d'implémenter le système d'authentification suivant :  
Authentification OAuth 2.0 avec 42. Les principales caractéristiques et objectifs incluent 

***WARNING***
	La gestion des noms d’utilisateurs et des adresses email en double est à votre discrétion. Vous devez fournir une solution logique.

	◦ Intégrer le système d’authentification, permettant aux utilisateurs de se connecter de manière sécurisée.  
	◦ Obtenir les informations d’identification nécessaires et les autorisations de l’autorité compétente pour activer une connexion sécurisée.  
	◦ Mettre en place des flux de connexion et d’autorisation conviviaux respectant les meilleures pratiques et normes de sécurité.  
	◦ Assurer l’échange sécurisé des tokens d’authentification et des informations utilisateur entre l’application web et le fournisseur d’authentification.

Ce module majeur vise à mettre en place une authentification à distance des utilisateurs, offrant ainsi aux utilisateurs un moyen sécurisé et pratique d'accéder à l'application web.

**IV.4 Gameplay et expérience utilisateur**  
Ces modules sont conçus pour améliorer l'expérience générale de jeu du projet.

• **Module majeur : Joueurs à distance**  
Il est possible d'avoir deux joueurs distants. Chaque joueur est situé sur un ordinateur séparé, accédant au même site web et jouant au même jeu de Pong.  

***WARNING***
	Pensez aux problèmes de réseau, tels que les déconnexions inattendues ou le lag.  
	Vous devez offrir la meilleure expérience utilisateur possible.

• **Module majeur : Plusieurs joueurs**  
Il est possible d'avoir plus de deux joueurs. Chaque joueur doit avoir un contrôle en temps réel (d'où la recommandation d'utiliser le module "Joueurs à distance"). Il vous appartient de définir comment le jeu pourrait être joué avec 3, 4, 5, 6... joueurs. En plus du jeu standard à 2 joueurs, vous pouvez choisir un nombre de joueurs supérieur à 2 pour ce module multijoueur. Exemple : 4 joueurs peuvent jouer sur un plateau carré, chaque joueur ayant un côté unique du carré.

• **Module majeur : Ajouter un autre jeu avec historique utilisateur et matchmaking.**  
Dans ce module majeur, l'objectif est d'introduire un nouveau jeu, distinct de Pong, et d'incorporer des fonctionnalités telles que le suivi de l'historique des utilisateurs et le matchmaking.  
Les principales caractéristiques et objectifs incluent :
  ◦ Développer un nouveau jeu captivant pour diversifier les offres de la plateforme et divertir les utilisateurs.  
  ◦ Implémenter un suivi de l’historique des utilisateurs pour enregistrer et afficher les statistiques de jeu de chaque utilisateur.  
  ◦ Créer un système de matchmaking permettant aux utilisateurs de trouver des adversaires et de participer à des matchs équitables et équilibrés.  
  ◦ S’assurer que l’historique des jeux des utilisateurs et les données de matchmaking sont stockés de manière sécurisée et restent à jour.  
  ◦ Optimiser les performances et la réactivité du nouveau jeu afin d’offrir une expérience utilisateur agréable. Mettre régulièrement à jour et maintenir le jeu pour corriger les bugs, ajouter de nouvelles fonctionnalités et améliorer le gameplay.  

Ce module majeur vise à étendre votre plateforme en introduisant un nouveau jeu, à améliorer l'engagement des utilisateurs grâce à l'historique de jeu et à faciliter le matchmaking pour une expérience de jeu agréable.

• **Module mineur : Options de personnalisation du jeu.**  
Dans ce module mineur, l'objectif est de fournir des options de personnalisation pour tous les jeux disponibles sur la plateforme. Les principales caractéristiques et objectifs incluent :  
◦ **Offrir des fonctionnalités de personnalisation**, telles que des power-ups, des attaques ou différentes cartes, qui améliorent l'expérience de jeu.  
◦ Permettre aux utilisateurs de choisir une version par défaut du jeu avec des fonctionnalités de base s'ils préfèrent une expérience plus simple.  
◦ Assurer que les options de personnalisation soient disponibles et applicables à tous les jeux proposés sur la plateforme.  
◦ Mettre en place des menus ou interfaces conviviaux pour ajuster les paramètres du jeu.  
◦ Maintenir la cohérence des fonctionnalités de personnalisation à travers tous les jeux afin d’offrir une expérience utilisateur unifiée.

Ce module vise à offrir aux utilisateurs la flexibilité de personnaliser leur expérience de jeu à travers tous les jeux disponibles, en fournissant une variété d'options de personnalisation tout en offrant une version par défaut pour ceux qui préfèrent une expérience de jeu simple.

• **Module majeur : Chat en direct.**  
Vous devez créer un chat pour vos utilisateurs dans ce module :
  ◦ L'utilisateur doit pouvoir envoyer des messages directs à d'autres utilisateurs.  
  ◦ L'utilisateur doit pouvoir bloquer d'autres utilisateurs. De cette manière, il ne verra plus les messages du compte qu'il a bloqué.  
  ◦ L'utilisateur doit pouvoir inviter d'autres utilisateurs à jouer à un jeu de Pong via l'interface de chat.  
  ◦ Le système de tournois doit être capable de prévenir les utilisateurs attendus pour le prochain jeu.  
  ◦ L'utilisateur doit pouvoir accéder aux profils d'autres joueurs via l'interface de chat.

**IV.5 AI-Algo**  
Ces modules ont pour objectif d'introduire des éléments basés sur des données dans le projet, avec le module majeur introduisant un adversaire IA pour améliorer le gameplay, et le module mineur se concentrant sur les tableaux de bord des statistiques des utilisateurs et des jeux, offrant aux utilisateurs un aperçu minimaliste mais pertinent de leur expérience de jeu.

• **Module majeur : Introduire un adversaire IA.**  
Dans ce module majeur, l'objectif est d'incorporer un joueur IA dans le jeu. Il est à noter que l'utilisation de l'algorithme A* n'est pas autorisée pour cette tâche. Les principales caractéristiques et objectifs incluent :
  ◦ Développer un adversaire IA qui offre une expérience de jeu stimulante et engageante pour les utilisateurs.  
  ◦ L'IA doit reproduire le comportement humain, ce qui signifie que dans votre implémentation de l'IA, vous devez simuler l'entrée clavier. La contrainte ici est que l'IA ne peut rafraîchir sa vue du jeu qu'une fois par seconde, ce qui nécessite qu'elle anticipe les rebonds et autres actions. 

  ***info*** 
  L'IA doit utiliser les power-ups si vous avez choisi d'implémenter le module d'options de personnalisation du jeu.  

  ◦ Implémenter la logique de l'IA et les processus de prise de décision permettant à l'IA de faire des mouvements intelligents et stratégiques.  
  ◦ Explorer des algorithmes et des techniques alternatifs pour créer un joueur IA efficace sans se baser sur A*.  
  ◦ Assurer que l'IA s'adapte à différents scénarios de jeu et interactions avec l'utilisateur.  

***Warning*** 
Vous devrez expliquer en détail comment votre IA fonctionne lors de l’évaluation. Créer une IA qui ne fait rien est strictement interdit ; elle doit avoir la capacité de gagner occasionnellement.  
Ce module majeur vise à améliorer le jeu en introduisant un adversaire IA qui ajoute de l'excitation et de la compétitivité sans se baser sur l'algorithme A*.

• **Module mineur : Tableaux de bord des statistiques des utilisateurs et des jeux.**  
Dans ce module mineur, l'objectif est d'introduire des tableaux de bord qui affichent des statistiques pour les utilisateurs individuels et les sessions de jeu. Les principales caractéristiques et objectifs incluent :
  ◦ Créer des tableaux de bord conviviaux qui fournissent aux utilisateurs des informations sur leurs propres statistiques de jeu.
  ◦ **Développer un tableau de bord séparé pour les sessions de jeu**, affichant des statistiques détaillées, les résultats et les données historiques pour chaque match.  
  ◦ S'assurer que les tableaux de bord offrent une interface utilisateur intuitive et informative pour suivre et analyser les données.  
  ◦ Implémenter des techniques de visualisation des données, telles que des graphiques et des diagrammes, pour présenter les statistiques de manière claire et visuellement attrayante.  
  ◦ Permettre aux utilisateurs d'accéder facilement à leur historique de jeu et aux métriques de performance.  
  ◦ N'hésitez pas à ajouter toute métrique que vous jugez utile.

Ce module mineur vise à permettre aux utilisateurs de suivre leurs statistiques de jeu et les détails de leurs sessions de jeu à travers des tableaux de bord conviviaux, offrant une vue d'ensemble complète de leur expérience de jeu.

**IV.6 Cybersecurity**  
Ces modules de cybersécurité sont conçus pour renforcer la posture de sécurité du projet, avec le module majeur se concentrant sur une protection robuste via une configuration de pare-feu d'application web (WAF) et de ModSecurity, ainsi que sur HashiCorp Vault pour la gestion sécurisée des secrets. Les modules mineurs complètent cet effort en ajoutant des options pour la conformité au RGPD, l'anonymisation des données utilisateurs, la suppression de comptes, l'authentification à deux facteurs (2FA) et les JSON Web Tokens (JWT), assurant ainsi l'engagement du projet envers la protection des données, la confidentialité et la sécurité de l'authentification.

• **Module majeur : Implémentation de WAF/ModSecurity avec une configuration renforcée et HashiCorp Vault pour la gestion des secrets.**  
Dans ce module majeur, l'objectif est d'améliorer l'infrastructure de sécurité du projet en mettant en œuvre plusieurs composants clés. Les principales caractéristiques et objectifs incluent :
  ◦ **Configurer et déployer un pare-feu d'application web (WAF)** et **ModSecurity** avec une configuration stricte et sécurisée pour protéger contre les attaques basées sur le web.  
  ◦ **Intégrer HashiCorp Vault** pour gérer et stocker de manière sécurisée des informations sensibles, telles que des clés API, des identifiants et des variables d'environnement, en veillant à ce que ces secrets soient correctement cryptés et isolés.

Ce module majeur vise à renforcer l'infrastructure de sécurité du projet en mettant en œuvre des mesures de sécurité robustes, y compris WAF/ModSecurity pour la protection des applications web et HashiCorp Vault pour la gestion des secrets, afin de garantir un environnement sécurisé.

• **Module mineur : Options de conformité RGPD avec anonymisation des utilisateurs, gestion locale des données et suppression de comptes.**  
Dans ce module mineur, l'objectif est d'introduire des options de conformité au RGPD permettant aux utilisateurs d'exercer leurs droits en matière de confidentialité des données. Les principales caractéristiques et objectifs incluent :
  ◦ **Mettre en œuvre des fonctionnalités conformes au RGPD** permettant aux utilisateurs de demander l'anonymisation de leurs données personnelles, garantissant que leur identité et leurs informations sensibles sont protégées.  
  ◦ **Fournir des outils permettant aux utilisateurs de gérer leurs données locales**, y compris la possibilité de consulter, modifier ou supprimer leurs informations personnelles stockées dans le système.  
  ◦ **Offrir un processus simplifié pour que les utilisateurs demandent la suppression permanente** de leurs comptes, y compris toutes les données associées, garantissant ainsi la conformité aux réglementations sur la protection des données.  
  ◦ **Maintenir une communication claire et transparente avec les utilisateurs** concernant leurs droits en matière de confidentialité des données, avec des options facilement accessibles pour exercer ces droits.

Ce module mineur vise à améliorer la confidentialité des utilisateurs et la protection des données en offrant des options de conformité RGPD permettant aux utilisateurs de contrôler leurs informations personnelles et d'exercer leurs droits en matière de confidentialité des données au sein du système.  

Si vous n'êtes pas familiarisé avec le **Règlement Général sur la Protection des Données (RGPD)**, il s'agit d'une législation de l'Union Européenne qui impose des règles strictes concernant la collecte, le stockage et la gestion des données personnelles des citoyens de l'UE.
Il est essentiel de comprendre les principes et les implications du RGPD, en particulier en ce qui concerne la gestion des données utilisateur et la confidentialité. Le RGPD est un règlement qui vise à protéger les données personnelles et la confidentialité des individus au sein de l'Union Européenne (UE) et de l'Espace Économique Européen (EEE). Il établit des règles strictes et des lignes directrices pour les organisations sur la manière de traiter et de gérer les données personnelles.

Pour mieux comprendre le RGPD et ses exigences, il est fortement recommandé de visiter le site web officiel de la Commission Européenne sur la protection des données. Ce site fournit des informations complètes sur le RGPD, y compris ses principes, objectifs et droits des utilisateurs. Il propose également des ressources supplémentaires pour approfondir le sujet et garantir la conformité avec le règlement.

Si vous n'êtes pas familier avec le RGPD, prenez le temps de visiter le lien fourni et familiarisez-vous avec les règlements avant de poursuivre ce projet.

• **Module majeur : Implémentation de l'authentification à deux facteurs (2FA) et des JSON Web Tokens (JWT).**  
Dans ce module majeur, l'objectif est d'améliorer la sécurité et l'authentification des utilisateurs en introduisant l'authentification à deux facteurs (2FA) et en utilisant les JSON Web Tokens (JWT). Les principales caractéristiques et objectifs incluent :  
  ◦ **Implémenter l'authentification à deux facteurs (2FA)** comme couche supplémentaire de sécurité pour les comptes utilisateurs, exigeant des utilisateurs qu'ils fournissent une méthode de vérification secondaire, comme un code à usage unique, en plus de leur mot de passe.  
  ◦ **Utiliser les JSON Web Tokens (JWT)** comme méthode sécurisée pour l'authentification et l'autorisation, garantissant que les sessions des utilisateurs et l'accès aux ressources sont gérés de manière sécurisée.  
  ◦ **Fournir un processus de configuration convivial pour activer la 2FA**, avec des options pour les codes SMS, les applications d'authentification ou la vérification par email.  
  ◦ **S'assurer que les jetons JWT sont émis et validés de manière sécurisée** pour empêcher l'accès non autorisé aux comptes utilisateurs et aux données sensibles.

Ce module majeur vise à renforcer la sécurité des comptes utilisateurs en offrant l'authentification à deux facteurs (2FA) et en améliorant l'authentification et l'autorisation grâce à l'utilisation des JSON Web Tokens (JWT).
**IV.7 DevOps**  
Ces modules visent collectivement à améliorer l'infrastructure et l'architecture du projet, les modules majeurs abordant la mise en place de l'infrastructure pour une gestion efficace des journaux via ELK (Elasticsearch, Logstash, Kibana), la conception du backend sous forme de microservices pour plus de flexibilité et d'évolutivité, ainsi que la mise en place de Prometheus/Grafana pour une surveillance complète du système.

• **Module majeur : Mise en place de l'infrastructure avec ELK (Elasticsearch, Logstash, Kibana) pour la gestion des journaux.**  
Dans ce module majeur, l'objectif est de mettre en place une infrastructure robuste pour la gestion et l'analyse des journaux en utilisant la pile ELK (Elasticsearch, Logstash, Kibana). Les principales caractéristiques et objectifs incluent :  
  ◦ **Déployer Elasticsearch** pour stocker et indexer efficacement les données de journal, permettant ainsi une recherche et un accès faciles.  
  ◦ **Configurer Logstash** pour collecter, traiter et transformer les données de journal provenant de différentes sources et les envoyer vers Elasticsearch.  
  ◦ **Mettre en place Kibana** pour visualiser les données de journal, créer des tableaux de bord et générer des informations à partir des événements de journal.  
  ◦ **Définir des politiques de rétention et d'archivage des données** pour gérer efficacement le stockage des journaux.  
  ◦ **Mettre en œuvre des mesures de sécurité** pour protéger les données de journal et l'accès aux composants de la pile ELK.

Ce module majeur vise à établir un système puissant de gestion et d'analyse des journaux utilisant la pile ELK, permettant une résolution des problèmes, une surveillance et des informations efficaces sur l'opération et la performance du système.

• **Module mineur : Système de surveillance.**  
Dans ce module mineur, l'objectif est de mettre en place un système de surveillance complet en utilisant Prometheus et Grafana. Les principales caractéristiques et objectifs incluent :  
  ◦ **Déployer Prometheus** comme outil de surveillance et d'alerte pour collecter des métriques et surveiller la santé et la performance des différents composants du système.  
  ◦ **Configurer les exportateurs de données et les intégrations** pour capturer les métriques des différents services, bases de données et composants d'infrastructure.  
  ◦ **Créer des tableaux de bord personnalisés** et des visualisations à l'aide de Grafana pour fournir des informations en temps réel sur les métriques et la performance du système.  
  ◦ **Configurer des règles d'alerte dans Prometheus** pour détecter et répondre de manière proactive aux problèmes critiques et anomalies.  
  ◦ **Assurer une stratégie de rétention et de stockage appropriée** pour les données de métriques historiques.  
  ◦ **Mettre en œuvre des mécanismes d'authentification sécurisés et de contrôle d'accès** pour Grafana afin de protéger les données sensibles de surveillance.

Ce module mineur vise à offrir une surveillance complète du système en utilisant Prometheus pour collecter des métriques et Grafana pour visualiser et analyser les performances du système en temps réel.

**• Module majeur : Conception du backend en tant que microservices.**  
Dans ce module majeur, l'objectif est d'architecturer le backend du système en utilisant une approche basée sur les microservices. Les principales caractéristiques et objectifs incluent :  
  ◦ **Diviser le backend** en microservices plus petits et faiblement couplés, chacun étant responsable de fonctions ou de fonctionnalités spécifiques.  
  ◦ **Définir des frontières et des interfaces claires** entre les microservices pour permettre un développement, un déploiement et une mise à l'échelle indépendants.  
  ◦ **Mettre en œuvre des mécanismes de communication** entre les microservices, tels que des API RESTful ou des files de messages, pour faciliter l'échange de données et la coordination.  
  ◦ **Assurer que chaque microservice est responsable d'une seule tâche ou capacité métier** bien définie, favorisant ainsi la maintenabilité et l'évolutivité.

Ce module majeur vise à améliorer l'architecture du système en adoptant une approche de conception basée sur les microservices, permettant ainsi une plus grande flexibilité, évolutivité et maintenabilité des composants backend.

**IV.8 Gaming**  
Ces modules sont conçus pour améliorer l’aspect de la gamification du projet, avec le module majeur introduisant de nouveaux jeux, le suivi de l’historique des utilisateurs et un système de matchmaking, tandis que le module mineur se concentre sur l’ajout d'options de personnalisation pour tous les jeux disponibles.

**• Module majeur : Ajouter un autre jeu avec historique des utilisateurs et matchmaking.**  
L’objectif de ce module majeur est d'introduire un nouveau jeu, distinct de Pong, et d'incorporer des fonctionnalités telles que le suivi de l'historique des utilisateurs et le matchmaking. Les principales caractéristiques et objectifs incluent :  
  ◦ Développer un nouveau jeu engageant pour diversifier l'offre de la plateforme et divertir les utilisateurs.  
  ◦ Implémenter le suivi de l’historique des utilisateurs pour enregistrer et afficher les statistiques de jeu de chaque utilisateur.  
  ◦ Créer un système de matchmaking pour permettre aux utilisateurs de trouver des adversaires et de participer à des matchs équilibrés et équitables.  
  ◦ S’assurer que l’historique des jeux des utilisateurs et les données de matchmaking sont stockés en toute sécurité et restent à jour.  
  ◦ Optimiser les performances et la réactivité du nouveau jeu pour offrir une expérience utilisateur agréable. Mettre régulièrement à jour et maintenir le jeu pour corriger les bugs, ajouter de nouvelles fonctionnalités et améliorer le gameplay.

Ce module majeur vise à élargir votre plateforme en introduisant un nouveau jeu, en renforçant l’engagement des utilisateurs grâce à l’historique des jeux et en facilitant le matchmaking pour une expérience de jeu agréable.

**• Module mineur : Options de personnalisation des jeux.**  
Dans ce module mineur, l’objectif est de fournir des options de personnalisation pour tous les jeux disponibles sur la plateforme. Les principales caractéristiques et objectifs incluent :  
  ◦ Offrir des fonctionnalités de personnalisation, telles que des power-ups, des attaques ou des cartes différentes, pour améliorer l’expérience de jeu.  
  ◦ Permettre aux utilisateurs de choisir une version par défaut du jeu avec des fonctionnalités de base s’ils préfèrent une expérience plus simple.  
  ◦ Veiller à ce que les options de personnalisation soient disponibles et applicables à tous les jeux proposés sur la plateforme.  
  ◦ Mettre en place des menus de paramètres ou des interfaces conviviaux pour ajuster les paramètres du jeu.  
  ◦ Maintenir la cohérence des fonctionnalités de personnalisation à travers tous les jeux pour offrir une expérience utilisateur unifiée.

Ce module vise à donner aux utilisateurs la flexibilité de personnaliser leur expérience de jeu à travers tous les jeux disponibles, en fournissant une variété d'options de personnalisation tout en offrant une version par défaut pour ceux qui préfèrent une expérience de jeu plus simple.

**IV.9 Graphics**  
**• Module majeur : Mise en œuvre des techniques 3D avancées**  
Ce module majeur, intitulé "Graphics", se concentre sur l'amélioration des aspects visuels du jeu Pong. Il introduit l’utilisation de techniques 3D avancées pour créer une expérience de jeu plus immersive. Plus précisément, le jeu Pong sera développé à l’aide de ThreeJS/WebGL pour atteindre les effets visuels désirés.
 
  ◦ **Graphismes 3D avancés** : L’objectif principal de ce module est d’implémenter des techniques graphiques 3D avancées pour élever la qualité visuelle du jeu Pong. L’utilisation de ThreeJS/WebGL permettra de créer des effets visuels impressionnants qui immergeront les joueurs dans l’environnement de jeu.  
  ◦ **Gameplay immersif** : L’intégration des techniques 3D avancées améliore l’expérience de jeu globale en offrant aux utilisateurs un jeu Pong visuellement captivant et engageant.  
  ◦ **Intégration technologique** : La technologie choisie pour ce module est ThreeJS/WebGL. Ces outils seront utilisés pour créer les graphismes 3D, garantissant ainsi la compatibilité et des performances optimales.

Ce module majeur vise à révolutionner les éléments visuels du jeu Pong en introduisant des techniques 3D avancées. Grâce à l’utilisation de ThreeJS/WebGL, nous aspirons à offrir aux joueurs une expérience de jeu immersive et visuellement époustouflante.

**IV.10 Accessibility**  
Ces modules visent à améliorer l'accessibilité de notre application web, en garantissant sa compatibilité sur tous les appareils, en élargissant le support des navigateurs, en offrant des capacités multilingues, en fournissant des fonctionnalités d'accessibilité pour les utilisateurs malvoyants, et en intégrant le rendu côté serveur (SSR) pour améliorer les performances et l'expérience utilisateur.

**• Module mineur : Support sur tous les appareils**  
Dans ce module, l'objectif principal est de garantir que votre site fonctionne parfaitement sur tous les types d'appareils.  

  ◦ **Responsive design** : S'assurer que le site soit réactif, s’adaptant à différentes tailles d'écran et orientations, offrant une expérience utilisateur cohérente sur les ordinateurs de bureau, ordinateurs portables, tablettes et smartphones.  
  ◦ **Navigation adaptée** : Veiller à ce que les utilisateurs puissent facilement naviguer et interagir avec le site en utilisant différents moyens d’entrée, comme les écrans tactiles, les claviers et les souris, selon l'appareil utilisé.  

Ce module vise à offrir une expérience cohérente et conviviale sur tous les appareils, maximisant ainsi l'accessibilité et la satisfaction des utilisateurs.

**• Module mineur : Extension de la compatibilité avec les navigateurs**  
Dans ce module mineur, l'objectif est d'améliorer la compatibilité de l'application web en ajoutant un support pour un navigateur web supplémentaire.  
 
  ◦ **Compatibilité avec un navigateur supplémentaire** : Étendre la compatibilité des navigateurs pour inclure un navigateur supplémentaire, garantissant que les utilisateurs puissent accéder et utiliser l’application sans problème.  
  ◦ **Tests et optimisation** : Effectuer des tests approfondis et optimiser le site pour qu’il fonctionne correctement et s'affiche correctement sur le nouveau navigateur supporté.  
  ◦ **Résolution des problèmes de compatibilité** : Corriger les éventuels problèmes de compatibilité ou de rendu qui pourraient survenir sur le navigateur ajouté.  
  ◦ **Expérience utilisateur cohérente** : Veiller à offrir une expérience utilisateur cohérente sur tous les navigateurs supportés, en maintenant la convivialité et la fonctionnalité.  

Ce module vise à élargir l'accessibilité de l'application web en supportant un navigateur supplémentaire, offrant ainsi aux utilisateurs plus de choix pour leur expérience de navigation.

**• Module mineur : Support multilingue**  
Dans ce module mineur, l'objectif est de garantir que votre site prenne en charge plusieurs langues afin de s’adresser à un large public.  
 
  ◦ **Support multilingue** : Implémenter le support d'un minimum de trois langues sur le site pour toucher une audience diversifiée.  

  ◦ **Sélecteur de langue** : Fournir un sélecteur de langue ou un interrupteur qui permet aux utilisateurs de changer facilement la langue du site selon leurs préférences.  
  ◦ **Traduction du contenu essentiel** : Traduire le contenu essentiel du site, tel que les menus de navigation, les titres et les informations clés, dans les langues prises en charge.  
  ◦ **Navigation fluide** : S'assurer que les utilisateurs puissent naviguer et interagir avec le site sans difficulté, quel que soit la langue sélectionnée.  
  ◦ **Utilisation de bibliothèques de localisation** : Envisager l'utilisation de packs de langue ou de bibliothèques de localisation pour simplifier le processus de traduction et maintenir la cohérence entre les différentes langues.  
  ◦ **Langue par défaut** : Permettre aux utilisateurs de définir leur langue préférée comme choix par défaut lors de leurs prochaines visites sur le site.  

Ce module vise à améliorer l'accessibilité et l'inclusivité de votre site en offrant du contenu dans plusieurs langues, rendant le site plus convivial pour un public international diversifié.

**• Module mineur : Ajouter l'accessibilité pour les utilisateurs malvoyants**  
Ce module a pour objectif de rendre votre site plus accessible pour les utilisateurs malvoyants.  
  
  ◦ **Support des lecteurs d'écran** : Assurer la compatibilité avec les lecteurs d'écran et autres technologies d'assistance.  
  ◦ **Texte alternatif descriptif** : Fournir un texte alternatif clair et descriptif pour les images.  
  ◦ **Schéma de couleurs à contraste élevé** : Utiliser un schéma de couleurs à contraste élevé pour améliorer la lisibilité.  
  ◦ **Navigation au clavier et gestion du focus** : Permettre une navigation fluide au clavier et une gestion adéquate du focus pour faciliter l'utilisation sans souris.  
  ◦ **Options d'ajustement de la taille du texte** : Offrir des options pour que les utilisateurs puissent ajuster la taille du texte selon leurs besoins.  
  ◦ **Mises à jour régulières** : Assurer la mise à jour régulière pour respecter les normes d'accessibilité.  

Ce module vise à améliorer l'utilisabilité du site pour les personnes malvoyantes et garantir la conformité avec les normes d'accessibilité.

**• Module mineur : Intégration du rendu côté serveur (SSR)**  
Ce module se concentre sur l'intégration du rendu côté serveur (SSR) pour améliorer les performances et l'expérience utilisateur de votre site.  

  ◦ **Implémentation de SSR** : Mettre en place SSR pour améliorer la vitesse de chargement du site et les performances générales.  
  ◦ **Prérendu du contenu** : S'assurer que le contenu soit pré-rendu sur le serveur et livré directement dans les navigateurs des utilisateurs pour des chargements de page initiaux plus rapides.  
  ◦ **Optimisation du SEO** : Améliorer le référencement en fournissant aux moteurs de recherche du contenu HTML pré-rendu.  
  ◦ **Expérience utilisateur cohérente** : Maintenir une expérience utilisateur homogène tout en bénéficiant des avantages du SSR.  

Ce module vise à augmenter la performance du site et son SEO en intégrant le rendu côté serveur pour un chargement plus rapide des pages et une meilleure expérience utilisateur.

### IV.11 Pong côté serveur

**• Module majeur : Remplacer le Pong de base par un Pong côté serveur et implémenter une API.**

Dans ce module majeur, l'objectif est de remplacer le jeu Pong de base par un jeu Pong côté serveur, accompagné de l'implémentation d'une API. Les caractéristiques et objectifs principaux incluent :

◦ Développer la logique côté serveur pour le jeu Pong afin de gérer le gameplay, les mouvements de la balle, le score et les interactions des joueurs.
◦ Créer une API qui expose les ressources et points de terminaison nécessaires pour interagir avec le jeu Pong, permettant une utilisation partielle du jeu via l'interface en ligne de commande (CLI) et l'interface web.
◦ Concevoir et implémenter les points de terminaison de l'API pour soutenir l'initialisation du jeu, le contrôle des joueurs et les mises à jour de l'état du jeu.
◦ Assurer que le jeu Pong côté serveur soit réactif, offrant une expérience de jeu engageante et agréable.
◦ Intégrer le jeu Pong côté serveur avec l'application web, permettant aux utilisateurs de jouer directement sur le site.

Ce module majeur vise à améliorer le jeu Pong en le migrer côté serveur, permettant une interaction via l'interface web et la CLI tout en offrant une API pour un accès facile aux ressources et fonctionnalités du jeu.

**• Module majeur : Activer le gameplay de Pong via CLI contre des utilisateurs web avec intégration de l'API.**

Dans ce module majeur, l'objectif est de développer une interface en ligne de commande (CLI) permettant aux utilisateurs de jouer à Pong contre des joueurs utilisant la version web du jeu. La CLI doit se connecter à l'application web de manière fluide, permettant aux utilisateurs de la CLI de rejoindre et d'interagir avec les joueurs web. Les caractéristiques et objectifs principaux incluent :

◦ Créer une application CLI robuste qui réplique l'expérience de jeu de Pong disponible sur le site web, permettant aux utilisateurs de la CLI d'initier et de participer à des matchs de Pong.
◦ Utiliser l'API pour établir une communication entre la CLI et l'application web, permettant aux utilisateurs de la CLI de se connecter au site et d'interagir avec les joueurs web.
◦ Développer un mécanisme d'authentification des utilisateurs dans la CLI, permettant aux utilisateurs de la CLI de se connecter de manière sécurisée à l'application web.
◦ Implémenter une synchronisation en temps réel entre les utilisateurs de la CLI et les utilisateurs web, assurant que les interactions de gameplay sont fluides et cohérentes.
◦ Permettre aux utilisateurs de la CLI de rejoindre et de créer des matchs de Pong avec les joueurs web, facilitant le gameplay multiplateforme.
◦ Fournir une documentation complète et des conseils sur la manière d'utiliser la CLI de manière efficace pour les matchs de Pong contre les utilisateurs web.

Ce module majeur vise à améliorer l'expérience de jeu de Pong en créant une interface en ligne de commande (CLI) qui connecte de manière fluide les utilisateurs de la CLI aux joueurs web via l'intégration de l'API, offrant ainsi un environnement de jeu interactif et unifié.  

***WARNING***
	Si vous souhaitez réaliser ce module, nous vous recommandons fortement de commencer par le module précédent.

**Chapitre V : Partie Bonus**

Pour ce projet, la section bonus est conçue pour être simple. Vous devez inclure davantage de modules.

- **Cinq points** seront attribués pour chaque module mineur.
- **Dix points** seront attribués pour chaque module majeur.

La partie bonus ne sera évaluée que si la partie obligatoire est **PARFAITE**. Parfaite signifie que la partie obligatoire a été entièrement réalisée et fonctionne sans dysfonctionnement. Si vous n'avez pas rempli **TOUS** les critères obligatoires, votre partie bonus ne sera pas évaluée du tout.


