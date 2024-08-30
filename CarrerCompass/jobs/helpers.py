def getPostTime(seconds):

    if seconds > 86400:
        seconds = round(seconds // 86400)
        text = f"{seconds} days"
            
    elif seconds > 3600:
        print(True)
        seconds = round(seconds // 3600)
        text = f"{seconds} hours"
    
    elif seconds > 60:
        seconds = round(seconds // 60)
        text = f"{seconds} minutes"

    else:
        seconds = round(seconds)
        text = f"{seconds} seconds"
    
    return text