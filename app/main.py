from fastapi import FastAPI

app = FastAPI(title="API Security Lab", version="0.1.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/")
def root() -> dict:
    return {
        "project": "api-security-lab",
        "message": "Scaffold running. Next: auth, RBAC, and security tests.",
    }
