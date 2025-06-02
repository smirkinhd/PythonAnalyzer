from docker_runner import run_container
from browser import scan_url
from report import generate_report
import time

if __name__ == "__main__":
    print("[*] Starting container...")
    container = run_container()

    try:
        print("[*] Waiting for service to be ready...")
        time.sleep(3)

        print("[*] Scanning with browser...")
        result = scan_url("http://localhost:8080")

        print("[*] Saving report...")
        generate_report(result)

    finally:
        print("[*] Cleaning up...")
        container.stop()
        container.remove()
