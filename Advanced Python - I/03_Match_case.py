def https_status(status):
    match status :
        case 200:
            return "O.K"
        case 404:
            return "Not Found"
        case 500:
            return "None"
        case _:
            return "Unknown status"
        
print(https_status(404))
print(https_status(200))
print(https_status(500))
print(https_status(604))
