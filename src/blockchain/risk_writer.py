from stellar_sdk import Keypair, TransactionBuilder, Network, Server
import os

SERVER_URL = "https://horizon-testnet.stellar.org"
NETWORK_PASSPHRASE = Network.TESTNET_NETWORK_PASSPHRASE


def write_risk_to_stellar(project_id: str, risk_score: float) -> str:
    """
    Writes the risk result to the Stellar testnet:
    - memo: "projectId:riskScore"
    - manageData: key = "risk-<projectId>", value = "<riskScore>"
    Returns the transaction hash.
    """
    secret_key = os.environ.get("STELLAR_SECRET_KEY")
    if not secret_key:
        raise RuntimeError("STELLAR_SECRET_KEY environment variable is not set.")

    server = Server(SERVER_URL)
    keypair = Keypair.from_secret(secret_key)
    public_key = keypair.public_key

    # Hesap bilgilerini yükle
    account = server.load_account(public_key)

    # Memo en fazla 28 karakter
    memo_text = f"{project_id}:{int(risk_score)}"
    memo_text = memo_text[:28]

    # Manage Data key/value
    data_key = f"risk-{project_id}"[:64]   # max 64 char
    data_value = str(int(risk_score)).encode("utf-8")

    tx = (
        TransactionBuilder(
            source_account=account,
            network_passphrase=NETWORK_PASSPHRASE,
            base_fee=100,
        )
        .add_text_memo(memo_text)
        .append_manage_data_op(data_name=data_key, data_value=data_value)
        .set_timeout(300)  # TimeBounds uyarısını da çözüyor
        .build()
    )

    tx.sign(keypair)
    response = server.submit_transaction(tx)
    return response["hash"]

