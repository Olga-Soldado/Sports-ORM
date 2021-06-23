from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count
from . import team_maker

def home(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/main.html",context)

def index(request):

	Alex =  Player.objects.order_by('first_name').filter(first_name="Alexander")
	Wyatt = Player.objects.order_by('first_name').filter(first_name="Wyatt")
	context = {
		"beisbol": League.objects.filter(sport="Baseball"),
		"mujeres": League.objects.filter(name__contains=" Lacrosse"),
		"hockey": League.objects.filter(sport__contains="Hockey"),
		"no_football": League.objects.exclude(sport__contains="Football"),
		"conferencias": League.objects.filter(name__icontains="Conference"),
		"atlantic":League.objects.filter(name__contains="Atlantic"),
		"Dallas": Team.objects.filter(location="Dallas"),
		"Raptors": Team.objects.filter(team_name__icontains="Wolverines"),
		"Ciudad": Team.objects.filter(location__icontains="City"),
		"T": Team.objects.filter(team_name__startswith="t"),
		"orden_alf": Team.objects.order_by("location"),
		"orden_inverso": Team.objects.order_by("-team_name"),
		"Cooper": Player.objects.filter(last_name="Cooper"),
		"Joshua": Player.objects.filter(first_name="Joshua"),
		"Cooper_EXCEPTO_Joshua": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"Alex_o_Wyatt": Alex | Wyatt,
				}

	return render(request, "leagues/index.html",context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("home")