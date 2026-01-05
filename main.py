import streamlit as st
from google import genai

# 페이지 설정
st.set_page_config(
    page_title="숲쌤의 비서",
    page_icon="🌲",
    layout="wide"
)

# 시스템 프롬프트
SYSTEM_PROMPT = """# Role Definition
당신은 20년 경력의 베테랑 '유아 숲 지도사'이자 '생태 유아 교육 전문가'입니다. 
당신의 목표는 현장 교사들을 위해 [누리과정]에 기반한 창의적이고 안전하며, 
무엇보다 아이들의 주도성이 살아있는 '숲 체험 교육 계획안'을 작성하는 것입니다.

# Tone & Manner
1. 전문적이지만 따뜻하게: 교사에게 선배가 조언하듯 친절하고 격려하는 어조를 사용하세요.
2. 감각적 묘사: 숲의 날씨, 질감, 소리를 생생하게 묘사하세요.
3. 실용성 최우선: 뜬구름 잡는 이론 대신, 당장 숲에서 쓸 수 있는 구체적인 놀이 방법을 제시하세요.

# Generation Rules (반드시 지킬 것)
1. [누리과정 연계]: 활동이 누리과정의 5개 영역(신체운동·건강, 의사소통, 사회관계, 예술경험, 자연탐구) 중 어디에 해당하는지 명시하세요.
2. [맞춤형 안전 수칙]: 입력된 '날씨'와 '계절'에 딱 맞는 구체적인 안전 지침을 포함하세요. (예: 비 오는 날은 미끄러운 이끼 주의, 가을엔 뱀/벌 주의)
3. [교사의 발문(Teacher's Talk)]: 활동 중간중간 아이들의 사고를 확장할 수 있는 매력적인 질문 예시를 3개 이상 포함하세요.
4. [확장 활동]: 숲 활동 후 교실이나 가정에서 연계할 수 있는 간단한 활동을 추천하세요.

# Output Format (Markdown)
## 🌿 [제목: {계절}의 숲, {주제}와 함께 놀아요]

### 1. 활동 개요
- **대상:** {연령}
- **날씨 및 환경:** {날씨}
- **누리과정 요소:** (관련 영역 및 내용 기술)

### 2. 오늘의 안전 약속 (Safety First)
- (날씨와 지형을 고려한 핵심 수칙 3가지)

### 3. 활동 시나리오
**[도입: 숲과 인사하기] (10분)**
- 마음 열기 활동 및 주의 집중

**[전개: {주제} 탐색 및 놀이] (40분)**
- 메인 활동 (오감을 활용한 놀이 구체적 서술)
- 💡 **선생님의 발문 팁:** "아이들에게 이렇게 물어보세요!"

**[정리: 느낌 나누기] (10분)**
- 활동 회상 및 자연물 제자리에 돌려주기

### 4. 가정 연계 알림장 (복사해서 바로 쓰세요!)
- (학부모님께 보내는 정중하고 감성적인 요약 메시지)
"""

# 사이드바 - API Key 입력
st.sidebar.title("🔐 API 설정")
api_key = st.sidebar.text_input(
    "Gemini API Key",
    type="password",
    placeholder="API Key를 입력하세요"
)

# 모델 선택
model_option = st.sidebar.selectbox(
    "🤖 모델 선택",
    options=["gemini-3-pro-preview", "gemini-2.5-flash", "gemini-2.0-flash"],
    index=0
)

# 메인 화면
st.title("🌲 숲쌤의 비서")
st.markdown("*유아 숲 체험 교육 계획안을 손쉽게 작성하세요!*")
st.divider()

# 입력 폼
col1, col2 = st.columns(2)

with col1:
    season_weather = st.text_input(
        "🌤️ 계절/날씨",
        placeholder="예: 가을, 맑고 선선한 날씨"
    )

with col2:
    target_age = st.selectbox(
        "👶 대상 연령",
        options=["만 3세", "만 4세", "만 5세", "혼합"]
    )

core_topic = st.text_input(
    "🌿 핵심 주제",
    placeholder="예: 낙엽, 도토리, 나무 관찰"
)

st.divider()

# 계획안 생성 버튼
if st.button("📝 계획안 생성하기", type="primary", use_container_width=True):
    # 입력 검증
    if not api_key:
        st.error("⚠️ 사이드바에서 Gemini API Key를 입력해주세요!")
    elif not season_weather:
        st.warning("계절/날씨를 입력해주세요.")
    elif not core_topic:
        st.warning("핵심 주제를 입력해주세요.")
    else:
        # Gemini API 설정
        try:
            client = genai.Client(api_key=api_key)
            
            # 사용자 입력 데이터 구성
            user_input = f"""# User Input Data
- 계절/날씨: {season_weather}
- 대상 연령: {target_age}
- 핵심 주제: {core_topic}

위 정보를 바탕으로 숲 체험 교육 계획안을 작성해주세요."""

            # 전체 프롬프트 구성
            full_prompt = SYSTEM_PROMPT + "\n\n" + user_input

            # API 호출
            with st.spinner("🌲 숲쌤이 계획안을 작성하고 있어요..."):
                response = client.models.generate_content(
                    model=model_option,
                    contents=full_prompt
                )
                
                # 결과 출력
                st.success("✅ 계획안이 생성되었습니다!")
                st.divider()
                st.markdown(response.text)
                
                # 다운로드 버튼
                st.download_button(
                    label="💾 계획안 다운로드받기",
                    data=response.text,
                    file_name="숲체험_계획안.md",
                    mime="text/markdown"
                )
                
        except Exception as e:
            st.error(f"❌ 오류가 발생했습니다: {str(e)}")

# 푸터
st.divider()
st.caption("Made with ❤️ for Forest Teachers | 숲쌤의 비서 v1.0")
