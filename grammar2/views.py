from django.shortcuts import render, redirect
from .models import User


def home(request):
    if request.method == 'POST':
        user = request.POST.get('usernameG2')
        new_user = User.objects.create(name=user)
        new_user.save()
        context = {new_user: "new_user"}
        return redirect('topic_expG2', playerG2=new_user.name)
    return render(request, 'grammar2/home.html')


def topic_explanationG2(request, playerG2):
    user_player = User.objects.get(name=playerG2)
    context_temp = {'user_player': user_player}
    return render(request, 'grammar2/grammar2_exp.html', context_temp)


def game_explanationG2(request, playerG2):
    user_player = User.objects.get(name=playerG2)
    context_temp = {'user_player': user_player}
    return render(request, 'grammar2/grammar2_gameexp.html', context_temp)


def exercise_1(request, playerG2):
    user_player = User.objects.get(name=playerG2)
    context_temp = {'user_player': user_player}
    return render(request, 'grammar2/exercise_1.html', context_temp)


def exercise_2(request, playerG2):
    user_player = User.objects.get(name=playerG2)
    context_temp = {'user_player': user_player}
    return render(request, 'grammar2/exercise_2.html', context_temp)


def exercise_3(request, playerG2):
    user_player = User.objects.get(name=playerG2)
    context_temp = {'user_player': user_player}
    return render(request, 'grammar2/exercise_3.html', context_temp)


def exercise_4(request, playerG2):
    user_player = User.objects.get(name=playerG2)
    context_temp = {'user_player': user_player}
    return render(request, 'grammar2/exercise_4.html', context_temp)


def exercise_5(request, playerG2):
    user_player = User.objects.get(name=playerG2)
    context_temp = {'user_player': user_player}
    return render(request, 'grammar2/exercise_5.html', context_temp)


def exercise_6(request, playerG2):
    user_player = User.objects.get(name=playerG2)
    context_temp = {'user_player': user_player}
    return render(request, 'grammar2/exercise_6.html', context_temp)


def exercise_7(request, playerG2):
    user_player = User.objects.get(name=playerG2)
    context_temp = {'user_player': user_player}
    return render(request, 'grammar2/exercise_7.html', context_temp)

def exercise_8(request, playerG2):
    user_player = User.objects.get(name=playerG2)
    context_temp = {'user_player': user_player}
    return render(request, 'grammar2/exercise_8.html', context_temp)


def exercise_9(request, playerG2):
    user_player = User.objects.get(name=playerG2)
    context_temp = {'user_player': user_player}
    return render(request, 'grammar2/exercise_9.html', context_temp)


def exercise_10(request, playerG2):
    user_player = User.objects.get(name=playerG2)
    context_temp = {'user_player': user_player}
    return render(request, 'grammar2/exercise_10.html', context_temp)

def final_score(request, playerG2):
    users = User.objects.order_by('-score', 'id')
    user_player = User.objects.get(name=playerG2)
    context = {'users': users,
               'user_player': user_player}
    return render(request, 'grammar2/final_score.html', context)


def assign_score(request):
    user = request.POST["user"]
    new_score = request.POST["new_score"]
    nominal_number = request.POST["nominal_group"]
    user_g = User.objects.get(name=user)
    user_g.score = new_score
    user_g.save()
    if nominal_number == "1":
        user_g.stage = 2
        user_g.save()
        return redirect(exercise_2, playerG2=user)
    if nominal_number == "2":
        user_g.stage = 3
        user_g.save()
        return redirect(exercise_3, playerG2=user)
    if nominal_number == "3":
        user_g.stage = 4
        user_g.save()
        return redirect(exercise_4, playerG2=user)
    if nominal_number == "4":
        user_g.stage = 5
        user_g.save()
        return redirect(exercise_5, playerG2=user)
    if nominal_number == "5":
        user_g.stage = 6
        user_g.save()
        return redirect(exercise_6, playerG2=user)
    if nominal_number == "6":
        user_g.stage = 7
        user_g.save()
        return redirect(exercise_7, playerG2=user)
    if nominal_number == "7":
        user_g.stage = 8
        user_g.save()
        return redirect(exercise_8, playerG2=user)
    if nominal_number == "8":
        user_g.stage = 9
        user_g.save()
        return redirect(exercise_9, playerG2=user)
    if nominal_number == "9":
        user_g.stage = 10
        user_g.save()
        return redirect(exercise_10, playerG2=user)
    if nominal_number == "10":
        user_g.stage = 10
        user_g.save()
        return redirect(final_score, playerG2=user)