def gps_tracker():
    x, y = 0, 0
    print(f"Starting position: ({x}, {y})")

    while True:
        command = input("Enter direction (N/S/E/W) or 'STOP' to end: ").upper()

        if command == "STOP":
            print(f"\nFinal position: ({x}, {y})")
            if x == 0 and y == 0:
                print("You returned to the origin (0, 0)!")
            else:
                print("You did not return to the origin.")
            break

        if command in ['N', 'NORTH']:
            y += 1
        elif command in ['S', 'SOUTH']:
            y -= 1
        elif command in ['E', 'EAST']:
            x += 1
        elif command in ['W', 'WEST']:
            x -= 1
        else:
            print("Invalid input. Use N, S, E, W, or STOP.")
            continue

        print(f"Current position: ({x}, {y})")

if __name__ == "__main__":
    gps_tracker()
N