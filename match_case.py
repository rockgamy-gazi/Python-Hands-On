while True:
    command = input("Enter a command (start, stop, exit): ").strip().lower()

    match command:
        case "start":
            print("System is starting...")
        case "stop":
            print("System is stopping...")
        case "exit":
            print("Exiting program. Goodbye!")
            break
        case _:
            print(f"Unrecognized command: '{command}'. Please try again.")

