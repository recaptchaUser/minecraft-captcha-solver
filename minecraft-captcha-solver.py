import capsolver
from urllib.parse import urlparse

# Change this information
capsolver.api_key = "Your pay per usage key"

def solve_funcaptcha_minecraft():
    solution = capsolver.solve({
   "type": "FunCaptchaTaskProxyLess",
        "websiteURL": "https://www.minecraft.net",
        "websitePublicKey": "D39B0EE3-2973-4147-98EF-C92F93451E2D",
        "funcaptchaApiJSSubdomain": "https://client-api.arkoselabs.com"
    })
    return solution

def main():
    
    print("Solving minecraft captcha")
    solution = solve_funcaptcha_minecraft()
    
    token = solution["token"]
    
    print("Token Solution " + token)
    
if __name__ == "__main__":
    main()
