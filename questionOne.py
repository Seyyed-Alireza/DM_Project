class Station:
    def __init__(self, station_id, connected_stations):
        self.id = station_id
        self.connected_stations = connected_stations  

    def add_connection(self, station_id):
        self.connected_stations.append(station_id)

def station_index(station_id):
    global stations
    for station in stations:
        if station.id == station_id:
            return stations.index(station)

def find_lowest_stations(start_station_id, end_station_id):
    global stations
    routes_from_start_to_end = []
    temp_routes = [[start_station_id]]
    temp = []
    if start_station_id == end_station_id:
        return 0
    else:
        while True:
            for route in temp_routes:
                end_id = route[-1]
                for connected_station in stations[station_index(station_id=end_id)].connected_stations:
                    if connected_station not in route:
                        temp.append(route + [connected_station])
                    if connected_station == end_station_id:
                        routes_from_start_to_end.append(route + [connected_station])
            if len(temp) == 0:
                break
            temp_routes = temp
            temp = []
        if len(routes_from_start_to_end) == 0:
            return -1
        min_route = routes_from_start_to_end[0]
        for route in routes_from_start_to_end:
            if len(route) < len(min_route):
                min_route = route
        return len(min_route) - 1
        
stations = []

def lowest_stations(input_text):
    global stations
    stations.clear()
    ans = ''
    lines = [line.strip() for line in input_text.strip().split('\n')]
    try:
        m, n = list(map(int, lines[0].split()))
    except:
        return 'invalid'
    if len(lines) != m + n + 2:
        return 'invalid'
    try:
        for station_name in lines[1: m + 1]:
            stations.append(Station(station_name, []))
        for connection in lines[m + 1: -1]:
            source, destination = connection.split()
            stations[station_index(source)].add_connection(destination)
            stations[station_index(destination)].add_connection(source)
    except:
        return 'invalid'
    source = lines[-1]
    if source not in [station.id for station in stations]:
        return 'invalid'
    for station in stations:
        ans += station.id + ' ' + str(find_lowest_stations(source, station.id)) + '\n'
    return ans.strip()


'''
4 2
Shiraz
Tehran
Isfahan
Mashhad
Shiraz Tehran
Mashhad Isfahan
Mashhad
'''