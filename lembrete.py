import time
from plyer import notification

def lembrete():
    notification.notify(
        title="Quantas garrafas de água já bebeu hoje?",
        message="Beber água 🫗",
        timeout=10
    )

while True:
    lembrete()
    time.sleep(3600)