# Download the repository / DL le dépôt git

Installation de base:

```
  mkdir beers4flags
  cd beers4flags
  git clone https://github.com/Beers4Flags/ctftools.git
  git clone https://github.com/Beers4Flags/writeups.git
```

The 2 folders will be created in your local computer, they are git repositories.
Les 2 dossiers seront créés sur votre ordi, ce sont des dépôts git.

```
  $ ls
  ctftools writeups
```

All next commands must be run IN a git repository:
Toutes les commandes qui suivent doivent être exécutées dans un dépôt git:

```
  :~/git/beers4flags$ cd ctftools # OR
  :~/git/beers4flags$ cd writeups
```

# Update your local files / Mettre à jour vos fichiers locaux

```
  :~/git/beers4flags/ctftools$ git pull origin master
```

This command will update your local files. Do it before any push.
Cette commande va mettre à jour vos fichiers locaux.

# Add a new folder and push it / Créer un nouveau dossier et le mettre en ligne

When you want to create new folders / files, just use your local filesystem and create / modify them.
Quand vous voulez créer des nouveaux fichiers, faites comme d'habitude sur votre système de fichier local.

## Add and commit / Valider vos changements

You did all your changes and ready to make it online ?
Vous avez fait tous vos changements et êtes prêts à mettre en ligne ?

(exemple: création d'un dossier script avec un fichier example)

### See the status

```
  :~/git/beers4flags/ctftools$ git status
  On branch master
  Your branch is up-to-date with 'origin/master'.
  Untracked files:
    (use "git add <file>..." to include in what will be committed)
      script/
```

All the files are red ? You need to add them.

### Add your files

You need to add the folder to the git / Il faut référencer vos fichiers

```
  :~/git/beers4flags/ctftools$ git add script
  :~/git/beers4flags/ctftools$ git status
  On branch master
  Your branch is up-to-date with 'origin/master'.
  Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)
    new file:   script/example.py
```

The files became green ? Good !
Files still red ? Need to add them too.

### Commit the changes

When you are ready, commit the changes, then push it /
Quand vous avez tout add, commit, pull puis push.

```
  :~/git/beers4flags/ctftools$ git commit -m " COMMENT "
```

Don't put shitty comment / Mettre un commentaire pas débile svp

### Update your local repository

```
  :~/git/beers4flags/ctftools$ git pull origin master
```

Update local repository / Mettre à jour le dossier local
This helps avoiding conflicts / ça permet d'éviter les problèmes de synchronisation

### Update remote repository

Send the files to the repository / Envoyer les fichiers sur le github.

```
  :~/git/beers4flags/ctftools$ git push origin master
```

You will be asked for your github login / password.
