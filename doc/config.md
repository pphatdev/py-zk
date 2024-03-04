### How to config and testing
The way to config fingerprint and database.

#### Configuration file

Create `config.json` file or copy and rename `example.config.json` file.

-   with creating file 

```sh
touch config.json
```
>_  after execute goto `example.config.json` and copy everything inside then go back to `config.json` and paste inside. then update your configuration device or database.

-   with copy and rename file 

```sh
cp example.config.json config.json
```
>_  then update your configuration device or database.


#### Testing Finger Print (fp)

```sh
py .\connection.fp.py  
```
then check your configuration inside file config.json. 
example: `turbotech`
```sh
Configured fingerprint name: (check file config.json) : turbotech
```
wait afew minutes the result will show up.


#### Testing Database (db)

```sh
py .\connection.db.py  
```
then check your configuration inside file config.json. 
example: `sit`
```sh
Configured fingerprint name: (check file config.json) : sit
```
wait afew minutes the result will show up.


### Config Options Example

```json
{
    "processor": "py", // python, python2, python3 : python execute machine
    "fingerprint": {
        "device1": {
            "ip": "123.123.10.124", 
            "port": "4370"
        },
        "device2": {
            "ip": "123.123.10.123", 
            "port": "4370"
        }
    },
    "database": {
        "server1": {
            "name": "ServerName",   
            "host": "111.110.11.22",   
            "user": "postgres",   
            "password": "postgres",   
            "port": "5432"
        },
        "server2": {
            "name": "ServerName",   
            "host": "111.110.11.22",   
            "user": "postgres",   
            "password": "postgres",   
            "port": "5432"
        }
    }
}
```


### About Configuration

-   [Discussion](https://github.com/orgs/turbotechlabs/discussions/7) 

### New Issues 

-   [New Issues](https://github.com/turbotechlabs/py-attendance/issues/new) 
-   [New Discussion ](https://github.com/orgs/turbotechlabs/discussions/new/choose)