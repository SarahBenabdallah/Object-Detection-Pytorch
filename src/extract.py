def extract_hour(s):
    """extract hour of the video from the input"""
    hour = ""
    # if hour is composed from one number : 1-9
    if s[len(s) - 7] == '_':
        hour = (s[len(s) - 6])
    # if hour is composed from two numbers : 10-00
    else:
        hour = (s[len(s) - 7:len(s) - 5])
    return (hour)


def extract_index(s):
    """extract index of the highway video from the input"""
    i = s.index("_") + 1
    index = ""
    while i != len(s)-1 and s[i] != '_':
        index += s[i]
        i += 1
    return (index)


def get_area_coord(zones, highway):
    """extract the coord of area of interest"""
    highways = list(zones.keys())
    i = 0
    while i < len(zones):
        if highway == highways[i]:
            xmin = min(zones[highway][0])[0]
            xmax = max(zones[highway][0])[0]
            ymin = min(zones[highway][0])[1]
            ymax = max(zones[highway][0])[1]
            break
        i += 1
    if i == len(highways):
        print("the interest area of this video is not available")
    return xmin, xmax, ymin, ymax
