import random

from graphics import *


def write_country_to_file(country, file_name):
    file1 = open(file_name, "a")
    file1.write(str(country.get_code()) + "_" + country.get_name() + "_" + str(country.get_elo()) + "_" +
                country.get_conf() + "_" + country.get_region() + "_")
    file1.close()


def clear_file(file_name):
    file1 = open(file_name, "w")
    file1.write("")
    file1.close()


def draw_groups_4_4():

    pot_1 = ["PAN", "TRI", "USA", "CRC"]
    pot_2 = ["CAN", "MEX", "MTQ", "HON"]
    pot_3 = ["HAI", "JAM", "SLV", "GUA"]
    pot_4 = ["ARU", "GLP", "CUB", "DOM"]

    print("Group A")
    for i in range(16):
        if i == 4:
            print("Group B")
        if i == 8:
            print("Group C")
        if i == 12:
            print("Group D")
        if i % 4 == 0:
            lenpot = len(pot_1)
            rando = random.random()
            numbo = int(lenpot * rando)
            print(pot_1.pop(numbo))
        elif i % 4 == 1:
            lenpot = len(pot_2)
            rando = random.random()
            numbo = int(lenpot * rando)
            print(pot_2.pop(numbo))
        elif i % 4 == 2:
            lenpot = len(pot_3)
            rando = random.random()
            numbo = int(lenpot * rando)
            print(pot_3.pop(numbo))
        elif i % 4 == 3:
            lenpot = len(pot_4)
            rando = random.random()
            numbo = int(lenpot * rando)
            print(pot_4.pop(numbo))


def draw_groups_2_4():
    pot_1 = ["BER", "GDL", "GUY", "BLZ"]
    pot_2 = ["TCA", "SMT", "CAY", "SKN"]

    print("Group A")
    for i in range(8):
        if i == 4:
            print("Group B")
        if i % 2 == 0:
            lenpot = len(pot_1)
            rando = random.random()
            numbo = int(lenpot * rando)
            print(pot_1.pop(numbo))
        else:
            lenpot = len(pot_2)
            rando = random.random()
            numbo = int(lenpot * rando)
            print(pot_2.pop(numbo))


def draw_groups_3_3():
    pot = ["AIA", "ARU", "DMA", "VGB", "VIR", "BON"]

    print("Group 1")
    for i in range(6):
        if i == 2:
            print("Group 2")
        if i == 4:
            print("Group 3")
        lenpot = len(pot)
        rando = random.random()
        numbo = int(lenpot * rando)
        print(pot.pop(numbo))


def draw_ties_2():

    pot = ["NCA", "SLV", "GUA"]

    for i in range(len(pot)):
        lenpot = len(pot)
        rando = random.random()
        numbo = int(lenpot * rando)
        print(pot.pop(numbo))
        if i % 2 == 1:
            print("----------------------------")


def draw_ties():
    pot1 = ["VIN", "VIR", "MSR"]
    pot2 = ["VGB", "AIA", "DMA"]

    for i in range(3):
        lenpot = len(pot1)
        rando = random.random()
        numbo = int(lenpot * rando)
        print(pot1.pop(numbo))
        lenpot = len(pot2)
        rando = random.random()
        numbo = int(lenpot * rando)
        print(pot2.pop(numbo))
        print("----------------------------")


def set_elo(country_1, country_2, result, home):
    if result >= 1:
        game_res_1 = 1
        game_res_2 = 0
    elif result == 0:
        game_res_1 = 0.5
        game_res_2 = 0.5
    else:
        game_res_1 = 0
        game_res_2 = 1
        result = result * -1

    k_rate = 50
    if result == 2:
        k_rate = 75
    elif result == 3:
        k_rate = 87.5
    elif result > 3:
        k_rate = 50 + (50 * (3/4 + ((result-3)/8)))

    diff_rat_1 = country_1.get_elo() - country_2.get_elo() + (100*home)
    diff_rat_2 = country_2.get_elo() - country_1.get_elo() - (100 * home)

    expected_res_1 = (1 / (10**((-diff_rat_1)/400) + 1))
    expected_res_2 = (1 / (10 ** ((-diff_rat_2) / 400) + 1))

    new_elo_1 = country_1.get_elo() + (k_rate * (game_res_1 - expected_res_1))
    new_elo_2 = country_2.get_elo() + (k_rate * (game_res_2 - expected_res_2))

    #print(country_1.get_code() + ": " + str(country_1.get_elo()) + " -> " + str(new_elo_1))
    #print(country_2.get_code() + ": " + str(country_2.get_elo()) + " -> " + str(new_elo_2))
    #print()

    country_1.set_elo(new_elo_1)
    country_2.set_elo(new_elo_2)




def sort_helper(country):
    return country.get_elo()


def sort_helper_2(team_array):
    return team_array[7]

def sort_helper_3(team_array):
    return team_array[2]

def sort_helper_4(competition_country):
    return competition_country.get_rank()

#def text_output(self, outputs):
#    for output in outputs:
#        print(output)

class Round:

    def __init__(self, num_of_teams, robin, neutral, round_number, print_package, sort_type="None"):
        self.num_of_teams = num_of_teams
        self.robin = robin
        self.neutral = neutral
        self.round_number = round_number
        self.sort_type = sort_type
        self.teams = None
        self.high_rank = 0
        self.low_rank = 0
        self.lowest_advancing_rank = 0
        self.num_advancing = 0


    def set_teams(self, teams, high_rank, low_rank):
        self.teams = teams
        self.high_rank = high_rank
        self.low_rank = low_rank
        self.lowest_advancing_rank = self.high_rank + self.num_advancing

    def get_num_of_teams(self):
        return self.num_of_teams

    def get_round_number(self):
        return self.round_number

#    def __str__(self):
#        myStr = ''
#        myStr = 'Number of Teams: ' + str(self.num_of_teams) + myStr
#        myStr = 'Number of Teams: ' + str(self.num_of_teams) + myStr
#        myStr = 'Number of Teams: ' + str(self.num_of_teams) + myStr
#        myStr = 'Number of Teams: ' + str(self.num_of_teams) + myStr
#        myStr = 'Number of Teams: ' + str(self.num_of_teams) + myStr
#        myStr = 'Number of Teams: ' + str(self.num_of_teams) + myStr
#        myStr = 'Number of Teams: ' + str(self.num_of_teams) + myStr
#        myStr = 'Number of Teams: ' + str(self.num_of_teams) + myStr
#        myStr = 'Number of Teams: ' + str(self.num_of_teams) + myStr

class GroupRound(Round):

    def __init__(self, teams, robin, neutral, round_number, num_advancing, num_groups, print_package, sort_type="Group Rank"):
        super().__init__(teams, robin, neutral, round_number, print_package, sort_type)
        self.num_groups = num_groups
        self.num_advancing = num_advancing
        self.groups = []
        self.has_drawn = False
        self.print_package = []
        for part in print_package:
            self.print_package.append(part)
        self.print_package.append("Round " + str(round_number))
        self.print_package.append(str(robin) + " Robin Group")

    def draw_groups(self):
        teams_helper = [None] * len(self.teams)
        for i in range(len(self.teams)):
            teams_helper[i] = self.teams[i]
        pots = [[]]
        groups = []
        current_num = 0
        pot_count = 0
        end_num = self.num_groups
        teams_helper.sort(key=sort_helper_4)
        while len(teams_helper) > 0:
            if current_num == end_num:
                pots.append([])
                pot_count += 1
                current_num = end_num
                end_num += self.num_groups
            pots[pot_count].append(teams_helper.pop(0))
            current_num += 1
        print(pots)
#        text_output(pots)
        for k in range(self.num_groups):
            new_group = []
            for i in range(len(pots)):
                if len(pots[i]) == 0:
                    continue
                lenpot = len(pots[i])
                rando = random.random()
                numbo = int(lenpot * rando)
                new_group.append(pots[i].pop(numbo))
            groups.append(new_group)
        for group in groups:
            new_group = Group(group, self.neutral, self.robin, self.print_package)
            self.groups.append(new_group)
        for group in self.groups:
            group.print_standings()
        self.has_drawn = True

    def play_round(self):
        self.draw_groups()
        #for group in self.groups:
            #group.play_current_matchday()
            #group.print_standings()
        matchdays_to_play = True
        while matchdays_to_play:
            for group in self.groups:
                group.print_current_matchday()
                group.play_current_matchday()
                group.print_standings()
            matchdays_to_play = self.increment_matchday()
        self.round_end()

    def round_end(self):
        if self.sort_type == "Group Position":
            curr_rank = self.high_rank
            for group in self.groups:
                teams_list = group.get_teams_in_group()
                for i in range(len(teams_list)):
                    new_rank = i * self.num_groups + curr_rank
                    teams_list[i][0].set_rank(new_rank)
                curr_rank += 1
        if self.sort_type == "Group Rank":
            rank_list = []
            for group_index in range(len(self.groups)):
                teams_list = self.groups[group_index].get_teams_in_group()
                if group_index == 0:
                    for k in range(len(teams_list)):
                        rank_list.append([])
                for i in range(len(teams_list)):
                    rank_list[i].append(teams_list[i])

            for team_list in rank_list:
                team_list.sort(key=lambda item: (item[7], item[6], item[4]), reverse=True)
            curr_rank = self.high_rank
            for team_list in rank_list:
                for team in team_list:
                    team[0].set_rank(curr_rank)
                    curr_rank += 1
            #for group in self.groups:
                #teams_list
        self.teams.sort(key=sort_helper_4)
        for team in self.teams:
            if team.get_rank() < self.lowest_advancing_rank:
                print(team.get_name() + " advances.")
#                text_output([team.get_name(), " advances."])
                team.increment_round()
            else:
                print(team.get_name() + " is eliminated.")



    def increment_matchday(self):
        matchdays_to_play = False
        for group in self.groups:
            if group.increment_matchday():
                matchdays_to_play = True
        return matchdays_to_play


class TieRound(Round):

    def __init__(self, num_of_teams, robin, neutral, round_number, draw_style, print_package, sort_type="None"):
        super().__init__(num_of_teams, robin, neutral, round_number, print_package, sort_type)
        self.draw_style = draw_style
        self.has_drawn = False
        self.ties = []
        self.print_package = []
        for part in print_package:
            self.print_package.append(part)
        self.print_package.append("Round " + str(round_number))
        self.print_package.append(str(robin) + "-Leg Tie")

    def draw_ties(self):
        if self.draw_style == "Pots":
            return self.draw_ties_pots()
        elif self.draw_style == "Seeded":
            return self.draw_ties_seeded()

    def draw_ties_seeded(self):
        ties = []
        home_team_index = 0
        away_team_index = len(self.teams) - 1
        teams_helper = [None] * len(self.teams)
        for i in range(len(self.teams)):
            teams_helper[i] = self.teams[i]
        teams_helper.sort(key=sort_helper_4)
        while home_team_index < away_team_index:
            new_tie = Tie([teams_helper[home_team_index], teams_helper[away_team_index]], self.neutral, self.robin, self.print_package)
            home_team_index += 1
            away_team_index -= 1
            ties.append(new_tie)
        return ties


    def draw_ties_pots(self):
        ties = []
        pot1 = []
        pot2 = []
        pot_size = len(self.teams) // 2
        for i in range(pot_size):
            pot1.append(self.teams[i])
            pot2.append(self.teams[i + pot_size])

        for i in range(pot_size):
            new_tie = [None, None]
            lenpot = len(pot1)
            rando = random.random()
            numbo = int(lenpot * rando)
            new_tie[1] = pot1.pop(numbo)
            lenpot = len(pot2)
            rando = random.random()
            numbo = int(lenpot * rando)
            new_tie[0] = pot2.pop(numbo)
            new_tie_object = Tie(new_tie, self.neutral, self.robin, self.print_package)
            ties.append(new_tie_object)
        return ties

    def increment_matchday(self):
        matchdays_to_play = False
        for tie in self.ties:
            if tie.increment_matchday():
                matchdays_to_play = True
        return matchdays_to_play

    def play_round(self):
        if not self.has_drawn:
            self.ties = self.draw_ties()
        print()
        matchdays_to_play = True
        while matchdays_to_play:
            for tie in self.ties:
                tie.print_current_matchday()
                tie.play_current_matchday()
            matchdays_to_play = self.increment_matchday()
        self.round_end()

    def round_end(self):
        curr_win_rank = self.high_rank
        curr_lose_rank = self.low_rank

        for tie in self.ties:
            tie.print_result()
            winner = tie.get_winner()
            loser = tie.get_loser()
            winner.increment_round()
            winner.set_rank(curr_win_rank)
            curr_win_rank += 1
            loser.set_rank(curr_lose_rank)
            curr_lose_rank -= 1
            print(winner.get_name() + " advances.")
            print(loser.get_name() + " is eliminated.")
            # str(self.agg_away_score))
            # print(away_country.get_name() + " is eliminated.")

class KnockoutRound(Round):

    def __init__(self, num_of_teams, robin, neutral, round_number, draw_style, print_package, sort_type="Bracket"):
        super().__init__(num_of_teams, robin, neutral, round_number, print_package, sort_type)
        self.draw_style = draw_style
        self.print_package = []
        for part in print_package:
            self.print_package.append(part)
        self.print_package.append("Round " + str(round_number))
        self.print_package.append("Knockout Round")

    def play_round(self):
        no_champion = True
        knockout_round_number = 3
        num_still_remaining = self.num_of_teams
        while no_champion:
            teams_for_round = []
            knockout_round = TieRound(num_still_remaining, self.robin, self.neutral, knockout_round_number, self.draw_style, self.print_package)
            knockout_round.set_teams(self.teams, self.high_rank, self.low_rank)
            knockout_round.play_round()
            knockout_round_number += 1
            self.teams.sort(key=sort_helper_4)


            num_still_remaining = num_still_remaining // 2

            new_teams_list = [None]*num_still_remaining
            for i in range(num_still_remaining):
                new_teams_list[i] = self.teams[i]
            self.teams = new_teams_list
            if num_still_remaining == 1:
                no_champion = False
        print()
        print(self.teams[i].get_name() + " is the champion.")
            

class CompetitionCountry:

    def __init__(self, country, rank):
        self.country = country
        self.rank = rank
        self.round = 1

    def set_rank(self, rank):
        self.rank = rank

    def get_rank(self):
        return self.rank

    def get_round(self):
        return self.round

    def get_country(self):
        return self.country

    def get_code(self):
        return self.country.get_code()

    def get_name(self):
        return self.country.get_name()

    def get_elo(self):
        return self.country.get_elo()

    def get_region(self):
        return self.country.get_region()

    def get_conf(self):
        return self.country.get_conf()

    def increment_round(self):
        self.round += 1

    def set_elo(self, new_elo):
        self.country.set_elo(new_elo)

class Competition:

    def __init__(self, title, conf, region, teams):
        self.title = title
        self.conf = conf
        self.region = region
        self.teams = []
        self.current_round = 1
        self.rounds = []
        self.print_package = [self.title]
        for i in range(len(teams)):
            new_comp_country = CompetitionCountry(teams[i], i+1)
            self.teams.append(new_comp_country)

    def get_teams_for_round(self, round):
        self.teams.sort(key=sort_helper_4, reverse=True)
        num_of_teams = round.get_num_of_teams()
        round_number = round.get_round_number()
        competing_counter = num_of_teams
        list_of_teams_in_round = []
        first = True
        high_rank = 0
        low_rank = 0
        for team in self.teams:
            if team.get_round() < round_number:
                continue
            if competing_counter > 0:
                if first:
                    low_rank = team.get_rank()
                    first = False
                list_of_teams_in_round.append(team)
                high_rank = team.get_rank()
                competing_counter -= 1
            else:
                team.increment_round()
        round.set_teams(list_of_teams_in_round, high_rank, low_rank)

    def add_round(self, round_type, num_of_teams, num_advancing, neutral, robin, round_number, num_groups=1, draw_style="Pots", sort_type="None"):
        new_round = None
        if round_type == "Groups":
            if sort_type is not None:
                new_round = GroupRound(num_of_teams, robin, neutral, round_number, num_advancing, num_groups, self.print_package, sort_type)
            else:
                new_round = GroupRound(num_of_teams, robin, neutral, round_number, num_advancing, num_groups, self.print_package)
        elif round_type == "Ties":
            new_round = TieRound(num_of_teams, robin, neutral, round_number, draw_style, self.print_package, sort_type)
        elif round_type == "Knockout":
            new_round = KnockoutRound(num_of_teams, robin, neutral, round_number, draw_style, self.print_package, sort_type)
        self.rounds.append(new_round)


    def add_groups_round(self, num_of_teams_competing, group_number):
        competing_counter = num_of_teams_competing
        list_of_teams_in_round = []
        self.teams.sort(key=sort_helper_3, reverse=True)
        for team in self.teams:
            if team[1] < self.current_round:
                continue
            if competing_counter > 0:
                list_of_teams_in_round.append(team)
                competing_counter -= 1
            else:
                team[1] += 1
        list_of_teams_in_round.sort(key=sort_helper_3)
        self.draw_groups(list_of_teams_in_round, group_number)

    def draw_groups(self, teams, group_number):
        pots = [[]]
        groups = []
        current_num = 0
        pot_count = 0
        end_num = group_number
        while len(teams) > 0:
            if current_num == end_num:
                pots.append([])
                pot_count += 1
                current_num = end_num
                end_num += group_number
            pots[pot_count].append(teams.pop(0))
            current_num += 1
        print(pots)
        for k in range(group_number):
            new_group = []
            for i in range(len(pots)):
                if len(pots[i]) == 0:
                    continue
                lenpot = len(pots[i])
                rando = random.random()
                numbo = int(lenpot * rando)
                new_group.append(pots[i].pop(numbo))
            groups.append(new_group)
        for group in groups:
            countries_in_group = []
            for country in group:
                countries_in_group.append(country[0])
            new_group = Group(countries_in_group, False, 1)
            self.round_groups.append(new_group)
        for group in self.round_groups:
            group.print_standings()


    def draw_ties(self, teams):
        ties = []
        pot1 = []
        pot2 = []
        pot_size = len(teams) // 2
        for i in range(pot_size):
            pot1.append(teams[i])
            pot2.append(teams[i + pot_size])



        for i in range(pot_size):
            new_tie = []
            lenpot = len(pot1)
            rando = random.random()
            numbo = int(lenpot * rando)
            new_tie.append(pot1.pop(numbo))
            lenpot = len(pot2)
            rando = random.random()
            numbo = int(lenpot * rando)
            new_tie.append(pot2.pop(numbo))
            ties.append(new_tie)
        return ties

    def add_ties_round(self, num_of_teams_competing, seeded=True):
        self.teams.sort(key=sort_helper_3, reverse=True)
        competing_counter = num_of_teams_competing
        list_of_teams_in_round = []
        for team in self.teams:
            if team[1] < self.current_round:
                continue
            if competing_counter > 0:
                list_of_teams_in_round.append(team)
                competing_counter -= 1
            else:
                team[1] += 1
        round_ties_help = self.draw_ties(list_of_teams_in_round)
        for tie in round_ties_help:
            countries_in_tie = []
            for country in tie:
                countries_in_tie.append(country[0])
            new_group = Group(countries_in_tie, False, 2, tie=True)
            self.round_groups.append(new_group)
        for group in self.round_groups:
            group.print_standings()


    def play_current_round(self):
        current_round = self.rounds[self.current_round - 1]
        self.get_teams_for_round(current_round)
        current_round.play_round()
        self.current_round += 1



    def print_current_matchday(self, round_groups):
        for group in round_groups:
            group.print_current_matchday()

    def play_current_matchday(self, round_groups):
        for group in round_groups:
            group.play_current_matchday()

    def increment_matchday(self, round_groups):
        matchdays_to_play = False
        for group in round_groups:
            if group.increment_matchday():
                matchdays_to_play = True
        return matchdays_to_play

    def get_title(self):
        return self.title

class Match:

    def __init__(self, home_country, away_country, print_package, home_score=0, away_score=0, neutral=False, played=False, winner=False):
        self.print_package = []
        for part in print_package:
            self.print_package.append(part)
        self.home_country = home_country
        self.away_country = away_country
        self.home_score = home_score
        self.away_score = away_score
        self.neutral = neutral
        self.played = played
        self.winner = winner
        self.pens = False
        self.pwinner = 0
        self.aggregate = 0
        self.display_string = ''
        self.set_print_package()

    def set_print_package(self):
        self.print_package.append(self.home_country.get_name() + " vs. " + self.away_country.get_name())

    def add_to_display_string(self, new_str_things):
        for new_str in new_str_things:
            self.display_string += new_str

    def set_winner_true(self):
        self.winner = True

    def set_aggregate(self, home_score, away_score):
        self.print_package.append("(First Leg: " + self.away_country.get_name() + " " + str(away_score) + " - " + str(home_score) + " " + self.home_country.get_name() + ")")
        self.aggregate = home_score - away_score

    def get_home_goals(self):
        return self.home_score

    def get_away_goals(self):
        return self.away_score

    def get_home_code(self):
        return self.home_country.get_code()

    def get_away_code(self):
        return self.away_country.get_code()

    def get_pens(self):
        return self.pens

    def get_pwinner(self):
        return self.pwinner

    def print_match(self):
        return
        if not self.played:
            #print(self.home_country.get_code() + " vs. " + self.away_country.get_code())
            self.add_to_display_string([self.home_country.get_code(), ' vs. ', self.away_country.get_code(), '\n'])
        else:
            #print(self.home_country.get_code + " " + str(self.home_score) + " - " + str(self.away_score) + " " + self.away_country.get_code())
            self.add_to_display_string([self.home_country.get_code, " ", str(self.home_score), " - ", str(self.away_score),
                                       " ", self.away_country.get_code(), "\n"])

    def play_match(self):
        if self.played:
            #print("Match already played")
            self.add_to_display_string(["Match already played", '\n'])
        else:
            elo_home_string = "{:.3f}".format(self.home_country.get_elo())
            elo_away_string = "{:.3f}".format(self.away_country.get_elo())
            self.print_package.append(elo_home_string + " vs. " + elo_away_string)
            self.print_package.append("------------MATCH BEGIN------------------")
            self.sim_game()
            self.played = True
        for old_str in self.print_package:
            print(old_str)
        print(self.display_string)

    def sim_game(self):
        diff = self.home_country.get_elo() - self.away_country.get_elo()
        home_score = 0
        away_score = 0
        if not self.neutral:
            diff = diff + 100
        home_rand = .017 + (.000017 * diff)
        away_rand = .017 - (.000017 * diff)
        if home_rand < .002:
            home_rand = .002
        if away_rand < .002:
            away_rand = .002
        # print(home_rand)
        # print(away_rand)
        for i in range(1, 91):
            if random.random() < home_rand:
                self.print_package.append(self.home_country.get_name() + " Goal in minute " + str(i))
                #self.add_to_display_string([self.home_country.get_name(), " Goal in minute ", str(i), '\n'])
                home_score = home_score + 1
            if random.random() < away_rand:
                self.print_package.append(self.away_country.get_name() + " Goal in minute " + str(i))
                #self.add_to_display_string([self.away_country.get_name(), " Goal in minute ", str(i), '\n'])
                away_score = away_score + 1


        #self.add_to_display_string(["Final score: ", self.home_country.get_code(), str(home_score), "-", self.away_country.get_code(),
              #str(away_score), "\n"])
        self.print_package.append("------------------FULL TIME-----------------")
        self.print_package.append("Final score: " + self.home_country.get_code() + str(home_score) + "-" + self.away_country.get_code() + str(away_score) + "\n")
        result = home_score - away_score

        if (result + self.aggregate == 0) and self.winner:
            for i in range(91, 121):
                if random.random() < home_rand:
                    #print(self.home_country.get_name() + " Goal in minute " + str(i))
                    self.add_to_display_string([self.home_country.get_name(), " Goal in minute ", str(i), '\n'])
                    home_score = home_score + 1
                if random.random() < away_rand:
                    #print(self.away_country.get_name() + " Goal in minute " + str(i))
                    self.add_to_display_string([self.away_country.get_name(), " Goal in minute ", str(i), '\n'])
                    away_score = away_score + 1

            #print("Final score (after extra time): " + self.home_country.get_code() + str(home_score) + "-" +
                  #self.away_country.get_code() + str(away_score) + "\n")
            self.add_to_display_string(["Final score (after extra time): ", self.home_country.get_code(), str(home_score), "-",
                  self.away_country.get_code(), str(away_score), "\n"])

        pens = False
        pwinner = 0
        if ((home_score + self.aggregate) == away_score) and self.winner:
            pens = True
            if random.random() < 0.5:
                #print(self.home_country.get_name() + " wins in penalty shootout!")
                self.add_to_display_string([self.home_country.get_name(), " wins in penalty shootout!", '\n'])
                pwinner = 0
            else:
                #print(self.away_country.get_name() + " wins in penalty shootout!")
                self.add_to_display_string([self.away_country.get_name(), " wins in penalty shootout!", '\n'])
                pwinner = 1

        set_elo(self.home_country, self.away_country, result, not self.neutral)
        self.home_score = home_score
        self.away_score = away_score
        self.pens = pens
        self.pwinner = pwinner

class Tie:

    def __init__(self, teams, neutral, robin, print_package):
        self.print_package = []
        for part in print_package:
            self.print_package.append(part)
        self.teams = teams
        self.neutral = neutral
        self.robin = robin
        self.current_matchday = 0
        self.matchdays = self.create_match_list()
        self.agg_home_score = 0
        self.agg_away_score = 0
        self.pwinner = None
        self.winner = None
        self.loser = None
        self.win_score = 0
        self.lose_score = 0



    def get_winner(self):
        return self.winner

    def get_loser(self):
        return self.loser

    def increment_matchday(self):
        self.current_matchday += 1
        if self.current_matchday >= len(self.matchdays):
            return False
        return True

    def create_match_list(self):
        home_match = Match(self.teams[0], self.teams[1], self.print_package)
        away_match = Match(self.teams[1], self.teams[0], self.print_package)
        if self.robin == 1:
            return [home_match]
        if self.robin == 2:
            return [away_match, home_match]

    def print_current_matchday(self):
        return
        match = self.matchdays[self.current_matchday]
        if self.current_matchday == 1:
            print("First Leg: " + match.get_away_code() + ": " + str(self.agg_away_score) + " " + match.get_home_code()
                  + ": " + str(self.agg_home_score))
        print(match.get_home_code() + " vs. " + match.get_away_code())

    def play_current_matchday(self):
        match = self.matchdays[self.current_matchday]
        if self.current_matchday == 1:
            match.set_aggregate(self.agg_home_score, self.agg_away_score)
            match.set_winner_true()
        if len(self.matchdays) == 1:
            match.set_winner_true()
        match.play_match()
        self.update_stats(match)
        if self.current_matchday == len(self.matchdays) - 1:
            self.decide_winners()

    def update_stats(self, match):
        if len(self.matchdays) == 2 and self.current_matchday == 0:
            self.agg_away_score += match.get_home_goals()
            self.agg_home_score += match.get_away_goals()
        else:
            self.agg_away_score += match.get_away_goals()
            self.agg_home_score += match.get_home_goals()
        self.pwinner = match.get_pwinner()

    def print_result(self):
        print(self.winner.get_name() + ": " + str(self.win_score) + " - " + self.loser.get_name() + ": " + str(self.lose_score))
        if self.win_score == self.lose_score:
            print(self.winner.get_name() + " wins the penalty shootout.")

    def decide_winners(self):
        home_country = self.teams[0]
        away_country = self.teams[1]
        if self.agg_home_score > self.agg_away_score:
            #home_country.increment_round()
            #print(home_country.get_name() + " advances with an aggregate score " + str(self.agg_home_score) + "-" +
                  #str(self.agg_away_score))
            #print(away_country.get_name() + " is eliminated.")
            self.winner = home_country
            self.loser = away_country
            self.win_score = self.agg_home_score
            self.lose_score = self.agg_away_score
        elif self.agg_home_score < self.agg_away_score:
            #away_country.increment_round()
            #print(away_country.get_name() + " advances with an aggregate score " + str(self.agg_away_score) + "-" +
                  #str(self.agg_home_score))
            #print(home_country.get_name() + " is eliminated.")
            self.winner = away_country
            self.loser = home_country
            self.win_score = self.agg_away_score
            self.lose_score = self.agg_home_score
        else:
            if self.pwinner == 0:
                #home_country.increment_round()
                #print(home_country.get_name() + " advances on penalties after an aggregate score "
                      #+ str(self.agg_away_score) + "-" + str(self.agg_home_score))
                #print(away_country.get_name() + " is eliminated.")
                self.winner = home_country
                self.loser = away_country
            else:
                #away_country.increment_round()
                #print(away_country.get_name() + " advances on penalties after an aggregate score "
                      #+ str(self.agg_away_score) + "-" + str(self.agg_home_score))
                #print(home_country.get_name() + " is eliminated.")
                self.winner = away_country
                self.loser = home_country
            self.win_score = self.agg_away_score
            self.lose_score = self.agg_home_score





class Group:

    def __init__(self, teams, neutral, robin, print_package):
        self.print_package = []
        for part in print_package:
            self.print_package.append(part)
        self.teams_in_group = []
        for team in teams:
            # 0-country object, 1-wins, 2-draws, 3-losses, 4-goals for, 5-goals against, 6-goal difference, 7-points
            group_team = [team, 0, 0, 0, 0, 0, 0, 0]
            self.teams_in_group.append(group_team)

        self.neutral = neutral
        self.robin = robin
        self.matchdays = self.create_match_list()
        self.current_matchday = 0


    def get_next_matchday(self):
        return self.matchdays[self.current_matchday]

    def increment_matchday(self):
        self.current_matchday += 1
        if self.current_matchday >= len(self.matchdays):
            return False
        return True

    def get_current_matchday(self):
        if self.current_matchday >= len(self.matchdays):
            return -1
        return self.current_matchday

    def print_current_matchday(self):
        for match in self.matchdays[self.current_matchday]:
            print(match.get_home_code() + " vs. " + match.get_away_code())

    def play_current_matchday(self):
        for match in self.matchdays[self.current_matchday]:
            match.play_match()
            self.update_stats(match)
            print()


    #def input_match(self, home_country, away_country, result):
        #self.update_stats((self.matchdays[i_1][i_2][0]), result[0], result[1])
        #self.update_stats((self.matchdays[i_1][i_2][1]), result[1], result[0])

    def update_stats(self, match):
        home_goals = match.get_home_goals()
        away_goals = match.get_away_goals()
        for i in range(len(self.teams_in_group)):
            if match.get_home_code() == self.teams_in_group[i][0].get_code():
                index = i
        home_team_stats_list = self.get_teams_in_group()[index]
        for i in range(len(self.teams_in_group)):
            if match.get_away_code() == self.teams_in_group[i][0].get_code():
                index = i
        away_team_stats_list = self.get_teams_in_group()[index]
        if home_goals > away_goals:
            home_team_stats_list[1] = home_team_stats_list[1] + 1
            home_team_stats_list[7] = home_team_stats_list[7] + 3
            away_team_stats_list[3] = away_team_stats_list[3] + 1
        elif home_goals == away_goals:
            home_team_stats_list[2] = home_team_stats_list[2] + 1
            home_team_stats_list[7] = home_team_stats_list[7] + 1
            away_team_stats_list[2] = away_team_stats_list[2] + 1
            away_team_stats_list[7] = away_team_stats_list[7] + 1
        else:
            home_team_stats_list[3] = home_team_stats_list[3] + 1
            away_team_stats_list[1] = away_team_stats_list[1] + 1
            away_team_stats_list[7] = away_team_stats_list[7] + 3
        home_team_stats_list[4] = home_team_stats_list[4] + home_goals
        home_team_stats_list[5] = home_team_stats_list[5] + away_goals
        home_team_stats_list[6] = home_team_stats_list[4] - home_team_stats_list[5]
        away_team_stats_list[4] = away_team_stats_list[4] + away_goals
        away_team_stats_list[5] = away_team_stats_list[5] + home_goals
        away_team_stats_list[6] = away_team_stats_list[4] - away_team_stats_list[5]



    def next_matchday(self):
        self.current_matchday = self.current_matchday + 1

    def get_teams_in_group(self):
        return self.teams_in_group

    def get_neutral(self):
        return self.neutral

    def create_match_list(self):
        odd = True
        matchday_num = len(self.teams_in_group)
        positions = (matchday_num + 1) // 2
        if len(self.teams_in_group) % 2 == 0:
            odd = False
            matchday_num = matchday_num - 1
        matchday_num = matchday_num * self.robin
        matchdays = []

        pos_array = [None]*positions
        for i in range(len(pos_array)):
            pos_array[i] = i

        for i in range(matchday_num):
            curr_match_day = []
            for j in range(positions - 1):
                team1 = self.teams_in_group[pos_array[j]][0]
                temp = ((positions - j) - 1) * 2
                team2 = self.teams_in_group[(pos_array[j] + temp) % ((positions * 2) - 1)][0]
                if i % 2 == 0:
                    new_match = Match(team1, team2, self.print_package)
                    curr_match_day.append(new_match)
                else:
                    new_match = Match(team2, team1, self.print_package)
                    curr_match_day.append(new_match)
                #print("______")
            if not odd:
                team1 = self.teams_in_group[pos_array[positions - 1]][0]
                team2 = self.teams_in_group[len(self.teams_in_group) - 1][0]
                if i % 2 == 0:
                    new_match = Match(team1, team2, self.print_package)
                    curr_match_day.append(new_match)
                    #curr_match_day.append([team1, team2, False])
                else:
                    new_match = Match(team2, team1, self.print_package)
                    curr_match_day.append(new_match)
                    #curr_match_day.append([team2, team1, False])
            # print("____")
            # print("____")
            for k in range(len(pos_array)):
                if pos_array[k] == 0:
                    if odd:
                        pos_array[k] = len(self.teams_in_group) - 1
                    else:
                        pos_array[k] = len(self.teams_in_group) - 2
                else:
                    pos_array[k] = pos_array[k] - 1
            matchdays.append(curr_match_day)
        if self.robin == 2 and len(matchdays) == 6:
            temp = matchdays[0]
            matchdays[0] = matchdays[3]
            matchdays[3] = temp
        return matchdays

    def get_standings(self):
        self.teams_in_group.sort(key=lambda item: (item[7], item[6], item[4]), reverse=True)
        return self.teams_in_group


    def print_standings(self):
        self.get_standings()
        print("                                      W - D - L  GF-GA\tGD\tPTS")
        index = 1
        for team_array in self.teams_in_group:
            print(f"{index}  {team_array[0].get_code()}  {team_array[0].get_name():30}{team_array[1]} - "
                  f"{team_array[2]} - {team_array[3]}   {team_array[4]}-{team_array[5]}   "
                  f"{team_array[6]}    {team_array[7]}")
            index = index + 1
            #print(str(index) + "\t" + team_array[0].get_code() + "\t\t" + team_array[0].get_name() + "\t\t" +
            #      str(team_array[1]) + "-" + str(team_array[2]) + "-" + str(team_array[3]) + "\t" + str(team_array[4])
            #      + "-" + str(team_array[5]) + "\t\t" + str(team_array[6]))
        print()


class Country:

    def __init__(self, code, name, elo, conf, region):
        self.conf = conf
        self.region = region
        self.code = code
        self.name = name
        self.elo = float(elo)

    def get_code(self):
        return self.code

    def get_name(self):
        return self.name

    def get_region(self):
        return self.region

    def get_elo(self):
        return self.elo

    def set_elo(self, elo):
        self.elo = elo

    def get_conf(self):
        return self.conf


class Runner:

    def __init__(self):

        self.countries_list = []
        self.competitions = []

    def create_competition(self, title, conf, region, teams):
        new_competition = Competition(title, conf, region, teams)
        self.competitions.append(new_competition)

    def list_competitions(self):
        for i in range(len(self.competitions)):
            print(str(i) + ": " + self.competitions[i].get_title())

    def competition_round_create(self, competition_number, num_of_teams, type, neutral, robin, round_number, draw_style="Pots",
                                 num_groups=1, num_advancing=None, sort_type="None"):
        self.competitions[competition_number].add_round(type, num_of_teams, num_advancing, neutral, robin, round_number,
                                                        num_groups, draw_style, sort_type)

    def competition_play_current_round(self, competition_number):
        self.competitions[competition_number].play_current_round()

    def get_country_by_code(self, code):
        for country in self.countries_list:
            if code == country.code:
                return country

    #def do_group(self, group):

        #matchday = group.get_next_matchday()
        #for game_index in range(len(matchday)):
            #result = self.run_game_auto(group.get_teams_in_group()[matchday[game_index][0]][0],
                                        #group.get_teams_in_group()[matchday[game_index][1]][0],
                                        #group.get_neutral(), 0)
            #group.input_match(group.get_current_matchday(), game_index, result)
        #width = 1200
        #height = 850
        #self.win = GraphWin("Standings Window", width, height)
        #self.show_standings(self.win, group)

    def hard_load_country(self, conf, region):
        code = input("Enter Code: ")
        name = input("Enter Name: ")
        elo = input("Enter Elo: ")
        #conf = input("Enter Confederation: ")
        #region = input("Enter Region: ")
        print("-----------------------")
        self.countries_list.append(Country(code, name, elo,
                                           conf, region))

    def show_standings(self, win, group):
        group_array = group.get_standings()
        width = 1200
        height = 850
        eff_height = 800
        text_to_write = Text(Point(50, 25), "Code")
        text_to_write.draw(win)
        text_to_write = Text(Point(200, 25), "Country Name")
        text_to_write.draw(win)
        text_to_write = Text(Point(350, 25), "W - D - L")
        text_to_write.draw(win)
        text_to_write = Text(Point(500, 25), "GF - GA")
        text_to_write.draw(win)
        text_to_write = Text(Point(600, 25), "GD")
        text_to_write.draw(win)
        text_to_write = Text(Point(width - 50, 25), "Points")
        text_to_write.draw(win)
        #win.yUp()

        for i in range(len(group_array)):
            line_height = ((1 / len(group_array)) * eff_height * i) + 50
            line = Line(Point(0, line_height), Point(width, line_height))
            line.draw(win)

            mid_height = (eff_height *  ((( 2* (i+1)) - 1)) / 8) + 50
            text_to_write = Text(Point(10, mid_height), i+1)
            text_to_write.draw(win)
            text_to_write = Text(Point(50, mid_height), group_array[i][0].get_code())
            text_to_write.draw(win)
            text_to_write = Text(Point(200, mid_height), group_array[i][0].get_name())
            text_to_write.draw(win)
            text_to_write = Text(Point(350, mid_height), str(group_array[i][1]) + " - " + str(group_array[i][2]) + " - "
                                 + str(group_array[i][3]))
            text_to_write.draw(win)
            text_to_write = Text(Point(500, mid_height), str(group_array[i][4]) + " - " + str(group_array[i][5]))
            text_to_write.draw(win)
            text_to_write = Text(Point(600, mid_height), str(group_array[i][6]))
            text_to_write.draw(win)

            text_to_write = Text(Point(width - 50, mid_height), str(group_array[i][7]))
            text_to_write.draw(win)

        win.getMouse()
        win.close()

    def print_countries(self, conf):

        self.countries_list.sort(key=sort_helper, reverse=True)

        index = 1

        no_conf_check = False

        if conf is not None:
            print(conf + " Rankings")
        else:
            print("World Rankings")
            no_conf_check = True

        for country in self.countries_list:
            if no_conf_check or country.get_conf() == conf or country.get_region() == conf:
                print(str(index) + ") " + country.get_code() + " " + country.get_name() + " " +
                      str(int(country.get_elo())))
                index = index + 1

    # Opens Text File, creates Country objects, adds to self.countries_list
    def load_countries(self, file_name):

        for line in open(file_name, 'r'):
            count = 0
            st1 = 0
            st2 = 0
            country_code = ""
            country_name = ""
            country_conf = ""
            country_elo = ""
            while st2 < len(line):
                if line[st2] == "_" or line[st2] == "!":
                    if count % 5 == 0:
                        country_code = line[st1:st2]
                    elif count % 5 == 1:
                        country_name = line[st1:st2]
                    elif count % 5 == 2:
                        country_elo = line[st1:st2]
                    elif count % 5 == 3:
                        country_conf = line[st1:st2]
                    else:
                        country_region = line[st1:st2]
                        self.countries_list.append(Country(country_code, country_name, country_elo,
                                                           country_conf, country_region))

                    st1 = st2 + 1
                    count = count + 1
                st2 = st2 + 1

    def load_countries_temp(self, file_name):

        for line in open(file_name, 'r'):
            count = 0
            st1 = 0
            st2 = 0
            country_code = ""
            country_name = ""
            country_conf = ""
            country_elo = ""
            while st2 < len(line):
                if line[st2] == "_" or line[st2] == "!":
                    if count % 4 == 0:
                        country_code = line[st1:st2]
                    elif count % 4 == 1:
                        country_name = line[st1:st2]
                    elif count % 4 == 2:
                        country_elo = line[st1:st2]
                    else:
                        country_conf = line[st1:st2]
                        st1 = st2 + 1
                        st2 = st2 + 1
                        while st2 < len(line) and (not line[st2] == "_"):
                            st2 = st2 + 1
                        country_region = line[st1:st2 - 3]
                        st2 = st2 - 4
                        print(country_region)
                        self.countries_list.append(Country(country_code, country_name, country_elo, country_conf,
                                                           country_region))

                    st1 = st2 + 1
                    count = count + 1
                st2 = st2 + 1

    def save_file(self, file_name):
        clear_file(file_name)
        for country in self.countries_list:
            write_country_to_file(country, file_name)

    def save_file_manual(self, file_name, starter):
        for i in range(starter, len(self.countries_list)):
            country = self.countries_list[i]
            print(country.get_name())
            corr_elo = float(input(": Input elo: "))
            country.set_elo(corr_elo)
            write_country_to_file(country, file_name)


    def input_game(self, neutral):
        not_ready_to_exit = True
        hc = None
        ac = None
        while not_ready_to_exit:
            hcc = input("Home Team Code: ")
            acc = input("Away Team Code: ")
            # neu = int(input("Neutral? "))
            # winner = int(input("Winner Needed? "))
            for country in self.countries_list:
                if country.get_code() == hcc:
                    hc = country
                elif country.get_code() == acc:
                    ac = country
            if hc is not None and ac is not None:
                not_ready_to_exit = False
        home_score = int(input("Home Score: "))
        away_score = int(input("Away Score: "))
        result = home_score - away_score
        set_elo(hc, ac, result, not neutral)

    def run_game_auto(self, team1, team2, neu, winner):
        Match.sim_game(team1, team2, neu, winner)

    def run_game(self):
        not_ready_to_exit = True
        hc = None
        ac = None
        winner = None
        while not_ready_to_exit:
            hcc = input("Home Team Code: ")
            acc = input("Away Team Code: ")
            neu = int(input("Neutral? "))
            winner = int(input("Winner Needed? "))
            for country in self.countries_list:
                if country.get_code() == hcc:
                    hc = country
                elif country.get_code() == acc:
                    ac = country
            if hc is not None and ac is not None:
                not_ready_to_exit = False

        Match.sim_game(hc, ac, neu, winner)

    def extra_time(self, neutral):
        not_ready_to_exit = True
        home_country = None
        away_country = None
        while not_ready_to_exit:
            hcc = input("Home Team Code: ")
            acc = input("Away Team Code: ")
        # neu = int(input("Neutral? "))
        # winner = int(input("Winner Needed? "))
            for country in self.countries_list:
                if country.get_code() == hcc:
                    home_country = country
                elif country.get_code() == acc:
                    away_country = country
            if home_country is not None and away_country is not None:
                not_ready_to_exit = False
        diff = home_country.get_elo() - away_country.get_elo()
        home_score = 0
        away_score = 0
        if not neutral:
            diff = diff + 100
        home_rand = .017 + (.000017 * diff)
        away_rand = .017 - (.000017 * diff)
        if home_rand < .002:
            home_rand = .002
        if away_rand < .002:
            away_rand = .002
        for i in range(91, 121):
            if random.random() < home_rand:
                print(home_country.get_name() + " Goal in minute " + str(i))
                home_score = home_score + 1
            if random.random() < away_rand:
                print(away_country.get_name() + " Goal in minute " + str(i))
                away_score = away_score + 1

        print("Final score (after extra time): " + home_country.get_code() + str(home_score) + "-" +
              away_country.get_code() + str(away_score) + "\n")

        if home_score == away_score:
            if random.random() < 0.5:
                print(home_country.get_name() + " wins in penalty shootout!")
            else:
                print(away_country.get_name() + " wins in penalty shootout!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #win = GraphWin("Math", 1100, 200)
    #win.getMouse()
    #win.close()


    # draw_groups_3_3()


    # runner.draw_groups_4_4()
    # draw_ties()
    # runner.clear_file()
    # runner.hard_load_country()
    #runner.load_countries("TestFile.txt")


    #runner.save_file_manual("cycle_start.txt", 154)

    #runner.print_countries(conf=None)



    #c1 = runner.countries_list[14]
    #c2 = runner.countries_list[114]
    #c3 = runner.countries_list[140]
    #c4 = runner.countries_list[134]
    #c5 = runner.countries_list[91]
    #c6 = runner.countries_list[43]

    #test_group = Group([c1, c4, c5, c6], 0, 2)

    #runner.do_group(test_group)

    #test_group.print_standings()
    # for i in range(10):
       # runner.hard_load_country("UEFA", "EEFA")
    # runner.save_for_now()
    # runner.print_countries()
    # runner.clear_file()
    # for i in range(8):
    # runner.extra_time(0)
    # runner.input_game(False)
    # for i in range(2):
      # runner.run_game()
    #runner.save_file()
    # runner.print_countries(None)
    # runner.print_countries()

    # runner.sim_game(usa, mex, 0)
    # runner.sim_game(usa, aia, 1)

    # sim_game(skn, sin, False)
    # sim_game(brb, guy, False)
    # draw_groups_3_3()










    #2026 Cycle Work Down Here
    runner = Runner()
    runner.load_countries("testwork.txt")
    aff_champ_country_codes = ["THA", "VIE", "PHI", "MAS", "IDN", "SGP", "MYA", "CAM", "LAO", "TLS", "BRU"]
    aff_champ_countries = []
    for code in aff_champ_country_codes:
        aff_champ_countries.append(runner.get_country_by_code(code))
    runner.create_competition("2022 AFF Championship", "AFC", "AFF", aff_champ_countries)
    runner.list_competitions()
    runner.competition_round_create(0, 2, "Ties", False, 2, 1)
    runner.competition_round_create(0, 10, "Groups", False, 1, 2, num_groups=2, num_advancing=4, sort_type="Group Position")
    runner.competition_round_create(0, 4, "Knockout", False, 2, 3, draw_style="Seeded")
    runner.competition_play_current_round(0)
    runner.competition_play_current_round(0)
    runner.competition_play_current_round(0)


    gulf_cup_country_codes = ["IRQ", "BHR", "QAT", "KSA", "UAE", "OMA", "KUW", "YEM"]
    gulf_cup_countries = []
    for code in gulf_cup_country_codes:
        gulf_cup_countries.append(runner.get_country_by_code(code))
    runner.create_competition("25th Arabian Gulf Cup", "AFC", "WAFF", gulf_cup_countries)
    runner.list_competitions()
    runner.competition_round_create(1, 8, "Groups", True, 1, 1, num_groups=2, num_advancing=4, sort_type="Group Position")
    runner.competition_round_create(1, 4, "Knockout", True, 1, 2, draw_style="Seeded")
    runner.competition_play_current_round(1)
    runner.competition_play_current_round(1)

    acon_country_codes = ["CIV", "SEN", "MAR", "ALG", "TUN", "NGA", "EGY", "CMR", "GHA", "MLI", "BFA", "COD", "RSA",
                          "CPV", "GUI", "UGA", "BEN", "ZAM", "GAB", "CGO", "MAD", "KEN", "MTN", "GNB", "SLE", "NAM",
                          "NIG", "EQG", "LBY", "MOZ", "ZIM", "TOG", "SDN", "ANG", "MWI", "CTA", "TAN", "COM", "RWA",
                          "ETH", "BDI", "LBR", "LES", "SWZ", "BOT", "GAM", "SSD", "MRI", "CHA", "STP", "DJI", "SOM",
                          "SEY", "ERI"]
    acon_countries = []
    for code in acon_country_codes:
        acon_countries.append(runner.get_country_by_code(code))
    runner.create_competition("2023 Africa Cup of Nations", "CAF", None, acon_countries)
    runner.list_competitions()
    runner.competition_round_create(2, 12, "Ties", False, 2, 1)
    runner.competition_round_create(2, 48, "Groups", False, 2, 2, num_advancing=24, sort_type="Group Position", num_groups=12)
    runner.competition_round_create(2, 24, "Groups", True, 1, 3, num_advancing=16, sort_type="Group Rank", num_groups=6)
    runner.competition_round_create(2, 16, "Knockout", True, 1, 4, draw_style="Seeded")
    runner.competition_play_current_round(2)
    runner.competition_play_current_round(2)
    runner.competition_play_current_round(2)
    runner.competition_play_current_round(2)
