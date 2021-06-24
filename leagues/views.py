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
def index_2(request):
	context={
		#sports orm 2
		"equipo_atlantica": Team.objects.filter(league__name__contains="Atlantic Soccer Conference"),
		"jugador": Player.objects.filter(curr_team__team_name__contains="Devils", curr_team__location__contains="Cleveland"),
		"jugador_beisbol": Player.objects.filter(curr_team__league__name__contains="Pacific Basketball League"),
		"jugador_lopez": Player.objects.filter(curr_team__league__name__contains="Pacific Basketball League", last_name__contains="Wilson"),
		"jugador_futboll": Player.objects.filter(curr_team__league__sport__contains="football"),
		"Sophia": Team.objects.filter(curr_players__first_name__contains="Sophia"),
		"liga_Sophia": League.objects.filter(teams__curr_players__first_name__contains="Sophia"),
		"flores": Player.objects.filter(Q(last_name__contains="Hernandez"), ~Q(curr_team__location__contains="Washington", curr_team__team_name__contains="Roughriders")),
		"samuel": Team.objects.filter(all_players__first_name__contains="Lucas", all_players__last_name__contains="Evans"),
		"tigres":Player.objects.filter(all_teams__team_name = "Pacers", all_teams__location = "Idaho"),
		"Viking": Player.objects.filter(Q(all_teams__location__contains="Cincinnati", all_teams__team_name__contains="Wild"), ~Q(curr_team__location__contains="Quebec", curr_team__team_name__contains="Chargers")),
		"jacob":Team.objects.exclude(team_name="Colts", location="Oregon").filter(all_players__first_name__contains="Anthony", all_players__last_name__contains="Ross"),
		"joshua": Player.objects.filter(first_name__contains="Joshua", all_teams__league__name="International League of Ice Hockey"),
		"tweleveOrMore": Team.objects.annotate(count_players=Count("all_players")).filter(count_players__gte=12),
		"teamArgByNum": Player.objects.annotate(count_teams=Count("all_teams")).order_by("-count_teams", "first_name"),
		}
	return render(request, "leagues/index_2.html",context)

#Anthony Ross
def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("home")