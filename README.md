# NSI-COVID- BILAL ET AYOUB
Désolé pour l'instant on a pas réussi a mettre en ligne le site donc si vous voulez le lancer uiliser

git clone https://github.com/youbyoub48/NSI-COVID.git

cd NSI-COVID

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

cd src

python manage.py collectstatic

python manage.py runserver

puis allez sur le 127.0.0.1:80000

Pour commencer on a voulu créer un application web, on s'est renseigner et on a appris qu'il y avait deux parties dans le developpement web: le Front-end et le Back-end. Le front-end c'est plutôt la partie que l'utilisateur va voir et intéragir avec, c'est le côté client. Il est surtout composer de html, css(bootstrap) et de javascript. Le back-end c'est la partie que l'utilisateur ne vois pas et qui fait des calculs en arrière plan. C'est le côté serveur du site web qui est souvent fait avec php , python(Django, Flask), Ruby ou Javascript avec certains frameworks. C'est surtout fait avec des frameworks donc on a choisi Python avec le framework Django, car on était plus a l'aise et qu'on avait pas réussis a comprendre Flask. Ensuite on s'est demander comment font les autres sites pour avoir un design responsive et bien c'est que la plupart utilise Bootstrap, donc on a essayer d'apprendre à l'utiliser mais on a manquer de temps. C'est pour celà que le index.html à son propre fichier css. Avec javascript on a eu le même problème de temps et on a donc pas pus bien l'apprendre car Django nous a pris trop de temps. On a aussi dû apprendre la programmation orienté objet de python. Comme on s'y connaissais peu en javascript on a décider d'utiliser chart.js, qui permet de faire des graphiques facilement. De là nous avons eu l'idée de faire une application sur des statistiques surtout que python est très performent sur la communication avec les API. On voulait un petit truc en plus que les autres sites, qu'on puisse comparer facilement les résultats de tous les pays.

![index](https://user-images.githubusercontent.com/49432032/116346885-65ae3180-a7eb-11eb-9313-c09457fc65a8.png)
Quel bg ;)
