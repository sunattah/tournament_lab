def make_fixture(fexture_id, home_id, away_id) -> dict:
    make_dict = {"id":fexture_id, "home_id": home_id, "away_id": away_id, "status":"pending", "home_score": None, "away_score": None}
    return make_dict
def generate_fixture_id(league) -> str:
    return "M" + str(league["next_fixture_num"]).zfill(3)

def generate_fixtures(league) -> tuple[bool, str]:
    if len(league["teams"]) < 4:
        return (False, "Need at least 4 teams to generate fixtures")
    if league["fextures"] == "":
        return (False,  "Fixtures already generated for this season")
     
def get_fixture(league, fixture_id) -> dict | None:
    for fiture in league["fixtures"]:
        if fiture == fixture_id:
            return "match by ID"
        else:
            return None
def list_fixtures(league) -> list[dict]:
    return list(league["fixtures"])