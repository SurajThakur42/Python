letter = '''Dear <|Name|>, 
            You are selected! 
            <|Date|> '''

print (letter.replace("<|Name|>",("Suraj")).replace("<|Date|>",("14 June 2025")))
