# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VOZsQranxGwvraJns05XuDvFAETQ5aP3

## ECO 제주 음식물 쓰레기 예측모델 실행 파일
#### 꿈은 없지만 놀고 싶어요
빅콘테스트 2021 데이터분석 분야 ECO제주 - 음식물 쓰레기 배출량 예측모델의 실행파일입니다.

### Step0. 환경설정
전처리부터 데이터 예측까지의 과정에서 필요한 라이브러리 환경을 구축합니다.
"""

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

"""### Step1. EDA
데이터 EDA를 위한 EDA.py을 실행하기 위해 preprocessing 폴더로 이동합니다.

"""

# Commented out IPython magic to ensure Python compatibility.
# %cd preprocess

"""#### Step1-1. EDA.py 파일을 실행합니다. """

!python EDA.py

"""### Step2. Preprocessing
모델 구축에 사용되는 내부 데이터와 외부 데이터에 대한 데이터 전처리를 실행합니다.
"""

!python preprocess.py

"""#### Stemp2-1. 결측치 처리
data imputation 라이브러리인 datawig를 활용해 제주시와 서귀포시에 해당하는 데이터 결측치를 채웁니다.
"""

install_and_import('datawig')
!python missing_datawig.py

"""#### Step2-2.상관관계
변수 간의 상관관계를 파악합니다.
"""

!python correlation.py

"""### Step3. Modeling & Predict
모델링 및 데이터 예측을 위한 model.py을 실행하기 위해 model 폴더로 이동합니다. 
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd ../model

"""#### Step3-1. model.py 파일을 실행합니다.
구축된 모델 파일들은 model 폴더에 저장되며, 모델을 통해 예측된 음식물 쓰레기 배출량 데이터는 predict 폴더에 저장됩니다. 
"""

!pip install -U imbalanced-learn

pip install pycaret

install_and_import('pycaret')
install_and_import('shap')
!python model.py

"""### Step4. Visualize
제주도 전지역의 음식물 쓰레기 배출량에 영향을 주는 요인을 파악하기 위해 2018-01-01 ~ 2021-06-30 데이터를 기반으로 예측 모델 및 Shap를 통한 모델 해석을 진행하였습니다.
"""

!python visualize.py