import random
from rest_framework.response import Response
from rest_framework.views import APIView
from app_questions.models import Questions, SetOfQuestion
from app_score.models import Score


def get_random_40_question():
    items = list(Questions.objects.all())

    random_items = random.sample(items, 40)
    return random_items


def get_random_list_question():
    list_question = get_random_40_question()
    list_question_id = []
    for question in list_question:
        list_question_id.append(str(question.uuid))
    list_question_id_str = ', '.join(list_question_id)
    return list_question_id_str


def get_default_set_question():
    for i in range(20):
        list_question = get_random_40_question()
        list_question_id = []
        for question in list_question:
            list_question_id.append(str(question.uuid))
        list_question_id_str = ', '.join(list_question_id)
        set_of_question = SetOfQuestion.objects.create(list_question=list_question_id_str)
        set_of_question.save()


class GetListQuestion(APIView):
    def get(self, request):
        user_id = request.GET.get('user')
        try:
            set_index = int(request.GET.get('index'))
        except:
            set_index = None
        if set_index is None:
            list_set_question = list(SetOfQuestion.objects.all())
            rand_set = random.sample(list_set_question, 1)
            list_question = rand_set[0].list_question.split(', ')
        elif set_index == -1:
            list_question = ['8f6fed29a6e64d6db9006568636cb0ff',
                             '47d8aac87e53417aa41c607df5cd7be9',
                             '980e1b140f994e18839eb02039a54b18',
                             'f55c0e81b0bb4bd38f865f388880f893',
                             'd8c234e2c8d24e6aa5828edabd46584e']

            response_question = []
            for question_id in list_question:
                question_obj = Questions.objects.get(uuid=question_id)
                question = {
                    "question": question_obj.question,
                    "options": question_obj.list_answer.split(', '),
                    "correct_option": question_obj.correct_answer,
                }
                response_question.append(question)
            return Response({
                        "list_question": response_question,
                        "score": 0,
                        "index_question": 0
                    }, status=200)
        else:
            set_question = SetOfQuestion.objects.all()[set_index]
            list_question = set_question.list_question.split(', ')

        response_question = []
        for question_id in list_question:
            question_obj = Questions.objects.get(uuid=question_id)
            question = {
                "question": question_obj.question,
                "options": question_obj.list_answer.split(', '),
                "correct_option": question_obj.correct_answer,
            }
            response_question.append(question)
        score, index_question = get_score_index_question(user_id, set_index)
        return Response({
            "list_question": response_question,
            "score": score,
            "index_question": index_question
        }, status=200)


def get_score_index_question(user_id, set_question_index):
    if user_id is None:
        return 0, 0
    score = Score.objects.filter(user_id=user_id, index_set_question=set_question_index)
    if score.count() == 0:
        return 0, 0
    if score[0].index_question == 39:
        return 0, 0
    return score[0].score, score[0].index_question


def remove_bad_question():
    print(Questions.objects.count())
    list_question = Questions.objects.all()
    for question in list_question:
        if question.list_answer.count(',') != 3:
            question.delete()
    print(Questions.objects.count())
