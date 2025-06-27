def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "unknown status" # usage print(hhttp_status(200)) #Output: OK print(http_status(404))
                # Output: not Found print(http_status(500)) # Output: Internal Server
                
print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(50076))


