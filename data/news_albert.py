# # Author  : 조익준           
# # Contact : harry960629@naver.com  
# # Date    : 2022-10-26(수)



# # Required Modules
# import tokenization_kbalbert as tk

# from transformers          import AlbertForSequenceClassification
# from transformers          import pipeline



# # 토크나이저 설정
# tokenizer = tk.KbAlbertCharTokenizer.from_pretrained('lww7438/news_albert', use_auth_token=True)

# # 모델 설정
# model = AlbertForSequenceClassification.from_pretrained('lww7438/news_albert', use_auth_token=True)

# # 뉴스 분류 파이프라인 설정
# news_classifier = pipeline(
#   'sentiment-analysis',
#   model=model.cpu(),
#   tokenizer=tokenizer,
#   framework='pt'
# )



# # Functions
# def get_score(news_head:str):
#   """
#   뉴스 헤드라인을 받아 모델을 거쳐 호재, 악재 확률을 반환한다.

#   [Parameters]
#   news_head (str) : 뉴스 헤드라인

#   [Returns]
#   float : 호재/악재 확률 [-1.0, +1.0]
#   """

#   score = 0 # score 초기화
#   # 모델 결과 저장 후 호재(+), 악재(-)에 따라 확률 반환
  
#   results = news_classifier(news_head)

#   for r in results:
#     if r['label'] == 'LABEL_1':
#       score = r['score']
#     else:
#       score = -r['score']

#   return score
  