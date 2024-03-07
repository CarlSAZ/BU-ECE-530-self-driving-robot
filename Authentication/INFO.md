
# User Authentication Module

## Basic User Entry

Database of all user accounts

| Field | Type | Example Value | Description |
| ----- | ---- | ------------- | ----------- |
| UserID | int64 | 20493 | Unique user ID |
| name | string | "John Smith" | String identifier for user |
| email | string | "`jsmith@bu.edu`" | email of user |
| created_on | datetime | March 2, 2024 16:55:00 | time of user creation |

## User to Car lookup table

Basic table matching users to cars they are authorized to operate.

| Field | Type | Example Value | Description |
| ----- | ---- | ------------- | ----------- |
| UserID | int64 | 20493 | Unique user ID |
| CarID | int64 | 20493 | Car allowed for user to access |
