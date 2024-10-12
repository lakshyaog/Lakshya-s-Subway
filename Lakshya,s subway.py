import random
import time

def main():
    print("Welcome to the Text-Based Subway Surfer Game!")
    print("You are running on the subway tracks. Avoid the obstacles!")
    print("Press 'j' to jump, 'd' to dodge, and 'q' to quit the game.")
    
    score = 0
    game_over = False
    
    while not game_over:
        time.sleep(1)  # Wait for 1 second between moves
        obstacle = random.choice(['none', 'low', 'high'])  # Randomly choose an obstacle
        print(f"\nAn obstacle is coming: {obstacle}")

        action = input("Choose your action (j/d/q): ").lower()
        
        if action == 'q':
            print("Thanks for playing!")
            break
        elif action == 'j':
            if obstacle == 'high':
                print("You jumped over the high obstacle!")
                score += 1
            elif obstacle == 'none':
                print("No obstacles, you keep running!")
                score += 1
            else:
                print("You hit a low obstacle! Game Over.")
                game_over = True
        elif action == 'd':
            if obstacle == 'low':
                print("You dodged the low obstacle!")
                score += 1
            elif obstacle == 'none':
                print("No obstacles, you keep running!")
                score += 1
            else:
                print("You couldn't dodge the high obstacle! Game Over.")
                game_over = True
        else:
            print("Invalid input. Please choose 'j', 'd', or 'q'.")
    
    print(f"Game Over! Your final score is: {score}")

if __name__ == "__main__":
    main()
