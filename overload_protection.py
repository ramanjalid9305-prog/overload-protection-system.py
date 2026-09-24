import time
from datetime import datetime

MAX_LOAD = 10.0  # Maximum allowed load in Amps


def read_load():
    """Simulate reading the load/current from a sensor."""
    try:
        return float(input("Enter current load (A): "))
    except ValueError:
        print("Invalid input.")
        return None


def overload_protection(load):
    """Check the load and activate/deactivate protection."""
    if load is None:
        return

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if load > MAX_LOAD:
        print("\n⚠️ OVERLOAD DETECTED!")
        print(f"Load: {load:.2f} A")
        print(f"Limit: {MAX_LOAD:.2f} A")
        print("🔴 Protection activated - LOAD DISCONNECTED")
        print(f"Time: {current_time}")

        with open("overload_log.txt", "a") as log:
            log.write(
                f"{current_time} | OVERLOAD | "
                f"Load={load:.2f}A | Protection=ON\n"
            )
    else:
        print("\n🟢 Load is normal.")
        print(f"Load: {load:.2f} A")
        print(f"Limit: {MAX_LOAD:.2f} A")
        print("Protection: OFF")


def main():
    print("================================")
    print("   OVERLOAD PROTECTION SYSTEM")
    print("================================")
    print(f"Maximum Load: {MAX_LOAD} A")

    while True:
        load = read_load()

        if load is not None:
            overload_protection(load)

        choice = input("\nContinue? (y/n): ").lower()

        if choice != "y":
            print("System stopped.")
            break

        time.sleep(1)


if __name__ == "__main__":
    main()
