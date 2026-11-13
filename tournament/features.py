def make_feature(fexture_id, home_id, away_id) -> dict:
    make_dict = {"id":fexture_id, "home_id": home_id, "away_id": away_id, "status":"pending", "home_score": None, "away_score": None}
    return make_dict