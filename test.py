from product import oldProduct
from dotenv import load_dotenv
import os 
load_dotenv()

def main(): 
    print(os.getenv('SLACK_APP_TOKEN'))    



if __name__ == '__main__':
    main()