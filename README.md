##  Hybrid_Recommender_System
Recommender System is a system that seeks to predict or filter preferences according to the user’s choices. The dataset (ml-latest-small) describes 5-star rating and activity from [Movie Lens] (http://movielens.org), a movie recommendation service. 
It contains 100836 ratings across 9742 movies. These data were created by 610 users between March 29, 1996 and September 24, 2018. The dataset used was generated on September 26, 2018. 
This project is collectively made by Anjali Pal ,Niranjan Jena, Prakhar Gupta, Satyajit Kumar and  Soumyabrata Ghosh 

OUR APPROACH

Content Filtering Algorithm

Here, we have only taken into account the three movies, the user has provided. 
Based on the genres, the system tries to find similar movies using cosine similarity.

Collaborative Filtering System
 
We have used a hybrid recommendation wherein we are using plot and genres of movies for content-based filtering and Users are used for collaborative filtering.
Then, we have clubbed the two approaches together to get our final recommendation list.


REFERENCES:
1. Research Paper:
	https://dl.acm.org/citation.cfm?id=3052569
	By: He Xiangnan , Liao Lizi , et.al 
	Published in 2017
2.  Neu-mf approach https://nipunbatra.github.io/blog/2017/neural-collaborative-filtering.html
3. GeeksForGeeks
4. Analytics Vidhya
