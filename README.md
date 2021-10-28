# 빅콘테스트 2021 
---
### 퓨처스리그 ECO제주 : 제주도 음식물 쓰레기양 예측을 통한 배출량 감소 방안 도출
#### 꿈은 없지만 놀고 싶어요
![image](https://user-images.githubusercontent.com/69336270/139187686-8a0e2ec2-a249-46b0-987d-ba4e3df3ad1b.png)

## Structure
---
```python
꿈은 없지만 놀고 싶어요  
├── README.md
├── main.py
├── 데이터분석분야_퓨처스리그_ECO제주_꿈은 없지만 놀고싶어요_결과보고서.pdf
├── 데이터분석분야_퓨처스리그_ECO제주_꿈은 없지만 놀고싶어요_추가제출파일.html
├── raw  
│    └───외부데이터  
│         ├───인구__가구_및_주택__읍면동_2015_2020___시군구_20162019__20210822212745.csv  
│         └───가구원수별_가구_일반가구___읍면동_2015_2020___시군구_20162019__202108230141  36.csv
│   
├── preprocess
│    ├───EDA.py
│    ├───preprocess.py
│    ├───missing_datawig.py
│    ├───correlation.py
│    ├───add_missing_total_data_final.csv
│    ├───add_missing_total_data_final_known.csv
│    ├───total_data_final_unknown_end.csv
│    └───total_data_final_known_end.csv
│    
└── model
     ├───model.py
     ├───visualize.py
     ├───compare_model_건입동.pkl
     │             ...
     ├───compare_model_알수없음.pkl
     ├───model_건입동.pkl
     │            ...
     └───model_알수없음.pkl
```
**main.py** : 전체 파일 실행 코드입니다.    
**EDA.py** : 음식물 쓰레기 배출량에 대한 EDA 코드입니다.   
**preprocess.py** : 데이터 전처리 코드입니다.  
**missing_datawig.py** : Datawig library를 사용해 전처리 데이터 중 결측치를 처리하는 코드입니다.   
**correlation.py** : 모델에 사용할 변수에 대한 상관관계를 확인하는 코드입니다.  
**model.py** : AutoML인 Pycaret을 사용하여 지역별 음식물 쓰레기 배출량 예측 모델을 구축하는 코드입니다.  
**visualize.py** : Pycaret과 Shap를 사용하여 변수 중요도 및 특정 변수와 음식물 쓰레기 배출량과의 관계를 해석하는 코드입니다.  

## Results
---
![image](https://user-images.githubusercontent.com/69336270/139192002-dc05e439-f9ec-4496-99f1-0d5cf7b24b2d.png)
![image](https://user-images.githubusercontent.com/69336270/139191917-75156565-4dea-4676-819d-aed409c92cb2.png)

## Contributors
---
<table>
  <tr>
    <td align="center"><a href="https://github.com/yoonj98"><br /><b>이윤정</b></sub></td>
    <td align="center"><a href="https://github.com/jiwon4178"><br /><b>박지원</b></sub></td>
    <td align="center"><a href="https://github.com/jihyeon4028"><br /><b>박지현</b></sub></td>
    <td align="center"><a href="https://github.com/didwldn3032"><br /><b>양지우</b></sub></td>
</table>

