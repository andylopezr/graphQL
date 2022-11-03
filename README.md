# GraphQL API with Python and Flask
<img src="https://graphql.org/img/og-image.png">

> Backend API using GraphQL architecture, receivesd a mutation to create a user and a query to get the list of users. 

>  Instructions to run the app on ```localhost```


* Run venv ```source app/bin/activate```

Install Dependencies:
```pip install -r /path/to/requirements.txt```

Create environ var to run Flask server using app.py

```export FLASK_APP=app.py```

Run the app using ```flask run```

Playground running on:
```http://localhost:5000/graphql```

> Sample Queries

* List all users

    ``` bash
    query all_users {
    list_users {
        success
        errors
        users {
        id
        first_name
        last_name
        address
        recommended
        created_at
        }
    }
    }
    ```

* List a user by id

    ``` bash
    query get_user {
    get_user(id: "1") {
        user {
        id
        first_name
        last_name
        address
        recommended
        created_at
        }
        success
        errors
    }
    }
    ```

> Sample Mutations

* Create a user

    ``` bash
    mutation create_user {
    create_user(
        first_name: "Jhon",
        last_name: "Cena",
        address: "34 Evergreen Av",
        recommended: true) {
        user {
        id
        first_name
        last_name
        address
        recommended
        }
        success
        errors
    }
    }
    ```

* Update a user

    ``` bash
    mutation update_user {
    update_user(
        id:"4", 
        first_name:"Travis", 
        last_name:"Baker", 
        address:"32 Daydream St", 
        recommended:true
    ) {
        user {
        id
        first_name
        last_name
        address
        }
        success
        errors
    }
    }
    ```

* Delete a user

    ``` bash
    mutation delete_user {
    delete_user(id:"5") {
        success
        errors
        user {
        id
        first_name
        last_name
        address
        }
    }
    }
    ```



