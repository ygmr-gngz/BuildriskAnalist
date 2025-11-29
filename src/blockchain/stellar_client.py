from stellar_sdk import Server

def test_stellar_connection():
    """
    Connects to Stellar testnet and fetches the latest ledger.
    Used to verify that the connection works.
    """
    try:
        server = Server("https://horizon-testnet.stellar.org")
        ledger = server.ledgers().order(desc=True).limit(1).call()
        return {
            "status": "ok",
            "latest_ledger": ledger["_embedded"]["records"][0]["sequence"]
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
