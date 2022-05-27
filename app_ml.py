import streamlit as st
import seaborn as sns
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import make_scorer, f1_score, accuracy_score, confusion_matrix, classification_report

def run_ml():
    st.header('Music-Genre, ML')

    st.write('''##### 인공지능학습을 통해서 실제와 예측값을 히트맵을 통해 비교합니다.''')
    key_encoder = joblib.load('data/key_encoder.pkl')
    scaler = joblib.load('data/scaler.pkl')
    mode_encoder = joblib.load('data/mode_encoder.pkl')
    model = joblib.load('data/model.pkl')

    music = pd.read_csv('data/music_genre.csv')
    music.reset_index(inplace = True)
    music = music.drop(["index", "instance_id", "track_name", "obtained_date"], axis = 1)

    # 해당 NaN값 제거
    music.drop([10000, 10001, 10002, 10003, 10004], inplace = True)

    # # artist_name에 empty_field에 비중이 높아 제거
    music = music.drop(music[music["artist_name"] == "empty_field"].index)

    # # 아티스트 확인 후 제거
    music.drop("artist_name", axis = 1, inplace = True)

    # # ? 값을 할당하면 정확한 수치 비교가 불가하므로, ? 값이 할당된 모든행을 제거
    music = music.drop(music[music["tempo"] == "?"].index)

    # # tempo의 값을 float으로 type 변환
    music["tempo"] = music["tempo"].astype("float")

    # # 소수점을 반올림해서 정리한다. decimals가 2이므로 소수점 둘째자리에서 반올림한다.
    music["tempo"] = np.around(music["tempo"], decimals = 2)

    # # key와 mode는 문자열로 되어있기 때문에 인코딩을 해야 한다.(LabelEncoder)
    music["key"] = key_encoder.transform(music['key'])
    music["mode"] = mode_encoder.transform(music["mode"])

    # # scaler 피처 스케일링 해준다.
    X_ge = music.drop("music_genre", axis = 1)
    X = scaler.transform(X_ge)

    # # y 기능
    y = music["music_genre"]

    # # 정확도와 테스트 정확도 함수 정의
    def classification_task(estimator, features, labels):
  
        predictions = estimator.predict(features)
        
        st.write(f"Accuracy: {accuracy_score(labels, predictions)}")
        st.write(f"F1 Score: {f1_score(labels, predictions, average = 'weighted')}")
    
    st.dataframe(music)
    st.write("""***""")

    # # 정확도와 테스트 정확도
    st.write('''##### Accuracy는 정확도를 의미, F1 Score는 정밀도와 재현율의 조화 평균을 의미한다.''')
    classification_task(model, X, y)

    st.write("""***""")
    st.write('''º 해당 테이블은 모든 클레스에 정밀, 호출 및 fi 점수를 표시해줍니다.''')
    st.text(classification_report(y, model.predict(X)))
    st.write("""***""")

    # # 행 : 실제 클래스, 열 : 예측 클래스
    # # ex) Alternative 곡을 수직열으로 해석하면, 사실 131곡 중에 Anime가 9곡 Blues가 17곡이라고 예측
    # # 하지만, 수평행 즉, 실제 클래스로 해석하자면 131곡 중에 Anime가 2곡이었고, Blues가 7곡이었다.
    fig = plt.figure()
    sns.heatmap(confusion_matrix(y, model.predict(X)),
        annot = True,
        fmt = ".0f",
        cmap = "vlag",
        linewidths = 2,
        linecolor = "red",
        xticklabels = model.classes_,
        yticklabels = model.classes_)
    st.write('''### Actual values''')
    st.text('''º 실제값과 예측값을 비교하는 Heatmap입니다.
º 수평으로 보면 실제값들의 분포, 수직으로 보면 인공지능이 학습한 예측값을 뜻합니다.''')
    st.pyplot(fig)