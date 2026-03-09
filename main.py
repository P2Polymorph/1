# -*- coding: utf-8 -*-
"""
Консольный интерфейс тренажёра китайского языка
Запускает интерактивную викторину в терминале
"""

import sys
from vocabulary import VOCABULARY, get_topic_keys, get_topic_name, get_total_words_count
from quiz import create_quiz_session


def print_header():
    """Печатает заголовок программы"""
    print("\n" + "=" * 60)
    print("       汉语学习 - Тренажёр китайского языка (HSK1)")
    print("=" * 60)
    print(f"Всего слов в базе: {get_total_words_count()}")
    print()


def show_topics():
    """Показывает список доступных тем"""
    print("\nДоступные темы:")
    print("-" * 40)
    topic_keys = get_topic_keys()
    for i, key in enumerate(topic_keys, 1):
        print(f"  {i}. {get_topic_name(key)} [{key}]")
    print(f"  0. Все темы")
    print("-" * 40)
    return topic_keys


def select_topic(topic_keys):
    """Предлагает пользователю выбрать тему"""
    while True:
        try:
            choice = input("\nВыберите тему (номер или название): ").strip().lower()
            
            if choice == "0":
                return "all"
                
            # Проверка по номеру
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(topic_keys):
                    return topic_keys[idx]
                    
            # Проверка по названию ключа
            if choice in topic_keys:
                return choice
                
            print("Неверный выбор. Попробуйте снова.")
        except (ValueError, IndexError):
            print("Ошибка ввода. Введите номер темы или её ключ.")


def select_num_questions():
    """Предлагает выбрать количество вопросов"""
    while True:
        try:
            num = input("\nКоличество вопросов (5-20, по умолчанию 10): ").strip()
            if not num:
                return 10
            num = int(num)
            if 5 <= num <= 20:
                return num
            print("Число должно быть от 5 до 20")
        except ValueError:
            print("Введите число")


def run_quiz(topic, num_questions):
    """Запускает викторину"""
    print(f"\n{'=' * 60}")
    if topic == "all":
        print("Тема: ВСЕ ТЕМЫ")
    else:
        print(f"Тема: {get_topic_name(topic)}")
    print(f"Вопросов: {num_questions}")
    print(f"{'=' * 60}\n")
    
    session = create_quiz_session(topic=topic, num_questions=num_questions)
    
    while not session.is_finished():
        current, total = session.get_progress()
        question = session.get_current_question()
        
        print(f"\nВопрос {current} из {total}")
        print(f"Счёт: {session.score} правильных\n")
        print(f"❓ {question.question_text}\n")
        
        # Показываем варианты ответов
        for i, option in enumerate(question.options, 1):
            print(f"  {i}. {option}")
        
        # Получаем ответ пользователя
        while True:
            try:
                answer_idx = input("\nВаш ответ (номер варианта): ").strip()
                if not answer_idx.isdigit():
                    print("Введите номер варианта")
                    continue
                answer_idx = int(answer_idx)
                if 1 <= answer_idx <= len(question.options):
                    break
                print(f"Номер должен быть от 1 до {len(question.options)}")
            except ValueError:
                print("Ошибка ввода")
        
        selected_answer = question.options[answer_idx - 1]
        is_correct = session.answer_question(selected_answer)
        
        if is_correct:
            print("\n✅ Правильно!")
        else:
            print(f"\n❌ Неправильно. Правильный ответ: {question.correct_answer}")
            print(f"   Слово: {question.word['chinese']} ({question.word['pinyin']})")
        
        # Пауза перед следующим вопросом
        if not session.is_finished():
            input("\nНажмите Enter для продолжения...")
    
    # Показываем результаты
    show_results(session)


def show_results(session):
    """Показывает результаты викторины"""
    results = session.get_results_summary()
    
    print("\n" + "=" * 60)
    print("                 РЕЗУЛЬТАТЫ")
    print("=" * 60)
    print(f"Всего вопросов: {results['total_questions']}")
    print(f"Правильных ответов: {results['correct_answers']}")
    print(f"Процент правильных: {results['percentage']}%")
    print("=" * 60)
    
    # Оценка результата
    percentage = results['percentage']
    if percentage >= 90:
        print("\n🏆 Отлично! Вы прекрасно знаете эти слова!")
    elif percentage >= 70:
        print("\n👍 Хорошо! Но есть куда расти.")
    elif percentage >= 50:
        print("\n📚 Неплохо, но нужно повторить материал.")
    else:
        print("\n💪 Не сдавайтесь! Продолжайте учиться!")
    
    # Показываем ошибки
    wrong_answers = [a for a in results['answers_history'] if not a['is_correct']]
    if wrong_answers:
        print("\n📝 Работа над ошибками:")
        print("-" * 60)
        for i, ans in enumerate(wrong_answers, 1):
            print(f"{i}. {ans['question']}")
            print(f"   Ваш ответ: {ans['user_answer']}")
            print(f"   Правильно: {ans['correct_answer']}")
            print(f"   Слово: {ans['word']['chinese']} ({ans['word']['pinyin']})")
            print()
    
    print("=" * 60)


def main_menu():
    """Главное меню программы"""
    while True:
        print_header()
        
        print("МЕНЮ:")
        print("  1. Начать тестирование")
        print("  2. Просмотреть все темы")
        print("  3. Просмотреть слова темы")
        print("  4. Выход")
        print()
        
        choice = input("Выберите пункт меню (1-4): ").strip()
        
        if choice == "1":
            topic_keys = show_topics()
            topic = select_topic(topic_keys)
            num_questions = select_num_questions()
            run_quiz(topic, num_questions)
            
        elif choice == "2":
            topic_keys = show_topics()
            print(f"\nВсего тем: {len(topic_keys)}")
            
        elif choice == "3":
            topic_keys = show_topics()
            topic = select_topic(topic_keys)
            
            if topic == "all":
                print("\nВыберите конкретную тему для просмотра слов")
                continue
                
            from vocabulary import get_words_by_topic
            words = get_words_by_topic(topic)
            
            print(f"\n{'=' * 60}")
            print(f"Тема: {get_topic_name(topic)}")
            print(f"Слов: {len(words)}")
            print(f"{'=' * 60}")
            print(f"{'№':<3} {'Китайский':<10} {'Пиньинь':<15} {'Перевод'}")
            print("-" * 60)
            
            for i, word in enumerate(words, 1):
                print(f"{i:<3} {word['chinese']:<10} {word['pinyin']:<15} {word['translation']}")
            
            print("-" * 60)
            input("\nНажмите Enter для возврата в меню...")
            
        elif choice == "4":
            print("\n谢谢！До свидания! Удачи в изучении китайского!")
            sys.exit(0)
            
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана. До свидания!")
        sys.exit(0)
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")
        sys.exit(1)
