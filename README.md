# 🌲 숲쌤의 비서

> 유아 숲 체험 교육 계획안을 AI로 손쉽게 작성하세요!

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)

## 📖 소개

**숲쌤의 비서**는 유아 숲 지도사와 생태 유아 교육 교사를 위한 AI 기반 교육 계획안 생성 도구입니다. 
Google Gemini API를 활용하여 [누리과정]에 기반한 창의적이고 안전한 숲 체험 교육 계획안을 자동으로 작성해줍니다.

## ✨ 주요 기능

- 🌿 **누리과정 연계**: 5개 영역(신체운동·건강, 의사소통, 사회관계, 예술경험, 자연탐구)에 맞춘 교육 계획
- 🛡️ **맞춤형 안전 수칙**: 계절과 날씨에 맞는 구체적인 안전 지침 제공
- 💬 **교사 발문 팁**: 아이들의 사고를 확장하는 질문 예시 포함
- 🏠 **가정 연계 활동**: 교실/가정에서 연계 가능한 확장 활동 추천
- 📋 **알림장 템플릿**: 학부모용 메시지 자동 생성

## 🚀 시작하기

### 1. 사전 요구사항

- Python 3.8 이상
- Google Gemini API Key ([Google AI Studio](https://aistudio.google.com/)에서 발급)

### 2. 설치

```bash
# 저장소 클론 또는 파일 다운로드 후
cd 20260105

# 의존성 설치
pip install -r requirements.txt
```

### 3. 실행

```bash
streamlit run main.py
```

브라우저에서 `http://localhost:8501`로 접속합니다.

## 📝 사용 방법

1. **사이드바**에서 Gemini API Key를 입력합니다.
2. **모델 선택**: `gemini-2.0-flash` 또는 `gemini-3-pro-preview` 중 선택합니다.
3. **계절/날씨**: 현재 계절과 날씨를 입력합니다. (예: "겨울, 눈 온 뒤 맑은 날")
4. **대상 연령**: 만 3세, 4세, 5세, 혼합 중 선택합니다.
5. **핵심 주제**: 숲 활동의 주제를 입력합니다. (예: "낙엽 놀이", "곤충 관찰")
6. **"계획안 생성하기"** 버튼을 클릭합니다.

## 📂 프로젝트 구조

```
20260105/
├── main.py           # Streamlit 메인 애플리케이션
├── requirements.txt  # Python 의존성 목록
└── README.md         # 프로젝트 설명서
```

## 🤖 지원 모델

| 모델 | 설명 |
|------|------|
| `gemini-2.0-flash` | 빠른 응답 속도, 일반적인 사용에 적합 |
| `gemini-3-pro-preview` | 더 정교한 응답, 복잡한 계획안에 적합 |

## 📋 생성되는 계획안 구성

```markdown
## 🌿 [제목: {계절}의 숲, {주제}와 함께 놀아요]

### 1. 활동 개요
- 대상, 날씨 및 환경, 누리과정 요소

### 2. 오늘의 안전 약속 (Safety First)
- 날씨와 지형을 고려한 핵심 수칙 3가지

### 3. 활동 시나리오
- [도입] 숲과 인사하기 (10분)
- [전개] 주제 탐색 및 놀이 (40분)
- [정리] 느낌 나누기 (10분)

### 4. 가정 연계 알림장
- 학부모용 메시지 템플릿
```

## 🔧 기술 스택

- **Frontend**: [Streamlit](https://streamlit.io/)
- **AI Model**: [Google Gemini API](https://ai.google.dev/)
- **Language**: Python 3.x

## 📜 라이선스

이 프로젝트는 교육 목적으로 자유롭게 사용할 수 있습니다.

## 💚 만든 이

숲에서 아이들과 함께하는 모든 선생님들을 응원합니다! 🌲

---

Made with ❤️ for Forest Teachers | 숲쌤의 비서 v1.0
