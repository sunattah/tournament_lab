def normalize_name(name: str) -> str:
## strip() then casefold(), return

    return    name.strip().casefold()
def make_team(team_id: str, name: str) -> dict:
    return {"id": team_id, "name": name}    