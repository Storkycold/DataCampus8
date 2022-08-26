# DataProject
데이터청년캠퍼스_8조

## 아동상담을 위한 맞춤형 컬러링 도안 제공 서비스(text_to_coloringpages)

아동 내담자의 발화를 기반으로 맞춤형 컬러링 도안을 실시간으로 제공합니다.
본 도안을 활용한 컬러링 활동이 내담자와 상담자의 원활한 상호작용을 유도하는 ‘마음 마중물’의 역할을 수행할 것입니다.

프로젝트의 개괄은 text-to-coloringpages.pptx 를 통해 확인하실 수 있습니다.

## 서비스 프로세스 설명
(image)

##모델 설명

#T.C.CLIP (text_to_images)

CLIP모델에 unsplash 데이터셋을 추가하고, Trigram KeyBERT를 활용해 실시간 crawling을 진행해 이미지를 추가함.

(image)

#Coloring processor (images_to_coloringpages)

pix2pix를 바탕으로 전처리와 후처리 코드를 추가했습니다.

(image)

pix2pix에 관한 자세한 사항은 pix2pix 폴더 pix2pix 에 업로드된 Colab Notebooks 파일을 통해 확인할 수 있습니다.
ReadMe_Pix2Pix 파일에서 구조 및 학습의 순서를 확인할 수 있으며 모델 생성 및 학습의 과정은 나머지 .ipynb 파일을 순서대로 보시면 확인할 수 있습니다.


## 본 전체 모델을 사용방법
모델 중 중간 images로 illustration을 추출하는 경우는 [final]_text_to_coloring_pages(1).ipynb를 통해,
real photo를 추출하는 경우는 [final]_text_to_coloring_pages(2).ipynb를 통해 전체 모델을 사용하는 방법을 확인하실 수 있습니다.

실제로 텍스트를 넣어 결과물을 내보고 싶으신 경우에는 해당 파일의 Open in Colab 버튼을 통해 Colab Notebook에서 실행해보실 수 있습니다.


# 공부와 모델 생성에 활용한 논문 및 코드는 다음과 같음
(논문)

(깃허브 코드)

