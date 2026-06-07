from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.resume import router as resume_router
from routes.roles import router as roles_router
from routes.interview import router as interview_router
from routes.upload import router as upload_router
from routes.chat import router as chat_router
from routes.jobs import router as jobs_router

app = FastAPI(
    title="AI Data Analyst Interview Coach",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(
    resume_router,
    prefix="/resume",
    tags=["Resume"]
)

app.include_router(
    roles_router,
    prefix="/roles",
    tags=["Roles"]
)

app.include_router(
    interview_router,
    prefix="/interview",
    tags=["Interview"]
)

app.include_router(
    upload_router,
    prefix="/upload",
    tags=["Upload"]
)

app.include_router(
    chat_router,
    prefix="/chat",
    tags=["Chat"]
)

app.include_router(
    jobs_router,
    prefix="/jobs",
    tags=["Jobs"]
)

@app.get("/")
def home():
    return {
        "status": "running"
    }