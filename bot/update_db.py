from bot.modules.mongodb import MongoDB
from bot import (
    logger,
    bot_token,
    owner_id,
    owner_username,
    bot_pic,
    welcome_img,
    github_repo,
    mongodb_uri,
    db_name,
    server_url,
    shortener_api_key,
    omdb_api,
    weather_api_key
)


async def update_database():
    find = await MongoDB.find("bot_docs", "_id")

    if find:
        logger.info("MongoDB Database Exist! Skiping update...")
        return
    
    data = {
        "bot_token": bot_token,
        "owner_id": int(owner_id),
        "owner_username": owner_username,
        "bot_pic": bot_pic,
        "welcome_img": bool(welcome_img),
        "github_repo": github_repo,
        #database
        "mongodb_uri": mongodb_uri,
        "db_name": db_name,
        #alive
        "server_url": server_url,
        #api's
        "shortener_api_key": shortener_api_key,
        "omdb_api": omdb_api,
        "weather_api_key": weather_api_key
    }

    try:
        await MongoDB.insert_single_data("bot_docs", data)
        logger.info("Database updated from config.env ...")
        return True
    except Exception as e:
        logger.warning(e)
        return False
