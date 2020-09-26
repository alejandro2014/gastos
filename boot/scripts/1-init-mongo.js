db.createUser(
    {
        user: "gastos",
        pwd: "gastos",
        roles: [
            {
                role: "readWrite",
                db: "gastosdb"
            }
        ]
    }
)
