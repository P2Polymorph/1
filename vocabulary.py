# -*- coding: utf-8 -*-
"""
База слов HSK1, разбитая по темам
Каждое слово содержит: китайский иероглиф, пиньинь, перевод
"""

VOCABULARY = {
    "greeting": {
        "name": "Приветствие (问候)",
        "words": [
            {"chinese": "你好", "pinyin": "nǐ hǎo", "translation": "здравствуйте, привет"},
            {"chinese": "您好", "pinyin": "nín hǎo", "translation": "здравствуйте (вежливо)"},
            {"chinese": "再见", "pinyin": "zài jiàn", "translation": "до свидания"},
            {"chinese": "谢谢", "pinyin": "xiè xie", "translation": "спасибо"},
            {"chinese": "不客气", "pinyin": "bú kè qi", "translation": "не за что"},
            {"chinese": "对不起", "pinyin": "duì bu qǐ", "translation": "извините"},
            {"chinese": "没关系", "pinyin": "méi guān xi", "translation": "ничего страшного"},
            {"chinese": "早上好", "pinyin": "zǎo shang hǎo", "translation": "доброе утро"},
            {"chinese": "晚安", "pinyin": "wǎn ān", "translation": "спокойной ночи"},
        ]
    },
    "communication": {
        "name": "Общение (交流)",
        "words": [
            {"chinese": "是", "pinyin": "shì", "translation": "быть, являться"},
            {"chinese": "不是", "pinyin": "bú shì", "translation": "не быть"},
            {"chinese": "有", "pinyin": "yǒu", "translation": "иметь, есть"},
            {"chinese": "没有", "pinyin": "méi yǒu", "translation": "не иметь, нет"},
            {"chinese": "在", "pinyin": "zài", "translation": "находиться, в"},
            {"chinese": "吗", "pinyin": "ma", "translation": "вопросительная частица"},
            {"chinese": "什么", "pinyin": "shén me", "translation": "что"},
            {"chinese": "谁", "pinyin": "shéi", "translation": "кто"},
            {"chinese": "哪", "pinyin": "nǎ", "translation": "который"},
            {"chinese": "怎么", "pinyin": "zěn me", "translation": "как"},
            {"chinese": "为什么", "pinyin": "wèi shén me", "translation": "почему"},
            {"chinese": "说", "pinyin": "shuō", "translation": "говорить"},
            {"chinese": "问", "pinyin": "wèn", "translation": "спрашивать"},
            {"chinese": "回答", "pinyin": "huí dá", "translation": "отвечать"},
            {"chinese": "知道", "pinyin": "zhī dào", "translation": "знать"},
        ]
    },
    "family": {
        "name": "Семья (家庭)",
        "words": [
            {"chinese": "家", "pinyin": "jiā", "translation": "семья, дом"},
            {"chinese": "爸爸", "pinyin": "bà ba", "translation": "папа"},
            {"chinese": "妈妈", "pinyin": "mā ma", "translation": "мама"},
            {"chinese": "哥哥", "pinyin": "gē ge", "translation": "старший брат"},
            {"chinese": "弟弟", "pinyin": "dì di", "translation": "младший брат"},
            {"chinese": "姐姐", "pinyin": "jiě jie", "translation": "старшая сестра"},
            {"chinese": "妹妹", "pinyin": "mèi mei", "translation": "младшая сестра"},
            {"chinese": "儿子", "pinyin": "ér zi", "translation": "сын"},
            {"chinese": "女儿", "pinyin": "nǚ ér", "translation": "дочь"},
            {"chinese": "人", "pinyin": "rén", "translation": "человек"},
            {"chinese": "我", "pinyin": "wǒ", "translation": "я"},
            {"chinese": "你", "pinyin": "nǐ", "translation": "ты, вы"},
            {"chinese": "他", "pinyin": "tā", "translation": "он"},
            {"chinese": "她", "pinyin": "tā", "translation": "она"},
        ]
    },
    "numbers_time": {
        "name": "Числа и время (数字和时间)",
        "words": [
            {"chinese": "一", "pinyin": "yī", "translation": "один"},
            {"chinese": "二", "pinyin": "èr", "translation": "два"},
            {"chinese": "三", "pinyin": "sān", "translation": "три"},
            {"chinese": "四", "pinyin": "sì", "translation": "четыре"},
            {"chinese": "五", "pinyin": "wǔ", "translation": "пять"},
            {"chinese": "六", "pinyin": "liù", "translation": "шесть"},
            {"chinese": "七", "pinyin": "qī", "translation": "семь"},
            {"chinese": "八", "pinyin": "bā", "translation": "восемь"},
            {"chinese": "九", "pinyin": "jiǔ", "translation": "девять"},
            {"chinese": "十", "pinyin": "shí", "translation": "десять"},
            {"chinese": "百", "pinyin": "bǎi", "translation": "сто"},
            {"chinese": "千", "pinyin": "qiān", "translation": "тысяча"},
            {"chinese": "现在", "pinyin": "xiàn zài", "translation": "сейчас"},
            {"chinese": "今天", "pinyin": "jīn tiān", "translation": "сегодня"},
            {"chinese": "明天", "pinyin": "míng tiān", "translation": "завтра"},
            {"chinese": "昨天", "pinyin": "zuó tiān", "translation": "вчера"},
            {"chinese": "年", "pinyin": "nián", "translation": "год"},
            {"chinese": "月", "pinyin": "yuè", "translation": "месяц"},
            {"chinese": "日", "pinyin": "rì", "translation": "день, число"},
            {"chinese": "号", "pinyin": "hào", "translation": "число (дата)"},
            {"chinese": "点", "pinyin": "diǎn", "translation": "час (времени)"},
            {"chinese": "分", "pinyin": "fēn", "translation": "минута"},
        ]
    },
    "travel": {
        "name": "Путешествие (旅行)",
        "words": [
            {"chinese": "去", "pinyin": "qù", "translation": "идти, ехать"},
            {"chinese": "来", "pinyin": "lái", "translation": "приходить"},
            {"chinese": "回", "pinyin": "huí", "translation": "возвращаться"},
            {"chinese": "到", "pinyin": "dào", "translation": "прибывать, до"},
            {"chinese": "站", "pinyin": "zhàn", "translation": "станция"},
            {"chinese": "机场", "pinyin": "jī chǎng", "translation": "аэропорт"},
            {"chinese": "飞机", "pinyin": "fēi jī", "translation": "самолёт"},
            {"chinese": "火车", "pinyin": "huǒ chē", "translation": "поезд"},
            {"chinese": "出租车", "pinyin": "chū zū chē", "translation": "такси"},
            {"chinese": "公共汽车", "pinyin": "gōng gòng qì chē", "translation": "автобус"},
            {"chinese": "地图", "pinyin": "dì tú", "translation": "карта"},
            {"chinese": "票", "pinyin": "piào", "translation": "билет"},
            {"chinese": "行李", "pinyin": "xíng li", "translation": "багаж"},
        ]
    },
    "food_drink": {
        "name": "Еда и напитки (饮食)",
        "words": [
            {"chinese": "吃", "pinyin": "chī", "translation": "есть, кушать"},
            {"chinese": "喝", "pinyin": "hē", "translation": "пить"},
            {"chinese": "水", "pinyin": "shuǐ", "translation": "вода"},
            {"chinese": "茶", "pinyin": "chá", "translation": "чай"},
            {"chinese": "咖啡", "pinyin": "kā fēi", "translation": "кофе"},
            {"chinese": "米饭", "pinyin": "mǐ fàn", "translation": "рис"},
            {"chinese": "面条", "pinyin": "miàn tiáo", "translation": "лапша"},
            {"chinese": "包子", "pinyin": "bāo zi", "translation": "баоцзы (пельмени на пару)"},
            {"chinese": "饺子", "pinyin": "jiǎo zi", "translation": "цзяоцзы (пельмени)"},
            {"chinese": "水果", "pinyin": "shuǐ guǒ", "translation": "фрукты"},
            {"chinese": "苹果", "pinyin": "píng guǒ", "translation": "яблоко"},
            {"chinese": "香蕉", "pinyin": "xiāng jiāo", "translation": "банан"},
            {"chinese": "菜", "pinyin": "cài", "translation": "блюдо, овощи"},
            {"chinese": "肉", "pinyin": "ròu", "translation": "мясо"},
            {"chinese": "鱼", "pinyin": "yú", "translation": "рыба"},
            {"chinese": "鸡蛋", "pinyin": "jī dàn", "translation": "яйцо"},
        ]
    },
    "places_directions": {
        "name": "Места и направления (地点和方向)",
        "words": [
            {"chinese": "地方", "pinyin": "dì fang", "translation": "место"},
            {"chinese": "这里", "pinyin": "zhè lǐ", "translation": "здесь"},
            {"chinese": "那里", "pinyin": "nà lǐ", "translation": "там"},
            {"chinese": "哪里", "pinyin": "nǎ lǐ", "translation": "где"},
            {"chinese": "上", "pinyin": "shàng", "translation": "верх, на"},
            {"chinese": "下", "pinyin": "xià", "translation": "низ, под"},
            {"chinese": "里", "pinyin": "lǐ", "translation": "внутри"},
            {"chinese": "外", "pinyin": "wài", "translation": "снаружи"},
            {"chinese": "前", "pinyin": "qián", "translation": "перед"},
            {"chinese": "后", "pinyin": "hòu", "translation": "позади"},
            {"chinese": "左", "pinyin": "zuǒ", "translation": "левый"},
            {"chinese": "右", "pinyin": "yòu", "translation": "правый"},
            {"chinese": "中", "pinyin": "zhōng", "translation": "центр, в"},
            {"chinese": "学校", "pinyin": "xué xiào", "translation": "школа"},
            {"chinese": "医院", "pinyin": "yī yuàn", "translation": "больница"},
            {"chinese": "商店", "pinyin": "shāng diàn", "translation": "магазин"},
            {"chinese": "饭馆", "pinyin": "fàn guǎn", "translation": "ресторан"},
            {"chinese": "酒店", "pinyin": "jiǔ diàn", "translation": "отель"},
        ]
    },
    "description": {
        "name": "Описание предметов (描述)",
        "words": [
            {"chinese": "大", "pinyin": "dà", "translation": "большой"},
            {"chinese": "小", "pinyin": "xiǎo", "translation": "маленький"},
            {"chinese": "多", "pinyin": "duō", "translation": "много"},
            {"chinese": "少", "pinyin": "shǎo", "translation": "мало"},
            {"chinese": "好", "pinyin": "hǎo", "translation": "хороший"},
            {"chinese": "不好", "pinyin": "bù hǎo", "translation": "плохой"},
            {"chinese": "贵", "pinyin": "guì", "translation": "дорогой"},
            {"chinese": "便宜", "pinyin": "pián yi", "translation": "дешёвый"},
            {"chinese": "热", "pinyin": "rè", "translation": "горячий, жарко"},
            {"chinese": "冷", "pinyin": "lěng", "translation": "холодный"},
            {"chinese": "忙", "pinyin": "máng", "translation": "занятый"},
            {"chinese": "累", "pinyin": "lèi", "translation": "уставший"},
            {"chinese": "高兴", "pinyin": "gāo xìng", "translation": "радостный"},
            {"chinese": "喜欢", "pinyin": "xǐ huan", "translation": "нравиться"},
            {"chinese": "爱", "pinyin": "ài", "translation": "любить"},
            {"chinese": "想", "pinyin": "xiǎng", "translation": "хотеть, думать"},
            {"chinese": "要", "pinyin": "yào", "translation": "хотеть, нужно"},
            {"chinese": "可以", "pinyin": "kě yǐ", "translation": "можно"},
            {"chinese": "能", "pinyin": "néng", "translation": "мочь"},
            {"chinese": "会", "pinyin": "huì", "translation": "уметь"},
        ]
    },
}

def get_all_words():
    """Возвращает все слова из всех тем"""
    all_words = []
    for topic_key, topic_data in VOCABULARY.items():
        for word in topic_data["words"]:
            word_copy = word.copy()
            word_copy["topic"] = topic_key
            word_copy["topic_name"] = topic_data["name"]
            all_words.append(word_copy)
    return all_words


def get_topic_keys():
    """Возвращает список ключей тем"""
    return list(VOCABULARY.keys())


def get_topic_name(topic_key):
    """Возвращает название темы по ключу"""
    return VOCABULARY.get(topic_key, {}).get("name", "Неизвестная тема")


def get_words_by_topic(topic_key):
    """Возвращает слова по ключу темы"""
    return VOCABULARY.get(topic_key, {}).get("words", [])


def get_total_words_count():
    """Возвращает общее количество слов"""
    return sum(len(data["words"]) for data in VOCABULARY.values())
