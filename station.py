# Riyaz Faizullabhoy
# 1/14/2013
# Bart Station Decoder


station_list = ["12th", "16th", "19th", "24th", "ashb", "balb", "bayf", "cast", "civc", "cols", "colm", "conc", "daly", "dbrk", "dubl", "deln", "plza", "embr", "frmt", "ftvl", "glen", "hayw", "lafy", "lake", "mcar", "mlbr", "mont", "nbrk", "ncon", "orin", "pitt", "phil", "powl", "rich", "rock", "sbrn", "sfia", "sanl", "shay", "ssan", "ucty", "wcrk", "woak"]


def match_stations(orig, dest):
    input = [orig.lower(), dest.lower()]
    output = []

    for s in input:
        global station_list
        if len(s) == 4 and s in station_list:
            output.append(s.upper())
            continue

        if "12" in s:
            res = "12TH"
        elif "16th" in s:
            res = "16TH"
        elif "19th" in s:
            res = "19TH"
        elif "24th" in s:
            res = "24TH"
        elif "ashby" in s:
            res = "ASHB"
        elif "balboa" in s:
            res = "BALB"
        elif "bay" in s and "fair" in s:
            res = "BAYF"
        elif "castro" in s:
            res = "CAST"
        elif "civic" in s:
            res = "CIVC"
        elif "coliseum" in s or ("oak" in s and "airport" in s):
            res = "COLS"
        elif "colma" in s:
            res = "COLM"
        elif "concord" in s and "north" not in s:
            res = "CONC"
        elif "daly" in s:
            res = "DALY"
        elif ("downtown" in s or "dtwn" in s) and "berkeley" in s:
            res = "DBRK"
        elif "dublin" in s or "pleasanton" in s:
            res = "DUBL"
        elif "norte" in s:
            res = "DELN"
        elif "plaza" in s:
            res = "PLZA"
        elif "embarcadero" in s:
            res = "EMBR"
        elif "fremont" in s:
            res = "FRMT"
        elif "fruitvale" in s:
            res = "FTVL"
        elif "glen" in s:
            res = "GLEN"
        elif "hayward" in s and "south" not in s:
            res = "HAYW"
        elif "lafayette" in s:
            res = "LAFY"
        elif "lake" in s:
            res = "LAKE"
        elif "macarthur" in s:
            res = "MCAR"
        elif "millbrae" in s:
            res = "MLBR"
        elif "montgomery" in s:
            res = "MONT"
        elif "north" in s and "berkeley" in s:
            res = "NBRK"
        elif ("north" in s and "concord" in s) or "martinez" in s:
            res = "NCON"
        elif "orinda" in s:
            res = "ORIN"
        elif "pittsburg" in s or "bay point" in s:
            res = "PITT"
        elif "pleasant" in s and "hill" in s:
            res = "PHIL"
        elif "powell" in s:
            res = "POWL"
        elif "richmond" in s:
            res = "RICH"
        elif "rock" in s:
            res = "ROCK"
        elif "bruno" in s:
            res = "SBRN"
        elif "sfo" in s or ("fran" in s and "airport" in s):
            res = "SFIA"
        elif "san" in s and "leandro" in s:
            res = "SANL"
        elif "south" in s and "hayward" in s:
            res = "SHAY"
        elif "south" in s and "san" in s and "francisco" in s:
            res = "SSAN"
        elif "union" in s:
            res = "UCTY"
        elif "walnut" in s:
            res = "WCRK"
        elif "west" in s:
            res = "WOAK"
        else:
            raise Exception("Invalid destination input: " + s)

        output.append(res)
    return output

