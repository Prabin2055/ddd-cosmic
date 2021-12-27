import asyncio
from entrypoint import create_app
from entrypoint import settings
from sanic import response
app = asyncio.run(create_app(settings.settings_factory()))
app.config.FALLBACK_ERROR_FORMAT = "json"
app.config.DEBUG = True
app.config.AUTO_RELOAD = True


@app.main_process_start
async def start_db(request, loop):
    await app.ctx.db.connect()
    print("DB Connected")


@app.main_process_stop
async def start_db(request, loop):
    await app.ctx.db.disconnect()
    print("DB Disconnected")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, auto_reload=True)
