# AI 기반 국내 카드 추천 서비스 (AI Card Recommender)

이 프로젝트는 Python Flask와 OpenAI API를 활용하여 사용자의 질문에 맞춰 적합한 국내 신용/체크카드를 추천하는 백엔드 API 서비스입니다.  
카드 데이터(JSON)를 기반으로 AI가 근거 있는 추천 결과를 제공합니다.

---

## 주요 기능

- 카드 데이터 로딩: JSON 파일을 읽어 메모리에 저장합니다.
- AI 맞춤 추천: 사용자의 자연어 쿼리를 기반으로 카드 추천을 수행합니다.
- 추천 근거 설명: 추천 이유와 혜택, 관련 링크를 함께 제공합니다.
- CORS 지원: 프론트엔드 연동을 위한 CORS 설정 포함.

---

## 기술 스택

- Python 3.x  
- Flask  
- Flask-CORS  
- OpenAI API (GPT 기반)

---

## 설치 및 실행

### 1. 필수 라이브러리 설치

```bash
pip install flask flask-cors openai
```

### 2. 데이터 파일 준비

프로젝트 루트에 `국내카드데이터.json` 파일을 배치합니다.

예시:
```json
[
  {
    "card_name": "OO카드",
    "benefits": "스타벅스 50% 할인, 대중교통 10% 적립",
    "link": "https://..."
  }
]
```

### 3. OpenAI API 키 설정

`app.py` 파일에서 API 키 입력:

```python
openai.api_key = "sk-..." 
```

### 4. 서버 실행

```bash
python app.py
```

서버 기본 주소: http://localhost:5000

---

## API 명세

### 카드 추천 API

- Endpoint: `/api/recommend-card`
- Method: POST
- Content-Type: application/json

#### 요청 본문

```json
{
    "query": "20대 대학생이 쓰기 좋은 대중교통 혜택 많은 카드 추천해줘"
}
```

#### 성공 응답

```json
{
    "recommendation": "고객님께 추천드리는 카드는 'OOO 카드'입니다..."
}
```

#### 실패 응답

```json
{
    "error": "Query is missing"
}
```

---

## 주의사항

- OpenAI API 사용 시 비용이 발생할 수 있습니다.
- 데이터 파일이 없거나 형식이 잘못된 경우 서버 실행 오류 또는 500 에러가 발생할 수 있습니다.
- 실제 배포 시 API 키는 코드에 직접 입력하지 말고 환경 변수로 관리하는 것을 권장합니다.

---
