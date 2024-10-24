from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Main Page"}

@app.get("/user/admin")
async def read_admin():
    return {"message": "HI, Administrator!"}

@app.get("/user/{user_id}")
async def read_user(user_id: int):  # Параметр user_id должен быть целым числом
    return {"message": f"You join as № {user_id}"}

@app.get("/user")
async def read_user(username: str, age: int):  # Параметры username и age
    return {"message": f"User INFO. NAME: {username}, AGE: {age}"}