import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run_eda() :
    # 필요없는 컬럼 정리
    music = pd.read_csv('data/music_genre.csv')
    music.reset_index(inplace = True)
    music = music.drop(["index", "instance_id", "track_name", "obtained_date"], axis = 1)

    # artist_name에 empty_field에 비중이 높아 제거
    music = music.drop(music[music["artist_name"] == "empty_field"].index)

    # 컬럼선택으로 해당 컬럼들 확인
    st.write('''##### ***Columns***에 선택을 통해 해당 데이터값을 볼 수 있습니다.''')
    column_list = st.multiselect('Choice Columns',music.columns)
    
    if len(column_list) != 0 :
        st.dataframe(music[column_list])
    st.write("""***""")

    # 빈필드 아티스트 제거 후 20명에 아티스트 선정
    top_20_artists = music["artist_name"].value_counts()[:20].sort_values(ascending = True)

    # 20명에 아티스트 정렬 후, 그래프 표현
    st.write('')
    st.write('')
    st.write('''##### - 많은 ***Artists***중에 정렬해서 20명에 인원만 그래프로 표현했습니다.''')
    st.text('''º 가장 우세한 아티스트는 우에마쓰 노부오로 일본 작곡가이며, 
º 다음은 모두가 아는 모차르트, 베토벤 순으로 정렬했습니다.
    ''')
    music1 = plt.figure()
    plt.barh(top_20_artists.index, top_20_artists, color = 'black', alpha = 0.4)
    plt.xlabel("Number of songs per artist")
    plt.title("Songs per artist")
    st.pyplot(music1)
    st.write("""***""")

    # 주요 컬럼들 그래프
    st.write('')
    # key 컬럼 그래프
    st.write('''##### - ***key***와 관련된 그래프입니다.''')
    st.text('º 기본 음악 코드인 C메이저와 G메이저가 어느 코드보다 월등히 높다는걸 알 수 있습니다.')
    key_ = plt.figure()
    sns.countplot(x = 'key', data = music, palette = "ocean", order = None)
    plt.title(f"Counts in each {'key'}")
    st.pyplot(key_)
    st.write("""***""")

    # mode 컬럼 그래프
    st.write('''##### - ***mode***와 관련된 그래프입니다.''')
    st.text('º 어두운 단조보다는 밝은 장조에 노래가 많음을 확인 할 수 있습니다.')
    mode_ = plt.figure()
    sns.countplot(x = 'mode', data = music, palette = "ocean", order = None)
    plt.title(f"Counts in each {'mode'}")
    st.pyplot(mode_)
    st.write("""***""")

    # music_genre 컬럼 그래프
    st.write('''##### - ***music_genre***와 관련된 그래프입니다.''')
    st.text('º 그래프를 통해 각 장르가 동등하게 표현됨을 확인할 수 있습니다.')
    genre_ = plt.figure()
    sns.countplot(x = 'music_genre', data = music, palette = "ocean", order = None)
    plt.title(f"Counts in each {'music_genre'}")
    st.pyplot(genre_)