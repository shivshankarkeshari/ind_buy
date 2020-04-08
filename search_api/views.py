from django.http import JsonResponse
from .models import CuniqueData
from django.db.models import Avg
from django.db.models import Q


def data_view_details(request, msg):

    if request.method == 'GET':
        list_data = CuniqueData.objects.filter(message__icontains=msg)

        remove_id = []

        for i in reversed(list_data):
            if msg not in [word for word in i.message.split(" ")]:
                remove_id.append(i.id)

        list_data = list_data.filter(~Q(id__in=remove_id))

        if list_data:
            output_dict = {
                'total_matches': len(list_data),
                'truth': {
                    'spam': list_data.filter(truth='spam').count(),
                    'not-spam': list_data.filter(truth__contains='not-spam').count()
                },
                'cube': {
                    'spam': list_data.filter(cube='spam').count(),
                    'not-spam': list_data.filter(cube='not-spam').count()
                },
                'google': {
                    'spam': list_data.filter(google='spam').count(),
                    'not-spam': list_data.filter(google='not-spam').count(),
                    "avg-spam-score": float(list_data.aggregate(sp_avg=Avg('google_spam'))['sp_avg']),
                    "avg-not-spam-score": float(list_data.aggregate(nsp_avg=Avg('google_not_spam'))['nsp_avg'])
                },
                'ibm': {
                    'spam': list_data.filter(ibm='spam').count(),
                    'not-spam': list_data.filter(ibm='not-spam').count(),
                    "avg-spam-score": float(list_data.aggregate(sp_avg=Avg('ibm_spam'))['sp_avg']),
                    "avg-not-spam-score": float(list_data.aggregate(nsp_avg=Avg('ibm_not_spam'))['nsp_avg'])
                },
            }

            return JsonResponse(output_dict, safe=False)
        return JsonResponse({"Error": f"In any message word---> '{msg}' doesn't exist"}, safe=False)


def data_view_details_msg(request, msg):
    print(msg)
    print("ok", CuniqueData.objects.all()[0].message)

    if request.method == 'GET':
        list_data = CuniqueData.objects.filter(message__contains=msg)

        # remove_id = []
        #
        # for i in reversed(list_data):
        #     if msg not in [word for word in i.message.split(" ")]:
        #         remove_id.append(i.id)
        #
        # list_data = list_data.filter(~Q(id__in=remove_id))

        if list_data:
            output_dict = {
                'total_matches': len(list_data),
                'truth': {
                    'spam': list_data.filter(truth='spam').count(),
                    'not-spam': list_data.filter(truth__contains='not-spam').count()
                },
                'cube': {
                    'spam': list_data.filter(cube='spam').count(),
                    'not-spam': list_data.filter(cube='not-spam').count()
                },
                'google': {
                    'spam': list_data.filter(google='spam').count(),
                    'not-spam': list_data.filter(google='not-spam').count(),
                    "avg-spam-score": float(list_data.aggregate(sp_avg=Avg('google_spam'))['sp_avg']),
                    "avg-not-spam-score": float(list_data.aggregate(nsp_avg=Avg('google_not_spam'))['nsp_avg'])
                },
                'ibm': {
                    'spam': list_data.filter(ibm='spam').count(),
                    'not-spam': list_data.filter(ibm='not-spam').count(),
                    "avg-spam-score": float(list_data.aggregate(sp_avg=Avg('ibm_spam'))['sp_avg']),
                    "avg-not-spam-score": float(list_data.aggregate(nsp_avg=Avg('ibm_not_spam'))['nsp_avg'])
                },
            }

            return JsonResponse(output_dict, safe=False)
        return JsonResponse({"Error": f"In any msg word-->'{msg}' doesn't exist"}, safe=False)


def data_import(request):
    pass
