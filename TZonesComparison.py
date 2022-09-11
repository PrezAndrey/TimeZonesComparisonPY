zone_12 = [-12]
zone_11 = [-11]
zone_10 = [-10]
zone_9 = [-9]
zone_8 = [-8]
zone_7 = [-7, "los-angeles"]
zone_6 = [-6]
zone_5 = [-5, "chicago"]
zone_4 = [-4, "new-york", "miami"]
zone_3 = [-3]
zone_2 = [-2]
zone_1 = [-1]
zone0 = [0]
zone1 = [1]
zone2 = [2]
zone3 = [3, "moscow"]
zone4 = [4, "dubai"]
zone5 = [5]
zone6 = [6]
zone7 = [7]
zone8 = [8, "bali"]
zone9 = [9]
zone10 = [10]
zone11 = [11]
zone12 = [12]

list_of_zones = [zone_12, zone_11, zone_10, zone_9, zone_8, zone_7, zone_6, zone_5, zone_4, zone_3, zone_2, zone_1, zone0, zone1, zone2, zone3, zone4, zone5, zone6, zone7, zone8, zone9, zone10, zone11, zone12]

time = ["0:00", "1:00", "2:00", "3:00", "4:00", "5:00", "6:00", "7:00", "8:00", "9:00", "10:00", "11:00","12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]

place1_zone = 0
place2_zone = 0

place1 = input()
place2 = input()


def check_time_zone(list_of_zones, place1, place2):
    
    place1_checked = False
    place2_checked = False
    
    place1_zone = 0
    place2_zone = 0    
    
    for i in range(len(list_of_zones)):
        if place1.lower() in list_of_zones[i] and not place1_checked:
            place1_checked = True
            place1_zone = list_of_zones[i][0]
        
        if place2.lower() in list_of_zones[i] and not place2_checked:
            place2_checked = True
            place2_zone = list_of_zones[i][0]
    
        if place1_checked and place2_checked:
            break
    else:
        print("Unknow city")

    return (place1_zone, place2_zone)

def show_comparison(shift, time):
    
    second_time = time.copy()
    
    for i in range(abs(shift)):
        second_time.insert(0, second_time[-1])
        second_time.pop()
    print(second_time)
    print(f"{place1} --- {place2}")
    
    for x in range(len(time)):
        print(f"{time[x]} --- {second_time[x]}")

zone1, zone2 = check_time_zone(list_of_zones, place1, place2)
time_shift = zone2 - zone1
print(zone1, zone2, time_shift)
show_comparison(time_shift, time)






        
        
        