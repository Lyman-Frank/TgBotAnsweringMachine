import time
from commands import start_bot

def main():
    try:
        start_bot()
    except Exception as e:
        print(f"Error: {e}")
        print("Restarting in 3 seconds...")
        time.sleep(3)
        main()

if __name__ == "__main__":
    main()
