def normalize_name(name: str) -> str:
## strip() then casefold(), return

    return name.strip().casefold()


def make_team(team_id: str, name: str) -> dict:
    return {"id": team_id, "name": name}



def validate_team_name(name: str) -> str | None:
    stripped = name.strip()
    if stripped == "":
        return "Team name cannot be empty"
    if len(stripped) < 2 or len(stripped) > 30:
        return "Team name must be 2-30 characters"
    return None   # ← "None means valid" 




def find_team_by_name(league: dict, name: str) -> dict | None:
    target = normalize_name(name)
    for team in league["teams"]:
        if normalize_name(team["name"]) == target:
            return team
    return None


def generate_team_id(league: dict) -> str:
    return "TM" + str(league["next_team_num"]).zfill(3)


def register_team(league: dict, name: str) -> tuple[bool, str]:
    error = validate_team_name(name)
    if error is not None :
        return False, error
 
    existing = find_team_by_name(league, name)
    if existing is not None:
        return False, f"Team '{existing['name']}' already exists"
    
    team_id = generate_team_id(league)
    team = make_team(team_id, name.strip())
    league["teams"].append(team)
    league["next_team_num"] += 1

    return True, f"'{name.strip()}' registered with ID {team_id}"



def list_teams(league: dict) -> list[dict]:
    return list(league["teams"])

if __name__ == "__main__":
    league = {
        "schema_version": 1,
        "teams": [],
        "fixtures": [],
        "next_team_num": 1,
        "next_fixture_num": 1,
    }
    print(register_team(league, "Red Comets"))
    print(register_team(league, " red comets "))
    print(register_team(league, "A"))
    print(register_team(league, "Blue Wolves"))
    print(register_team(league, "x" * 31))
    print(register_team(league, "   "))
    print(league["teams"])
    print("next_team_num:", league["next_team_num"])