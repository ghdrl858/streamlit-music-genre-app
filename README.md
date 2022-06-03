# 🎷🎶 streamlit-music-genre-app

 ✔️ 주제 선정에서 음악 관련 데이터를 생각하다가 찾아보니 음악 관련 데이터가 있어서 주제를 선정했습니다.

 ✔️ tempo, key, mode, valence 등 많은 컬럼들이 음악 장르에 얼마나 영향을 주는가가 궁금해 예측해보기로 결정했습니다.

 ✔️ 데이터 작업은 'Google Colab' 으로 작업했고, 'Streamlit' 사용으로 웹 대시보드를 만들어 시각화하기 위해 'Visual Studio Code' 로 작업한 데이터를 옮기면서 'Streamlit' 에 문법에 맞게 만드는 작업을 했습니다.

 ✔️ 'music_genre.csv' 파일과 데이터 작업 도움은 아래 출처에서 도움을 받았습니다.

 ➡️ 출처 : https://www.kaggle.com/datasets/vicsuperman/prediction-of-music-genre

# 🎼 주요 컬럼 정리
 1) popularity       : 인기도를 나타냅니다.
 2) acousticness     : 음향의 정도를 나타냅니다.
 3) danceability     : 무용성을 나타냅니다.
 4) duration_ms      : 지속시간을 나타내며 단위는 ms입니다.
 5) energy           : 에너지를 나타냅니다.
 7) key              : A, A#, B와 같은 키를 의미합니다.
 8) mode             : 'major' 와 'miner' 를 의미합니다.
 9) tempo            : 음악의 빠르기를 의미합니다.
 10) music_genre     : 음악의 장르를 의미합니다.

# 💻 작업진행률
 ✔️ 1일차 : 'music_genre.csv' 파일을 받아 데이터를 정리하는 작업을 'Google Colab' 을 통해
             
             간단한 info 확인 및 통계, 각 컬럼의 값을 통한 그래프 작업을 진행했습니다.

 ✔️ 2일차 : 인공지능학습을 위해 모델링 선정 및 예측값 추출, 실제값 / 예측값을 이용한
             
             heatmap 그래프를 작업했습니다.

 ✔️ 3일차 : VSC(Visual Studio Code)를 이용해 'Streamlit' 시각화 작업을 했습니다.

 ✔️ 4일차 : VSC로 작업한 'Streamlit' 을 웹 대시보드로 출력해 결과를 확인하고,
            
            추가적인 수정작업을 거쳐 완성했습니다.