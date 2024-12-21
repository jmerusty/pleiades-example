import asyncio
import logging
from pymec import ClientBuilder, api


logging.basicConfig(level=logging.INFO)


async def main():
    client = (
        ClientBuilder()
        .host("http://master.local/api/v0.5")
        .build()
    )

    # register worker
    register = await client.request(api.worker.Register(runtimes=["pymec+example"]))

    # contract job
    contract = await client.request(
        api.worker.Contract(
            worker_id=register.worker_id,
            timeout=10,
        )
    )

    if contract.job_id is None:
        print("No job available")
        return

    # job info
    job_info = await client.request(api.job.Info(job_id=contract.job_id))

    # input
    input = await client.request(api.data.Download(data_id=job_info.input.data_id))
    print(input.data)

    # output
    output = await client.request(api.data.Upload(data=b"example output"))

    # job update
    _ = await client.request(
        api.job.Update(
            job_id=contract.job_id,
            data_id=output.data_id,
            status="finished",
        )
    )
    print("job finished")


if __name__ == "__main__":
    asyncio.run(main())
