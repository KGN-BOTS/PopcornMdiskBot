import asyncio
import config

async def auto_delete(txt=None, m=None):
    try:
        if config.AUTO_DELETE is not False:

            if txt and m or not None:
            # Waiting for the time to pass.
                await asyncio.sleep(config.AUTO_DELETE_TIME)
                if m is not None:
                    await m.delete()
                if txt is not None:
                    await txt.delete()

    except Exception as e:
        print(e)