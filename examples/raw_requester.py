import asyncio
import logging
from pymec import ClientBuilder, api


logging.basicConfig(level=logging.INFO)


async def main():
    client = (
        ClientBuilder()
        .host("http://master.local/api/v0.5/")
        .build()
    )

    # create lambda
    lambda_ = await client.request(
        api.lambda_.Create(data_id="0", runtime="pymec+example")
    )

    # input
    input = await client.api.data.upload(b"example input")

    # job
    job = await client.api.job.create(lambda_.lambda_id, input.data_id)

    # wait for finish
    job_info = await client.api.job.info(job.job_id, except_="Finished", timeout=10)

    # output
    _ = await client.api.data.download(job_info.output.data_id)

    print("job finished")


if __name__ == "__main__":
    asyncio.run(main())
