Self Driving Car Interface 

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



## Navigation API documentation
### High level interface user:
journey_get_status()
- Returns an object with the current status

journey_halt()
- stops the current journey and stops the car

journey_set_start()
- Sets the starting location of the journey

journey_set_destination()
- Sets the end point of the journey

journey_begin()
- Starts the car on the journey

journey_limit_speed()
- Sets a maximum speed limit for the journey


### Navigation Module Developers:
get_state_vector()
* returns current state vector of the car

get_lat_lon()
* Returns coordinates of current position
