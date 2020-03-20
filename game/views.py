from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render ,redirect
# Create your views here.
from django.contrib.auth.models import User
from users.models import CustomUser
from .models import Game


def home(request):
    all_users = CustomUser.objects.all().order_by('-high_score')
    if request.user.is_authenticated:
        check_custom_user = CustomUser.objects.filter(user=request.user)
        flag = False
        print(check_custom_user)
        if len(check_custom_user) == 0:
            new_user = CustomUser()
            new_user.user = User.objects.get(username=request.user)
            new_user.current_score = 0
            new_user.high_score = 0
            new_user.save()
            flag = True
        check_game_details = Game.objects.filter(user_id=request.user)
        if len(check_game_details) == 0:
            new_game_user = Game()
            new_game_user.user_id = User.objects.get(username=request.user)
            new_game_user.current_level = 0
            new_game_user.save()
            flag =True

        if flag :
            return redirect(home)
    
    return render(request,'home.html', {'users': all_users})

def start_game(request):
    if not request.user.is_authenticated:
        return redirect(home)
    return render(request,'start_game.html')

def game(request):

    if request.POST:
        data = request.POST
        size = data['size']
        flash = data['flash']
        numbers = data['numbers']
        try:
            game_details = Game.objects.get(user_id=request.user)
            game_details.current_level = 1
            game_details.size = size
            game_details.flash = flash
            game_details.numbers = numbers
            game_details.save()
            user_details = CustomUser.objects.get(user=request.user)
            user_details.current_score = 0
            user_details.save()
        except :
            return redirect(home)
        return render(request,'game.html',{ 'size' : size, 'flash': flash, 'numbers': numbers,'current_level':1,'current_score':0 })
    else:
        print("GET")
        game_details = Game.objects.get(user_id=request.user)
        game_details.numbers += 1
        game_details.current_level += 1
        size = game_details.size
        flash = game_details.flash
        numbers = game_details.numbers
        current_level = game_details.current_level
        game_details.save()
        user_details = CustomUser.objects.get(user=request.user)
        user_details.current_score += 1
        if user_details.current_score > user_details.high_score:
            user_details.high_score = user_details.current_score 
        current_score  = user_details.current_score
        user_details.save()
        return render(request,'game.html',{ 'size' : size, 'flash': flash, 'numbers': numbers,'current_level':current_level,'current_score': current_score })

def login(request):
    return render(request,'registration/login.html')
