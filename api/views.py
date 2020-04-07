from django.http import JsonResponse, HttpResponse
from .models import CuniqueData
from django.db.models import Avg


def data_view_details(request, msg):

    if request.method == 'GET':
        list_data = CuniqueData.objects.filter(message__icontains=msg)
        # matched_data=[]
        c=0
        for i in list_data:
            if msg in [word for word in i.message.split(" ")]:
                c += 1
                pass
            # list_data.exclude(message=i.message)
        print(c, msg, type(list_data), len(list_data))
        # lis = list(list_data)
        # c = 0
        # for i in range(lis):
        #     if msg in [word for word in i.message.split(" ")]:
        #         c += 1
        #         pass



        # print(list_data.exclude(message

        if list_data:
            output_dict = {
                'total_matches': list_data.count(),
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
        return JsonResponse({"Error": f"In any msg word-->{msg} doesn't exist"}, safe=False)


def data_import(request):
    pass
