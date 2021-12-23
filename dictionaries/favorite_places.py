favorite_places = {
    'sonic': ['green hill'],
    'tails': ['emerald coast', 'chemical plant'],
    'knuckles': ['stardust speedway', 'speed highway', 'lava mountain'],
}

for name, zones in favorite_places.items():
    if len(zones) > 1:
        print(f"\n{name.title()}'s favorite zones are:")
    else:
        print(f"\n{name.title()}'s favorite zone is:")
    for zone in zones:
        print(f"\t{zone.title()}")