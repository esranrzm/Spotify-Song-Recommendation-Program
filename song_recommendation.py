# -*- coding: utf-8 -*-
"""song_recommendation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZyowzJyBz0dGYjvXIhU1o-efN-wrbfe0

#Visualizations of Aggregated Forms Based on Features

* So far, we examined how the features of songs and features of the genres changed over the years. Now by using proper methods we can compare these changes.
* Below you will see the comparisons of two different features of songs.
"""

#change in the danceability and energy over the years

plt.figure(figsize=(12, 4))
sns.set(style="whitegrid")
columns = ["danceability","energy"]
for col in columns:
    x = first_data.groupby("year")[col].mean()
    ax= sns.lineplot(x=x.index,y=x,label=col)
ax.set_title('dancebility vs energy')
ax.set_ylabel('Count')
ax.set_xlabel('Year')


#change in the acousticness and energy over the years
plt.figure(figsize=(12, 4))
sns.set(style="whitegrid")
columns = ["acousticness","energy"]
for col in columns:
    x = first_data.groupby("year")[col].mean()
    ax= sns.lineplot(x=x.index,y=x,label=col)
ax.set_title('acousticness vs energy')
ax.set_ylabel('Count')
ax.set_xlabel('Year')


#change in the instrumentalness and energy over the years
plt.figure(figsize=(12, 4))
sns.set(style="whitegrid")
columns = ["instrumentalness","energy"]
for col in columns:
    x = first_data.groupby("year")[col].mean()
    ax= sns.lineplot(x=x.index,y=x,label=col)
ax.set_title('instrumentalness vs energy')
ax.set_ylabel('Count')
ax.set_xlabel('Year')


#change in the loudness and energy over the years
plt.figure(figsize=(12, 4))
sns.set(style="whitegrid")
columns = ["instrumentalness","acousticness"]
for col in columns:
    x = first_data.groupby("year")[col].mean()
    ax= sns.lineplot(x=x.index,y=x,label=col)
ax.set_title('instrumentalness vs acousticness')
ax.set_ylabel('Count')
ax.set_xlabel('Year')

#change in the speechiness and liveness over the years
plt.figure(figsize=(12, 4))
sns.set(style="whitegrid")
columns = ["speechiness","liveness"]
for col in columns:
    x = first_data.groupby("year")[col].mean()
    ax= sns.lineplot(x=x.index,y=x,label=col)
ax.set_title('speechiness vs liveness')
ax.set_ylabel('Count')
ax.set_xlabel('Year')
;

"""### Making some comments on comparisons

  * When we look at the first graph, both features have increased after the year they started. However, energy increased much more than dancebility.


  *  If we look for the second graph, the features have an opposite progression from each other. While the acoustics decreased from the year it started, the energy has been increasing since the year it started.

  * When we look at the third graph, the features that had very close values between the years 1930-1960 diverged from each other after 1960. The energy has increased continuously and has reached a much higher point than when it started. Instrumentalness first decreased, then increased again to a point close to its original value.

  * When we look at fourth graph, acoustics had a fluctuated graphic until 1960. After 1960, the value of acoustics started to decline and comes to the same value with the instrumentalness that we compare with acoustics. Instrumentalness reaches almost the same value it started after its fluctuated graphic until today.

  * When we look at fifth graph, while speechless has a fluctuated graphic between 1920-1960, it has not changed much after 1960 and has a value slightly higher than the value it started with when it came to the present day. Liveness, on the other hand, has a graphic that does not have large fluctuations, unlike speechless. However, when the starting value is compared with the current value, there is a decrease. When the values of both features are compared, liveness has a higher value than speechless.


---

## Comparing Multiple Datas
* As we did in the previous code cells, we will compare multiple features of the songs by using only one box.

* This will help us to understand the differences among features better.

* As you see below, over the years, the song became more energetic and less acoustic. On the other hand, there is not a huge change in the level of valance, liveness, and danceability of the songs over the years.

* The fluctuation in the speechiness became more stable towards 2020.
"""

#audio characteristics over years

plt.figure(figsize=(16, 10))
sns.set(style="whitegrid")
columns = ["acousticness","danceability","energy","speechiness","liveness"]
for col in columns:
    x = data_for_years.groupby("year")[col].mean()
    ax= sns.lineplot(x=x.index,y=x,label=col)
ax.set_title('Change in Audio characteristics over years')
ax.set_ylabel('Measure')
ax.set_xlabel('Year')
;

"""---



---



---

## Analysing distribution of attributes for songs dataset

* So far we examined the distribution of song's features over the years and the distributions of genre's features over the years.

* This time we will visualize our data with respect to the artists. We will examine how the features of an artists' songs changed over the years.

* Our data that is shown below has similar columns with other data that we examined before.

        ['artists', 'acousticness', 'danceability', 'duration_ms', 'energy',
         'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo',
         'valence', 'popularity', 'key', 'mode', 'count']
"""

data_for_artist.hist(figsize=(20, 20),color='g', edgecolor='black')
plt.show()

"""* We can also look at the artists who made thousands of songs in their careers.
  * As you can see below, the first 30 artists are listed in order.

## Efforts on hyper-parameter tuning to increase the performance of models

* We will use decision tree model as an example
* As we did in the recitation, we will play with the max_depth of our tree to increase the performance of our model
"""

decisionTree_Model.get_params()

max_depth_values = np.arange(1, 15)

acc_training_scores = []
acc_val_scores = []

for max_depth in max_depth_values:
  model = DecisionTreeClassifier(max_depth=max_depth)
  model.fit(X_train,y_train)

  y_pred_training = model.predict(X_train)
  y_pred_val = model.predict(X_valid)

  acc_training = accuracy_score(y_train, y_pred_training)
  acc_val = accuracy_score(y_valid, y_pred_val)

  acc_training_scores.append(acc_training)
  acc_val_scores.append(acc_val)

"""* Now, our max_depth value is changed from none to a number
* From now on we can set its value
"""

model.get_params()

model = DecisionTreeClassifier(max_depth=4)

model.fit(X_train, y_train)

from sklearn.model_selection import cross_val_score

accuracies = cross_val_score(model, X_train, y_train, cv=5, scoring="accuracy")
accuracies

"Accuracy: {:.2f} (+/- {:.2f})".format(accuracies.mean(), accuracies.std() * 2)

"""* With hyper-parameter tuning, we incresed the performance of our model and we got a better accuracy value which is 0.88"""

# tree plot function
from sklearn.tree import plot_tree

# generate the tree
fig = plt.figure(figsize=(35, 15))
plot_tree(model, feature_names=X_test.columns.values, class_names=["not popular", "popular"], filled=True);

"""## Creating a simple song recommendation system

* In this part of the project, we will implement a basic song recommendation program
* To acieve this, we will use manhattan distance to find the KNN of the given song
* After that, we will sort them according to their distance value to our source song
"""

from tqdm import tqdm
recommended_data = first_data

class SpotifyRecommender():
    def __init__(self, rec_data):
        #our class should understand which data to work with
        self.rec_data_ = rec_data
    
    #if we need to change data
    def change_data(self, rec_data):
        self.rec_data_ = rec_data
    
    #function which returns recommendations, we can also choose the amount of songs to be recommended
    def get_recommendations(self, song_name, amount=1):
        distances = []
        #choosing the data for our song
        song = self.rec_data_[(self.rec_data_.name.str.lower() == song_name.lower())].head(1).values[0]
        #dropping the data with our song
        res_data = self.rec_data_[self.rec_data_.name.str.lower() != song_name.lower()]
        for r_song in tqdm(res_data.values):
            dist = 0
            for col in np.arange(len(res_data.columns)):
                #indeces of non-numerical columns
                if not col in [1, 6, 12, 14, 18]:
                    #calculating the manhettan distances for each numerical feature
                    dist = dist + np.absolute(float(song[col]) - float(r_song[col]))
            distances.append(dist)
        res_data['distance'] = distances
        #sorting our data to be ascending by 'distance' feature
        res_data = res_data.sort_values('distance')
        columns = ['artists', 'name']
        return res_data[columns][:amount]

recommend_machine = SpotifyRecommender(recommended_data)

"""* Here are a couple of example runnings"""

recommend_machine.get_recommendations('champagne problems', 5)

recommend_machine.get_recommendations('Girls Like You (feat. Cardi B)', 5)

recommend_machine.get_recommendations('drivers license', 5)