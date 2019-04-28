from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
# from . import constent
from.models import *
from django.core import serializers
import ast
import json

# def Home(request):
#     return HttpResponse('MOKKA RAVEENDR')

@csrf_exempt
def LoginPage(request):
    return render(request, 'login_administrator.html')

@csrf_exempt
def Signup_page(request):
    if request.method == 'POST':
        First_Name = request.POST.get('firstname')
        Last_Name = request.POST.get('lastname')
        User_name = request.POST.get('user_name')
        Phone = request.POST.get('phone_no')
        Email = request.POST.get('emailid')
        Date_birth = request.POST.get('date_birth')
        Password = request.POST.get('password')
        Confirm_password = request.POST.get('confirm_password')
        if Password == Confirm_password:
            if First_Name and Last_Name and User_name and Phone and Email and Date_birth and Password and Confirm_password:

                data = Signup(first_name=First_Name, last_name=Last_Name, username=User_name,
                              phone=Phone, email_id=Email, date_birth=Date_birth, password=Password,
                              confirm_password=Confirm_password)
                data.save()
                return render(request, 'login_administrator.html')
            else:

                return render(request, 'sign_up.html', {'massage': 'Please fill in the all fields','firstname':First_Name,
                                                        'lastname':Last_Name, 'user_name':User_name, 'phone_no':Phone,
                                                        'emailid':Email, 'date_birth':Date_birth, 'password':Password,
                                                        'confirm_password':Confirm_password})
        else:
            return render(request, 'sign_up.html', {'massage': 'Password and ConfirmPassword do not match', 'firstname': First_Name,
                                                    'lastname': Last_Name, 'user_name': User_name, 'phone_no': Phone,
                                                    'emailid': Email, 'date_birth': Date_birth, 'password': Password,
                                                    'confirm_password': Confirm_password})
    else:return render(request, 'sign_up.html', {'massage' : ''})



@csrf_exempt
def HomePage(request):
    if request.method == 'POST':
        User_name = request.POST.get('username')
        Password = request.POST.get('password')
        if User_name and Password:
            data = Signup.objects.filter(username=User_name)
            data = serializers.serialize('json', data)
            user_data = json.loads(data)
            if user_data:
                username = user_data[0]['fields']['username']
                password = user_data[0]['fields']['password']
                if User_name == username and Password == password:
                    data = Homepagetext.objects.all().select_related().values('hotel_data_id__hotel_name',
                                                                              'hotel_data_id__learn_text',
                                                                              'hotel_data_id__home_text',
                                                                              'hotel_data_id__wel_home_text')
                    print(data)
                    if data:
                        hotel_name = data[0]['hotel_data_id__hotel_name']
                        learn_text = data[0]['hotel_data_id__learn_text']
                        home_text = data[0]['hotel_data_id__home_text']
                        wel_home_text = data[0]['hotel_data_id__wel_home_text']
                        d_text = {'hotel_name':hotel_name,'learn_text':learn_text, 'home_text':home_text, 'wel_home_text':wel_home_text}
                        context = {'data': d_text}

                        return render(request, 'home_page.html', context)
                    else:
                        d_text = {'hotel_name': 'Five Star Hotel Rainbow', 'learn_text': 'Learn More', 'home_text':'View Room',
                                  'wel_home_text': 'Welcome Hotel Rainbow'}
                        context = {'data': d_text}
                        return render(request, 'home_page.html', context)
                else:
                    return render(request, 'login_administrator.html', {'massage':'Invalid Username and Password'})
            else:
                return render(request, 'login_administrator.html', {'massage': 'Invalid Username and Password'})
        else:
            return render(request, 'login_administrator.html', {'massage': 'Please enter Username and Password'})
    else:
        data = Homepagetext.objects.all().select_related().values('hotel_data_id__hotel_name',
                                                                  'hotel_data_id__learn_text',
                                                                  'hotel_data_id__home_text',
                                                                  'hotel_data_id__wel_home_text')
        if data:
            hotel_name = data[0]['hotel_data_id__hotel_name']
            learn_text = data[0]['hotel_data_id__learn_text']
            home_text = data[0]['hotel_data_id__home_text']
            wel_home_text = data[0]['hotel_data_id__wel_home_text']
            d_text = {'hotel_name': hotel_name, 'learn_text': learn_text, 'home_text': home_text,'wel_home_text':wel_home_text}
            context = {'data': d_text}
            return render(request, 'home_page.html', context)
        else:
            d_text = {'hotel_name': 'Five Star Hotel Rainbow', 'learn_text': 'Learn More', 'home_text': 'View Room',
                      'wel_home_text': 'Welcome Hotel Rainbow'}
            context = {'data': d_text}
            return render(request, 'home_page.html', context)






def Learnmore(request):
    if request.method == 'GET':
        Value = request.GET.get('lear')
        if Value == 'lear1':
            Room_Value = 'Room1'
            data = Hotelrooms.objects.filter(room_flag=Room_Value)
            if data:
                data = serializers.serialize('json', data)
                room_data = json.loads(data)
                Lear_data = room_data[0]['fields']
                print(data)
                context = {'data': Lear_data}
                print(context)
                return render(request, 'learn_more.html',context)
            else:
                context = {'data': {'profile_text':'View Room Profile', 'room_no_text':200 ,'day_price':500, 'day_price_dis':10,
                                    'month_price':15000, 'mont_price_dis':30, 'room_flag':'Room1'}}
                print(context)
                return render(request, 'learn_more.html', context)

        elif Value =='lear2':
            Room_Value = 'Room2'
            data = Hotelrooms.objects.filter(room_flag=Room_Value)
            if data:
                data = serializers.serialize('json', data)
                room_data = json.loads(data)
                Lear_data = room_data[0]['fields']
                print(data)
                context = {'data': Lear_data}
                print(context)
                return render(request, 'learn_more.html', context)
            else:
                context = {'data': {'profile_text': 'View Room Profile', 'room_no_text': 201, 'day_price': 600,
                                    'day_price_dis': 10,
                                    'month_price': 16000, 'mont_price_dis': 30, 'room_flag': 'Room2'}}
                print(context)
                return render(request, 'learn_more.html', context)
        elif Value =='lear3':
            Room_Value = 'Room3'
            data = Hotelrooms.objects.filter(room_flag=Room_Value)
            if data:
                data = serializers.serialize('json', data)
                room_data = json.loads(data)
                Lear_data = room_data[0]['fields']
                print(data)
                context = {'data': Lear_data}
                print(context)
                return render(request, 'learn_more.html', context)
            else:
                context = {'data': {'profile_text': 'View Room Profile', 'room_no_text': 202, 'day_price': 700,
                                    'day_price_dis': 10,
                                    'month_price': 17000, 'mont_price_dis': 30, 'room_flag': 'Room3'}}
                print(context)
                return render(request, 'learn_more.html', context)
        elif Value =='lear4':
            Room_Value = 'Room4'
            data = Hotelrooms.objects.filter(room_flag=Room_Value)
            if data:
                data = serializers.serialize('json', data)
                room_data = json.loads(data)
                Lear_data = room_data[0]['fields']
                print(data)
                context = {'data': Lear_data}
                print(context)
                return render(request, 'learn_more.html', context)
            context = {'data': {'profile_text': 'View Room Profile', 'room_no_text': 200, 'day_price': 800,
                                'day_price_dis': 10,
                                'month_price': 18000, 'mont_price_dis': 30, 'room_flag': 'Room4'}}
            print(context)
            return render(request, 'learn_more.html', context)
