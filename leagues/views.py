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
		"jugador": Player.objects.filter(curr_team__team_name__contains="Penguin", curr_team__location__contains="Boston"),
		"jugador_beisbol": Player.objects.filter(curr_team__league__name__contains="International Collegiate Baseball Conference"),
		"jugador_lopez": Player.objects.filter(curr_team__league__name__contains="American Conference of Amateur Football", last_name__contains="Lopez"),
		"jugador_football": Player.objects.filter(curr_team__league__sport__contains="football"),
		"Sophia": Team.objects.filter(curr_players__first_name__contains="Sophia"),
		"liga_Sophia": League.objects.filter(teams__curr_players__first_name__contains="Sophia"),
		"floresNotRough": Player.objects.filter(Q(last_name__contains="Flores"), ~Q(curr_team__location__contains="Washington", curr_team__team_name__contains="Roughriders")),
		"samuel": Team.objects.filter(all_players__first_name__contains="Samuel", all_players__last_name__contains="Evans"),
		"tigres":Player.objects.filter(all_teams__location__contains="Manitoba", all_teams__team_name__contains="Tiger-Cats"),
		"wasViking": Player.objects.filter(Q(all_teams__location__contains="Wichita", all_teams__team_name__contains="Vikings"), ~Q(curr_team__location__contains="Wichita", curr_team__team_name__contains="Vikings")),
		"jacobWhere":Team.objects.exclude(team_name="Colts", location="Oregon").filter(all_players__first_name__contains="Jacob", all_players__last_name__contains="Gray"),
		"joshuaPlays": Player.objects.filter(first_name__contains="Joshua", all_teams__league__name="Atlantic Federation of Amateur Baseball Players"),
		"tweleveOrMore": Team.objects.annotate(count_players=Count("all_players")).filter(count_players__gte=12),
		"teamArgByNum": Player.objects.annotate(count_teams=Count("all_teams")).order_by("-count_teams", "first_name"),
		}
	return render(request, "leagues/index_2.html",context)


def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("home")