QUERY = {
    "all": """
        SELECT
            lastnames.lastname,
            firstnames.firstname,
            surnames.surname,
            main.tel,
            streets.street,
            main.building,
            main.building_k,
            main.apartment
        FROM main
        LEFT JOIN lastnames ON main.lastname = lastnames.id
        LEFT JOIN firstnames ON main.firstname = firstnames.id
        LEFT JOIN surnames ON main.surname = surnames.id
        LEFT JOIN streets ON main.street = streets.id
    """,

    "firstnames": """
        SELECT firstname
        FROM firstnames
        ORDER BY firstname
    """,

    "lastnames": """
        SELECT lastname
        FROM lastnames
        ORDER BY lastname
    """,

    "surnames": """
        SELECT surname
        FROM surnames
        ORDER BY surname
    """,

    "streets": """
        SELECT street
        FROM streets
        ORDER BY street
    """,
}