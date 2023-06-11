# Projet 7 OC API 

# Introduction

- **Objectif du projet** : L'objectif de notre projet est de mettre en œuvre un outil de **scoring crédit** au service des chargés de relation client d'une société financière. 

- **Contexte** : La société **Prêt à dépenser** propose des crédit à la consommation pour des personnes ayant peu ou pas du tout d'historique de prêt. 


# Exemple de requêtes : 

Dans votre navigateur tapez l'une des requêtes suivantes : 

```python
# Pour afficher la liste des id clients : 
https://scoringapp.pythonanywhere.com/listeidclients
```

```python
# Pour afficher probabilité de défaut d'un client : client dont l'id : 100005
https://scoringapp.pythonanywhere.com/proba/100005
```

```python
# Pour afficher les data d'un client : client dont l'id : 100005
https://scoringapp.pythonanywhere.com/data/100005
```
```python
# Pour afficher la liste des colonnes du data frame
https://scoringapp.pythonanywhere.com/listecolumnsnames
```