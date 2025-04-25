import json
import os
from aa_inflight_tracker.client.aa_client import AAInflightClient
from multiprocessing import Process, Value
import time
import signal
import sys
from loguru import logger

class AAInflightAgent:
    def __init__(self):
        self._client = AAInflightClient()
        self._stop_flag = Value('b', False)  # Shared flag to stop the process
        self.refetch_interval = 5 # Seconds to next fetch
        self.data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data"))
        self.flight_status = None
        self.flight_status_update_process = Process(target=self.flight_status_update_worker)
        logger.warning(f"Flight status data will be dump to {self.data_path}")

    def set_current_flight_status(self):
        """Fetch the current flight status from the client."""
        self.flight_status = self._client.get_current_flight_status()
        logger.success(f"Updated flight status")
        logger.info(f"{self.flight_status}")
        self.dump_flight_status()
        
    def dump_flight_status(self):
        """Dump the current flight status to a file."""
        if (not self.flight_status):
            logger.warning("No flight status available to dump.")
            return
        file_name = f"flight_status_{int(self.flight_status.timestamp.timestamp())}.json"
        file_path = os.path.join(self.data_path, file_name)
        with open(file_path, "w") as f:
            json.dump(self.flight_status.model_dump(mode="json"), f, indent=2)
        logger.success(f"Flight status dumped to file: {file_path}")

    def flight_status_update_worker(self):
        """Background worker to periodically update flight status."""
        logger.trace("Instantiated the background process for flight status updates.")
        while not self._stop_flag.value:
            self.set_current_flight_status()
            time.sleep(self.refetch_interval)

    def start_flight_status_updates(self):
        """Start the background process for updating flight status."""
        if not self.flight_status_update_process.is_alive():
            self.flight_status_update_process.start()

    def stop_flight_status_updates(self):
        """Stop the background process for updating flight status."""
        self._stop_flag.value = True
        self.flight_status_update_process.join()

    def __del__(self):
        """Ensure the background process is stopped when the object is deleted."""
        self.stop_flight_status_updates()


def signal_handler(signal, frame):
    """Handle termination signals to clean up the process."""
    logger.warning("Terminating...")
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C gracefully

    agent = AAInflightAgent()
    agent.start_flight_status_updates()

    try:
        while True:
            time.sleep(1)  # Keep the main thread alive
    except KeyboardInterrupt:
        agent.stop_flight_status_updates()
        logger.warning("Stopped flight status updates.")