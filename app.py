import asyncio


async def custom_coroutine():
    print('Hello world')

# Running the two coroutines simultaneosuly using asncio.gather() 
async def greet(name):
    await asyncio.sleep(1)  # Simulates an asynchronous operation
    print(f"Hello, {name}!")

async def main():
    await asyncio.gather(greet("Alice"), greet("Bob"))

cor = custom_coroutine()
if __name__ == "__main__":
    asyncio.run(main())