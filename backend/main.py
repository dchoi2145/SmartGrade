from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "SmartGrade backend is running!"}

@app.post("/upload")
async def create_item(uploaded_file: UploadFile = File(...)):
    contents = await uploaded_file.read() # Load file into memory
    filename = uploaded_file.filename # Get file name
    return {"message": "File uploaded", "filename": filename}
