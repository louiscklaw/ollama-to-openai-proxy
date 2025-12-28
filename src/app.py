#!/usr/bin/env python

import uvicorn
from fastapi import FastAPI
from routes.helloworld import router as helloworld_router
from routes.proxy import router as proxy_router

app = FastAPI(title="Ollama to OpenAI Proxy")

# Include routers
app.include_router(helloworld_router)
app.include_router(proxy_router)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
