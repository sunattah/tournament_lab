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