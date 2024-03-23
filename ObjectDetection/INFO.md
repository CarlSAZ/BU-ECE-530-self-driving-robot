# Purpose

The object detection module collects reports of obstacles and hazards. The module keeps a database that can then be queried about the existing reports. This module does not provide any obstacle avoidance capabilities or object detection capabilities. It merely stores object detection reports to buffer for other systems to fetch.

Note: This probably doesn't work well as a REST style API, but this module will experiment with whether any database model will work.

## Object Collision API
### General User:
collision_detection_set_module()
* User will pass an object of the collision detection module

collision_add_sensor()
* User can pass a sensor object that is dependent on the sub detection module?

### Collision Detection / Avoidance Developers:
get_distances()
* returns distances measured from each sensor available?
* returns in a car centric reference frame?

get_state_vector()
* returns current state vector of the car

## Obstacle Database

The obstacle database will be a document style database. The attached detection systems or sensors can provide additional data through this, as long
as the basic required fields are provided

| Field | Type | Required? | Example Value | Description |
| ----- | ---- | --------- | ------------- | ----------- |
| ID    | int  | Y | 32   | Unique Id for report |
| sensor_ID   | int  | Y | 7   | ID of reporting system/sensor |
| sensor_name   | string  | Y | "Lidar"  | name of reporting system/sensor |
| Timestamp    | int  | Y | 1711071742  | timestamp of last detection |
| AZ1_deg    | float  | Y | 20 (deg)  | Body relative direction of outer angle 1 |
| AZ2_deg    | float  | Y | 45  (deg) | Body relative direction of outer angle 2 |
| Dist_m    | float  | N | 45 (m)  | distance to obstacle |
