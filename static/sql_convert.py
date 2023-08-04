print("installing sqlglot")
import micropip
await micropip.install("sqlglot")
import sqlglot
import sys

import sql_namespace



print("sqlglot version: ", sqlglot.__version__)
print("starting convert")

import js

# js.sql_query mostly works if global
#print(js.sql_query)
print(sql_namespace.sql_text)
print(sql_namespace.read_dialect)
print(sql_namespace.write_dialect)

try:
    converted_code = sqlglot.transpile(sql_namespace.sql_text,
                                       read=sql_namespace.read_dialect,
                                       write=sql_namespace.write_dialect,
                                       pretty=True)[0]
    #converted_code = sqlglot.transpile(js.sql_query, read="tsql", write="snowflake")[0]
except Exception as e:
    converted_code = e
print(converted_code)

js.converted_query = converted_code

sql_namespace.converted_query = converted_code

# to clean up the module + allow for reload
del sys.modules['sql_namespace']

