import os
from verifysystem import VerificationSystem

if __name__ == "__main__":
    key = os.environ["SecertClientKey"]

    VerificationSystem.run(key)
