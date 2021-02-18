from django.db import connection
from django.http import JsonResponse
from django.views import View
import json


class ReturnId(View):
    @staticmethod
    def get(request):
        auth_token = request.GET.get('authToken')
        with connection.cursor() as cursor:
            cursor.execute("select user_id from authtoken_token where key = " + "'" + auth_token + "'")
            user_id = cursor.fetchone()
            return JsonResponse({'id': user_id})


class ReturnUserInfo(View):
    @staticmethod
    def get(requset):
        id = requset.GET.get('id')
        with connection.cursor() as cursor:
            cursor.execute("""\
            SELECT username, last_name, first_name, email, level, date_joined, introduction, id\
             FROM accounts_user\
             WHERE id =""" + id)

            data = cursor.fetchone()
            userInfo = {'username': data[0], 'last_name': data[1], 'first_name': data[2], 'email': data[3],
                        'level': data[4], 'date_joined': data[5], 'introduction': data[6], 'id': data[7]}

        return JsonResponse({'userInfo': userInfo})
