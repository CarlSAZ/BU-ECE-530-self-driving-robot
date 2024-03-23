# Generalize Restful Autonomous Vehicle Environment (G.R.A.V.E)

Here lies the G.R.A.V.E repository for my software design course. The primary purpose of this codebase is to explore concepts in Restful API design, databases, unit testing, and CI/CD practices.


## Documentation

Most submodules have their documentation contained in markdown files - Info.md -  in their folders. These describe the database components and the API for that submodule.

## Submodules

### Authentication
Implements a basic authenticator to restrict access to the autonomous vehicle. [Read Further](/Authentication/INFO.md)

### Navigation
This submodule keeps track of navigation steps in a lookup database. Direction steps will be either entered via manual entry, or by piping input from a mapping service such as google maps.[Read Further](/navigation/INFO.md)

### Obstacle Detections
Stores reports of obstacles or collision alerts in a database. These can then be fetched by an obstacle avoidance module (TBD). [Read Further](/ObjectDetection/INFO.md)

### Sensors
Basic templates for potential camera or Lidar units. [Read Further](/Sensors/INFO.md)

### Steering
Self contained resful api to control the main steering component. [Read Further](/steering/INFO.md)


