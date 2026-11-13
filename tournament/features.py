def make_fixture(fixture_id, home_id, away_id) -> dict:
    make_dict = {"id":fixture_id, "home_id": home_id, "away_id": away_id, "status":"pending", "home_score": None, "away_score": None}
    return make_dict
def generate_fixture_id(league) -> str:
    return "M" + str(league["next_fixture_num"]).zfill(3)

def generate_fixtures(league: dict) -> tuple[bool, str]:
    n = len(league["teams"])
    if n < 4:
        return False, "Need at least 4 teams to generate fixtures"
    if league["fixtures"]:
        return False, "Fixtures already generated for this season"

    teams = league["teams"]
    next_num = league["next_fixture_num"]
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            fixture_id = next_num + count
            
            fixture = {
                "id": fixture_id,
                "home": teams[i],
                "away": teams[j],
                "played": False,
                "home_score": None,
                "away_score": None,
            }
            
            league["fixtures"].append(fixture)
            count += 1

    league["next_fixture_num"] += count
    return True, f"Generated {count} fixtures"

     
def get_fixture(league, fixture_id) -> dict | None:
    for fiture in league["fixtures"]:
        if fiture["id"] == fixture_id:
            return fiture
        
        return None
def list_fixtures(league) -> list[dict]:
    return list(league["fixtures"])