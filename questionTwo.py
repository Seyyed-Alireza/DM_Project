class Station:
    def __init__(self, station_id, connected_stations):
        self.id = station_id
        self.connected_stations = connected_stations  

    def add_connection(self, station_id, distance):
        self.connected_stations.append([station_id, float(distance)])

def station_index(station_id):
    global stations
    for station in stations:
        if station.id == station_id:
            return stations.index(station)

def find_shortest_path(start_station_id, end_station_id):
    global stations
    routes_from_start_to_end = []
    temp_routes = [[0, [start_station_id]]]
    temp = []
    if start_station_id == end_station_id:
        return 0
    else:
        while True:
            for route in temp_routes:
                end_id = route[1][-1]
                for connected_station in stations[station_index(station_id=end_id)].connected_stations:
                    if connected_station[0] not in route[1]:
                        temp.append([route[0] + connected_station[1], route[1] + [connected_station[0]]])
                    if connected_station[0] == end_station_id:
                        routes_from_start_to_end.append([route[0] + connected_station[1], route[1] + [connected_station[0]]])
            if len(temp) == 0:
                break
            temp_routes = temp
            temp = []
        if len(routes_from_start_to_end) == 0:
            return -1
        min_route = routes_from_start_to_end[0]
        for route in routes_from_start_to_end:
            if route[0] < min_route[0]:
                min_route = route
        return min_route
        
stations = []

def shortest_path(input_text):
    global stations
    stations.clear()
    ans = ''
    lines = [line.strip() for line in input_text.strip().split('\n')]
    try:
        m, n = list(map(int, lines[0].split()))
    except:
        return 'invalid'
    if len(lines) != m + n + 3:
        return 'invalid'
    try:
        for station_name in lines[1:m + 1]:
            stations.append(Station(station_name, []))
        for connection in lines[m + 1: -2]:
            source, destination, distanse = connection.split()
            distanse = float(distanse)
            stations[station_index(source)].add_connection(destination, distanse)
            stations[station_index(destination)].add_connection(source, distanse)
    except:
        return 'invalid'
    source = lines[-2]
    destination = lines[-1]
    if source not in [station.id for station in stations] or destination not in [station.id for station in stations]:
        return 'invalid'
    if source == destination:
        ans += '0.00\n'
        ans += source + ' ' + source
        return ans
    path = find_shortest_path(source, destination)
    if path == -1:
        return f'There is no way between {source} and {destination}'
    else:
        ans += f'{path[0]:.2f}\n'
        ans += ' '.join(path[1])
        return ans 


# input
'''
5 6
A
B
C
D
E
E C 136.81
D B 12.74
C B 14.63
B A 60.48
A D 45.63
A E 514.74
A
C
'''