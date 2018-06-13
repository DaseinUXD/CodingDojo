# Errors
## Login Errors
wrong password: `pymysql.err.OperationalError: (1045, "Access denied for user 'root'@'localhost' (using password: YES)")`
wrong user:`pymysql.err.OperationalError: (1045, "Access denied for user 'u'@'localhost' (using password: YES)")`
## Setup Errors
wrong host: `pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on 'host' ([Errno 11001] getaddrinfo failed)")`
wrong database variable name: ` db = d,` `ameError: name 'd' is not defined`