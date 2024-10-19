synonyms = {
    "삼성전자": ["삼성전자", "삼성 전자", "삼전"],
    "SK하이닉스": ["SK하이닉스", "에스케이하이닉스", "하이닉스", "SK 하이닉스", "에스케이 하이닉스"],
    "LG에너지솔루션": ["LG에너지솔루션", "엘지에너지솔루션", "LG엔솔", "엘지엔솔", "LG 에너지솔루션", "엘지 에너지솔루션"]
}

def find_synonym(word):
    for key, values in synonyms.items():
        if word in values:
            return key
    return word
