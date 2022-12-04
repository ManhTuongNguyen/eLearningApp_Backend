from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Score
from app_questions.models import SetOfQuestion


def get_question_quantity(index):
    return len(SetOfQuestion.objects.all()[index].list_question.split(', '))


def get_score(user_id, i):
    score = Score.objects.filter(user_id=user_id, index_set_question=i)
    if score.count() == 0:
        return "Chưa làm bài"
    return f"{score[0].score} / {get_question_quantity(i)}"


class GetListSetQuestion(APIView):
    def get(self, request):
        user_id = request.GET.get('user_id')
        list_set_question = SetOfQuestion.objects.all()
        list_score = []
        for i in range(0, list_set_question.count()):
            score = get_score(user_id, i)
            list_score.append(
                score
            )
        return Response(list_score, status=200)


class UpdateScore(APIView):
    def post(self, request):
        user_id = request.data.get('user')
        if user_id is None:
            return Response("")
        set_index = request.data.get('index')
        score = request.data.get('score')
        question_index = request.data.get('question_index')
        if question_index == 0:
            return Response("")
        score_object = Score.objects.filter(user_id=user_id, index_set_question=set_index)
        if score_object.count() == 0:
            # Chưa có điểm của bài làm này
            new_score = Score.objects.create(user_id=user_id, index_set_question=set_index,
                                             score=score, index_question=question_index)
            new_score.save()
            return Response({
                "message": "Đã lưu điểm thành công!",
                "type": 1
            })
        if score_object[0].index_question < question_index:
            # Điểm đang lưu trên hệ thống nhỏ hơn điểm của bài đã hoàn thành hiện tại
            score_object[0].score = score
            score_object[0].index_question = question_index
            score_object[0].save()
        return Response({
            "message": "Đã lưu điểm thành công!",
            "type": 1
        })



