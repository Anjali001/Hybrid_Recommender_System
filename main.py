import numpy as np
import random
from flask import Flask, request, render_template
from model.simple_recommender_model import simple_recommend
import pandas as pd
from tensorflow import keras



from rake_nltk import Rake
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


app = Flask(__name__)

#@app.route('/')
#def homepage():
# return render_template('homepage.html')

#@app.route('/watchtrailer')
#def watch():
#  return render_template('fresh_tomatoes.html')

@app.route('/', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      moviesall=[]
      movies=[]
      def xstr(s):
        if s is None:
          return ""
        else:
          return str(s)  
      Movie1 = request.form.get('chk1')
      Movie1 = xstr(Movie1)
      moviesall.append(Movie1)
      Movie2 = request.form.get('chk2')
      Movie2 = xstr(Movie2)
      moviesall.append(Movie2)
      Movie3 = request.form.get('chk3')
      Movie3 = xstr(Movie3)
      moviesall.append(Movie3)
      Movie4 = request.form.get('chk4')
      Movie4 = xstr(Movie4)
      moviesall.append(Movie4)
      
      Movie5 = request.form.get('chk5')
      Movie5 = xstr(Movie5)
      moviesall.append(Movie5)
      Movie6 = request.form.get('chk6')
      Movie6 = xstr(Movie6)
      moviesall.append(Movie6)
      Movie7 = request.form.get('chk7')
      Movie7 = xstr(Movie7)
      moviesall.append(Movie7)
      Movie8 = request.form.get('chk8')
      Movie8 = xstr(Movie8)
      moviesall.append(Movie8)

      Movie9 = request.form.get('chk9')
      Movie9 = xstr(Movie9)
      moviesall.append(Movie9)
      Movie10 = request.form.get('chk10')
      Movie10 = xstr(Movie10)
      moviesall.append(Movie10)
      Movie11 = request.form.get('chk11')
      Movie11 = xstr(Movie11)
      moviesall.append(Movie11)
      Movie12 = request.form.get('chk12')
      Movie12 = xstr(Movie12)
      moviesall.append(Movie12)

      Movie13 = request.form.get('chk13')
      Movie13 = xstr(Movie13)
      moviesall.append(Movie13)
      Movie14 = request.form.get('chk14')
      Movie14 = xstr(Movie14)
      moviesall.append(Movie14)
      Movie15 = request.form.get('chk15')
      Movie15 = xstr(Movie15)
      moviesall.append(Movie15)
      Movie16 = request.form.get('chk16')
      Movie16 = xstr(Movie16)
      moviesall.append(Movie16)

      Movie17 = request.form.get('chk17')
      Movie17 = xstr(Movie17)
      moviesall.append(Movie17)
      Movie18 = request.form.get('chk18')
      Movie18 = xstr(Movie18)
      moviesall.append(Movie18)
      Movie19 = request.form.get('chk19')
      Movie19 = xstr(Movie19)
      moviesall.append(Movie19)
      Movie20 = request.form.get('chk20')
      Movie20 = xstr(Movie20)
      moviesall.append(Movie20)
      
      Movie21 = request.form.get('chk21')
      Movie21 = xstr(Movie21)
      moviesall.append(Movie21)

      Movie22 = request.form.get('chk22')
      Movie22 = xstr(Movie22)
      moviesall.append(Movie22)

      Movie23 = request.form.get('chk23')
      Movie23 = xstr(Movie23)
      moviesall.append(Movie23)
      
      Movie24 = request.form.get('chk24')
      Movie24 = xstr(Movie24)
      moviesall.append(Movie24)

      Movie25 = request.form.get('chk25')
      Movie25 = xstr(Movie25)
      moviesall.append(Movie25)

      Movie26 = request.form.get('chk26')
      Movie26 = xstr(Movie26)
      moviesall.append(Movie26)

      Movie27 = request.form.get('chk27')
      Movie27 = xstr(Movie27)
      moviesall.append(Movie27)
      
      Movie28 = request.form.get('chk28')
      Movie28 = xstr(Movie28)
      moviesall.append(Movie28)

      Movie29 = request.form.get('chk29')
      Movie29 = xstr(Movie29)
      moviesall.append(Movie29)

      Movie30 = request.form.get('chk30')
      Movie30 = xstr(Movie30)
      moviesall.append(Movie30)
      
      Movie31 = request.form.get('chk31')
      Movie31 = xstr(Movie31)
      moviesall.append(Movie31)

      Movie32 = request.form.get('chk32')
      Movie32 = xstr(Movie32)
      moviesall.append(Movie32)

      Movie33 = request.form.get('chk33')
      Movie33 = xstr(Movie33)
      moviesall.append(Movie33)
      
      Movie34 = request.form.get('chk34')
      Movie34 = xstr(Movie34)
      moviesall.append(Movie34)

      Movie35 = request.form.get('chk35')
      Movie35 = xstr(Movie35)
      moviesall.append(Movie35)

      Movie36 = request.form.get('chk36')
      Movie36 = xstr(Movie36)
      moviesall.append(Movie36)


      for item in moviesall:
        if item:
          movies.append(item)
        else:
          continue  

      
      dataset = pd.read_csv(r'C:\Users\Lenovo PC\Downloads\ml-latest-small\ratings.csv')
      M = pd.read_csv(r'C:\Users\Lenovo PC\Desktop\Summary Work - Sheet1.csv', encoding='latin-1')
  

      dataset.userId = dataset.userId.astype('category').cat.codes.values
      dataset.movieId = dataset.movieId.astype('category').cat.codes.values
      M.movieId=M.movieId.astype('category').cat.codes.values
      R=dataset
      
      #content based filtering

      #indices = pd.Series(M.index, index=M['title'])
      #from sklearn.feature_extraction.text import TfidfVectorizer
      #tf = TfidfVectorizer(analyzer='word', ngram_range = (1,2), min_df=0, stop_words='english')
      #tfidf_matrix = tf.fit_transform(M['genres'])

      #from sklearn.metrics.pairwise import linear_kernel
      #cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
      #def genre_recommendations(title):
      #  idx = indices[title]
      #  sim_scores = list(enumerate(cosine_sim[idx]))
      #  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse = True)
      #  sim_scores = sim_scores[1:3]
      # movie_indices = [i[0] for i in sim_scores]
      #  return movie_indices



      M['genres']=M['genres'].str.replace("|" , " ")
      M['Bag_of_words']= M["genres"].astype(str) +" "+ M["summary"].astype(str)
      titles = M['title']
      indices = pd.Series(M.index, index=M['title'])
      M.drop(columns=['summary','genres'])

      from sklearn.feature_extraction.text import TfidfVectorizer
      tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 10),min_df=0, stop_words='english')
      tfidf_matrix = tf.fit_transform(M['Bag_of_words'])
      count = CountVectorizer()
      count_matrix = count.fit_transform(M['Bag_of_words'])
      # generating the cosine similarity matrix
      cosine_sim = cosine_similarity(count_matrix, count_matrix)

      def genre_recommendations(title):
        idx = indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6]
        movie_indices = [i[0] for i in sim_scores]
        return movie_indices



      list1=[]
      for i in range(0,3):
        a = genre_recommendations(movies[i])
        b = M[a[0]:a[0]+1].title.values[0]
        c = M[a[1]:a[1]+1].title.values[0]
        d = M[a[2]:a[2]+1].title.values[0]
        e = M[a[3]:a[3]+1].title.values[0]
        f = M[a[4]:a[4]+1].title.values[0]        
        list1.append(b)
        list1.append(c)
        list1.append(d)
        list1.append(e)
        list1.append(f)


      listnew = [] 
       
      for x in list1:  
        if x not in listnew: 
          listnew.append(x)

      #end of content based flitering
      # selecting the top 10 most rated movies  
      
      listmostfamous2=[]
      listmostfamous1=[]
      for item in range(0, 9724):
        a = R[R['movieId']==item]['rating'].values
        listmostfamous2.append([item,np.mean(a),len(a)])

      for i in range(0, 9724):
        if(listmostfamous2[i][2]>10):
          listmostfamous1.append(listmostfamous2[i])

      def sortSecond(val):
        return val[1]
  
      listmostfamous1.sort(key = sortSecond)
      listmostfamous1.reverse()
      MostRated=[]
      for i in range(len(listmostfamous1)):
        MostRated.append( M[ listmostfamous1[i][0] : listmostfamous1[i][0] + 1].title.values[0] )



      

      #machine learning model
      model = simple_recommend()

      #start of collborative filtering
      
      from math import sqrt
      def pearson_correlation(id1, id2):
        both_rated = {}
        for item in R[R['userId']==id1]['movieId'].values:
          if item in R[R['userId']==id2]['movieId'].values:
            both_rated[item]=1
  
        number_of_ratings = len(both_rated)
  
        if number_of_ratings == 0:
          return 0
        person1_preferences_sum = sum([R[R['userId']==id1][R[R['userId']==id1]['movieId']==item]['rating'].values[0] for item in both_rated])
        person2_preferences_sum = sum([R[R['userId']==id2][R[R['userId']==id2]['movieId']==item]['rating'].values[0] for item in both_rated])
  
  
        person1_square_preferences_sum = sum([pow(R[R['userId']==id1][R[R['userId']==id1]['movieId']==item]['rating'].values[0],2) for item in both_rated])
        person2_square_preferences_sum = sum([pow(R[R['userId']==id2][R[R['userId']==id2]['movieId']==item]['rating'].values[0],2) for item in both_rated])
  
  
  
        product_sum_of_both_users = sum([R[R['userId']==id1][R[R['userId']==id1]['movieId']==item]['rating'].values[0] * R[R['userId']==id2][R[R['userId']==id2]['movieId']==item]['rating'].values[0]  for item in both_rated])
  
        numerator_value = product_sum_of_both_users-(person1_preferences_sum*person2_preferences_sum/number_of_ratings)
  
        denominator_value = sqrt((person1_square_preferences_sum - pow(person1_preferences_sum,2)/number_of_ratings) * (person2_square_preferences_sum -pow(person2_preferences_sum,2)/number_of_ratings))
        if denominator_value == 0:
          return 0
        else:
          r = numerator_value/denominator_value
          return r
        
      movieslist = movies        #movies selected from the select page
      arr=np.zeros((610,5))
      arr1=0
      for i in range(0,610):
        arr[i][0]=i
        for j in range(1,4):
          arr[i][j] =  model.predict([[i],  [M[M['title']==movieslist[j-1]].movieId.values[0]]])
          arr1=arr1+arr[i][j]
        arr[i][4]=arr1
        arr1=0
      alpha=np.argmax(arr, axis=0)      #user who likes these kind of movies
        
      #collaborative filtering  
      def user_recommendations(id1):
        totals={}
        simSums={}
        rankings=[]
        for id in range(0, 610):
          if id1==id:
            continue
          sim=pearson_correlation(id1, id)
          if sim<=0:
            continue
          for item in R[R['userId']==id]['movieId'].values:
            if item not in R[R['userId']==id1]['movieId'].values:
        
              totals.setdefault(item, 0)
              totals[item] = totals[item] + R[R['userId']==id][R[R['userId']==id]['movieId']==item]['rating'].values[0] * sim
              simSums.setdefault(item, 0)
              simSums[item]+=sim
  
        rankings = [(total/simSums[item], item) for item,total in totals.items()]
        rankings.sort()
        rankings.reverse()
        recommendations_list = [M[M['movieId']==recommend_item].title.values[0] for score, recommend_item in rankings]
  
        return recommendations_list


      recommendations_list=[]
      rankings=[]
      answer=[]
      recommendations_list=user_recommendations(alpha[4])
      def sortSecond(val): 
	      return val[1]
      print ("Recommendations for %d"  %alpha[4])
      from sklearn.metrics import mean_absolute_error
      for i in range(0, 10):
        y_hat_2 = np.round(model.predict([[alpha[4]],  [M[M['title']==recommendations_list[i]].movieId.values[0]]]), 0)
      #print(mean_absolute_error(y_true, y_hat_2))
        rankings.append([recommendations_list[i], y_hat_2])
      #print(mean_absolute_error(y_true, model.predict([test.userId, test.movieId])))

      rankings.sort(key = sortSecond)
      rankings.reverse()
      answer=[recommendations_list for recommendations_list, y_hat_2 in rankings]
    
      #combining collaborative and content answers

      listnew.extend(answer)
      z = np.asarray(listnew)  #list into array
      np.random.shuffle(z)   #random shuffling
      final = z.tolist()         #array to list       

      return render_template('shopping.html', final=final)
    
    return render_template('alternatedesign.html')



if __name__ == "__main__":
    app.run(debug=True)