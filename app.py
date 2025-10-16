from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
import json

app = Flask(__name__)
CORS(app)

openai.api_key = ""


def load_card_data_from_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        pretty_string = json.dumps(data, indent=2, ensure_ascii=False)
        print("✅ Card data loaded successfully from .json file.")
        return pretty_string
    except Exception as e:
        print(f"🛑 ERROR: Could not read the json file '{file_path}'. Error: {e}")
        return "Error: 카드 정보를 불러올 수 없습니다. 관리자에게 문의하세요."

CARD_DATA_FILE = "국내카드데이터.json"
CARD_DATA = load_card_data_from_json(CARD_DATA_FILE)


@app.route('/api/recommend-card', methods=['POST'])
def recommend_card():
    data = request.get_json()
    user_query = data.get('query')

    if not user_query:
        return jsonify({'error': 'Query is missing'}), 400

    if "Error:" in CARD_DATA:
        return jsonify({'error': CARD_DATA}), 500

    try:
        system_prompt = f"""
        당신은 국내 카드 회사의 친절한 카드 추천 전문가입니다.
        아래에 제공되는 JSON 형식의 카드 정보를 바탕으로 사용자의 질문에 가장 적합한 카드를 추천해야 합니다.
        추천할 때는 반드시 그 이유를 명확하고 이해하기 쉽게 설명해주세요.
        카드 정보에 없는 내용은 절대로 언급해서는 안 됩니다.
        설명 끝에 해당하는 카드 링크 첨부 해주셔야 합니다.
        중요! 여러개의 카드를 추천하실때는 무조건 개행을 2번정도 하시고 다음 카드 추천해야합니다.

        --- 카드 정보 (JSON) ---
        {CARD_DATA}
        -----------------------
        """
        
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            temperature=0.7
        )

        ai_response = response.choices[0].message.content
        return jsonify({'recommendation': ai_response})

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'AI 추천을 생성하는 중 오류가 발생했습니다.'}), 500
