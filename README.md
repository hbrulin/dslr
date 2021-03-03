# dslr

#describe
https://www.investopedia.com/terms/s/standarddeviation.asp#:~:text=A%20standard%20deviation%20is%20a,deviation%20relative%20to%20the%20mean.
https://datascience.stackexchange.com/questions/52613/what-does-pandas-describe-percentiles-values-tell-about-our-data 
https://www.statisticshowto.com/probability-and-statistics/percentiles-rank-range/

#Visualization
https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/subplots_demo.html


#python
https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal

#training
https://openclassrooms.com/fr/courses/4444646-entrainez-un-modele-predictif-lineaire/4507846-classifiez-vos-donnees-en-plus-de-deux-classes

Bonuses:
#compute most homogenous
#overview scatter_plot with normalization
#check accuracy



Multiclassifieur : 
- pour classifier en plus de deux classes;
- K étant le nb de classes
- On vs all / one vs rest = créer un classifieur f pour chacune des classes, qui sépare les points de cette classe de tous les autres points. 
C'est la dérivée partielle thetaj, j étant la classe. Le xj est représente donc les données de la classe.

Nos classifieurs sont des régressions logistiques.
On fait passer X par les 4 classifieurs, donc on utilise 4 fois predict() avec les 4 thetas : x appartient à la classe pour laquelle cette prédiction est la plus élevée.