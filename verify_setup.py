import fastapi
import pydantic
import uvicorn

print("Environment verification successful\n")

print("FastAPI version:", fastapi.__version__)
print("Pydantic version:", pydantic.__version__)
print("Uvicorn version:", uvicorn.__version__)

print("\nAll core dependencies are installed correctly.")