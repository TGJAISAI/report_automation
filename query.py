class Query:
    
    unidata = """select concat( first_name , " " ,last_name , " ", speciality ) as data from universal3 limit 1000;"""