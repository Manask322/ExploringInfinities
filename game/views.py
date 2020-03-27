from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render ,redirect
# Create your views here.
from django.contrib.auth.models import User
from users.models import CustomUser
from .models import Game


level_list = [['1', '1500', '5'], ['1', '1500', '10'], ['1', '1500', '15'], 
            ['1', '1500', '20'], ['1', '1000', '5'], ['1', '1000', '10'], 
            ['1', '1000', '15'], ['1', '1000', '20'], ['1', '750', '5'], 
            ['1', '750', '10'], ['1', '750', '15'], ['1', '750', '20'], 
            ['2', '2000', '3'], ['2', '2000', '5'], ['2', '2000', '7'], 
            ['2', '1500', '3'], ['2', '1500', '5'], ['2', '1500', '7'], 
            ['2', '1000', '3'], ['2', '1000', '5'], ['2', '1000', '7'], 
            ['1', '500', '5'], ['1', '500', '10'], ['1', '500', '15'], 
            ['1', '500', '20']]

list_length = len(level_list)

score_list = [0]
initial = 100
for i in range(list_length):
    score_list.append(initial)
    initial += 50


def home(request):
    all_users = CustomUser.objects.all().order_by('-high_score')
    if request.user.is_authenticated:
        check_custom_user = CustomUser.objects.filter(user=request.user)
        flag = False
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


def game(request,attemps,level):
    if int(level) > 25 :
        return redirect(home)
    if not request.session.get('attemps'):
        request.session['attemps'] = attemps
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
        game_details = Game.objects.get(user_id=request.user)
        user_details = CustomUser.objects.get(user=request.user)
        if (game_details.current_level + 1 ) != int(level) and game_details.current_level != 0:
            return redirect(games)
        if( int(attemps) >= 2 ):
            return redirect(games)
        level_details = level_list[game_details.current_level]
        game_details.current_level += 1
        size = level_details[0]
        flash = level_details[1]
        numbers = level_details[2]
        current_level = game_details.current_level
        game_details.save()
        if int(attemps) > int(request.session['attemps']) :
            request.session['attemps'] = attemps
        else:
            user_details.current_score += score_list[game_details.current_level-1]
        if user_details.current_score > user_details.high_score:
            user_details.high_score = user_details.current_score 
        current_score  = user_details.current_score
        user_details.save()
        return render(request,'game.html',{ 'size' : size, 'flash': flash, 'numbers': numbers,'current_level':current_level,'current_score': current_score })

def login(request):
    return render(request,'registration/login.html')

def games(request):
    if not request.session.get('attemps'):
        request.session['attemps'] = 0
    else:
        request.session['attemps'] = 0
    try:
        game = Game.objects.get(user_id=request.user)
        game.current_level = 0
        game.save()
        current_level = 1
        user_details = CustomUser.objects.get(user=request.user)
        user_details.current_score = 0
        user_details.save()
        attemps = 0
    except :
        return redirect(home)
    return render(request,'games.html',{'current_level':current_level,'attemps':attemps,'current_score':0})