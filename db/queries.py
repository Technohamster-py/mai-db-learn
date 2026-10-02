QUERY = {
    "all": """
            SELECT
                main.id,
                lastnames.lastname,
                firstnames.firstname,
                surnames.surname,
                streets.street,
                main.building,
                main.building_k,
                main.apartment,
                main.tel
            FROM main
            LEFT JOIN lastnames
                ON main.lastname = lastnames.id
            LEFT JOIN firstnames
                ON main.firstname = firstnames.id
            LEFT JOIN surnames
                ON main.surname = surnames.id
            LEFT JOIN streets
                ON main.street = streets.id;
            """
}