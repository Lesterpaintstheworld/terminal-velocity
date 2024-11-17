# Directives Opérationnelles - Terminal Velocity

## Contexte KinOS
Ce projet opère entièrement dans l'environnement KinOS. Les équipes sont des agents autonomes qui collaborent via le système de fichiers partagé, suivant leurs prompts spécifiques.

## Principes de Base

### Structure du Système de Fichiers
- Chaque équipe opère dans son espace dédié
- Les fichiers sont le seul moyen de communication
- La coordination se fait par lecture/écriture de fichiers
- L'historique est préservé dans le système

### Mécanisme de Collaboration
- Surveillance continue des fichiers pertinents
- Réaction aux modifications détectées
- Mises à jour autonomes des contenus
- Propagation naturelle des changements

### Validation et Cohérence
- Vérification automatique par les agents
- Tests de cohérence via le système de fichiers
- Documentation continue dans les fichiers
- Résolution autonome des conflits

## Processus Autonomes

### Surveillance
- Chaque équipe surveille les fichiers pertinents
- Détection automatique des changements
- Analyse continue de la cohérence
- Mise à jour des états

### Résolution de Conflits
- Détection automatique des incohérences
- Documentation dans conflicts/
- Résolution par les équipes concernées
- Mise à jour des fichiers impactés

### Documentation Continue
- Mise à jour automatique des fichiers
- Traçabilité des décisions
- Historique des modifications
- États courants maintenus
