from django.shortcuts import render, get_object_or_404, redirect
from .models import tournament, play, player
from datetime import date
from .forms import RegisterForm
from django.contrib.auth.models import User

# Create your views here.
def tournament_list(request):
    tournaments = tournament.objects.all().order_by('-start_date')
    return render(request, 'golf/tournament_list.html', {'tournaments': tournaments, 'today': date.today()})

def tournament_detail(request, pk):
    tournament_ = get_object_or_404(tournament, pk=pk)
    plays = play.objects.filter(tournament=pk)
    return render(request, 'golf/tournament_detail.html', {'tournament': tournament_, 'players': plays})

def register_a_player(request, pk, user_id):
    tournament_ = get_object_or_404(tournament, pk=pk)
    try:
        user_ = User.objects.filter(id=user_id)[0]
        player_ = player.objects.filter(user=user_)[0]
        tournament_.no_of_players += 1
        tournament_.save()
        player_.no_of_tournaments += 1
        player_.save()
        play.objects.create(player=player_,tournament=tournament_, no_of_strokes=0, score=0)
    except:
        pass
    plays = play.objects.filter(tournament=pk)
    return render(request, 'golf/tournament_detail.html', {'tournament': tournament_, 'players': plays})

def edit_score(request, pk):
    play_ = get_object_or_404(play, pk=pk)
    return render(request, 'golf/edit_score.html', {'play': play_})

def update_score(request, pk):
    no_of_strokes = int(request.POST.get('no_of_strokes'))
    score = int(request.POST.get('score'))
    play_ = play.objects.get(pk=pk)
    play_.no_of_strokes = no_of_strokes
    play_.score = score
    play_.save()
    tournament_ = play_.tournament
    plays = play.objects.filter(tournament=tournament_)
    return render(request, 'golf/tournament_detail.html', {'tournament': tournament_, 'players': plays})

def reigster(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            age = int(request.POST.get('age')[0])
            handicap = int(request.POST.get('handicap')[0])
            user_ = form.save()
            player_ = get_object_or_404(player, user=user_)
            player_.age = age
            player_.handicap = handicap
            player_.save()
            return redirect('login')
    else:
        form = RegisterForm()
        return render(request, 'golf/register.html', {'form': form})