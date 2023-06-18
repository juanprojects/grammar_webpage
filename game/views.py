from django.shortcuts import render, redirect
from .models import User


def home(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        new_user = User.objects.create(name=user)
        new_user.save()
        context = {new_user: "new_user"}
        return redirect('topic_exp', player=new_user.name)

    return render(request, 'game/home.html')


def topic_explanation(request, player):
    context = {'player': player}
    return render(request, 'game/topic_explanation.html', context)


def game_explanation(request, player):
    context = {'player': player}
    return render(request, 'game/game_explanation.html', context)


def nominal_group_1(request, player):
    userd = User.objects.get(name=player)
    context = {'player': player,
               'user': userd}
    return render(request, 'game/nominal_group_1.html', context)


def nominal_group_2(request, player):
    userd = User.objects.get(name=player)
    context = {'player': player,
               'user': userd}
    return render(request, 'game/nominal_group_2.html', context)


def nominal_group_3(request, player):
    userd = User.objects.get(name=player)
    context = {'player': player,
               'user': userd}
    return render(request, 'game/nominal_group_3.html', context)


def nominal_group_4(request, player):
    userd = User.objects.get(name=player)
    context = {'player': player,
               'user': userd}
    return render(request, 'game/nominal_group_4.html', context)


def nominal_group_5(request, player):
    userd = User.objects.get(name=player)
    context = {'player': player,
               'user': userd}
    return render(request, 'game/nominal_group_5.html', context)


def nominal_group_6(request, player):
    userd = User.objects.get(name=player)
    context = {'player': player,
               'user': userd}
    return render(request, 'game/nominal_group_6.html', context)


def nominal_group_7(request, player):
    userd = User.objects.get(name=player)
    context = {'player': player,
               'user': userd}
    return render(request, 'game/nominal_group_7.html', context)


def final_score(request, player):
    users = User.objects.order_by('-score')
    userd = User.objects.get(name=player)
    context = {'users': users,
               'user': userd}
    return render(request, 'game/final_score.html', context)

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
        return redirect(nominal_group_2, player=user)
    if nominal_number == "2":
        user_g.stage = 3
        user_g.save()
        return redirect(nominal_group_3, player=user)
    if nominal_number == "3":
        user_g.stage = 4
        user_g.save()
        return redirect(nominal_group_4, player=user)
    if nominal_number == "4":
        user_g.stage = 5
        user_g.save()
        return redirect(nominal_group_5, player=user)
    if nominal_number == "5":
        user_g.stage = 6
        user_g.save()
        return redirect(nominal_group_6, player=user)
    if nominal_number == "6":
        user_g.stage = 7
        user_g.save()
        return redirect(nominal_group_7, player=user)
    if nominal_number == "7":
        user_g.stage = 10
        user_g.save()
        return redirect(final_score, player=user)