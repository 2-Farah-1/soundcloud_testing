import time
import pytest

from tests.test_registeration_flows_primitive import setup_page
def wait_for_done():
    print("\nBrowser opened.")
    print("1) Log into Podio manually")
    print("2) Open the Deals page")
    print("3) Make sure you are on the table/list view")
    print("4) Then type 'done' here\n")

    while True:
        x = input("Type 'done' when ready: ").strip().lower()
        if x == "done":
            return
        print("Please type exactly: done")



@pytest.mark.stress
def test_web_ui_stress_with_gremlins(driver):
    setup_page(driver)
    wait_for_done()

    # load gremlins
    driver.execute_script("""
        var script = document.createElement('script');
        script.src = 'https://unpkg.com/gremlins.js';
        document.head.appendChild(script);
    """)

    time.sleep(3)

    # run
    driver.execute_script("""
        window.horde = gremlins.createHorde();
        console.log("[STRESS] Gremlins started");
        window.horde.unleash();
    """)

    print("Gremlins attacking website...")
    time.sleep(20)

    # stop
    driver.execute_script("""
        if (window.horde) {
            window.horde.stop();
            console.log("[STRESS] Gremlins stopped");
        }
    """)

    logs = driver.get_log("browser")

    print("\n========== WEB STRESS RESULTS ==========")

    for log in logs:
        print(log["level"], "-", log["message"])

    print("=======================================\n")