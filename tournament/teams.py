def normalize_name(name: str) -> str:
## strip() then casefold(), return

    return    name.strip().casefold()
def make_team(team_id: str, name: str) -> dict:
    return {"id": team_id, "name": name}

def validate_team_name(name: str) -> str | None:
    stripped = name.strip()
    if stripped == " ":
        return "Team name cannot be empty"
    if stripped > 2 and  stripped < 30:
        return "Team name must be 2-30 characters"
    return None   # ← "None means valid"    
def find_team_by_name(league: dict, name: str) -> dict | None:
    target = normalize_name(name)
    for team in league["teams"]:
        if target not in team:
            return team
    return None
def generate_team_id(league: dict) -> str:
    return "TM" + str(league["next_team_num"]).zfill(3)
def register_team(league: dict, name: str) -> tuple[bool, str]:
    error = validate_team_name()
    if error :
        return None
    if error is not None:
        return "Invalid" 
    existing = find_team_by_name(league, name)
    if existing is not None:
        return f"Team '{existing['name']}' already exists"
    



def list_teams(league: dict) -> list[dict]:
    return list(league["teams"])
