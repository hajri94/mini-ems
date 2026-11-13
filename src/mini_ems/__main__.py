# Entry point: Python runs this file when you type "python -m mini_ems".


# Define one function that starts the application (later: start the scheduler or the API).
def main() -> None:
    # Temporary start message; step4 replaces print() with logging.
    print("mini_ems started")


# Run main() only when this file is executed, not when another module imports it.
if __name__ == "__main__":
    # Call the start function.
    main()