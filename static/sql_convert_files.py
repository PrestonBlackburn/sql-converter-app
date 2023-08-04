print("installing sqlglot")
import micropip
await micropip.install("sqlglot")
import sqlglot
import sys

import sql_file_namespace



print("sqlglot version: ", sqlglot.__version__)
print("starting convert")

import js
from js import Uint8Array

# js.sql_query mostly works if global
#print(js.sql_query)


return_results = []
for item in sql_file_namespace:
    # print("from python: ", item.file_name)
    # print("from python: ", item.file_contents)
    # print("from python: ", item.input_dialect)
    # print("from python: ", item.target_dialect)

    converted_code = sqlglot.transpile(item.file_contents,
                                       read=item.input_dialect,
                                       write=item.target_dialect,
                                       pretty=True)[0]

    converted_dict = {"file_name": item.file_name, "converted_sql": converted_code }
    print("python:", converted_dict)
    return_results.append(converted_dict)



# pass the objects back:
js.converted_query = return_results


# to clean up the module + allow for reload
del sys.modules['sql_file_namespace']