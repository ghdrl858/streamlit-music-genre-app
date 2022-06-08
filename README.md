# 🎶 streamlit-music-genre-app
✔️ 주제 선정에서 음악 관련 데이터를 생각하다가 찾아보니 음악 관련 데이터가 있어서 주제를 선정했습니다.

✔️ tempo, key, mode, valence 등 많은 컬럼들이 음악 장르에 얼마나 영향을 주는가가 궁금해 예측해보기로 결정했습니다.

✔️ 'music_genre.csv' 파일과 데이터 작업 도움은 아래 출처에서 도움을 받았습니다.
 
➡️ 출처 : https://www.kaggle.com/datasets/vicsuperman/prediction-of-music-genre

# 📚 Use the Library

- ### streamlit_option_menu
  ##### - 옵션 메뉴를 사용을 위해 설치.

```python
pip install streamlit-option-menu
```
- ### plotly.express
  ##### - 반응적인 그래프를 그리기 위해 설치 및 업데이트.
```python
pip install plotly

pip install plotly --update
```

- ### matplotlib.pyplot
  ##### - 함수를 사용해 그래프사용하기 위해 설치.
```python
pip install matplotlib
```

# 📄 Dataset Columns
#### 1. popularity : 인기도를 나타냅니다.

#### 2. acousticness : 음향의 정도를 나타냅니다.

#### 3. danceability : 무용성을 나타냅니다.

#### 4. duration_ms : 지속시간을 나타내며 단위는 ms입니다.

#### 5. energy : 에너지를 나타냅니다.

#### 6. key : A, A#, B와 같은 키를 의미합니다.

#### 7. mode : 'major' 와 'miner' 를 의미합니다.

#### 8. tempo : 음악의 빠르기를 의미합니다.

#### 9. music_genre : 음악의 장르를 의미합니다.

# 🗒️ Explanation
- ### app_home.py
✔️ 짧은 기타영상 하나를 추가해 이 웹 대시보드가 음악과 관련있음을 표현했습니다.  

![app_Mhome](https://user-images.githubusercontent.com/105832443/172642733-369eb1ff-725c-4a30-a573-aa45321356d0.png)

- ### app_eda.py
✔️ *multiselect* 를 이용해 여러 컬럼을 선택 후 데이터를 확인할 수 있게 만들었습니다.

✔️ *seaborn* 라이브러리에 그래프와 *matplotlib.pyplot* 라이브러리에 그래프를 같이 사용했습니다.

![app_eda](https://user-images.githubusercontent.com/105832443/172643595-ddacea7c-708a-4399-bfb0-1a5a86a8df1a.png)

![app_eda2](https://user-images.githubusercontent.com/105832443/172643620-91e807cc-a962-445d-95f3-f1b9318b9594.png)

![app_eda3](https://user-images.githubusercontent.com/105832443/172644722-366a3412-b3f1-4ea5-959f-18218507fd00.png)


- ### app_ml.py
✔️ 인공지능학습 시킨 결과를 보여주는 페이지입니다.

✔️ 인공지능 모델링은 GridSearchCV을 이용했습니다.  
> 정확도는 75%가 나왔습니다.

✔️ 실제값과 예측값을 heatmap 그래프로 표현했으며 수평은 실제값, 수직은 예측값을 뜻합니다.

- precision(정밀도) : 'precision이 높다' 에 의미는 알고리즘이 관련있는 결과를 그렇지 못한것 대비 충분히 맞추었다는 의미로 볼 수 있습니다.
> TP(True Positive, 실제 True -> 예측 True(정답)) 개수를 TP + FP(False Positive, 실제 False -> 예측 True(오답)) 나눈 값.

- recall(재현율) : 실제 True인 것 중에서 모델이 True라고 예측한 것의 비율입니다. 
> TP(True Positive)개수를 TP+FN(False negative, 실제 True -> 예측 False(오답))로 나눈 값.

- f1-score : F1 score는 Precision과 Recall의 조화평균입니다.

![app_Mml](https://user-images.githubusercontent.com/105832443/172646648-dacad3c7-294d-4fb9-bec7-68ab6c85fe9f.png)

![app_Mml2](https://user-images.githubusercontent.com/105832443/172646894-ae6db384-236a-4231-afa1-458e82537bc2.png)

💻 작업진행률  
✔️ 1일차 : 'music_genre.csv' 파일을 받아 데이터를 정리하는 작업을 'Google Colab' 을 통해 간단한 info 확인 및 통계, 각 컬럼의 값을 통한 그래프 작업을 진행했습니다.

✔️ 2일차 : 인공지능학습을 위해 모델링 선정 및 예측값 추출, 실제값 / 예측값을 이용한 heatmap 그래프를 작업했습니다.

✔️ 3일차 : VSC(Visual Studio Code)를 이용해 'Streamlit' 시각화 작업을 했습니다.

✔️ 4일차 : VSC로 작업한 'Streamlit' 을 웹 대시보드로 출력해 결과를 확인하고, 추가적인 수정작업을 거쳐 완성했습니다.
