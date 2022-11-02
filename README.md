# GraphQL API with Python and Flask
<img src="https://graphql.org/img/og-image.png">

> Backend API using GraphQL architecture, receivesd a mutation to create a user and a query to get the list of users. 
* User structure for mutation (create user):

``` bash
{
    first_name: “Juan”,
    last_name: “Sanchez”,
    address: “asd -asd #25 – 57”,
    recommended: false
}
```

Response from query (get user list)

``` bash
[
    {
        first_name: “Juan”,
        last_name: “Sanchez”,
        address: “asd -asd #25 – 57”,
        recommended: false
    },
]
```