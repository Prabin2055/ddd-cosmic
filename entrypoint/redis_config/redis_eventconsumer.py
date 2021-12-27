import asyncio
import json
import redis
from entrypoint import settings


r = redis.Redis(**settings.settings_factory().redis_settings)


async def main():
    print("entered")
    pubsub = r.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe("task")  # (1)

    for m in pubsub.listen():
        data = json.loads(m["data"].decode("utf-8"))
        task = data["task"]
        if task == "batch_added":
            await batch_added(data["event"])
        if task == "product_added":
            await product_added(data["event"])


async def batch_added(data):
    print("***********************  BATCH ADDED  ******************************")
    print(data)


async def product_added(data):
    print("***********************  BATCH ADDED  ******************************")
    print(data)


if __name__ == "__main__":
    asyncio.run(main())
