# -*- coding: utf-8 -*-
"""
Модуль викторины для тренажёра китайского языка
Содержит классы и функции для проведения тестирования
"""

import random
from vocabulary import VOCABULARY, get_words_by_topic, get_all_words, get_topic_name


class QuizQuestion:
    """Класс вопроса викторины"""
    
    def __init__(self, word, question_type):
        self.word = word
        self.question_type = question_type
        self.correct_answer = None
        self.options = []
        self.question_text = ""
        
    def generate(self, all_words):
        """Генерирует вопрос и варианты ответов"""
        if self.question_type == "chinese_to_translation":
            self._generate_chinese_to_translation(all_words)
        elif self.question_type == "translation_to_chinese":
            self._generate_translation_to_chinese(all_words)
        elif self.question_type == "pinyin_to_chinese":
            self._generate_pinyin_to_chinese(all_words)
        elif self.question_type == "chinese_to_pinyin":
            self._generate_chinese_to_pinyin(all_words)
            
    def _generate_chinese_to_translation(self, all_words):
        """Вопрос: китайский → перевод"""
        self.question_text = f"Что означает слово «{self.word['chinese']}»?"
        self.correct_answer = self.word["translation"]
        
        # Генерируем неправильные ответы
        wrong_answers = [
            w["translation"] for w in all_words 
            if w["translation"] != self.correct_answer
        ]
        wrong_options = random.sample(wrong_answers, min(3, len(wrong_answers)))
        self.options = wrong_options + [self.correct_answer]
        random.shuffle(self.options)
        
    def _generate_translation_to_chinese(self, all_words):
        """Вопрос: перевод → китайский"""
        self.question_text = f"Как будет по-китайски «{self.word['translation']}»?"
        self.correct_answer = self.word["chinese"]
        
        wrong_answers = [
            w["chinese"] for w in all_words 
            if w["chinese"] != self.correct_answer
        ]
        wrong_options = random.sample(wrong_answers, min(3, len(wrong_answers)))
        self.options = wrong_options + [self.correct_answer]
        random.shuffle(self.options)
        
    def _generate_pinyin_to_chinese(self, all_words):
        """Вопрос: пиньинь → китайский"""
        self.question_text = f"Какой иероглиф соответствует пиньинь «{self.word['pinyin']}»?"
        self.correct_answer = self.word["chinese"]
        
        wrong_answers = [
            w["chinese"] for w in all_words 
            if w["chinese"] != self.correct_answer
        ]
        wrong_options = random.sample(wrong_answers, min(3, len(wrong_answers)))
        self.options = wrong_options + [self.correct_answer]
        random.shuffle(self.options)
        
    def _generate_chinese_to_pinyin(self, all_words):
        """Вопрос: китайский → пиньинь"""
        self.question_text = f"Выберите правильный пиньинь для «{self.word['chinese']}»:"
        self.correct_answer = self.word["pinyin"]
        
        wrong_answers = [
            w["pinyin"] for w in all_words 
            if w["pinyin"] != self.correct_answer
        ]
        wrong_options = random.sample(wrong_answers, min(3, len(wrong_answers)))
        self.options = wrong_options + [self.correct_answer]
        random.shuffle(self.options)
        
    def check_answer(self, user_answer):
        """Проверяет ответ пользователя"""
        return user_answer == self.correct_answer


class QuizSession:
    """Класс сессии викторины"""
    
    def __init__(self, topic_keys=None, question_types=None, num_questions=10):
        """
        Инициализация сессии викторины
        
        Args:
            topic_keys: список тем для викторины (None = все темы)
            question_types: типы вопросов (None = все типы)
            num_questions: количество вопросов в сессии
        """
        self.topic_keys = topic_keys or list(VOCABULARY.keys())
        self.question_types = question_types or [
            "chinese_to_translation",
            "translation_to_chinese",
            "pinyin_to_chinese",
            "chinese_to_pinyin"
        ]
        self.num_questions = num_questions
        self.questions = []
        self.current_question_index = 0
        self.score = 0
        self.answers_history = []
        
        # Собираем слова из выбранных тем
        self.words_pool = []
        for topic_key in self.topic_keys:
            words = get_words_by_topic(topic_key)
            for word in words:
                word_copy = word.copy()
                word_copy["topic"] = topic_key
                word_copy["topic_name"] = get_topic_name(topic_key)
                self.words_pool.append(word_copy)
                
    def generate_questions(self):
        """Генерирует вопросы для сессии"""
        if len(self.words_pool) == 0:
            raise ValueError("Нет слов для генерации вопросов")
            
        self.questions = []
        used_words = set()
        
        for i in range(min(self.num_questions, len(self.words_pool))):
            # Выбираем случайное слово, которое ещё не использовалось
            available_words = [w for w in self.words_pool if w["chinese"] not in used_words]
            if not available_words:
                break
                
            word = random.choice(available_words)
            used_words.add(word["chinese"])
            
            # Выбираем случайный тип вопроса
            question_type = random.choice(self.question_types)
            
            question = QuizQuestion(word, question_type)
            question.generate(self.words_pool)
            self.questions.append(question)
            
        self.current_question_index = 0
        self.score = 0
        self.answers_history = []
        
    def get_current_question(self):
        """Возвращает текущий вопрос"""
        if self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index]
        return None
        
    def answer_question(self, user_answer):
        """
        Обрабатывает ответ на текущий вопрос
        
        Returns:
            bool: True если ответ правильный, False иначе
        """
        current_question = self.get_current_question()
        if current_question is None:
            return False
            
        is_correct = current_question.check_answer(user_answer)
        
        # Сохраняем историю ответа
        self.answers_history.append({
            "question": current_question.question_text,
            "correct_answer": current_question.correct_answer,
            "user_answer": user_answer,
            "is_correct": is_correct,
            "word": current_question.word
        })
        
        if is_correct:
            self.score += 1
            
        self.current_question_index += 1
        return is_correct
        
    def is_finished(self):
        """Проверяет, завершена ли сессия"""
        return self.current_question_index >= len(self.questions)
        
    def get_progress(self):
        """Возвращает прогресс сессии (номер текущего вопроса / общее количество)"""
        return (self.current_question_index + 1, len(self.questions))
        
    def get_score_percentage(self):
        """Возвращает процент правильных ответов"""
        if len(self.questions) == 0:
            return 0
        return int((self.score / len(self.questions)) * 100)
        
    def get_results_summary(self):
        """Возвращает краткую сводку результатов"""
        return {
            "total_questions": len(self.questions),
            "correct_answers": self.score,
            "percentage": self.get_score_percentage(),
            "answers_history": self.answers_history
        }


def create_quiz_session(topic="all", difficulty="normal", num_questions=10):
    """
    Фабричная функция для создания сессии викторины
    
    Args:
        topic: тема викторины ("all" для всех тем)
        difficulty: сложность (пока не используется,预留 для будущего)
        num_questions: количество вопросов
        
    Returns:
        QuizSession: настроенная сессия викторины
    """
    if topic == "all":
        topic_keys = None
    else:
        topic_keys = [topic] if topic in VOCABULARY else None
        
    session = QuizSession(
        topic_keys=topic_keys,
        num_questions=num_questions
    )
    session.generate_questions()
    
    return session
