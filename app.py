import streamlit as st
import pickle
import pandas as pd
import requests
def fench_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=dde7c1a87618b254af2edd29bf2d6ca8&language=en-US".format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommand(movie):
    mv_index = movies[movies['title'] == movie].index[0]
    distances=similarity[mv_index]
    movielist = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    recommand_mv=[]
    recommand_mv_img=[]
    for i in movielist:
        id=movies.iloc[i[0]].id
        recommand_mv.append(movies.iloc[i[0]].title)
        recommand_mv_img.append(fench_poster(id))
    return recommand_mv,recommand_mv_img
        
movies_dict=pickle.load(open('mv_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommdation System')
option=st.selectbox('Select the movie',movies['title'].values)

if st.button('recommend'):
    names,imgs=recommand(option)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(imgs[0])
    with col2:
        st.text(names[1])
        st.image(imgs[1])
    with col3:
        st.text(names[2])
        st.image(imgs[2])
    with col4:
        st.text(names[3])
        st.image(imgs[3])
    with col5:
        st.text(names[4])
        st.image(imgs[4])