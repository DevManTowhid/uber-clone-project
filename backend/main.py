from fastapi import FastAPI

# Initialize the application
app = FastAPI(
    title="Ride-Sharing Matchmaking API",
    description="High-concurrency backend for real-time ride matchmaking.",
    version="1.0.0"
)

# A simple health check route
@app.get("/health", tags=["System"])
async def health_check():
    return {
        "status": "healthy", 
        "message": "The ride-sharing engine is running."   
         }

@app.get("/", tags=["System"])
async def root():
    return {    
        "message": "Welcome to the Ride-Sharing Matchmaking API."   
        }
