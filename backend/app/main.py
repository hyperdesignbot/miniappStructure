import logging

from fastapi import FastAPI
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from pytz import timezone  # Import pytz for timezone handling

from app.telegram_bot import application
from app.routers import bot_routes

app = FastAPI(title="Telegram MiniApp Backend")

# Include routers
app.include_router(bot_routes.router, prefix="/bot", tags=["Bot API"])
# app.include_router(user_routes.router, prefix="/user", tags=["User API"])

# Initialize APScheduler
tehran_timezone = timezone("Asia/Tehran")
scheduler = AsyncIOScheduler(timezone=tehran_timezone)  # Use pytz timezone

async def example_task():
    print("example task")

@app.on_event("startup")
async def startup_event():
    print("Starting Telegram bot...")
    await application.initialize()  # Initialize bot
    await application.start()       # Start bot
    asyncio.create_task(application.updater.start_polling())  # Use polling in a background task
    # Add jobs to scheduler
    scheduler.add_job(
        example_task,
        trigger='interval',  # Runs every 10 seconds
        seconds=1,
    )

    # Start the scheduler
    scheduler.start()




@app.on_event("shutdown")
async def shutdown_event():
    print("Stopping Telegram bot...")
    await application.stop()        # Stop bot properly
